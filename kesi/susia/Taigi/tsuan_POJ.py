import unicodedata
import re

from kesi.susia.Taigi.TL import KONGKE_SIANNBO, KONGKE_UNBO
from kesi.susia.Taigi.臺灣閩南語羅馬字拼音轉白話字模組 import 臺羅數字調轉白話字

SI_TSUAN_TUASIA = 'SI_TSUAN_TUASIA'
SI_TSUAN_SIOSIA = 'SI_TSUAN_SIOSIA'
SI_THAU_TUASIA = 'SI_THAU_TUASIA'


def tsuanPOJ(bun):
    tuasiosia = khuann_tuasiosia(bun)
    # Kong-ke: siann, un, tiau
    try:
        siann, un, tiau = thiah(bun.lower())
    except SuSiaTshoNgoo as e:
        print('tsuanPOJ Exception=', e)
        return bun
    # tsuan
    poj = kapPOJ(siann, un, tiau)
    return tshiau_tuasiosia(tuasiosia, poj)


def khuann_tuasiosia(bun):
    if bun.isupper():
        return SI_TSUAN_TUASIA
    elif bun.islower():
        return SI_TSUAN_SIOSIA
    else:
        return SI_THAU_TUASIA


def tshiau_tuasiosia(tuasiosia, bun):
    if tuasiosia == SI_TSUAN_TUASIA:
        return bun.upper()
    elif tuasiosia == SI_TSUAN_SIOSIA:
        return bun.lower()
    else:
        return bun.capitalize()


def thiah(lomaji):
    siannun, tiau = theh_sianntiau(lomaji)
    print('siannun, tiau=', siannun, tiau)
    siann, un = thiah_siannun(siannun)
    # 音標是著的, 無調號音標 = _分離閏號聲調(音標)
    # 聲韻符合, 聲, 韻 = _揣聲韻(無調號音標)
    # _si_haphuat_susia(聲韻符合, 聲, 韻, 調)

    return siann, un, tiau


def theh_sianntiau(lomaji):
    nfd = unicodedata.normalize('NFD', lomaji)
    # Guân-té tō sòo-jī-tiāu
    if nfd[-1].isdigit():
        return nfd[:-1], nfd[-1]
    # Thuân-thóng-tiāu
    pitui = re.search(
        '\u0301|\u0300|\u0302|\u030c|\u0304|\u030d|\u030b|\u0306', nfd)
    tiau = pitui.group(0)
    siannun = nfd.replace(tiau, '')
    return siannun, tiau


def thiah_siannun(無調號音標):
    for 所在 in range(len(無調號音標)):
        聲母 = 無調號音標[:所在]
        if 聲母.lower() in KONGKE_SIANNBO:
            韻母 = 無調號音標[所在:]
            if 韻母.lower() in KONGKE_UNBO:
                return 聲母, 韻母
    raise SuSiaTshoNgoo('Bô tsit-khuán im-tsiat')


def kapPOJ(siann, un, tiau):
    return unicodedata.normalize(
        'NFC',
        臺羅數字調轉白話字.轉白話字(siann, un, tiau)
    )


class SuSiaTshoNgoo(ValueError):
    pass

    # def _si_haphuat_susia(聲韻符合, 聲, 韻, 調):
    # 	if not 聲韻符合:
    #         音標是著的 = False
    #     elif 韻[-1] in ['p', 't', 'k', 'h']:
    #         if 調 is None:
    #             調 = '4'
    #         elif 調 not in {'4', '8', '10', '0'}:  # 中高低調入聲、輕聲
    #             音標是著的 = False
    #     else:
    #         if 調 is None:
    #             調 = '1'
    #         elif 調 in {'4', '8', '10'}:
    #             音標是著的 = False
    #         elif len(調) == 1:
    #             pass
    #         else:
    #             音標是著的 = False
    #     if 聲 in ['m', 'n', 'ng']:
    #         if 韻 not in ['ng', 'ngh'] and ('n' in 韻 or 'm' in 韻):
    #             音標是著的 = False
    #         elif 韻[-1] in ['p', 't', 'k']:
    #             音標是著的 = False
    #         elif 韻 == 'o':
    #             音標是著的 = False
    #     if 聲 in ['b', 'l', 'g']:
    #         if 'nn' in 韻:
    #             音標是著的 = False
    #     return 音標是著的

    # def _thiah_un(self, 音標):
    #     一開始 = True
    #     字元陣列 = []
    #     for 字元 in 音標:
    #         if 一開始:
    #             字元 = 字元.lower()
    #             一開始 = False
    #         if 字元 == 'o͘':
    #             字元 = 'oo'
    #         elif 字元 == 'N':
    #             字元 = 'nn'
    #         elif 字元 == 'ⁿ':
    #             字元 = 'nn'
    #         else:
    #             字元 = 字元.lower()
    #         字元陣列.append(字元)
    #     return ''.join(字元陣列)

    # def _分離閏號聲調(self, 音標):
    #     # Ôa thiah-tsò Oa, 5
    #     # Oa5 thiah-tsò Oa, 5
    #     無調號音標 = ''
    #     前一字元 = ''
    #     前一音調 = ''
    #     愛結束矣 = False
    #     音標是著的 = True
    #     for 字元 in self.音標:
    #         if 前一音調 == '1' and 字元 == '0':
    #             self.調 = '10'
    #             愛結束矣 = True
    #         elif 字元.isdigit():
    #             if self.調 is None:
    #                 self.調 = 字元
    #             else:
    #                 self.調 += 字元
    #             愛結束矣 = True
    #             前一音調 = 字元
    #         elif 愛結束矣:
    #             音標是著的 = False
    #         elif 字元 in self.聲調符號表:
    #             無調字元, self.調 = self.聲調符號表[字元]
    #             無調號音標 += 前一字元 + 無調字元
    #             前一字元 = ''
    #         elif 前一字元 + 字元 in self.聲調符號表:
    #             無調字元, self.調 = self.聲調符號表[前一字元 + 字元]
    #             無調號音標 += 無調字元
    #             前一字元 = ''
    #         elif 無調號音標[-1:] + 前一字元 + 字元 in self.聲調符號表:
    #             無調字元, self.調 = self.聲調符號表[無調號音標[-1:] + 前一字元 + 字元]
    #             無調號音標 = 無調號音標[:-1] + 無調字元
    #             前一字元 = ''
    #         else:
    #             無調號音標 += 前一字元
    #             前一字元 = 字元
    #     無調號音標 += 前一字元
    #     無調號音標 = 無調號音標.replace('o͘', 'oo').replace('o•', 'oo')
    #     return 音標是著的, 無調號音標
