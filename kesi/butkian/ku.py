from kesi.butkian.kongiong import 分詞符號, 分字符號, 無音
from kesi.butkian.kongling import KongLing
from kesi.butkian.tsip import Tsip
from kesi.kaisik.tsho_ngoo import 型態錯誤


class Ku(KongLing):
    內底集 = None

    def __init__(self, han, lo=''):
        # 愛產生新的物件
        if isinstance(han, str):
            self.kianlip(han, lo)
        elif isinstance(han, list):
            self.kianlip_tsip_tinliat(han)
    
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

    def taibun(self):
        集的型 = []
        for 一集 in self.內底集:
            集的型.append(一集.看語句())
        return 分詞符號.join(集的型)

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
