## Context

KeSi 有三份 BDD feature files（ku、piautsunhua、susia）定義系統行為，用 Gherkin 語法寫，主要服務自動化測試。這回欲建立 OpenSpec spec.md，用人讀的格式記錄 kāng 一套行為規格。

## Goals / Non-Goals

**Goals:**
- 每個 feature file 對應一份 spec.md（1:1 mapping）
- 用折衷格式：規則描述 + 代表性 inline examples + 邊界情形
- Spec 本身就夠理解系統行為，毋免讀 Gherkin

**Non-Goals:**
- 無欲搬完整 examples table 入去 spec（留 tī feature files 做驗證）
- 無欲改 feature files 本身
- 無欲加新功能抑是改行為

## Decisions

### 1:1 mapping（feature → spec）
照現有 feature file 結構分 spec，毋是照 capability 重組。

**理由：** Feature files 已經是合理的分類（句仔操作 / Unicode 正規化 / 羅馬字轉換），重組會增加維護時的對照成本。

**替代方案：** 照 capability 拆做 5 份（sentence-parsing、word-segmentation、romanization-conversion、unicode-normalization、error-handling），但會將原本一個 feature 拆做幾若份，失去對照的便利性。

### 折衷格式
每條規則附代表性 examples（1-3 個），邊界情形獨立列出。

**理由：** 台語羅馬字轉換規則用純文字描述容易含糊（例: 「韻母照 POJ 調整」），需要 examples 來 ground。但完整 table（70+ 條）放 tī spec 會淹沒規則本身，嘛造成雙份維護。

## Risks / Trade-offs

- **Spec kah feature drift** → Spec 記錄規則層級，feature file 記錄完整 case。只要規則無改，drift 風險低。
- **Examples 選擇** → 代表性 examples 的選擇有主觀性 → 挑上能代表規則本質的，edge case 獨立標出。
