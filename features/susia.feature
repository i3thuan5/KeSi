Feature: Tsuán Tâi-gí 轉台語，kā羅馬字轉做其他音標系統

  Scenario Outline: Kā 書寫轉做POJ
    Given 一句 <bun>
     Then 書寫轉POJ會生做 <POJ>
    
    Examples: Jī
      | bun     | POJ    |
      | a1      | a      |
      | Sui2    | Súi    |
      | Tsui2   | Chúi   |
      | gua2    | góa    |
      | ang3    | àng    |
      | au3     | àu     |
      | tik4    | tek    |
      | mng5    | mn̂g   |
      | M5      | M̂     |
      | uan5    | oân    |
      | phîng   | phêng  |
      | PHÎNG   | PHÊNG  |
      | oo7     | ō͘     |
      | ou7     | ō͘     |
      | ainn7   | āiⁿ    |
      | hiunnh8 | hiu̍ⁿh |
      | őo      | ŏ͘     |
      | Chúi    | Chúi   |
      | àu      | àu     |
      | tek     | tek    |
      | òe      | òe     |
      | phêng   | phêng  |
      | ō͘      | ō͘     |
      | āⁿ      | āⁿ     |
      | āiⁿ     | āiⁿ    |
      | āN      | āⁿ     |
      | āNh     | āⁿh    |
      | ĀN      | ĀN     |
      | Ānn     | Āⁿ     |
      | Āⁿ      | Āⁿ     |
      | UĀIⁿ    | OĀIⁿ   |
      | OĀIⁿ    | OĀIⁿ   |
      | Nā      | Nā     |
      | ō͘ⁿ     | ōⁿ     |


    Examples: POJ tsuân tuā-siá ᴺ
      | bun | POJ |
      | Āᴺ  | Āⁿ  |
   
    Examples: 方言韻
      | bun   | POJ  |
      | tere5 | têre |
      | tir5  | tîr  |

    Examples: 輕聲
      | bun       | POJ       |
      | --Suí     | --Súi     |
      | --aih-iah | --aih-iah |

    Examples: NFD
      | bun | POJ |
      | ôa  | ôa  |
   
    Examples: M̄ sī Lô-má-jī
      | bun   | POJ   |
      | suii  | suii  |
      | súi2  | súi2  |
      | ĀIN   | ĀIN   |
      | hello | hello |
      | 5     | 5     |
      | 媠    | 媠    |
  
  Scenario Outline: Kā 書寫轉做KIP
    Given 一句 <bun>
     Then 書寫轉KIP會生做 <KIP>

    Examples: Jī
      | bun     | KIP      |
      | a1      | a       |
      | Sui2    | Suí     |
      | au3     | àu      |
      | tik4    | tik     |
      | mng5    | mn̂g    |
      | M5      | M̂      |
      | uan5    | uân     |
      | PHÎNG   | PHÎNG   |
      | om7     | ōm      |
      | āN      | ānn     |
      | hiunnh8 | hiu̍nnh |
      | OO9     | ŐO      |
      | AN      | AN      |
      | Ná      | Ná      |
    
    Examples: POJ
      | bun   | KIP    |
      | Chúi  | Tsuí  |
      | PHÊNG | PHÎNG |
      | tek   | tik   |
      | ôa    | uâ    |
      | oân   | uân   |
      | ō͘    | ōo    |
      | āⁿ    | ānn   |
      | OĀI   | UĀI   |
      | ō͘ⁿ   | ōnn   |

    Examples: 頭字大寫較tsē全大寫，而且全大寫ē-tàng ka-tī `upper()`
      | bun | KIP  |
      | O͘  | Oo  |
    
    Examples: 方言韻
      | bun   | KIP   |
      | tere5 | terê |
      | terê  | terê |
      | tir5  | tîr  |
      | ionn5 | iônn |
      | tee5  | têe  |


    Examples: 輕聲
      | bun       | KIP        |
      | --Súi     | --Suí     |
      | --aih-iah | --aih-iah |
    
    Examples: NFD
      | bun | KIP  |
      | ôa  | uâ  |

    Examples: M̄ sī Lô-má-jī
      | bun   | KIP    |
      | suii  | suii  |
      | súi2  | súi2  |
      | ĀIN   | ĀIN   |
      | hello | hello |
      | 5     | 5     |
      | 20    | 20    |
      | 媠    | 媠    |
