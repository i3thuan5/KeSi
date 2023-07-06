# KeSi
[![PyPI version](https://badge.fury.io/py/KeSi.svg)](https://badge.fury.io/py/KeSi)
[![Build Status](https://app.travis-ci.com/i3thuan5/KeSi.svg?branch=master)](https://app.travis-ci.com/i3thuan5/KeSi)

Tâi-bûn NLP ke-si.

## Tàu
```
pip install KeSi
```

## Iōng

有`Ku`, `TuiBeTse`, `normalize_taibun`, `kam_haphuat`, `PIAUTIAM`。

### Ku

分析台文，而且做書寫轉換。

#### class Ku(hanlo=None, lomaji=None)

建立台文ê句，做相關操作。
`hanlo`是主要ê台文，ē-tàng傳漢羅、全漢、全羅攏會用得。若台文有全羅對照，ē-tàng傳`lomaji`變數，kui-ê句會照`lomaji`來斷詞、標輕聲。若是`hanlo` kah `lomaji`字數bô-kâng，會傳`TuiBeTse`例外。

#### hanji

得tio̍h tshiâu過ê台文，有tshiâu khàng-pe̍h、Unicode NFC、教育部造字碼換做正式Unicode碼。其中若輕聲詞攏有輕聲符。

#### lomaji

得tio̍h tshiâu過ê羅馬字，有tshiâu khàng-pe̍h、Unicode NFC、教育部造字碼換做正式Unicode碼。其中若輕聲詞攏有輕聲符。

#### kiphanlo

得tio̍h tshiâu過ê台文，有tshiâu khàng-pe̍h、Unicode NFC、教育部造字碼換做正式Unicode碼。其中若輕聲詞頭字是漢字，袂有輕聲符。

#### KIP(), TL()

換做正式教育部羅馬字。

KIP數字調轉KIP：

```python
>>> from kesi import Ku
>>> Ku("Gâu5-tsa2").KIP().hanlo
'Gâu-tsá'
```

POJ轉KIP：

```python
>>> from kesi import Ku
>>> Ku("Gâu-chá").KIP().hanlo
'Gâu-tsá'
```

漢字、連字符、輕聲符lóng會好好留落來。

```python
>>> from kesi import Ku
>>> Ku("看--起-來chiâⁿ媠。").KIP().hanlo
'看--起-來tsiânn媠。'
```

修改記錄：1.4.3版以前POJ轉KIP函式號做TL()；1.5.0版以後改號做KIP()，tsit-má兩款函式lóng支援。未來KIP()會取代TL()。

#### POJ()

換做白話字。

KIP轉POJ：

```python
>>> from kesi import Ku
>>> Ku("Gâu-tsá").POJ().hanlo
'Gâu-chá'
```

漢字、連字符、輕聲符lóng會好好留落來。

```python
>>> from kesi import Ku
>>> Ku("看--起-來tsiânn媠。").POJ().hanlo
'看--起-來chiâⁿ媠。'
```

POJ數字調轉POJ：

```python
>>> from kesi import Ku
>>> Ku("Gâu5-cha2").POJ().hanlo
'Gâu-chá'
```

#### __iter__()

回傳句內下底全部`Su`ê`iter`。

#### __len__()

回傳句內下底有幾ê `Su`。

#### thianji()

回傳句內下底全部`Ji`ê`iter`。

### class Su

#### hanji

得tio̍h tshiâu過ê台文。其中若輕聲詞攏有輕聲符。

#### lomaji

得tio̍h tshiâu過ê羅馬字。其中若輕聲詞攏有輕聲符。

#### kiphanlo

得tio̍h tshiâu過ê台文。其中若輕聲詞頭字是漢字，袂有輕聲符。

#### KIP(), TL()

換做正式教育部羅馬字。

修改記錄：1.4.3版以前POJ轉KIP函式號做TL()；1.5.0版以後改號做KIP()，tsit-má兩款函式lóng支援。未來KIP()會取代TL()。

#### POJ()

換做白話字。

#### __iter__()

回傳句內下底全部`Ji`ê`iter`。

#### __len__()

回傳句內下底有幾ê `Ji`。

### class Ji

#### hanji

得tio̍h tshiâu過ê台文。其中若輕聲詞攏有輕聲符。

#### lomaji

得tio̍h tshiâu過ê羅馬字。其中若輕聲詞攏有輕聲符。

#### kiphanlo

得tio̍h tshiâu過ê台文。其中若輕聲詞頭字是漢字，袂有輕聲符。

#### KIP(), TL()

換做正式教育部羅馬字。

修改記錄：1.4.3版以前POJ轉KIP函式號做TL()；1.5.0版以後改號做KIP()，tsit-má兩款函式lóng支援。未來KIP()會取代TL()。

#### POJ()

換做白話字。

### class TuiBeTse

`Ku(hanlo, lomaji)`若`hanlo` kah `lomaji`字數bô-kâng ê時，回傳ê例外。

### def normalize_taibun(taibun)

有tshiâu Unicode NFC、教育部造字碼換做正式Unicode碼。

```
>>> from kesi import normalize_taibun
>>> normalize_taibun('a\u0301') == '\u00e1'
True
>>> normalize_taibun('\u00e1') == '\u00e1'
True
```

### def kam_haphuat(tsit_ji_lomaji)

判斷`tsit_ji_lomaji`敢是合法教育部羅馬字抑是白話字。若是數字調、調符、教育部傳統版，攏會當做合法。

```
>>> from kesi import kam_haphuat
>>> kam_haphuat('tsiânn')
True
>>> kam_haphuat('tsiann5')
True
>>> kam_haphuat('chiâⁿ')
True
>>> kam_haphuat('tsiâⁿ')
True
```

#### PIAUTIAM

含半型、全型標點符號ê `set()`。

## 其他

### 算字數

```bash
$ echo '我是Tâi-gí ê ke-si' | python le/sng_jisoo.py
# 字數= 7
```

## Khai-huat
```
tox -e behave
```
