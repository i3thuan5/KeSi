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
    '9': '\u0306'
}


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
    if nfd[-1] in TIAUHO_TIAUHU_PIO:
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


class SuSiaTshoNgoo(ValueError):
    pass


class 臺羅數字調轉白話字():

    @classmethod
    def 轉白話字(cls, 聲, 韻, 調):
        白話字聲 = cls.轉白話字聲(聲)
        白話字韻 = cls.轉白話字韻(韻)
        白話字調 = cls.轉白話字調(調)
        白話字傳統調韻 = cls.白話字韻標傳統調(白話字韻, 白話字調)
        return (
            白話字聲 +
            白話字傳統調韻
        )

    @classmethod
    def 轉白話字聲(cls, 聲):
        白話字聲 = None
        if 聲 == 'ts':
            白話字聲 = 'ch'
        elif 聲 == 'tsh':
            白話字聲 = 'chh'
        else:
            白話字聲 = 聲
        return 白話字聲

    @classmethod
    def 轉白話字韻(cls, un):
        un = (
            un
            .replace('nn', 'ⁿ')
            .replace('oo', 'o͘')
            .replace('ua', 'oa')
            .replace('ue', 'oe')
            .replace('ing', 'eng')
            .replace('ik', 'ek')
        )
        return un

    @classmethod
    def 轉白話字調(cls, tiau):
        # ă a̋
        return tiau.replace('\u030b', '\u0306')

    @classmethod
    def 白話字韻標傳統調(cls, 白話字韻無調, 調):
        該標調的字 = ''
        if 'o͘' in 白話字韻無調:
            該標調的字 = 'o͘'
        elif re.search('(iau)|(oai)', 白話字韻無調):
            # 三元音 攏標佇a面頂
            該標調的字 = 'a'
        elif re.search('[aeiou]{2}', 白話字韻無調):
            # 雙元音
            if 白話字韻無調[0] == 'i':
                該標調的字 = 白話字韻無調[1]
            elif 白話字韻無調[1] == 'i':
                該標調的字 = 白話字韻無調[0]
            elif len(白話字韻無調) == 2:
                # xx
                該標調的字 = 白話字韻無調[0]
            elif 白話字韻無調[-1] == 'ⁿ' and 白話字韻無調[-2:] != 'hⁿ':
                # xxⁿ
                該標調的字 = 白話字韻無調[0]
            else:
                # xxn, xxng, xxhⁿ
                該標調的字 = 白話字韻無調[1]
        elif re.search('[aeiou]', 白話字韻無調):
            # 單元音
            該標調的字 = 白話字韻無調[0]
        elif 'ng' in 白話字韻無調:
            # ng, mng
            該標調的字 = 'n'
        elif 'm' in 白話字韻無調:
            該標調的字 = 'm'
        結果 = cls.加上白話字調符(白話字韻無調, 該標調的字, 調)
        return 結果

    @classmethod
    def 加上白話字調符(cls, 白話字韻無調, 標調字母, 調):
        return 白話字韻無調.replace(標調字母, 標調字母 + 調, 1)
