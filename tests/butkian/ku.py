from unittest.case import TestCase
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from kesi.butkian.ku import Ku


class KuTanGuanTshiGiam(TestCase):

    def test_句烏白傳(self):
        self.assertRaises(型態錯誤, Ku, None)
        self.assertRaises(型態錯誤, Ku, [None])
        self.assertRaises(型態錯誤, Ku, ['sui2'])


class HanLoTshiGiam(TestCase):
    def test_tsua(self):
        hanlo = '恁老母ti3佗位'
        but = Ku(hanlo)
        self.assertEqual(but.taibun(), hanlo)
        self.assertEqual(but.hanji(), hanlo)
        self.assertEqual(but.lomaji(), hanlo)

class TsuanLoTshiGiam(TestCase):
    def test_kah_tsuanlo(self):
        hanlo = '恁老母ti3佗位'
        tsuanlo = 'lin1 lau3 bu2 ti3 to1 ui7'
        but = Ku(hanlo, tsuanlo)
        self.assertEqual(but.taibun(), hanlo)
