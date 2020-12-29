import re
from unicodedata import normalize

from kesi.butkian.kongiong import 組字式符號, 聲調符號, 標點符號, 敢是拼音字元,\
    敢是注音符號, LIAN_JI_HU, si_lomaji
from kesi.butkian.su import Su
from kesi.butkian.ji import Ji


class Ku:
    """
    ku = Ku()
    su = Su()
    ji = Ji()

    for su in ku:
        for ji in su:
            for guan in ji.hanlo:
    """
    _切組物件分詞 = re.compile('(([^ ｜]*[^ ]｜[^ ][^ ｜]*) ?|[^ ]+)')
    _是空白 = re.compile(r'[^\S\n]+')
    _是分字符號 = re.compile('{}+'.format(LIAN_JI_HU))
    _是數字 = set('0123456789')
    _是多字元標點 = re.compile(r'(\.\.\.)|(……)|(──)')

    def __init__(self, hanlo=None, lomaji=None):
        if hanlo is not None:
            hanlo = normalize('NFC', hanlo)
        if lomaji is not None:
            lomaji = normalize('NFC', lomaji)

        # Ku(lomaji='Goa')
        if hanlo is None:
            hanlo = lomaji
            lomaji = None

        if hanlo is None:
            self._su = []
        elif lomaji is None:
            tngji, tngji_khinsiann, si_bokangsu = (
                self._hunsik_tngji_tngsu(hanlo)
            )
            bun, khinsiann = self._tngsu(tngji, tngji_khinsiann, si_bokangsu)
            self._su = self._bun_tsuan_sutin(bun, khinsiann)
        else:
            """ 以羅馬字ê斷字斷詞為主，漢羅文--ê無效 """
            tnghanlo, _ps, _ps = self._hunsik_tngji_tngsu(hanlo)
            tnglomaji, tngji_khinsiann, si_bokangsu = (
                self._hunsik_tngji_tngsu(lomaji)
            )

            if len(tnghanlo) != len(tnglomaji):
                raise TuiBeTse(
                    'Kù bô pênn tn̂g: '
                    'Hanlo tn̂g {} jī, m̄-koh lomaji tn̂g {} jī'
                    .format(len(tnghanlo), len(tnglomaji)))

            hanlo_tin, _ps = self._tngsu(
                tnghanlo, tngji_khinsiann, si_bokangsu)
            lomaji_tin, khinsiann = self._tngsu(
                tnglomaji, tngji_khinsiann, si_bokangsu)

            self._su = self._phe_tsuan_sutin(
                hanlo_tin, lomaji_tin, khinsiann)

    def __str__(self):
        return self.hanlo

    def __iter__(self):
        yield from self._su

    def __getitem__(self, kui):
        return self._su[kui]

    def __len__(self):
        return len(self._su)

    def _bun_tsuan_sutin(self, bun_tin, khinsiann_tin):
        sutin = []
        for tsitsu, khinsiann in zip(bun_tin, khinsiann_tin):
            su = Su()
            for ji, si_khinsiann in zip(tsitsu, khinsiann):
                su.thiam(
                    Ji(ji, si_khinsiann=si_khinsiann)
                )
            sutin.append(su)
        return sutin

    def _phe_tsuan_sutin(self, hanlo_tin, lomaji_tin, khinsiann_tin):
        sutin = []
        for suhanlo_tin, sulomaji_tin, khinsiann in zip(
                hanlo_tin, lomaji_tin, khinsiann_tin):
            su = Su()
            for jihanlo, jilomaji, si_khinsiann in zip(
                    suhanlo_tin, sulomaji_tin, khinsiann):
                su.thiam(
                    Ji(jihanlo, lomaji=jilomaji,
                        si_khinsiann=si_khinsiann)
                )
            sutin.append(su)
        return sutin

    @property
    def hanlo(self):
        """
          會 kā 文本標準化：
          保留羅馬字 ê 空白，tshun--ê 空白會刣掉
        """
        bun = []
        頂一詞上尾是羅馬字 = False
        for su in self:
            suhanlo = su.hanlo
            #
            #  判斷愛先添空白符無
            #    H, H -> 'HH'
            #    H, L -> 'HL'
            #    L, L -> 'L L'
            #
            if 頂一詞上尾是羅馬字 and si_lomaji(suhanlo[0]):
                bun.append(' ')
            bun.append(suhanlo)
            頂一詞上尾是羅馬字 = si_lomaji(suhanlo[-1])
        return ''.join(bun)

    @property
    def lomaji(self):
        """
          會 kā 文本標準化：
          保留羅馬字 ê 空白，tshun--ê 空白會刣掉
        """
        bun = []
        頂一詞上尾是羅馬字 = False
        for su in self:
            sulomaji = su.lomaji
            #
            #  判斷愛先添空白符無
            #    H, H -> 'HH'
            #    H, L -> 'HL'
            #    L, L -> 'L L'
            #
            if 頂一詞上尾是羅馬字 and si_lomaji(sulomaji[0]):
                bun.append(' ')
            bun.append(sulomaji)
            頂一詞上尾是羅馬字 = si_lomaji(sulomaji[-1])
        return ''.join(bun)

    def thianji(self):
        """
        =臺灣言語工具.拆文分析器.篩出字物件
        """
        for tsit_su in self:
            yield from tsit_su

    def thiam(self, su):
        self._su.append(su)

    def POJ(self):
        sin_ku = Ku()
        for su in self:
            sin_ku.thiam(su.POJ())
        return sin_ku

    def TL(self):
        sin_ku = Ku()
        for su in self:
            sin_ku.thiam(su.TL())
        return sin_ku

    def _tngsu(self, 字陣列, 輕聲陣列, 佮後一个字無仝一个詞):
        巢狀詞陣列 = []
        巢狀輕聲陣列 = []
        位置 = 0
        while 位置 < len(字陣列):
            範圍 = 位置
            while 範圍 < len(佮後一个字無仝一个詞) and not 佮後一个字無仝一个詞[範圍]:
                範圍 += 1
            範圍 += 1
            巢狀詞陣列.append(字陣列[位置:範圍])
            巢狀輕聲陣列.append(輕聲陣列[位置:範圍])
            位置 = 範圍
        return 巢狀詞陣列, 巢狀輕聲陣列

    def _hunsik_tngji_tngsu(self, 語句):
        狀態 = self._分析狀態()
        if self._是空白.fullmatch(語句):
            return 狀態.分析結果()
        頂一个字 = None
        頂一个是連字符 = False
        頂一个是空白 = False
        頂一个是輕聲符號 = False
        頂一个是注音符號 = False
        位置 = 0
        while 位置 < len(語句):
            字 = 語句[位置]
            是連字符 = False
            是空白 = False
            是輕聲符號 = False
            是注音符號 = 敢是注音符號(字)
            if 狀態.是組字模式():
                狀態.這馬字加一个字元(字)
                狀態.組字模型加一个字元(字)
                if 狀態.組字長度有夠矣未():
                    狀態.這馬字好矣清掉囥入去字陣列()
                    狀態.變一般模式()
            elif 狀態.是一般模式():
                揣分字 = self._是分字符號.match(語句[位置:])
                if 揣分字:
                    # Hyphen
                    狀態.這馬字好矣清掉囥入去字陣列()
                    分字長度 = len(揣分字.group(0))
                    if 分字長度 == 1:
                        # LIAN_JI_HU
                        if not 狀態.敢有分析資料矣() or 頂一个是空白:
                            狀態.字陣列直接加一字(LIAN_JI_HU)
                            狀態.頂一字佮這馬的字無仝詞()
                        else:
                            狀態.頂一字佮這馬的字仝詞()
                            是連字符 = True
                            狀態.有連字符()
                    elif 分字長度 == 2:
                        是輕聲符號 = True
                        狀態.這陣是輕聲詞()
                        if not 頂一个是空白:
                            # hó --lah -> ['hó', '--lah']
                            # hó--lah -> ['hó--lah']
                            狀態.頂一字佮這馬的字仝詞()
                    else:
                        for _ in range(分字長度):
                            狀態.字陣列直接加一字(LIAN_JI_HU)
                            狀態.頂一字佮這馬的字無仝詞()
                    位置 += 分字長度 - 1
                elif self._是空白.fullmatch(字):
                    狀態.這馬字好矣清掉囥入去字陣列()
                    狀態.頂一字佮這馬的字無仝詞()
                    if 頂一个是連字符:
                        狀態.字陣列直接加一字(LIAN_JI_HU)
                        狀態.頂一字佮這馬的字無仝詞()
                    if 頂一个是輕聲符號:
                        狀態.字陣列直接加一字(LIAN_JI_HU)
                        狀態.頂一字佮這馬的字無仝詞()
                        狀態.字陣列直接加一字(LIAN_JI_HU)
                        狀態.頂一字佮這馬的字無仝詞()
                    是空白 = True
                # 羅馬字接做伙
                elif 敢是拼音字元(字):
                    # 頭前是羅馬字抑是輕聲、外來語的數字
                    # 「N1N1」、「g0v」濫做伙名詞，「sui2sui2」愛變做兩个字，予粗胚處理。
                    if (
                        not 敢是拼音字元(頂一个字) and
                        頂一个字 not in self._是數字
                    ):
                        # 頭前愛清掉
                        狀態.這馬字好矣清掉囥入去字陣列()
                        狀態.頂一字佮這馬的字無仝詞()
                    if 頂一个是輕聲符號:
                        狀態.這馬是輕聲字()

                    狀態.這馬字加一个字元(字)
                # 數字
                elif 字 in self._是數字:
                    if (
                        頂一个字 not in self._是數字 and
                        not 敢是拼音字元(頂一个字) and
                        not 頂一个是注音符號
                    ):
                        狀態.這馬字好矣清掉囥入去字陣列()
                        狀態.頂一字佮這馬的字無仝詞()
                    狀態.這馬字加一个字元(字)
                # 音標後壁可能有聲調符號 uainnˊ
                elif 字 in 聲調符號 and 敢是拼音字元(頂一个字):
                    狀態.這馬字加一个字元(字)
                # 處理注音，輕聲、注音、空三个後壁會當接注音
                elif 是注音符號:
                    if (
                        頂一个字 not in 聲調符號 and
                        not 頂一个是注音符號
                    ):
                        狀態.這馬字好矣清掉囥入去字陣列()
                    狀態.這馬字加一个字元(字)
                # 注音後壁會當接聲調
                elif 字 in 聲調符號 and 頂一个是注音符號:
                    狀態.這馬字加一个字元(字)

                elif 字 in 標點符號:
                    揣著多字元標點 = self._是多字元標點.match(語句[位置:])
                    if 字 == '•' and 狀態.上尾敢是o結尾():
                        狀態.這馬字加一个字元(字)
                    elif 揣著多字元標點:
                        符號 = 揣著多字元標點.group(0)
                        狀態.這馬字好矣清掉囥入去字陣列()
                        狀態.頂一字佮這馬的字無仝詞()
                        狀態.字陣列直接加一字(符號)
                        狀態.頂一字佮這馬的字無仝詞()
                        位置 += len(符號) - 1
                    else:
                        狀態.這馬字好矣清掉囥入去字陣列()
                        狀態.頂一字佮這馬的字無仝詞()
                        狀態.字陣列直接加一字(字)
                        狀態.頂一字佮這馬的字無仝詞()
                else:
                    if 狀態.這馬字敢全部攏數字():
                        狀態.這馬字好矣清掉囥入去字陣列()
                        狀態.頂一字佮這馬的字無仝詞()
                    elif 敢是拼音字元(頂一个字):
                        狀態.這馬字好矣清掉囥入去字陣列()
                        狀態.頂一字佮這馬的字無仝詞()
                    else:
                        狀態.這馬字好矣清掉囥入去字陣列()
                    if 頂一个是輕聲符號:
                        狀態.這馬是輕聲字()

                    狀態.這馬字加一个字元(字)

                    if 字 in 組字式符號:
                        狀態.變組字模式()
                    else:
                        狀態.這馬字好矣清掉囥入去字陣列()
            位置 += 1
            頂一个字 = 字
            頂一个是連字符 = 是連字符
            頂一个是空白 = 是空白
            頂一个是輕聲符號 = 是輕聲符號
            頂一个是注音符號 = 是注音符號
        if 狀態.這馬字敢閣有物件():
            if 狀態.是一般模式():
                狀態.這馬字好矣清掉囥入去字陣列()
            else:
                raise 解析錯誤('語句組字式無完整，語句＝{0}'.format(str(語句)))
        if 頂一个是連字符:
            狀態.字陣列直接加一字(LIAN_JI_HU)
            狀態.頂一字佮這馬的字無仝詞()
        if 頂一个是輕聲符號:
            狀態.字陣列直接加一字(LIAN_JI_HU)
            狀態.頂一字佮這馬的字無仝詞()
            狀態.字陣列直接加一字(LIAN_JI_HU)
            狀態.頂一字佮這馬的字無仝詞()
        return 狀態.分析結果()

    class _分析狀態:

        def __init__(self):
            self._字陣列 = []
            self._輕聲陣列 = []
            self._佮後一个字無仝一个詞 = []
            self.變一般模式()
            # 組字式抑是數羅會超過一个字元
            self._這馬字 = ''
            self._這馬是輕聲字 = False
            self._這陣是輕聲詞 = False
            self._這陣是輕聲詞_而且是輕聲詞ê一部份 = False

        def 分析結果(self):
            return self._字陣列, self._輕聲陣列, self._佮後一个字無仝一个詞

        def 敢有分析資料矣(self):
            return len(self._字陣列) > 0 or self.這馬字敢閣有物件()

        def 這馬字敢閣有物件(self):
            return self._這馬字 != ''

        def 這馬字敢全部攏數字(self):
            return self._這馬字.isdigit()

        def 變一般模式(self):
            self._模式 = '一般'
            self._組字長度 = 0

        def 變組字模式(self):
            self._模式 = '組字'
            self._組字長度 = -1

        def 是一般模式(self):
            return self._模式 == '一般'

        def 是組字模式(self):
            return self._模式 == '組字'

        def 組字模型加一个字元(self, 字):
            if 字 in 組字式符號:
                self._組字長度 -= 1
            else:
                self._組字長度 += 1

        def 組字長度有夠矣未(self):
            return self._組字長度 == 1

        def 這馬字加一个字元(self, 字):
            self._這馬字 += 字

        def 這馬是輕聲字(self):
            self._這馬是輕聲字 = True

        def 這陣是輕聲詞(self):
            self._這陣是輕聲詞 = True
            self._這陣是輕聲詞_而且是輕聲詞ê一部份 = True

        def 有連字符(self):
            if self._這陣是輕聲詞:
                self._這陣是輕聲詞_而且是輕聲詞ê一部份 = True

        def 字陣列直接加一字(self, 字):
            self._字陣列.append(字)
            self._輕聲陣列.append(False)
            self._佮後一个字無仝一个詞.append(None)

        def 這馬字好矣清掉囥入去字陣列(self):
            if self._這馬字 != '':
                if self._這陣是輕聲詞:
                    if not self._這陣是輕聲詞_而且是輕聲詞ê一部份:
                        self.頂一字佮這馬的字無仝詞()
                        self._這陣是輕聲詞 = False
                    self._這陣是輕聲詞_而且是輕聲詞ê一部份 = False
                self._字陣列.append(self._這馬字)
                self._輕聲陣列.append(self._這馬是輕聲字)
                self._佮後一个字無仝一个詞.append(None)
                self._這馬字 = ''
                self._這馬是輕聲字 = False

        def 頂一字佮這馬的字仝詞(self):
            try:
                self._佮後一个字無仝一个詞[-1] = False
            except IndexError:
                pass

        def 頂一字佮這馬的字無仝詞(self):
            try:
                if self._佮後一个字無仝一个詞[-1] is None:
                    self._佮後一个字無仝一个詞[-1] = True
            except IndexError:
                pass

        def 上尾敢是o結尾(self):
            for o in ['o', 'ó', 'ò', 'ô', 'ǒ', 'ō', 'o̍', 'ő']:
                if self._這馬字.endswith(o):
                    return True
            return False


class 解析錯誤(Exception):
    pass


class TuiBeTse(ValueError):
    pass
