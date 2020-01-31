from unittest.case import TestCase
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤


class 組單元試驗(TestCase):

    def test_組烏白傳(self):
        self.assertRaises(型態錯誤, Tsoo, None)
        self.assertRaises(型態錯誤, Tsoo, [None])
        self.assertRaises(型態錯誤, Tsoo, ['sui2'])

    def test_看組孤字(self):
        型 = '恁老母ti3佗位！'
        音 = 'lin1 lau3 bu2 ti3 to1 ui7 !'
        組物件 = Tsoo(型, 音)
        self.assertEqual(組物件.看型(), 型)
        self.assertEqual(組物件.看音(), 音)
        分詞 = '恁｜lin1 老｜lau3 母｜bu2 ti3｜ti3 佗｜to1 位｜ui7 ！｜!'
        self.assertEqual(組物件.看分詞(), 分詞)

    def test_看組連字(self):
        型 = '恁老母ti3佗位！'
        音 = 'lin1 lau3-bu2 ti3 to1-ui7 !'
        組物件 = Tsoo(型, 音)
        self.assertEqual(組物件.看型(), 型)
        self.assertEqual(組物件.看音(), 音)
        分詞 = '恁｜lin1 老-母｜lau3-bu2 ti3｜ti3 佗-位｜to1-ui7 ！｜!'
        self.assertEqual(組物件.看分詞(), 分詞)

    def test_接受無音的詞(self):
        組物件 = Tsoo('')
        組物件.內底詞 = [
            Su('梅山'),
            Su('猴-災'),
            Su('鄉-公所', 'hiong1-kong1-soo2'),
            Su('tshiann2-lang5'),
            Su('趕-走', 'kuann2-tsau2'),
            Su('猴山', 'kau5-san1'),
        ]
        分詞答案 = '梅-山 猴-災 鄉-公-所｜hiong1-kong1-soo2 tshiann2-lang5 趕-走｜kuann2-tsau2 猴-山｜kau5-san1'
        self.assertEqual(組物件.看分詞(), 分詞答案)

    def test_有字無音的詞(self):
        公詞物件 = Su('')
        公詞物件.內底字 = [
            Ji('鄉'),
            Ji('公', 'kong1'),
            Ji('所'),
        ]
        鄉所詞物件 = Su('')
        鄉所詞物件.內底字 = [
            Ji('鄉', 'hiang1'),
            Ji('公'),
            Ji('所', 'soo2'),
        ]
        公鄉所組物件 = Tsoo('')
        公鄉所組物件.內底詞 = [公詞物件, 鄉所詞物件]
        self.assertEqual(
            公鄉所組物件.看分詞(),
            '鄉-公-所｜-kong1- 鄉-公-所｜hiang1--soo2'
        )
