# -*- coding: utf-8 -*-
from kesi.susia.POJ import tsuanPOJ
from kesi.susia.TL import tsuanTL
from kesi.butkian.kongiong import KHIN_SIANN_HU
from kesi.butkian.kongiong import si_lomaji


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

    def __eq__(self, other):
        return (
            self.hanlo == other.hanlo
            and self.lomaji == other.lomaji
            and self.si_khinsiann == other.si_khinsiann
        )

    @property
    def kiphanlo(self):
        if self.si_khinsiann and not si_lomaji(self.hanlo[2]):
            return self.hanlo[2:]
        return self.hanlo

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

    KIP = TL

    @property
    def si_khinsiann(self):
        return self.hanlo.startswith(KHIN_SIANN_HU)
