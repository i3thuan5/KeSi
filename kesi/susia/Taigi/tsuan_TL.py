import unicodedata

from kesi.susia.Taigi.TL import TL_TIAUHO_UN
from kesi.susia.Taigi.tsuan_POJ import thiah, tshiau_tuasiosia, SuSiaTshoNgoo

# SI_TSUAN_TUASIA = 'SI_TSUAN_TUASIA'
# SI_TSUAN_SIOSIA = 'SI_TSUAN_SIOSIA'
# SI_THAU_TUASIA = 'SI_THAU_TUASIA'


def tsuanTL(bun):
    # si_khinsiann = bun.startswith('--')
    # if si_khinsiann:
    #     bun = bun.replace('--', '')
    try:
        siann, un, tiau, tuasiosia = thiah(bun)
    except SuSiaTshoNgoo as e:
        print('tsuanPOJ Exception=', e)
        return bun
    print('tsuanTL siann={}, un={}, tiau={}, tuasiosia={}'.format(
        siann, un, tiau, tuasiosia))
    tailo = kapTL(siann, un, tiau)
    kiatko = tshiau_tuasiosia(tuasiosia, tailo)
    # if si_khinsiann:
    #     kiatko = '--{}'.format(kiatko)
    return kiatko


def kapTL(siann, un, tiau):
    un = tau_tiauhu(un, tiau)
    print('tau_tiauhu=', un)
    return unicodedata.normalize(
        'NFC', siann + un)


def tau_tiauhu(un, tiau):
    lomaji = ''
    if 'a' in un:
        lomaji = un.replace('a', 'a' + tiau)
    elif 'oo' in un:
        lomaji = un.replace('oo', 'o' + tiau + 'o')
    elif 'e' in un:
        lomaji = un.replace('e', 'e' + tiau)
    elif 'o' in un:
        lomaji = un.replace('o', 'o' + tiau)
    elif 'ui' in un:
        lomaji = un.replace('i', 'i' + tiau)
    elif 'iu' in un:
        lomaji = un.replace('u', 'u' + tiau)
    elif 'i' in un:
        lomaji = un.replace('i', 'i' + tiau)
    elif 'u' in un:
        lomaji = un.replace('u', 'u' + tiau)
    #     該標調的字 = 'o͘'
    # elif re.search('[aeiou]{2}', un):
    #     # 雙元音
    #     if un[0] == 'i':
    #         該標調的字 = un[1]
    #     elif un[1] == 'i':
    #         該標調的字 = un[0]
    #     elif len(un) == 2:
    #         # xx
    #         該標調的字 = un[0]
    #     elif un[-1] == 'ⁿ' and un[-2:] != 'hⁿ':
    #         # xxⁿ
    #         該標調的字 = un[0]
    #     else:
    #         # xxn, xxng, xxhⁿ
    #         該標調的字 = un[1]
    # elif re.search('[aeiou]', un):
    #     # 單元音
    #     該標調的字 = un[0]
    # elif 'ng' in un:
    #     # ng, mng
    #     該標調的字 = 'n'
    # elif 'm' in un:
    #     該標調的字 = 'm'
    return lomaji
