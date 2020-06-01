# -*- coding: utf-8 -*-
from kesi.susia.POJ import tsuanPOJ
from kesi.susia.TL import tsuanTL


class Ji:

    def __init__(self, hanlo, lomaji=None, si_khinsiann=False):
        print('init ji.hanlo=', hanlo)
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
        print('hanlo of ji.TL() at first=', self.hanlo)
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
