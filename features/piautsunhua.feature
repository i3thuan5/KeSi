Feature: Unicode normalization

  Scenario Outline: 輸入若是有相容區ê漢字，ài轉做統一區
    Given 一句編碼是 <Compatibility> ê字
     Then 書寫ê編碼是 <Unified>

    Examples: CJK compatibility ài 取代
    | 字 | Unified | Compatibility |
    | 行 | 884C    | FA08     |
    | 數 | 6578    | F969     |
    | 年 | 5E74    | F98E     |

  Scenario Outline: 統一區內底，無仝語言ê漢字mài互相轉換，保持原本ê字碼
    Given 一句 <jit> 建立句仔
     Then 書寫ê漢字mài變做 <tai>

    Examples: CJK unified 免振動
    | jit  | tai  |
    | 様   | 樣    |

  Scenario Outline: 本底字母kah調符分開ê羅馬字，盡量kap做伙
    Given 一句編碼是 <thiah> ê字
     Then 書寫ê編碼是 <kap>

    Examples: lô-má-jī
    | 字 | kap       | thiah            | tsukai            |
    | á | 00E1       | 0061,0301        |                   |
    | ō͘ | 014D,0358  | 006F,0358,0304   | o7,tiam; o,tiam,7 |

  Scenario Outline: 教育部造字轉做Unicode
    Given 一句編碼是 <KIP> ê字
     Then 書寫ê編碼是 <Unicode>

    Examples: 教育部造字ài取代
    | 字 | KIP | Unicode |
    | 𪜶 | E701    | 2A736     |
    | 𬦰 | E705    | 2C9B0     |

  Scenario Outline: Bē顯示ê字元(Non-printable)，換做空白kā使用者提醒
    Given 一句編碼是 <guanpun> ê字
     Then 書寫ê編碼是 <tshuli>

    Examples: lô-má-jī
    | 字            | guanpun            | tshuli            |
    | o(backspace)a | 006F,0008,0061       | 006F,0020,0061        |
