# -*- coding: utf-8 -*-
# 瀏覽器希望無音愛有空白，但是處理標音時希望較好認
import unicodedata
import re
from unicodedata import normalize


LIAN_JI_HU = '-'
KHIN_SIANN_HU = '--'
# 句中是為著加速標音
句中標點符號 = {
    '、', '﹑', '､', '-', '—', '~', '～',
    '·', '‧',  # 外國人名中間
    "'", '＇', '"', '‘', '’', '“', '”', '〝', '〞', '′', '‵',
    '「', '」', '｢', '｣', '『', '』',
    '【', '】', '〈', '〉', '《', '》', '（', '）', '＜', '＞',
    '(', ')', '<', '>', '[', ']', '{', '}',
    '+', '*', '/', '=', '^', '＋', '－', '＊', '／', '＝', '$', '#', '#',
    ':', '：', '﹕', '–', '—', '―', '─', '──', '｜', '︱',
    '•',
}

# 斷句是考慮著翻譯，閣有語音合成愛做的正規化
斷句標點符號 = (
    {'\n', } |
    {'，', '。', '．', '！', '？', '…', '……', '...', } |
    {',', '.', '!', '?', } |
    {'﹐', '﹒', '﹗', '﹖', } |
    {';', '；', '﹔', }
)

NON_PRINTABLE_CHARS = re.compile(
    r'[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f-\u009f]'
)


# Siann-tiāu
HAGFA_TIAU = {
    '', 'ˊ', 'ˋ', 'ˇ', '+', '^'
}
NGOO_SIU_LE = {
    '0': '˙', '1': '', '2': 'ˋ', '3': '˪',
    '4': '', '5': 'ˊ', '6': '˫', '7': '˫',
    '8': '㆐', '9': '^', '10': '㆐'
}

# 造字
KIP_TSOJI = {
    '\uE701': '\U0002A736',
    '\uF5E9': '\U0002B74F',
    '\uE35C': '\U0002B75B',
    '\uF5EA': '\U0002B77A',
    '\uF5EE': '\U0002B77B',
    '\uE703': '\U0002B7BC',
    '\uF5EF': '\U0002B7C2',
    '\uE705': '\U0002C9B0',
    '\uF5E7': '\U000308FB',
}

聲調符號 = (
    HAGFA_TIAU |
    set(NGOO_SIU_LE.values())
) - {''}


標點符號 = 句中標點符號 | 斷句標點符號

組字式符號 = '⿰⿱⿲⿳⿴⿵⿶⿷⿸⿹⿺⿻⿿'

# Ll　小寫， Lu　大寫， Md　數字， Mn　有調號英文，Lo　其他, So 組字式符號…
_統一碼羅馬字類 = {'Ll', 'Lu', 'Mn'}


def si_lomaji(jiguan):
    return 敢是拼音字元(jiguan) or jiguan.isdigit()


def 敢是拼音字元(字元):
    try:
        種類 = unicodedata.category(字元)
    except TypeError:
        return False
    return 種類 in _統一碼羅馬字類 or 字元 in ['ⁿ', "'", '_', 'ᴺ', ]


def 敢是注音符號(字元):
    return unicodedata.name(字元, '').startswith('BOPOMOFO LETTER')


def normalize_kautian(taibun):
    for ji_kautian, ji_unicode in KIP_TSOJI.items():
        taibun = taibun.replace(ji_kautian, ji_unicode)
    return taibun


def normalize_taibun(taibun):
    taibun = re.sub(NON_PRINTABLE_CHARS, ' ', taibun)
    taibun = normalize_kautian(taibun)
    taibun = normalize('NFC', taibun)
    return taibun
