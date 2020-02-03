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


  Scenario Outline: 漢羅文 kah 全羅文做伙建立一 ê 句仔
    Given 兩句 <hanlo> kah <lomaji> 做伙建立一 ê 句仔
     Then hanlo是 <kiatko_hanlo>
      And lomaji是 <kiatko_lomaji>

    Examples: ku
   	| hanlo             | lomaji                    | kiatko_hanlo     | kiatko_lomaji            |
	| 我是 Ke-si ê 物件 | Guá sī Ke-si ê mi̍h-kiānn  | 我是Ke-si ê物件  | Guá sī Ke-si ê mi̍h-kiānn |


  Scenario: 句仔 ē-tàng 提著 ē-té ê 詞仔 kah 字仔
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


  Scenario: 句仔 ē-tàng 提著 ē-té ê 詞仔 kah 字仔
    Given 兩句 "我是 Ke-si ê 物件" kah "Guá sī Ke-si ê mi̍h-kiānn" 做伙建立一 ê 句仔
     Then 第 2 ê su 是 tsia-ê 字
       | hanlo | lomaji    |
	   | Ke    | Ke        |
	   | si    | si        |


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
