Feature: Ku 句仔


Scenario Outline: 一筆簡單 ê 句仔
    Given 一句 <bun> 建立句仔
    Then hanlo是 <kiatko>
    And lomaji是 <kiatko>

    Examples: Hàn-lô bûn kan-na 保留羅馬字之間 ê 空白，tshun--ê 空白清掉
        | bun          | kiatko       |
        | Guá sī Ke-si | Guá sī Ke-si |
        | 我是 Ke-si   | 我是Ke-si    |
        | 我 是Ke-si   | 我是Ke-si    |

    Examples: Khin-siann kah 頭前連寫
        | bun       | kiatko   |
        | Guá--lah  | Guá--lah |
        | Guá --lah | Guá--lah |

    Examples: Hàn-jī khin-siann
        | bun           | kiatko        |
        | 緊--出-來--啦 | 緊--出-來--啦 |
        | 正--月到--矣  | 正--月到--矣  |

    Examples: Sòo-jī
        | bun          | kiatko       |
        | 0800-092-000 | 0800-092-000 |


Scenario Outline: Bô-thuân mi̍h-kiānn kiàn-li̍p kù
    Given Kan-na傳 lomaji: <bun>建立句仔
    Then hanlo是 <kiatko>
    And lomaji是 <kiatko>

    Examples: Ku
        | bun          | kiatko       |
        | Guá sī Ke-si | Guá sī Ke-si |


Scenario Outline: 漢羅文 kah 羅馬字對照
    Given 兩句 <hanlo> kah <lomaji> 做伙建立一 ê 句仔
    Then hanlo是 <kiatko_hanlo>
    And lomaji是 <kiatko_lomaji>

    Examples: ku
        | hanlo             | lomaji                    | kiatko_hanlo    | kiatko_lomaji             |
        | 我是 Ke-si ê 物件 | Guá sī Ke-si ê mi̍h-kiānn | 我是Ke-si ê物件 | Guá sī Ke-si ê mi̍h-kiānn |

    Examples: 組字
        | hanlo      | lomaji       | kiatko_hanlo | kiatko_lomaji |
        | 癩⿸疒哥人 | thái-ko lâng | 癩⿸疒哥人   | thái-ko lâng  |

    Examples: 標點符號
        | hanlo                  | lomaji                                         | kiatko_hanlo             | kiatko_lomaji                                  |
        | Gâu-tsá,               | Gâu-tsá,                                       | Gâu-tsá,                 | Gâu-tsá,                                       |
        | 𠢕早，                 | Gâu-tsá,                                       | 𠢕早，                   | Gâu-tsá,                                       |
        | 𠢕早……                 | Gâu-tsá...                                     | 𠢕早……                   | Gâu-tsá...                                     |
        | 缺喙的食米粉──看現現。 | Khih-tshuì--ê tsia̍h bí-hún──khuànn-hiān-hiān. | 缺喙--的食米粉──看現現。 | Khih-tshuì--ê tsia̍h bí-hún──khuànn-hiān-hiān. |

    Examples: 數字
        | hanlo          | lomaji                  | kiatko_hanlo   | kiatko_lomaji           |
        | 落雨機率20 pha | lo̍h-hōo ki-lu̍t 20 pha | 落雨機率20 pha | lo̍h-hōo ki-lu̍t 20 pha |


Scenario Outline: 教育部漢羅袂有連字符
    Given 兩句 <hanlo> kah <lomaji> 做伙建立一 ê 句仔
    Then kiphanlo是 <kiphanlo>

    Examples: 教典ê情形
        | hanlo      | lomaji       | kiphanlo   |
        | oo-tóo-bái | oo-tóo-bái   | oo-tóo-bái |
        | 有--一-寡  | ū--tsi̍t-kuá | 有一寡     |
        | 有的無的   | ū--ê-bô--ê   | 有的無的   |
        | 啊         | --ah         | 啊         |
        | --ah       | --ah         | --ah       |

    Examples: 其他情形
        | hanlo        | lomaji       | kiphanlo     |
        | āu--ji̍t     | āu--ji̍t     | āu--ji̍t     |
        | ū--ê-bô--ê   | ū--ê-bô--ê   | ū--ê-bô--ê   |
        | ū--tsi̍t-kuá | ū--tsi̍t-kuá | ū--tsi̍t-kuá |


Scenario: 對照句仔提著 ē-té ê 詞仔 kah 字仔。
            """
            照羅馬字ê空白斷詞，有空白就斷，連做伙就算一詞。
            輕聲符 kah 連字符行為 kāng-khuán。
            """
    Given 兩句 "我是超潮的Ke-si--啦" kah "Guá sī超潮的Ke-si--lah" 做伙建立一 ê 句仔

    Then 詞仔是
        | hanlo     | lomaji     |
        | 我        | Guá        |
        | 是        | sī         |
        | 超潮的    | 超潮的     |
        | Ke-si--啦 | Ke-si--lah |

     And 字仔是
         | hanlo | lomaji |
         | 我    | Guá    |
         | 是    | sī     |
         | 超    | 超     |
         | 潮    | 潮     |
         | 的    | 的     |
         | Ke    | Ke     |
         | si    | si     |
         | --啦  | --lah  |

     And 詞仔 mā ē-tàng 提著字，像第3詞攏總3字，字仔是
         | hanlo | lomaji |
         | Ke    | Ke     |
         | si    | si     |
         | --啦  | --lah  |


Scenario Outline: 對照句仔ê時，照羅馬字決定輕聲符
    Given 兩句 <hanlo> kah <lomaji> 做伙建立一 ê 句仔
     Then hanlo是 <kiatko>

    Examples: ku
        | hanlo       | lomaji     | kiatko    |
       | 我啦        | Guá--lah   | 我--啦    |


Scenario Outline: 字數bô-kâng無法度對
    When <hanlo> kah <lomaji> 若欲對句仔會發錯誤

    Examples: ku
        | hanlo                    | lomaji          |
        | 我啦                     | --lah           |
        | 我                       | Guá--lah        |
        | 我 就是Ke-si-thâu-á 你好 | Guá tō sī lí-hó |


Scenario Outline: 羅馬字 ē-īng-eh kā 轉做其他書寫
    Given 一句 <bun> 建立句仔
    Then 轉出POJ句，伊 ê hanlo是 <POJ>
    And 轉出TL句，伊 ê hanlo是 <TL>
    But 原本ê句仔猶原是 <bun>

    Examples: ku
        | bun              | TL           | POJ          |
        | Guá sī Ke-si     | Guá sī Ke-si | Góa sī Ke-si |
        | Góa sī Ke-si     | Guá sī Ke-si | Góa sī Ke-si |
        | Gua2 si7 Ke1-si1 | Guá sī Ke-si | Góa sī Ke-si |
        | Góa sī家私       | Guá sī家私   | Góa sī家私   |


Scenario Outline: 漢羅文 kah 羅馬字對照 ē-īng-eh kā 轉做其他書寫
    Given 兩句 <hanlo> kah <lomaji> 做伙建立一 ê 句仔
    Then 轉出POJ句，伊 ê lomaji是 <POJ>
    And 轉出TL句，伊 ê lomaji是 <TL>

    Examples: ku
        | hanlo | lomaji | TL    | POJ   |
        | 一    | tsi̍t  | tsi̍t | chi̍t |
        | 一    | chi̍t  | tsi̍t | chi̍t |
