from unittest.case import TestCase
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤

class 集單元試驗(TestCase):

    def test_集烏白傳(self):
        self.assertRaises(型態錯誤, Tsip, None)
        self.assertRaises(型態錯誤, Tsip, [None])
        self.assertRaises(型態錯誤, Tsip, ['sui2'])

    def test_看集(self):
        型 = '恁老母ti3佗位'
        音 = 'lin1 lau3 bu2 ti3 to1 ui7'
        集物件 = Tsip(型, 音)
        self.assertEqual(集物件.看型(), 型)
        self.assertEqual(集物件.看音(), 音)
        分詞 = '恁｜lin1 老｜lau3 母｜bu2 ti3｜ti3 佗｜to1 位｜ui7'
        self.assertEqual(集物件.看分詞(), 分詞)

    def test_看集內底有兩組以上(self):
        型 = '恁老母ti3佗位'
        音 = 'lin1 lau3 bu2 ti3 to1 ui7'
        集物件 = Tsip([Tsoo(型, 音), Tsoo(型, 音)])
        self.assertRaises(解析錯誤, 集物件.看型)
        self.assertRaises(解析錯誤, 集物件.看音)
        self.assertRaises(解析錯誤, 集物件.看分詞)
