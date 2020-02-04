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


  Scenario Outline: 漢羅文 kah 羅馬字對照
    Given 兩句 <hanlo> kah <lomaji> 做伙建立一 ê 句仔
     Then hanlo是 <kiatko_hanlo>
      And lomaji是 <kiatko_lomaji>

    Examples: ku
   	| hanlo             | lomaji                    | kiatko_hanlo     | kiatko_lomaji            |
	| 我是 Ke-si ê 物件 | Guá sī Ke-si ê mi̍h-kiānn  | 我是Ke-si ê物件  | Guá sī Ke-si ê mi̍h-kiānn |

	Examples: 組字
    | hanlo         | lomaji            | kiatko_hanlo    | kiatko_lomaji  |
    | 癩⿸疒哥人    | thái-ko lâng      | 癩⿸疒哥人      | thái-ko lâng   |
    
    Examples: 標點符號
    | hanlo         | lomaji            | kiatko_hanlo    | kiatko_lomaji  |
    | Gâu-tsá,      | Gâu-tsá,          | Gâu-tsá         | Gâu-tsá        |
    | 𠢕早，        | Gâu-tsá,          | 𠢕早，          | Gâu-tsá,       |
    | 𠢕早……      |  Gâu-tsá...       | 𠢕早……        |  Gâu-tsá...    |
    

  Scenario: 對照句仔提著 ē-té ê 詞仔 kah 字仔。
            """
            照羅馬字ê空白斷詞，有空白就斷，連做伙就算一詞。
            輕聲符 kah 連字符行為 kāng-khuán。
            """
    Given 兩句 "我是Ke-si ê物件--啦" kah "Guá sī Ke-si ê mi̍h-kiānn--lah" 做伙建立一 ê 句仔
     Then 詞仔是
       | hanlo | lomaji    |
	   | 我    | Guá       |
	   | 是    | sī        |
	   | Ke-si | Ke-si     |
	   | ê     | ê         |
	   | 物件--啦  | mi̍h-kiānn--lah |
	 And 字仔是
	   | hanlo | lomaji    |
	   | 我    | Guá       |
	   | 是    | sī        |
	   | Ke    | Ke        |
	   | si    | si        |
	   | ê     | ê         |
	   | 物    | mi̍h       |
	   | 件    | kiānn     |
	   | --啦  | --lah     |
     And 第 2 詞 ê 字仔是
       | hanlo | lomaji    |
	   | Ke    | Ke        |
	   | si    | si        |


  Scenario Outline: 對照句仔ê時，照羅馬字決定輕聲符
    Given 兩句 <hanlo> kah <lomaji> 做伙建立一 ê 句仔
     Then hanlo是 <kiatko>
     
     Examples: ku
       | hanlo       | lomaji     | kiatko    |
       | 我啦        | Guá--lah   | 我--啦    |


  Scenario Outline: 羅馬字 ē-īng-eh kā 轉做其他書寫
    Given 一句 <bun> 建立句仔
     Then 轉出TL句，伊 ê hanlo是 <TL>
      And 轉出POJ句，伊 ê hanlo是 <POJ>
      But 原本ê句仔猶原是 <bun>

	Examples: ku
   	| bun             | TL          | POJ         |
	| Guá sī Ke-si    | Guá sī Ke-si| Góa sī Ke-si|
	| Góa sī Ke-si    | Guá sī Ke-si| Góa sī Ke-si|
	| Gua2 si7 Ke1-si1| Guá sī Ke-si| Góa sī Ke-si|
	| Góa sī 家私     | Guá sī 家私 | Góa sī 家私 |
