# -*- coding: utf-8 -*-
from kesi.susia.POJ import tsuanPOJ
from kesi.susia.TL import tsuanTL
from kesi.butkian.kongiong import KHIN_SIANN_HU


class Ji:

    def __init__(self, hanlo, lomaji=None, si_khinsiann=False):
        if si_khinsiann:
            self.hanlo = '--{}'.format(hanlo)
        else:
            if hanlo.startswith(KHIN_SIANN_HU):
                si_khinsiann = True
            self.hanlo = hanlo

        if lomaji and si_khinsiann:
            self.lomaji = '--{}'.format(lomaji)
        elif lomaji:
            self.lomaji = lomaji
        else:
            self.lomaji = self.hanlo
        self.si_khinsiann = si_khinsiann

    def POJ(self):
        if self.si_khinsiann:
            hanlo = self.hanlo[2:]
            lomaji = self.lomaji[2:]
        else:
            hanlo = self.hanlo
            lomaji = self.lomaji
        return Ji(
            tsuanPOJ(hanlo), tsuanPOJ(lomaji),
            si_khinsiann=self.si_khinsiann
        )

    def TL(self):
        if self.si_khinsiann:
            hanlo = self.hanlo[2:]
            lomaji = self.lomaji[2:]
        else:
            hanlo = self.hanlo
            lomaji = self.lomaji
        return Ji(
            tsuanTL(hanlo), tsuanTL(lomaji),
            si_khinsiann=self.si_khinsiann
        )
