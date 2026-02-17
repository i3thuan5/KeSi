### Requirement: 書寫轉做 POJ
系統 SHALL 將各種羅馬字輸入轉做 POJ（白話字）書寫。

韻母轉換規則：
- KIP `u` → POJ `o`（例: `Sui2` → `Súi`，`Tsui2` → `Chúi`，`gua2` → `góa`，`uan5` → `oân`）
- KIP `i` → POJ `e`（例: `phîng` → `phêng`，`tik4` → `tek`）

聲母轉換規則：
- KIP `ts` → POJ `ch`（例: `Tsui2` → `Chúi`）

數字調轉調符：
- 數字調號轉做對應調符（例: `a1` → `a`，`Sui2` → `Súi`，`ang3` → `àng`，`oo7` → `ō͘`）
- `oo` kah `ou` 攏轉做 `o͘`（例: `oo7` → `ō͘`，`ou7` → `ō͘`）

鼻音符號：
- KIP `nn` → POJ `ⁿ`（例: `ainn7` → `āiⁿ`，`hiunnh8` → `hiu̍ⁿh`）
- 小寫 `N` → `ⁿ`（例: `āN` → `āⁿ`，`āNh` → `āⁿh`）
- 大寫 `Ānn` → `Āⁿ`（頭字大寫保留）
- 全大寫 `ĀN` → `ĀN`（全大寫無轉換）
- 上標 `ᴺ` → `ⁿ`（例: `Āᴺ` → `Āⁿ`）
- `ō͘ⁿ` → `ōⁿ`（o͘ + 鼻音合併）

大小寫保持原樣：
- `PHÎNG` → `PHÊNG`（全大寫維持全大寫）
- `M5` → `M̂`

特殊第 9 調（őo）：
- `őo` → `ŏ͘`

邊界情形 — 方言韻：
- 方言韻照原輸出（例: `tere5` → `têre`，`tir5` → `tîr`）

邊界情形 — 輕聲：
- 輕聲詞照轉（例: `--Suí` → `--Súi`）
- 輕聲詞組保持（例: `--aih-iah` → `--aih-iah`）

邊界情形 — NFD：
- NFD 輸入正常處理（例: `ôa` → `ôa`）

邊界情形 — 毋是羅馬字：
- 無效羅馬字原樣輸出（例: `suii` → `suii`，`súi2` → `súi2`，`ĀIN` → `ĀIN`）
- 非羅馬字原樣輸出（例: `hello` → `hello`，`5` → `5`，`媠` → `媠`）

#### Scenario: KIP 韻母轉 POJ
- **WHEN** 輸入 `Tsui2`
- **THEN** POJ 輸出 `Chúi`

#### Scenario: 數字調轉調符
- **WHEN** 輸入 `oo7`
- **THEN** POJ 輸出 `ō͘`

#### Scenario: 鼻音符號轉換
- **WHEN** 輸入 `ainn7`
- **THEN** POJ 輸出 `āiⁿ`

#### Scenario: 方言韻保持
- **WHEN** 輸入 `tere5`
- **THEN** POJ 輸出 `têre`

#### Scenario: 毋是羅馬字原樣輸出
- **WHEN** 輸入 `hello`
- **THEN** POJ 輸出 `hello`

### Requirement: 書寫轉做 KIP
系統 SHALL 將各種羅馬字輸入轉做 KIP（教育部台羅）書寫。

韻母轉換規則：
- POJ `o` → KIP `u`（例: `Chúi` → `Tsuí`，`oân` → `uân`，`ôa` → `uâ`）
- POJ `e` → KIP `i`（例: `PHÊNG` → `PHÎNG`，`tek` → `tik`）
- `OĀI` → `UĀI`（大寫韻母轉換）

聲母轉換規則：
- POJ `ch` → KIP `ts`（例: `Chúi` → `Tsuí`）

數字調轉調符：
- 數字調號轉做對應調符（例: `a1` → `a`，`au3` → `àu`，`om7` → `ōm`）

鼻音符號：
- POJ `ⁿ` → KIP `nn`（例: `āⁿ` → `ānn`，`hiunnh8` → `hiu̍nnh`）
- `ō͘` → `ōo`
- `ō͘ⁿ` → `ōnn`（o͘ + 鼻音一起轉）
- 小寫 `N` → `nn`（例: `āN` → `ānn`）
- 全大寫 `AN` → `AN`（全大寫無轉換）

特殊第 9 調：
- `OO9` → `ŐO`

大小寫：
- 頭字大寫維持（例: `O͘` → `Oo`，頭字大寫較濟全大寫）
- `M5` → `M̂`
- `Ná` → `Ná`

邊界情形 — 方言韻：
- 方言韻照原（例: `tere5` → `terê`，`terê` → `terê`，`tir5` → `tîr`）
- 特殊方言韻（例: `ionn5` → `iônn`）

邊界情形 — 合音：
- 合音照轉（例: `khiai3` → `khiài`，`khiaih4` → `khiaih`，`loih4` → `loih`）

邊界情形 — 輕聲：
- 輕聲詞照轉（例: `--Súi` → `--Suí`）
- 輕聲詞組保持（例: `--aih-iah` → `--aih-iah`）

邊界情形 — NFD：
- NFD 輸入正常處理（例: `ôa` → `uâ`）

邊界情形 — 毋是羅馬字：
- 無效羅馬字原樣輸出（例: `suii` → `suii`，`súi2` → `súi2`，`ĀIN` → `ĀIN`）
- 非羅馬字原樣輸出（例: `hello` → `hello`，`5` → `5`，`20` → `20`，`媠` → `媠`）

#### Scenario: POJ 韻母轉 KIP
- **WHEN** 輸入 `Chúi`
- **THEN** KIP 輸出 `Tsuí`

#### Scenario: 數字調轉調符
- **WHEN** 輸入 `om7`
- **THEN** KIP 輸出 `ōm`

#### Scenario: 鼻音符號轉換
- **WHEN** 輸入 `āⁿ`
- **THEN** KIP 輸出 `ānn`

#### Scenario: 合音處理
- **WHEN** 輸入 `khiai3`
- **THEN** KIP 輸出 `khiài`

#### Scenario: 毋是羅馬字原樣輸出
- **WHEN** 輸入 `媠`
- **THEN** KIP 輸出 `媠`
