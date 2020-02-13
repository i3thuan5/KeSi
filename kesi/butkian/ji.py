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
