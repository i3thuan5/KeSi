Feature: Ku 句物件

  Scenario: 一筆簡單 ê 句物件
       Given 一句 "我是Ke-si"
       When 建立句物件
        Then taibun是 "我是 Ke-si"
          And lomaji是 "我是 Ke-si"
          And hanji是 "我是 Ke-si"

  Scenario: 漢羅文 kah 全羅文做伙建立一 ê 句物件
       Given 兩句 "我是Ke-si" kah "Guá sī Ke-si"
       When 做伙建立一 ê 句物件
        Then taibun是 "我是 Ke-si"
          And lomaji是 "Guá sī Ke-si"
          And hanji是 "我是 Ke-si"
          And 攏總 "2" 詞
          And 攏總 "4" 字

  Scenario: 藉詞建立句物件
       Given 兩句 "我是Ke-si" kah "Guá sī Ke-si"
       When 做伙建立一 ê 句物件
          And 選擇 uì 第 "2" ê 詞斷做兩句
        Then 第"1"句taibun是 "我是"
          And 第"2"句taibun是 "Ke-si"

  Scenario: 藉分詞建立句物件
       Given 分詞 "我｜Guá 是｜sī Ke-si｜Ke-si"
       When 建立句物件
        Then taibun是 "我是 Ke-si"

  Scenario: 全羅文 ē-īng-eh kā 轉做其他書寫
       Given 一句 "Guá sī Ke-si"
       When 建立句物件
       When 提 TL
         Then lomaji是 "Guá sī Ke-si"
       When 提 POJ
         Then lomaji是 "Goá sī Ke-si"

  Scenario: Kā 數字調轉做傳統調
       Given 一句 "Gua2 si7 Ke1-si1"
       When 建立句物件
       When 轉做 TL 傳統調
        Then taibun是 "Guá sī Ke-si"
          And lomaji是 "Guá sī Ke-si"
          And hanji是 "Guá sī Ke-si"
