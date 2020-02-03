Feature: Ku 句仔


  Scenario Outline: 一筆簡單 ê 句仔
    Given 一句 <bun> 建立句仔
     Then hanlo是 <kiatko>
      And lomaji是 <kiatko>

    Examples: ku
   	| bun               | kiatko          |
	| Guá sī Ke-si      | Guá sī Ke-si    |
	| 我是 Ke-si ê 物件 | 我是Ke-si ê物件 |
	| 我 是Ke-si ê物件  | 我是Ke-si ê物件 |
	| 緊--出-來--啦     | 緊--出-來--啦   |


  Scenario Outline: 漢羅文 kah 羅馬字做伙建立一 ê 句仔
    Given 兩句 <hanlo> kah <lomaji> 做伙建立一 ê 句仔
     Then hanlo是 <kiatko_hanlo>
      And lomaji是 <kiatko_lomaji>

    Examples: ku
   	| hanlo             | lomaji                    | kiatko_hanlo     | kiatko_lomaji            |
	| 我是 Ke-si ê 物件 | Guá sī Ke-si ê mi̍h-kiānn  | 我是Ke-si ê物件  | Guá sī Ke-si ê mi̍h-kiānn |

	Examples: 組字
    | hanlo         | lomaji                    | kiatko_hanlo     | kiatko_lomaji            |
    | 癩⿸疒哥人  | thái-ko lâng          | 癩⿸疒哥人 | thái-ko lâng |
    
    Examples: 標點符號
    | hanlo         | lomaji                    | kiatko_hanlo     | kiatko_lomaji            |
    | Gâu-tsá,           | Gâu-tsá,          | Gâu-tsá | Gâu-tsá |
    | 𠢕早，          | Gâu-tsá,      | 𠢕早，          | Gâu-tsá,     |
    | 𠢕早……        |  Gâu-tsá... | 𠢕早……        |  Gâu-tsá... |
    

  Scenario: 對照句仔提著 ē-té ê 詞仔 kah 字仔
    Given 兩句 "我是 Ke-si ê 物件" kah "Guá sī Ke-si ê mi̍h-kiānn" 做伙建立一 ê 句仔
     Then su是
       | hanlo | lomaji    |
	   | 我    | Guá       |
	   | 是    | sī        |
	   | Ke-si | Ke-si     |
	   | ê     | ê         |
	   | 物件  | mi̍h-kiānn |
	 And ji是
	   | hanlo | lomaji    |
	   | 我    | Guá       |
	   | 是    | sī        |
	   | Ke    | Ke        |
	   | si    | si        |
	   | ê     | ê         |
	   | 物    | mi̍h       |
	   | 件    | kiānn     |


  Scenario: 句仔 ē-té 詞仔 mā 提有字仔
    Given 兩句 "我是 Ke-si ê 物件" kah "Guá sī Ke-si ê mi̍h-kiānn" 做伙建立一 ê 句仔
     Then 第 2 ê su 是 tsia-ê 字
       | hanlo | lomaji    |
	   | Ke    | Ke        |
	   | si    | si        |


  Scenario: 對照句仔ê時，照羅馬字統一輕聲符
    Given 兩句 "我啦" kah "Guá--lah" 做伙建立一 ê 句仔
     Then su是
       | hanlo         | lomaji     |
	   | 我--啦        | Guá--lah   |


  Scenario Outline: 對照句仔ê時，照羅馬字斷詞
    Given 兩句 <hanlo> kah <lomaji> 做伙建立一 ê 句仔
     Then 有 <susoo> su

    Examples: ku
   	| hanlo         | lomaji     | susoo |
	| 我--啦        | Guá --lah  | 2     |
	

  Scenario Outline: 對照句仔ê時，輕聲詞若連做伙算一ê詞；若隔開算bô-kâng詞
    Given 兩句 <hanlo> kah <lomaji> 做伙建立一 ê 句仔
     Then 有 <susoo> su

    Examples: ku
   	| hanlo         | lomaji     | susoo |
	| 我啦          | Guá--lah   | 1     |
	| 我--啦        | Guá--lah   | 1     |
	| 我 --啦       | Guá --lah  | 2     |


  Scenario Outline: 羅馬字 ē-īng-eh kā 轉做其他書寫
    Given 一句 <bun> 建立句仔
    When 提 TL
    Then hanlo是 <TL>
    When 提 POJ
    Then hanlo是 <POJ>

	Examples: ku
   	| bun             | TL | POJ |
	| Guá sī Ke-si    | Guá sī Ke-si| Góa sī Ke-si|
	| Góa sī Ke-si    | Guá sī Ke-si| Góa sī Ke-si|
	| Gua2 si7 Ke1-si1| Guá sī Ke-si| Góa sī Ke-si|
	| Góa sī 家私     | Guá sī 家私 | Góa sī 家私 |
