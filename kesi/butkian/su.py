# -*- coding: utf-8 -*-
from kesi.butkian.kongiong import LIAN_JI_HU, si_lomaji
from kesi.butkian.kongiong import KHIN_SIANN_HU


class Su:

    def __init__(self):
        self._ji = []

    def __iter__(self):
        yield from self._ji

    def __len__(self):
        return len(self._ji)

    def __eq__(self, other):
        return self._ji == other._ji

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

    @property
    def kiphanlo(self):
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

        for ji in self:
            jihanlo = ji.kiphanlo
            if ting_ji_si_lomaji and si_lomaji(jihanlo[0]):
                " L, L -> 'L-L' "
                if ji.si_khinsiann:
                    buntin.append(KHIN_SIANN_HU)
                else:
                    buntin.append(LIAN_JI_HU)
            buntin.append(jihanlo)
            ting_ji_si_lomaji = si_lomaji(jihanlo[-1])
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

    KIP = TL
