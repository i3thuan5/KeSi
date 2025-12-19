import unicodedata
import re

from kesi.susia.pio import KONGKE_SIANNBO, KONGKE_UNBO

SI_TSUAN_TUASIA = 'SI_TSUAN_TUASIA'
SI_TSUAN_SIOSIA = 'SI_TSUAN_SIOSIA'
SI_THAU_TUASIA = 'SI_THAU_TUASIA'


TIAUHO_TIAUHU_PIO = {
    '1': '',
    '2': '\u0301',
    '3': '\u0300',
    '4': '',
    '5': '\u0302',
    '6': '\u030c',
    '7': '\u0304',
    '8': '\u030d',
    '9': '\u0306',
}

# 聲調 → 聲調數字
TIAUHU_TIAUHO_PIO = {v: k for k, v in TIAUHO_TIAUHU_PIO.items() if v}


def khuann_tuasiosia(bun):
    latin = bun.replace('ⁿ', '')
    if latin.islower():
        return SI_TSUAN_SIOSIA
    elif latin[:1].isupper() and not latin[1:].isupper():
        return SI_THAU_TUASIA
    else:
        return SI_TSUAN_TUASIA


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
    if nfd[-1:] in TIAUHO_TIAUHU_PIO:
        return nfd[:-1], TIAUHO_TIAUHU_PIO[nfd[-1]]
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
        .replace('oonn', 'onn')
    )
    return kiatko


def thiah_siannun(無調號音標):
    for 所在 in range(len(無調號音標)):
        聲母 = 無調號音標[:所在]
        if 聲母.lower() in KONGKE_SIANNBO:
            韻母 = 無調號音標[所在:]
            if 韻母.lower() in KONGKE_UNBO:
                return 聲母, 韻母
    raise SuSiaTshoNgoo('Bô tsit-khuán im-tsiat: {}'.format(無調號音標))


class SuSiaTshoNgoo(ValueError):
    pass


def tsuan_ascii(bun):
    # ⁿ → nn, o͘ → oo
    return bun.replace('o͘', 'oo').replace('O͘', 'OO').replace('ⁿ', 'nn')


def tsuan_sooji_tiau(lomaji, ascii=False):
    # 聲調符號轉數字調
    if not lomaji:
        return lomaji

    # 輕聲 --
    if '--' in lomaji:
        parts = [tsuan_sooji_tiau(p, ascii) for p in lomaji.split('--')]
        return '--'.join(parts)

    # 逐音節處理
    kiatko = []
    for siannun_tiau in lomaji.split('-'):
        if not siannun_tiau:
            kiatko.append('')
            continue
        siannun, tiau = theh_sianntiau(siannun_tiau)
        if tiau in TIAUHU_TIAUHO_PIO:
            kiatko.append(siannun + TIAUHU_TIAUHO_PIO[tiau])
        elif _si_jipsiann(siannun):
            # 第4調：尾溜是 -p, -t, -k, -h
            kiatko.append(siannun + '4')
        else:
            kiatko.append(siannun)  # 1 聲無調符

    bun = '-'.join(kiatko)
    if ascii:
        bun = tsuan_ascii(bun)
    return bun


def _si_jipsiann(siannun):
    # 判斷敢是第4調（結尾是 p, t, k, h）
    siannun_lower = siannun.lower().replace('ⁿ', '').replace('nn', '')
    return siannun_lower.endswith(('p', 't', 'k', 'h'))
