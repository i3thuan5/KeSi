# KeSi
[![PyPI version](https://badge.fury.io/py/KeSi.svg)](https://badge.fury.io/py/KeSi)
[![Build Status](https://app.travis-ci.com/i3thuan5/KeSi.svg?branch=master)](https://app.travis-ci.com/i3thuan5/KeSi)

Tâi-bûn NLP ke-si.

## Tàu
```
pip install KeSi
```

## Iōng

### POJ轉KIP
```python
Ku("Gâu-chá").TL().hanlo         # 'Gâu-tsá'
```
漢字、連字符、輕聲符lóng會好好留落來。
```python
Ku("看--起-來chiâⁿ媠。").TL().hanlo    # '看--起-來tsiânn媠。'
```
### KIP轉POJ
```python
Ku("Gâu-tsá").POJ().hanlo        # 'Gâu-chá'
```
漢字、連字符、輕聲符lóng會好好留落來。
```python
Ku("看--起-來tsiânn媠。").POJ().hanlo     # '看--起-來chiâⁿ媠。'
```
### 算字數
```bash
$ echo '我是Tâi-gí ê ke-si' | python le/sng_jisoo.py
# 字數= 7
```

## Khai-huat
```
tox -e behave
```
