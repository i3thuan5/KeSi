### Requirement: CJK 相容區漢字轉做統一區
系統 SHALL 將 CJK Compatibility Ideographs 轉做對應的 CJK Unified Ideographs。

規則：
- 相容區字碼轉做統一區（例: U+FA08 `行` → U+884C，U+F969 `數` → U+6578）
- 統一區內底無仝語言的漢字 MUST NOT 互相轉換（例: 日文 `様` U+69D8 袂變做台文 `樣` U+6A23）

#### Scenario: 相容區轉統一區
- **WHEN** 輸入字碼是 U+FA08（行的相容區）
- **THEN** 書寫的字碼是 U+884C（行的統一區）

#### Scenario: 統一區內底無互轉
- **WHEN** 輸入日文漢字 `様`（U+69D8）
- **THEN** 書寫 MUST NOT 變做 `樣`（U+6A23）

### Requirement: 羅馬字組合字元合做伙
系統 SHALL 將分開的字母 kah 調符（NFD）盡量組合做伙（NFC）。

規則：
- 基本調符組合（例: `a` + U+0301 → `á` U+00E1）
- 特殊組合照 Unicode 規範處理（例: `o` + U+0358 + U+0304 → `ō͘` U+014D + U+0358）

#### Scenario: 基本調符組合
- **WHEN** 輸入字碼是 U+0061,U+0301（a + 銳音符）
- **THEN** 書寫的字碼是 U+00E1（á）

#### Scenario: 特殊羅馬字組合
- **WHEN** 輸入字碼是 U+006F,U+0358,U+0304（o + 點 + 長音符）
- **THEN** 書寫的字碼是 U+014D,U+0358（ō͘）

### Requirement: 教育部造字轉做 Unicode
系統 SHALL 將教育部私用區（Private Use Area）造字轉做對應的 Unicode 字碼。

規則：
- 教育部造字碼對應到 Unicode 擴展區（例: U+E701 → U+2A736 `𪜶`，U+E705 → U+2C9B0 `𬦰`）

#### Scenario: 教育部造字轉換
- **WHEN** 輸入字碼是 U+E701（教育部造字 𪜶）
- **THEN** 書寫的字碼是 U+2A736

### Requirement: Non-printable 字元處理
系統 SHALL 將袂顯示的字元（non-printable）換做空白，予使用者看會著。

規則：
- Control characters（例: backspace U+0008）換做空白 U+0020

#### Scenario: Backspace 換做空白
- **WHEN** 輸入字碼是 U+006F,U+0008,U+0061（o + backspace + a）
- **THEN** 書寫的字碼是 U+006F,U+0020,U+0061（o + 空白 + a）
