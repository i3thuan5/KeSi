# -*- coding: utf-8 -*-
from kesi.butkian.kongiong import LIAN_JI_HU, si_lomaji


class Su:

    def __init__(self):
        self._ji = []

    def __iter__(self):
        yield from self._ji

    def __len__(self):
        return len(self._ji)

    @property
    def hanlo(self):
        """
        會 kā 文本標準化：
        判斷愛先添連字符無
          H, H -> 'HH'
          H, L -> 'HL'
          L, H -> 'LH'
          L, L -> 'L-L'
          L, --L -> 'L--L'
        """
        buntin = []
        ting_ji_si_lomaji = False
        su_u_khinsiann = False

        for ji in self:
            jihanlo = ji.hanlo
            if ji.si_khinsiann:
                " Mài thinn liân-jī-hû "
                su_u_khinsiann = True
            elif ting_ji_si_lomaji and si_lomaji(jihanlo[0]):
                " L, L -> 'L-L' "
                buntin.append(LIAN_JI_HU)
            elif su_u_khinsiann:
                " --H, H -> '--H-H' "
                buntin.append(LIAN_JI_HU)
            buntin.append(jihanlo)
            ting_ji_si_lomaji = si_lomaji(jihanlo[-1])
        return ''.join(buntin)

    @property
    def lomaji(self):
        """
        會 kā 文本標準化：
        判斷愛先添連字符無
          H, H -> 'HH'
          H, L -> 'HL'
          L, H -> 'LH'
          L, L -> 'L-L'
          L, --L -> 'L--L'
        """
        buntin = []
        ting_ji_si_lomaji = False
        su_u_khinsiann = False

        for ji in self:
            jilomaji = ji.lomaji
            if ji.si_khinsiann:
                " Mài thinn liân-jī-hû "
                su_u_khinsiann = True
            elif ting_ji_si_lomaji and si_lomaji(jilomaji[0]):
                " L, L -> 'L-L' "
                buntin.append(LIAN_JI_HU)
            elif su_u_khinsiann:
                " --H, H -> '--H-H' "
                buntin.append(LIAN_JI_HU)
            buntin.append(jilomaji)
            ting_ji_si_lomaji = si_lomaji(jilomaji[-1])
        return ''.join(buntin)

    def thiam(self, ji):
        self._ji.append(ji)

    def POJ(self):
        sin_su = Su()
        for ji in self:
            sin_su.thiam(ji.POJ())
        return sin_su

    def TL(self):
        sin_su = Su()
        for ji in self:
            sin_su.thiam(ji.TL())
        return sin_su
