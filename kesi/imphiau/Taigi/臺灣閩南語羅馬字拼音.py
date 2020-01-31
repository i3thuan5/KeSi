# -*- coding: utf-8 -*-
from 臺灣言語工具.音標系統.閩南語.教會系羅馬音標 import 教會系羅馬音標
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音轉方音符號吳守禮改良式模組 import 臺灣閩南語羅馬字拼音轉方音符號吳守禮改良式模組
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音轉音值模組 import 臺灣閩南語羅馬字拼音轉音值模組
from sys import stderr
from 臺灣言語工具.音標系統.閩南語.對照表 import 臺羅對白話字
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音轉白話字模組 import 臺羅轉白話字

臺灣閩南語羅馬字拼音聲母表 = {
    'p', 'ph', 'm', 'b',
    't', 'th', 'n', 'l',
    'k', 'kh', 'ng', 'g',
    'ts', 'tsh', 's', 'j',
    'h', '',
}
# 臺灣閩南語羅馬字拼音方案使用手冊 + 臺灣語語音入門 + 教育部辭典的字
# 歌仔戲：枝頭 ki1 thiou5， 土 thou。目前教羅共ou轉oo（因為台華辭典按呢處理）
臺灣閩南語羅馬字拼音通行韻母表 = {
    'a', 'ah', 'ap', 'at', 'ak', 'ann', 'annh',
    'am', 'an', 'ang',
    'e', 'eh', 'enn', 'ennh',
    'i', 'ih', 'ip', 'it', 'ik', 'inn', 'innh',
    'im', 'in', 'ing',
    'o', 'oh',
    'oo', 'ooh', 'op', 'ok', 'om', 'ong', 'onn', 'onnh',
    'u', 'uh', 'ut', 'un',
    'ai', 'aih', 'ainn', 'ainnh',
    'au', 'auh', 'aunn', 'aunnh',
    'ia', 'iah', 'iap', 'iat', 'iak', 'iam', 'ian', 'iang', 'iann', 'iannh',
    'io', 'ioh',
    'iok', 'iong', 'ionn',
    'iu', 'iuh', 'iut', 'iunn', 'iunnh',
    'ua', 'uah', 'uat', 'uak', 'uan', 'uann', 'uannh',
    'ue', 'ueh', 'uenn', 'uennh',
    'ui', 'uih', 'uinn', 'uinnh',
    'iau', 'iauh', 'iaunn', 'iaunnh',
    'uai', 'uaih', 'uainn', 'uainnh',
    'm', 'mh', 'ng', 'ngh',
    'ioo', 'iooh',  # 諾 0hioo 0hiooh, 詞目總檔.csv:khan35 jioo51
}
臺灣閩南語羅馬字拼音次方言韻母表 = {
    'er', 'erh', 'erm', 'ere', 'ereh',  # 泉　鍋
    'ee', 'eeh', 'uee',  # 漳　家
    'eng',
    'ir', 'irh', 'irp', 'irt', 'irk', 'irm', 'irn', 'irng', 'irinn',
    'ie',  # 鹿港偏泉腔
    'or', 'orh', 'ior', 'iorh',  # 蚵
    'uang',  # 金門偏泉腔　　風　huang1
    'oi', 'oih',  # 詞彙方言差.csv:硩⿰落去
}
臺灣閩南語羅馬字拼音韻母表 = 臺灣閩南語羅馬字拼音通行韻母表 | 臺灣閩南語羅馬字拼音次方言韻母表

臺灣閩南語羅馬字拼音數字調轉閏號調表 = {
    ('a', '2'): "á", ('a', '3'): "à", ('a', '5'): "â", ('a', '6'): "ǎ",
    ('a', '7'): "ā", ('a', '8'): "a̍", ('a', '9'): "a̋",
    ('e', '2'): "é", ('e', '3'): "è", ('e', '5'): "ê", ('e', '6'): "ě",
    ('e', '7'): "ē", ('e', '8'): "e̍", ('e', '9'): "e̋",
    ('ee', '2'): "ée", ('ee', '3'): "èe", ('ee', '5'): "êe", ('ee', '6'): "ěe",
    ('ee', '7'): "ēe", ('ee', '8'): "e̍e", ('ee', '9'): "e̋e",
    ('ere', '2'): "eré", ('ere', '3'): "erè", ('ere', '5'): "erê", ('ere', '6'): "erě",
    ('ere', '7'): "erē", ('ere', '8'): "ere̍", ('ere', '9'): "ere̋",
    ('i', '2'): "í", ('i', '3'): "ì", ('i', '5'): "î", ('i', '6'): "ǐ",
    ('i', '7'): "ī", ('i', '8'): "i̍", ('i', '9'): "i̋",
    ('iri', '2'): "irí", ('iri', '3'): "irì", ('iri', '5'): "irî", ('iri', '6'): "irǐ",
    ('iri', '7'): "irī", ('iri', '8'): "iri̍", ('iri', '9'): "iri̋",
    ('m', '2'): "ḿ", ('m', '3'): "m̀", ('m', '5'): "m̂", ('m', '6'): "m̌",
    ('m', '7'): "m̄", ('m', '8'): "m̍", ('m', '9'): "m̋",
    ('ng', '2'): "ńg", ('ng', '3'): "ǹg", ('ng', '5'): "n̂g", ('ng', '6'): "ňg",
    ('ng', '7'): "n̄g", ('ng', '8'): "n̍g", ('ng', '9'): "n̋g",
    ('o', '2'): "ó", ('o', '3'): "ò", ('o', '5'): "ô", ('o', '6'): "ǒ",
    ('o', '7'): "ō", ('o', '8'): "o̍", ('o', '9'): "ő",
    ('oo', '2'): "óo", ('oo', '3'): "òo", ('oo', '5'): "ôo", ('oo', '6'): "ǒo",
    ('oo', '7'): "ōo", ('oo', '8'): "o̍o", ('oo', '9'): "őo",
    ('u', '2'): "ú", ('u', '3'): "ù", ('u', '5'): "û", ('u', '6'): "ǔ",
    ('u', '7'): "ū", ('u', '8'): "u̍", ('u', '9'): "ű",
    ('ui', '2'): "uí", ('ui', '3'): "uì", ('ui', '5'): "uî", ('ui', '6'): "uǐ",
    ('ui', '7'): "uī", ('ui', '8'): "ui̍", ('ui', '9'): "ui̋",
    ('iu', '2'): "iú", ('iu', '3'): "iù", ('iu', '5'): "iû", ('iu', '6'): "iǔ",
    ('iu', '7'): "iū", ('iu', '8'): "iu̍", ('iu', '9'): "iű",
}

臺羅對通用聲對照表 = {
    'p': 'b', 'ph': 'p', 'm': 'm', 'b': 'bh',
    't': 'd', 'th': 't', 'n': 'n', 'l': 'l',
    'k': 'g', 'kh': 'k', 'ng': 'ng', 'g': 'gh',
    'ts': 'z', 'tsh': 'c', 's': 's', 'j': 'r',
    'h': 'h', '': '',
}
臺羅對通用韻對照表 = {
    'a': 'a', 'am': 'am', 'an': 'an', 'ang': 'ang',
    'ah': 'ah', 'ap': 'ap', 'at': 'at', 'ak': 'ak',
    'ann': 'ann', 'annh': 'annh',
    'ai': 'ai', 'aih': 'aih', 'ainn': 'ainn', 'ainnh': 'ainnh',
    'au': 'au', 'auh': 'auh', 'aunn': 'aunn', 'aunnh': 'aunnh',
    'e': 'e', 'eh': 'eh', 'enn': 'enn', 'ennh': 'ennh',
    'ia': 'ia', 'iah': 'iah', 'iap': 'iap', 'iat': 'et', 'iak': 'iak',
    'iam': 'iam', 'ian': 'en', 'iang': 'iang',
    'iann': 'iann', 'iannh': 'iannh',
    'iau': 'iau', 'iauh': 'iauh', 'iaunn': 'iaunn', 'iaunnh': 'iaunnh',
    'i': 'i', 'ih': 'ih', 'ip': 'ip', 'it': 'it', 'ik': 'ik',
    'im': 'im', 'in': 'in', 'ing': 'ing',
    'inn': 'inn', 'innh': 'innh',
    'io': 'ior', 'ioh': 'iorh',
    'ioo': 'io', 'iooh': 'ioh', 'ionn': 'ionn', 'iok': 'iok', 'iong': 'iong',
    'iu': 'iu', 'iuh': 'iuh', 'iut': 'iut', 'iunn': 'iunn', 'iunnh': 'iunnh',
    'm': 'm', 'mh': 'mh', 'ng': 'ng', 'ngh': 'ngh',
    'o': 'or', 'oh': 'orh', 'op': 'op',
    'om': 'om', 'ong': 'ong',
    'oo': 'o', 'ooh': 'oh', 'ok': 'ok', 'onn': 'onn', 'onnh': 'onnh',
    'oi': 'oi', 'oih': 'oih',
    'ua': 'ua', 'uah': 'uah', 'uat': 'uat', 'uak': 'uak',
    'uann': 'uann', 'uannh': 'uannh', 'uan': 'uan',
    'uai': 'uai', 'uaih': 'uaih', 'uainn': 'uainn', 'uainnh': 'uainnh',
    'ue': 'ue', 'ueh': 'ueh', 'uenn': 'uenn', 'uennh': 'uennh',
    'ui': 'ui', 'uih': 'uih', 'uinn': 'uinn', 'uinnh': 'uinnh',
    'u': 'u', 'uh': 'uh', 'ut': 'ut',
    'un': 'un',
    'uang': 'uang',
}
臺羅對通用調對照表 = {
    '1': '1', '7': '2', '3': '3', '2': '4', '5': '5',
    '8': '6', '4': '7', '10': '8', '9': '9',
    '6': '4', '0': '3',
}


class 臺灣閩南語羅馬字拼音(教會系羅馬音標):
    聲母表 = 臺灣閩南語羅馬字拼音聲母表
    韻母表 = 臺灣閩南語羅馬字拼音韻母表

    數字調轉閏號調表 = 臺灣閩南語羅馬字拼音數字調轉閏號調表

    對通用聲對照表 = 臺羅對通用聲對照表
    對通用韻對照表 = 臺羅對通用韻對照表
    對通用調對照表 = 臺羅對通用調對照表

    對白話字聲對照表 = 臺羅對白話字.聲對照表
    對白話字韻對照表 = 臺羅對白話字.韻對照表
    對白話字調對照表 = 臺羅對白話字.調對照表

    轉音值模組 = 臺灣閩南語羅馬字拼音轉音值模組()

    def __init__(self, 音標):
        super(臺灣閩南語羅馬字拼音, self).__init__()
        self.分析聲韻調(音標)
        if self.調 not in self.對通用調對照表:
            self.調 = None
            self.音標 = None
        self.原本音標 = 音標

    def 轉換到臺灣閩南語羅馬字拼音(self):
        return self.音標

    def 轉調符(self):
        if self.音標 is None:
            return None

        for 符號 in ['a', 'oo', 'o', 'ee', 'ere', 'e', 'iri', 'ui', 'iu', 'u', 'i', 'ng', 'm']:
            if 符號 in self.音標:
                if self.調 in ['1', '4']:  # 第一調、第四調，免符號
                    韻 = self.韻
                else:
                    韻 = self.韻.replace(符號, self.數字調轉閏號調表[(符號, self.調)])
                break
        聲韻 = self.聲 + 韻
        if self.原本音標.strip('01')[0].isupper():
            聲韻 = 聲韻[0].upper() + 聲韻[1:]
        return self.輕 + self.外來語 + 聲韻

    def 轉閏號調(self):
        print('「轉閏號調」會佇7.0版會提掉，請改用「轉調符」', file=stderr)
        return self.轉調符()

    def 轉通用拼音(self):
        if self.音標 is None:
            return None
        return (
            self.對通用聲對照表[self.聲] +
            self.對通用韻對照表[self.韻] +
            self.對通用調對照表[self.調]
        )

    def 轉白話字(self):
        if self.音標 is None:
            return None
        小寫的白話字 = 臺羅轉白話字.轉白話字(self.聲, self.韻, self.調)
        結果 = 小寫的白話字
        # 保留頭字大小寫 Tsai2 0Tsai2
        if self.原本音標[0].isupper() or (
            self.原本音標[0] == '0' and self.原本音標[1].isupper()
        ):
            結果 = 小寫的白話字[0].upper() + 小寫的白話字[1:]
        return self.輕 + 結果

    def 轉白話字數字調(self):
        if self.音標 is None:
            return None
        return (
            self.對白話字聲對照表[self.聲] +
            self.對白話字韻對照表[self.韻] +
            self.對白話字調對照表[self.調]
        )

    def 轉吳守禮方音(self):
        return 臺灣閩南語羅馬字拼音轉方音符號吳守禮改良式模組(self.聲, self.韻, self.調, self.輕).音標

    def 產生吳守禮方音物件(self):
        return 臺灣閩南語羅馬字拼音轉方音符號吳守禮改良式模組(self.聲, self.韻, self.調, self.輕)

    def 音值(self):
        if self.音標 is None:
            return self.轉音值模組.轉(None, None, None, None)
        return self.轉音值模組.轉(self.聲, self.韻, self.調, self.輕)
