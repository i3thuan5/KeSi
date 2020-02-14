# -*- coding: utf-8 -*-

TL_SIANNBO = {
    'p', 'ph', 'm', 'b',
    't', 'th', 'n', 'l',
    'k', 'kh', 'ng', 'g',
    'ts', 'tsh', 's', 'j',
    'h', '',
}
# 臺灣閩南語羅馬字拼音方案使用手冊 + 臺灣語語音入門 + 教育部辭典的字
# 歌仔戲：枝頭 ki1 thiou5， 土 thou。目前教羅共ou轉oo（因為台華辭典按呢處理）
TL_UNBO = {
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
    ######
    'er', 'erh', 'erm', 'ere', 'ereh',  # 泉　鍋
    'ee', 'eeh', 'uee',  # 漳　家
    'eng',
    'ir', 'irh', 'irp', 'irt', 'irk', 'irm', 'irn', 'irng', 'irinn',
    'ie',  # 鹿港偏泉腔
    'or', 'orh', 'ior', 'iorh',  # 蚵
    'uang',  # 金門偏泉腔　　風　huang1
    'oi', 'oih',  # 詞彙方言差.csv:硩⿰落去
}

KONGKE_SIANNBO = TL_SIANNBO
KONGKE_UNBO = TL_UNBO
