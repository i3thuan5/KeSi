from .butkian.ku import Ku
from .butkian.ku import TuiBeTse
from .butkian.kongiong import KHIN_SIANN_HU
from .butkian.kongiong import normalize_taibun
from .butkian.kongiong import 標點符號 as PIAUTIAM
from .susia.kongke import thiah, SuSiaTshoNgoo


def kam_haphuat(tsit_ji_lomaji):
    # 輕聲音節頭--ê '--' 先提掉才判斷（#47）
    lomaji = tsit_ji_lomaji
    if lomaji.startswith(KHIN_SIANN_HU):
        lomaji = lomaji[len(KHIN_SIANN_HU):]
    try:
        thiah(lomaji)
    except SuSiaTshoNgoo:
        return False
    return True


__all__ = [
    'Ku', 'TuiBeTse', 'normalize_taibun',
    'kam_haphuat', PIAUTIAM,
]
