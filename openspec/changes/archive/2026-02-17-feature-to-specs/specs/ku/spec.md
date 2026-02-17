## ADDED Requirements

### Requirement: 句仔建立（純羅馬字）
系統 SHALL 接受一段文字建立 `Ku` 物件，輸出 hanlo kah lomaji。

漢羅文規則：
- 羅馬字之間的空白保留，其他空白清掉（例: `我是 Ke-si` → `我是Ke-si`）
- 輕聲符 `--` kah 頭前連寫，無空白（例: `Guá --lah` → `Guá--lah`）
- 漢字輕聲保持原樣（例: `緊--出-來--啦`）
- 數字 kah 連字符保持原樣（例: `0800-092-000`）

嘛 ē-tàng kan-na 傳 lomaji 參數來建立句仔。

#### Scenario: 漢羅文空白處理
- **WHEN** 用 `我是 Ke-si` 建立句仔
- **THEN** hanlo 是 `我是Ke-si`，lomaji 是 `我是Ke-si`

#### Scenario: 輕聲符連寫
- **WHEN** 用 `Guá --lah` 建立句仔
- **THEN** hanlo 是 `Guá--lah`

#### Scenario: Kan-na 傳 lomaji
- **WHEN** kan-na 傳 lomaji `Guá sī Ke-si` 建立句仔
- **THEN** hanlo 是 `Guá sī Ke-si`，lomaji 是 `Guá sī Ke-si`

### Requirement: 漢羅 kah 羅馬字對照建立句仔
系統 SHALL 接受 hanlo kah lomaji 兩個參數建立 `Ku` 物件，照羅馬字決定斷詞 kah 輕聲。

規則：
- 漢字 kah 羅馬字對照，空白照羅馬字決定（例: hanlo `我是 Ke-si ê 物件` + lomaji `Guá sī Ke-si ê mi̍h-kiānn` → hanlo `我是Ke-si ê物件`）
- 組字式保持原樣（例: `癩⿸疒哥人`）
- 標點符號對照（例: 全形 `，` 對應半形 `,`，刪節號 `……` 對應 `...`）
- 數字保持原樣（例: `20 pha`）
- 照羅馬字決定輕聲符位置（例: hanlo `我啦` + lomaji `Guá--lah` → hanlo `我--啦`）

#### Scenario: 漢羅對照基本
- **WHEN** 用 hanlo `我是 Ke-si ê 物件` kah lomaji `Guá sī Ke-si ê mi̍h-kiānn` 建立句仔
- **THEN** hanlo 是 `我是Ke-si ê物件`，lomaji 是 `Guá sī Ke-si ê mi̍h-kiānn`

#### Scenario: 標點符號對照
- **WHEN** 用 hanlo `𠢕早，` kah lomaji `Gâu-tsá,` 建立句仔
- **THEN** hanlo 是 `𠢕早，`，lomaji 是 `Gâu-tsá,`

#### Scenario: 照羅馬字決定輕聲
- **WHEN** 用 hanlo `我啦` kah lomaji `Guá--lah` 建立句仔
- **THEN** hanlo 是 `我--啦`

### Requirement: 教育部漢羅（kiphanlo）
系統 SHALL 提供 `kiphanlo` 輸出，照教育部規範，漢字部分袂有連字符。

規則：
- 漢字之間的連字符 kah 輕聲符清掉（例: `有--一-寡` + `ū--tsi̍t-kuá` → kiphanlo `有一寡`）
- 純羅馬字保持原樣（例: `oo-tóo-bái` → `oo-tóo-bái`）
- 輕聲漢字 `啊` 對應 `--ah` 時，kiphanlo 是 `啊`
- 純羅馬字輕聲保持（例: `āu--ji̍t` → `āu--ji̍t`）

#### Scenario: 漢字連字符清掉
- **WHEN** 用 hanlo `有--一-寡` kah lomaji `ū--tsi̍t-kuá` 建立句仔
- **THEN** kiphanlo 是 `有一寡`

#### Scenario: 純羅馬字保持
- **WHEN** 用 hanlo `oo-tóo-bái` kah lomaji `oo-tóo-bái` 建立句仔
- **THEN** kiphanlo 是 `oo-tóo-bái`

### Requirement: 詞仔 kah 字仔分析
系統 SHALL 將句仔拆做詞仔（`Su`）kah 字仔（`Ji`），照羅馬字的空白斷詞。

規則：
- 有空白就斷做無仝詞，連寫算一詞
- 輕聲符 `--` kah 連字符 `-` 行為 kāng-khuán（攏是連做伙）
- 每個詞仔 ē-tàng 進一步提著字仔
- 輕聲字算獨立一字（例: `--啦` / `--lah`）

#### Scenario: 句仔斷詞
- **WHEN** 用 hanlo `我是超潮的Ke-si--啦` kah lomaji `Guá sī超潮的Ke-si--lah` 建立句仔
- **THEN** 詞仔是 `我/Guá`、`是/sī`、`超潮的/超潮的`、`Ke-si--啦/Ke-si--lah`

#### Scenario: 詞仔提著字仔
- **WHEN** 提著第 4 詞 `Ke-si--啦`
- **THEN** 字仔是 `Ke/Ke`、`si/si`、`--啦/--lah`

### Requirement: 字數對照錯誤
系統 SHALL tī 漢羅 kah 羅馬字字數對袂著的時陣，發出錯誤。

邊界情形：
- hanlo `我啦` vs lomaji `--lah`（漢字較濟）
- hanlo `我` vs lomaji `Guá--lah`（羅馬字較濟）
- 中間詞仔字數對袂著

#### Scenario: 字數無仝發錯誤
- **WHEN** 用 hanlo `我啦` kah lomaji `--lah` 建立句仔
- **THEN** 系統 SHALL 發出錯誤

#### Scenario: 詞內字數對袂著
- **WHEN** 用 hanlo `我 就是Ke-si-thâu-á 你好` kah lomaji `Guá tō sī lí-hó` 建立句仔
- **THEN** 系統 SHALL 發出錯誤

### Requirement: 羅馬字書寫轉換（POJ/KIP）
系統 SHALL 將句仔的羅馬字轉做 POJ 抑是 KIP 書寫，原本句仔袂變。

規則：
- POJ 轉換照 POJ 系統（例: `Guá` → `Góa`，`Ke-si` → `Ke-si`）
- KIP 轉換照教育部台羅（例: `Góa` → `Guá`）
- 數字調轉做調符（例: `Gua2` → KIP `Guá` / POJ `Góa`）
- 轉換產生新句仔，原本句仔不變
- 漢羅對照句仔嘛支援轉換（例: `一/tsi̍t` → POJ `chi̍t` / KIP `tsi̍t`）

#### Scenario: 純羅馬字轉 POJ
- **WHEN** 用 `Guá sī Ke-si` 建立句仔，轉做 POJ
- **THEN** POJ 句仔的 hanlo 是 `Góa sī Ke-si`

#### Scenario: 數字調轉換
- **WHEN** 用 `Gua2 si7 Ke1-si1` 建立句仔
- **THEN** 轉 KIP 是 `Guá sī Ke-si`，轉 POJ 是 `Góa sī Ke-si`

#### Scenario: 原本句仔不變
- **WHEN** 用 `Guá sī Ke-si` 建立句仔，轉做 POJ
- **THEN** 原本句仔猶原是 `Guá sī Ke-si`

#### Scenario: 漢羅對照轉換
- **WHEN** 用 hanlo `一` kah lomaji `tsi̍t` 建立句仔
- **THEN** 轉 POJ lomaji 是 `chi̍t`，轉 KIP lomaji 是 `tsi̍t`
