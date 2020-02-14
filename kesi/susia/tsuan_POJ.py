import unicodedata
import re

from kesi.susia.TL import KONGKE_SIANNBO, KONGKE_UNBO
from kesi.susia.臺灣閩南語羅馬字拼音轉白話字模組 import 臺羅數字調轉白話字, TIAUHO_TIAUHU_PIO

SI_TSUAN_TUASIA = 'SI_TSUAN_TUASIA'
SI_TSUAN_SIOSIA = 'SI_TSUAN_SIOSIA'
SI_THAU_TUASIA = 'SI_THAU_TUASIA'


def tsuanPOJ(bun):
    si_khinsiann = bun.startswith('--')
    if si_khinsiann:
        bun = bun.replace('--', '')
    try:
        siann, un, tiau, tuasiosia = thiah(bun)
    except SuSiaTshoNgoo as e:
        print('Exception of tsuanPOJ(): ', e)
        return bun
    poj = kapPOJ(siann, un, tiau)
    kiatko = tshiau_tuasiosia(tuasiosia, poj)
    if si_khinsiann:
        kiatko = '--{}'.format(kiatko)
    return kiatko


def khuann_tuasiosia(bun):
    latin = bun.replace('ⁿ', '')
    if latin.isupper():
        return SI_TSUAN_TUASIA
    elif latin.islower():
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

    siannun_n = thong_n(siannun)
    tuasiosia = khuann_tuasiosia(siannun_n)

    siannun_se = siannun_n.lower()
    kongke = tsuan_kongke(siannun_se)
    siann, un = thiah_siannun(kongke)

    return siann, un, tiau, tuasiosia


def theh_sianntiau(lomaji):
    nfd = unicodedata.normalize('NFD', lomaji)
    # Guân-té tō sòo-jī-tiāu
    if nfd[-1].isdigit():
        return nfd[:-1], tiauho_tsuan_tiauhu(nfd[-1])
    # Thuân-thóng-tiāu
    pitui = re.search(
        '\u0301|\u0300|\u0302|\u030c|\u0304|\u030d|\u030b|\u0306', nfd)
    try:
        tiau = pitui.group(0)
    except AttributeError:
        tiau = ''  # 1 or 4
    siannun = nfd.replace(tiau, '')
    return siannun, tiau


def thong_n(siannun):
    phinnim = re.sub('([a-z])(N)(h?)', r'\1ⁿ\3', siannun)
    phinnim = phinnim.replace('ᴺ', 'ⁿ')
    return phinnim


def tsuan_kongke(siannun):
    kiatko = (
        siannun
        .replace('ch', 'ts')
        .replace('ou', 'oo')
        .replace('o͘', 'oo')
        .replace('ⁿ', 'nn')
        .replace('oa', 'ua')
        .replace('oe', 'ue')
        .replace('eng', 'ing')
        .replace('ek', 'ik')
    )
    return kiatko


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


def tiauho_tsuan_tiauhu(tiauho):
    return TIAUHO_TIAUHU_PIO[tiauho]


class SuSiaTshoNgoo(ValueError):
    pass
