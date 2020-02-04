from kesi.butkian.kongiong import 分詞符號, 分字符號, 無音, 組字式符號, 聲調符號, 標點符號, 敢是拼音字元,\
    敢是注音符號
from kesi.kaisik.tsho_ngoo import 型態錯誤, 解析錯誤
import re


class Ku:
    _切組物件分詞 = re.compile('(([^ ｜]*[^ ]｜[^ ][^ ｜]*) ?|[^ ]+)')
    _是空白 = re.compile(r'[^\S\n]+')
    _是分字符號 = re.compile('{}+'.format(分字符號))
    _是數字 = set('0123456789')

    def __init__(self, hanlo, lomaji=''):
        # 愛產生新的物件
        全部型陣列, 型巢狀輕聲陣列 = self._拆句做巢狀詞(hanlo)
        全部音陣列, 音巢狀輕聲陣列 = self._拆句做巢狀詞(lomaji)
        # 對齊拆開的型、音
        內底詞 = self._對齊型音處理刪節號(
            全部型陣列, 全部音陣列,
            型巢狀輕聲陣列, 音巢狀輕聲陣列,
            hanlo, lomaji
        )

    def _對齊型音處理刪節號(
        self,
        型巢狀陣列, 音巢狀陣列, 型輕聲巢狀陣列, 音輕聲巢狀陣列,
        型, 音,
    ):
        # 取得按照詞組成的型音巢狀陣列之後，將型音對齊成詞物件陣列
        詞陣列 = []
        第幾字 = 0
        第幾音 = 0
        # 先將型巢狀陣列改成一維陣列
        型陣列 = []
        型輕聲陣列 = []
        for 一型陣列 in 型巢狀陣列:
            型陣列 += 一型陣列
        for 一型陣列 in 型輕聲巢狀陣列:
            型輕聲陣列 += 一型陣列
        # 對齊
        while 第幾音 < len(音巢狀陣列):
            if (
                型陣列[第幾字:第幾字 + 2] == ['─', '─'] and
                音巢狀陣列[第幾音:第幾音 + 3] == [['─'], ['─']]
            ):
                詞陣列.append(
                    self._拆好陣列對齊詞物件(['──'], ['──'], [False])
                )
                第幾字 += 2
                第幾音 += 2
            elif (
                型陣列[第幾字:第幾字 + 2] == ['…', '…'] and
                音巢狀陣列[第幾音:第幾音 + 3] == [['.'], ['.'], ['.']]
            ):
                詞陣列.append(
                    self._拆好陣列對齊詞物件(['……'], ['...'], [False])
                )
                第幾字 += 2
                第幾音 += 3
            elif (
                型陣列[第幾字:第幾字 + 2] == ['…', '…'] and
                音巢狀陣列[第幾音:第幾音 + 2] == [['…'], ['…']]
            ):
                詞陣列.append(
                    self._拆好陣列對齊詞物件(['……'], ['……'], [False])
                )
                第幾字 += 2
                第幾音 += 2
            elif (
                型陣列[第幾字:第幾字 + 3] == ['.', '.', '.'] and
                音巢狀陣列[第幾音:第幾音 + 3] == [['.'], ['.'], ['.']]
            ):
                詞陣列.append(
                    self._拆好陣列對齊詞物件(['...'], ['...'], [False])
                )
                第幾字 += 3
                第幾音 += 3
            else:
                # 對齊型音 組成詞物件
                #
                # 取得一个詞的音和型
                詞的音 = 音巢狀陣列[第幾音]
                音詞長 = len(詞的音)
                詞的型 = 型陣列[第幾字:第幾字 + 音詞長]
                型詞長 = len(詞的型)
                # 確定該詞的音kah該詞的型長度相kang5
                # 如果字數不合 取得的詞的型 = 非預期的全部型陣列
                # => 型：[美] 音：[sui2, sui2]
                if 音詞長 != 型詞長:
                    raise 解析錯誤(
                        '詞組內底的型「{}」比音「{}」少！配對結果：{}'.format(
                            型, 音, str(詞陣列)
                        )
                    )
                # 取得一个詞的音和型的輕聲符
                詞輕聲陣列 = []
                音輕聲陣列 = 音輕聲巢狀陣列[第幾音]
                詞的型輕聲 = 型輕聲陣列[第幾字:第幾字 + 音詞長]
                for 輕聲索引, 音輕聲 in enumerate(音輕聲陣列):
                    型輕聲 = 詞的型輕聲[輕聲索引]
                    詞輕聲陣列.append(音輕聲 or 型輕聲)
                try:
                    詞陣列.append(
                        self._拆好陣列對齊詞物件(詞的型, 詞的音, 詞輕聲陣列)
                    )
                except 解析錯誤 as 錯誤:
                    raise 解析錯誤(
                        '{0}\n配對結果：{3}\n對齊「{1}」kah「{2}」'.format(
                            錯誤, 型, 音, str(詞陣列)
                        )
                    )
                第幾字 += 型詞長
                第幾音 += 1
        # 確定全部的音都巡過了後，全部的型嘛攏有巡著、無tshun。
        # => 型：[美, 麗] 音：[sui2]
        if 第幾字 < len(型陣列):
            raise 解析錯誤(
                '詞組內底的型「{}」比音「{}」濟！配對結果：{}'.format(
                    型, 音, str(詞陣列)
                )
            )
        return 詞陣列

    def _拆句做字(self, 語句):
        return self._句分析(語句)[0]

    def _拆句做巢狀詞(self, 語句):
        字陣列, 輕聲陣列, 佮後一个字無仝一个詞 = self._句分析(語句)
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

    def _句分析(self, 語句):
        狀態 = self._分析狀態()
        if 語句 == 分詞符號 or self._是空白.fullmatch(語句):
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
                    狀態.這馬字好矣清掉囥入去字陣列()
                    分字長度 = len(揣分字.group(0))
                    if 分字長度 == 1:
                        if not 狀態.敢有分析資料矣() or 頂一个是空白:
                            狀態.字陣列直接加一字(分字符號)
                            狀態.頂一字佮這馬的字無仝詞()
                        else:
                            狀態.頂一字佮這馬的字仝詞()
                            是連字符 = True
                            狀態.有連字符()
                    elif 分字長度 == 2:
                        是輕聲符號 = True
                        狀態.這陣是輕聲詞()
                    else:
                        for _ in range(分字長度):
                            狀態.字陣列直接加一字(分字符號)
                            狀態.頂一字佮這馬的字無仝詞()
                    位置 += 分字長度 - 1
                elif 字 == 分詞符號 or self._是空白.fullmatch(字):
                    狀態.這馬字好矣清掉囥入去字陣列()
                    狀態.頂一字佮這馬的字無仝詞()
                    if 頂一个是連字符:
                        狀態.字陣列直接加一字(分字符號)
                        狀態.頂一字佮這馬的字無仝詞()
                    if 頂一个是輕聲符號:
                        狀態.字陣列直接加一字(分字符號)
                        狀態.頂一字佮這馬的字無仝詞()
                        狀態.字陣列直接加一字(分字符號)
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
                # 音標後壁可能有聲調符號
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
                    if 字 == '•' and 狀態.上尾敢是o結尾():
                        狀態.這馬字加一个字元(字)
                    else:
                        狀態.這馬字好矣清掉囥入去字陣列()
                        狀態.頂一字佮這馬的字無仝詞()
                        狀態.字陣列直接加一字(字)
                        狀態.頂一字佮這馬的字無仝詞()
                else:
                    if 狀態.這馬字敢全部攏數字():
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
            狀態.字陣列直接加一字(分字符號)
            狀態.頂一字佮這馬的字無仝詞()
        if 頂一个是輕聲符號:
            狀態.字陣列直接加一字(分字符號)
            狀態.頂一字佮這馬的字無仝詞()
            狀態.字陣列直接加一字(分字符號)
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


class Tsoo():
    內底詞 = None

    def __init__(self, han, lo=''):
        # 愛產生新的物件
        if isinstance(han, str):
            self.kianlip(han, lo)
        elif isinstance(han, list):
            self.kianlip_su_tinliat(han)

    def __eq__(self, 別个):
        return isinstance(別个, Tsoo) and self.內底詞 == 別个.內底詞

    def __hash__(self):
        return hash(tuple(self.內底詞))

    def __str__(self):
        return '組：{0}'.format(self.內底詞)

    def __repr__(self):
        return self.__str__()

    def kianlip(self, hanbun, lobun):
        self.內底詞 = ''
        if not isinstance(hanbun, str):
            raise 型態錯誤(
                '傳入來的型毋是字串：型＝{0}，音＝{1}'.format(
                    str(hanbun), str(lobun))
            )
        if not isinstance(lobun, str):
            raise 型態錯誤(
                '傳入來的音毋是字串：型＝{0}，音＝{1}'.format(
                    str(hanbun), str(lobun))
            )
        全部型陣列, 型巢狀輕聲陣列 = self._拆句做巢狀詞(hanbun)
        全部音陣列, 音巢狀輕聲陣列 = self._拆句做巢狀詞(lobun)
        self.內底詞 = self._對齊型音處理刪節號(
            全部型陣列, 全部音陣列,
            型巢狀輕聲陣列, 音巢狀輕聲陣列,
            hanbun, lobun,
        )

    def kianlip_su_tinliat(self, sutin):
        # 愛產生新的物件
        try:
            self.內底詞 = []
            for 詞物件 in sutin:
                if not isinstance(詞物件, Su):
                    raise 型態錯誤(
                        '詞陣列內底有毋是詞的：詞陣列＝{0}，詞物件＝{1}'.format(
                            str(sutin), str(詞物件))
                    )
                self.內底詞.append(Su(詞物件.內底字))
        except TypeError as 問題:
            raise 型態錯誤('傳入來的詞陣列毋法度疊代：{0}，問題：{1}'
                       .format(str(sutin), 問題))

    def 看語句(self):
        詞的型陣列 = []
        頂一詞上尾是羅馬字 = False
        for 一詞 in self.內底詞:
            詞型 = 一詞.看語句()
            if (
                頂一詞上尾是羅馬字
                and (敢是拼音字元(詞型[0]) or 詞型[0].isdigit() or 詞型[0] == 分字符號)
            ):
                詞的型陣列.append(分詞符號)
            # 輕聲詞 '--sui2' => '--sui2 '
            # 一般詞 'sui2' => 'sui2 '
            詞的型陣列.append(詞型)
            頂一詞上尾是羅馬字 = 敢是拼音字元(詞型[-1]) or 詞型[-1].isdigit()
        return ''.join(詞的型陣列)

    def 看型(self, 物件分字符號='', 物件分詞符號='', 物件分句符號=''):
        詞的型 = []
        for 一詞 in self.內底詞:
            詞的型.append(一詞.看型(物件分字符號, 物件分詞符號))
        return 物件分詞符號.join(詞的型)

    def 看音(self, 物件分字符號=分字符號, 物件分詞符號=分詞符號, 物件分句符號=分詞符號):
        詞的音 = []
        for 一詞 in self.內底詞:
            音標 = 一詞.看音(物件分字符號, 物件分詞符號)
            if 音標 != 無音:
                詞的音.append(音標)
        return 物件分詞符號.join(詞的音)

    def 看分詞(self):
        詞的音 = []
        for 一詞 in self.內底詞:
            音標 = 一詞.看分詞()
            if 音標 != '':
                詞的音.append(音標)
        return 分詞符號.join(詞的音)

    def 綜合標音(self, 語言綜合標音):
        詞組綜合標音 = {}
        for 一詞 in self.內底詞:
            for 欄位, 內容 in 一詞.綜合標音(語言綜合標音)[0].items():
                try:
                    詞組綜合標音[欄位].append(內容)
                except KeyError:
                    詞組綜合標音[欄位] = [內容]
        結果 = {}
        for 欄位, 內容 in 詞組綜合標音.items():
            結果[欄位] = ' '.join(內容)
        return [結果]

    def 篩出字物件(self):
        字陣列 = []
        for 詞物件 in self.內底詞:
            字陣列.extend(詞物件.篩出字物件())
        return 字陣列

    def 網出詞物件(self):
        return list(self.內底詞)

    def 轉音(self, 音標工具, 函式='預設音標'):
        # 逐个函式攏愛產生新的物件
        新組物件 = Tsoo()
        for 詞物件 in self.內底詞:
            新組物件.內底詞.append(詞物件.轉音(音標工具, 函式))
        return 新組物件


class _Punso:
    def kianlip(self, hanbun, lobun):
        if lobun == 無音:
            lobun = hanbun
        self.內底集 = [Tsip(hanbun, lobun)]

    def kianlip_tsip_tinliat(self, tsiptin):
        try:
            self.內底集 = []
            for 集物件 in tsiptin:
                if not isinstance(集物件, Tsip):
                    raise 型態錯誤(
                        '集陣列內底有毋是集的：集陣列＝{0}，集物件＝{1}'
                        .format(str(tsiptin), str(集物件))
                    )
                self.內底集.append(Tsip(集物件.內底組))
        except TypeError as 問題:
            raise 型態錯誤(
                '傳入來的集陣列毋法度疊代：{0}，問題：{1}'
                .format(str(tsiptin), 問題)
            )

    def __eq__(self, 別个):
        return isinstance(別个, Ku) and self.內底集 == 別个.內底集

    def __str__(self):
        return '句：{0}'.format(self.內底集)

    def __repr__(self):
        return self.__str__()

    def hanji(self, 物件分字符號='', 物件分詞符號=''):
        集的型 = []
        for 一集 in self.內底集:
            集的型.append(一集.看型(物件分字符號, 物件分詞符號))
        return 物件分詞符號.join(集的型)

    def lomaji(self, 物件分字符號=分字符號, 物件分詞符號=分詞符號):
        集的音 = []
        for 一集 in self.內底集:
            音標 = 一集.看音(物件分字符號, 物件分詞符號)
            if 音標 != 無音:
                集的音.append(音標)
        return 物件分詞符號.join(集的音)

    def hunsu(self):
        return

    def 篩出字物件(self):
        字陣列 = []
        for 集物件 in self.內底集:
            字陣列.extend(集物件.篩出字物件())
        return 字陣列

    def 網出詞物件(self):
        詞陣列 = []
        for 集物件 in self.內底集:
            詞陣列.extend(集物件.網出詞物件())
        return 詞陣列

    def 轉音(self, 音標工具, 函式='預設音標'):
        新句物件 = Ku()
        for 集物件 in self.內底集:
            新句物件.內底集.append(集物件.轉音(音標工具, 函式))
        return 新句物件
