## Why

專案已經有 BDD feature files 定義行為規格，但是缺少 OpenSpec 格式的 spec.md。將 feature files 轉做 spec.md，予 AI kah 開發者有一份結構化的參考文件，毋免讀 Gherkin 語法才知影系統行為。

## What Changes

- 新增三份 spec.md，分別對應現有的三個 feature files
- Spec 用折衷格式：規則 + 代表性 examples + 邊界情形，完整 examples table 留 tī feature files 做驗證

## Capabilities

### New Capabilities
- `ku`: 句仔建立、漢羅對照、詞仔/字仔分析、輕聲處理、POJ/KIP 轉換
- `piautsunhua`: Unicode normalization — 相容區漢字轉換、羅馬字組合、教育部造字、non-printable 字元處理
- `susia`: 羅馬字書寫系統轉換 — KIP/POJ 互轉，包含數字調、鼻音、方言韻、輕聲等規則

### Modified Capabilities

（無既有 specs，攏是新增）

## Impact

- 新增 `openspec/specs/ku/spec.md`
- 新增 `openspec/specs/piautsunhua/spec.md`
- 新增 `openspec/specs/susia/spec.md`
- 無影響現有程式碼，純文件新增
