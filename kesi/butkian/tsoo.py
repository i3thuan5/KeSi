# -*- coding: utf-8 -*-
from kesi.butkian.kongling import KongLing
from kesi.kaisik.tsho_ngoo import 型態錯誤, 解析錯誤
from kesi.butkian.kongiong import 分詞符號, 敢是拼音字元, 分字符號, 無音
from kesi.butkian.su import Su


class Tsoo(KongLing):
    內底詞 = None

    def __init__(self, han, lo=''):
        # 愛產生新的物件
        if isinstance(han, str):
            self.kianlip(han, lo)
        elif isinstance(han, list):
            self.kianlip_su_tinliat(han)

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

    def __eq__(self, 別个):
        return isinstance(別个, Tsoo) and self.內底詞 == 別个.內底詞

    def __hash__(self):
        return hash(tuple(self.內底詞))

    def __str__(self):
        return '組：{0}'.format(self.內底詞)

    def __repr__(self):
        return self.__str__()

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
