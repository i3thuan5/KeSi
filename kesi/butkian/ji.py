# -*- coding: utf-8 -*-
from kesi.kaisik.tsho_ngoo import 解析錯誤, 型態錯誤
from kesi.butkian.su import Su
from kesi.susia.Taigi.tsuan_POJ import tsuanPOJ
from kesi.susia.Taigi.tsuan_TL import tsuanTL


class Ji:

    def __init__(self, hanlo, lomaji=None, si_khinsiann=False):
        if si_khinsiann:
            self.hanlo = '--{}'.format(hanlo)
        else:
            self.hanlo = hanlo

        if lomaji and si_khinsiann:
            self.lomaji = '--{}'.format(lomaji)
        elif lomaji:
            self.lomaji = lomaji
        else:
            self.lomaji = self.hanlo
        self.si_khinsiann = si_khinsiann

    def POJ(self):
        return Ji(
            tsuanPOJ(self.hanlo), tsuanPOJ(self.lomaji),
            si_khinsiann=self.si_khinsiann
        )

    def TL(self):
        return Ji(
            tsuanTL(self.hanlo), tsuanTL(self.lomaji),
            si_khinsiann=self.si_khinsiann
        )


def ps():
    class _Punso:

        def __init__(self, 型, 音=無音, 輕聲標記=False):
            if 型 == '':
                raise 解析錯誤('傳入來的型是空的！')
            try:
                型是標點 = (型 in 標點符號)
            except TypeError:
                raise 型態錯誤('型音一定愛是string抑是tuple！「{}」佮「{}」'.format(型, 音))
            try:
                音.__iter__
            except AttributeError:
                raise 型態錯誤('音一定愛是iterative！「{}」佮「{}」'.format(型, 音))
            try:
                音是標點 = (音 in 標點符號)
            except TypeError:
                pass
            else:
                if (
                    not isinstance(型, tuple) and
                    音 not in [無音, (None,)] and
                    (型是標點 ^ 音是標點)
                ):
                    raise 解析錯誤('型佮音干焦一个是標點符號！「{}」佮「{}」'.format(型, 音))

            # 判斷輕聲
            self.輕聲標記 = 輕聲標記
            self.型 = 型
            self.音 = 音

        def 有音(self):
            return self.音 != 無音 and self.音 not in 標點符號

        def __eq__(self, 別个):
            return (
                isinstance(別个, Ji)
                and self.型 == 別个.型 and self.音 == 別个.音
                and self.輕聲標記 == 別个.輕聲標記
            )

        def __hash__(self):
            return hash((self.型, self.音))

        def __str__(self):
            return '字：{0} {1}'.format(self.型, self.音)

        def __repr__(self):
            return self.__str__()

        def 看語句(self):
            return self.型

        def 看型(self, 物件分字符號='', 物件分詞符號='', 物件分句符號=''):
            return self.型

        def 看音(self, 物件分字符號=分字符號, 物件分詞符號=分詞符號, 物件分句符號=分詞符號):
            return self.音

        def 看分詞(self):
            return Su([self]).看分詞()

        def 敢有輕聲標記(self):
            return self.輕聲標記 or self.音.startswith('0')

        def 敢是標點符號(self):
            return (
                self.型 in 標點符號 and
                (self.音 in 標點符號 or self.音 == 無音)
            )

        def 綜合標音(self, 語言綜合標音):
            return 語言綜合標音(self).轉json格式()

        def 篩出字物件(self):
            return [self]

        def 網出詞物件(self):
            詞物件 = Su()
            詞物件.內底字.append(self)
            return [詞物件]

        def 轉音(self, 音標工具, 函式='預設音標'):
            # 逐个函式攏愛產生新的物件
            if self.音 != 無音:
                新音物件 = 音標工具(self.音)
                新音 = getattr(新音物件, 函式)()
                if 新音 is None:
                    if self.型 in 標點符號 and self.音 in 標點符號:
                        新音 = self.音
                    else:
                        新音 = self.音
            else:
                新音 = 無音
            新型物件 = 音標工具(self.型)
            新型預設音標 = getattr(新型物件, 函式)()
            if self.音.startswith(self.型) and isinstance(新音, str):
                新型 = 新音
            elif (
                新型物件 is not None and 新型預設音標 is not None and
                isinstance(新型預設音標, str)
            ):
                新型 = 新型預設音標
            else:
                新型 = self.型
            return Ji(新型, 新音, self.輕聲標記)

        def 音標敢著(self, 音標工具):
            if self.敢是標點符號():
                return True
            if self.音 == 無音:
                return True
            新音物件 = 音標工具(self.音)
            if 新音物件.音標 is None:
                return False
            return True

        def khóopih字(self):
            return self.__class__(self.型, self.音, self.輕聲標記)
