Feature: Ku 句物件

  Scenario: 一 ê 簡單 ê 句物件
       Given 一句 "我是Ke-si"
       When 建立句物件
        Then taibun是 "我是 Ke-si"
          And lomaji是 "我是 Ke-si"
          And hanji是 "我是 Ke-si"

  Scenario: 有全羅文同齊建立一 ê 句物件
       Given 一句 "我是Ke-si" kah "Guá sī Ke-si"
       When 建立句物件
        Then taibun是 "我是 Ke-si"
          And lomaji是 "Guá sī Ke-si"
          And hanji是 "我是 Ke-si"
          And 攏總 "2" 詞
          And 攏總 "4" 字

  Scenario: 藉詞建立句物件
       Given 一句 "我是Ke-si" kah "Guá sī Ke-si"
       When 建立句物件
          And 選擇 uì 第 "2" ê 詞斷做兩句
         Then 第1句taibun是 "我是"
           And 第2句taibun是 "Ke-si"

  Scenario: Ē-īng-eh kā 全羅文轉做其他書寫
       Given 一句 "Guá sī Ke-si"
          And 建立句物件
       When 提 "TL"
        Then lomaji是 "Guá sī Ke-si"
       When 提 "POJ"
        Then lomaji是 "Goá sī Ke-si"

  Scenario: Kā 數字調轉做傳統調
       Given 一句 "Gua2 si7 Ke1-si1"
       When 建立句物件
          And 轉做傳統調
        Then taibun是 "Guá sī Ke-si"
          And lomaji是 "Guá sī Ke-si"
          And hanji是 "Guá sī Ke-si"

  Scenario: 接 TauPhahJi 自動 kā 全羅補起來
       Given 一句 "我是Ke-si"
       When 接 TauPhahJi
        Then taibun是 "我是Ke-si"
          And lomaji是 "Guá sī Ke-si"
          And hanji是 "我是家私"

  Scenario: 接 Kaldi 自動 kā 聲轉做台文
       Given 一段聲 "test_Kaldi.wav"
       When 轉做句物件
        Then taibun是 ""
          And lomaji是 ""
          And hanji是 ""
