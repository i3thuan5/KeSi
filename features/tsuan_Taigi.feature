Feature: Tsuán Tâi-gí 轉台語，kā羅馬字轉做其他音標系統

  Scenario Outline: Kā 書寫轉做POJ
    Given 一字 <bun>
     Then 書寫轉POJ會生做 <POJ>
    
    Examples: Jī
    | bun     | POJ   |
    | a1      | a     |
    | Sui2    | Súi   |
	| Tsui2   | Chúi  |
	| ang3    | àng   |
    | au3     | àu    |
    | tik4    | tek   |
    | mng5    | mn̂g  |
    | m5      | m̂    |
    | ua5     | ôa    |
    | phîng   | phêng |
    | oo7     | ō͘     |
    | ainn7   | āiⁿ   |
    | hiunnh8 | hiu̍ⁿh |
    | őo      | ŏ͘     |

    Examples: 方言韻
	| bun     | POJ    |
	| tere5   | terê   |
    | tir5    | tîr    |

	Examples: 輕聲
	| bun     | POJ   |
	| --Suí   | --Súi | 

    Examples: Bô正確--ê
    | bun     | POJ  |
	| suii    | suii |


  Scenario Outline: Kā 書寫轉做 TL
    Given 一字 <bun>
     Then 書寫轉TL會生做 <TL>

    Examples: Jī
    | bun     | TL    |
    | a1      | a     |
    | Sui2    | Suí   |
	| Tsui2   | Tsuí  |
	| ang3    | àng   |
    | au3     | àu    |
    | tik4    | tik   |
    | mng5    | mn̂g  |
    | m5      | m̂    |
    | ua5     | uâ    |
    | phîng   | phîng |
    | oo7     | ōo    |
    | ainn7   | āinn  |
    | hiunnh8 | hiu̍nnh|
    | Őo      | Őo    |
    
    Examples: 方言韻
	| bun     | TL     |
	| tere5   | terê   |
    | tir5    | tîr    |

	Examples: 輕聲
	| bun     | TL    |
	| --Suí   | --Súi | 

    Examples: Bô正確--ê
    | bun     | TL   |
	| suii    | suii |
    
    