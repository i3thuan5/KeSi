from .butkian.ku import Ku
from .butkian.ku import TuiBeTse
from .butkian.kongiong import normalize_taibun
from .susia.kongke import thiah, SuSiaTshoNgoo


def kam_haphuat(tsit_ji_lomaji):
    try:
        thiah(tsit_ji_lomaji)
    except SuSiaTshoNgoo:
        return False
    return True


__all__ = ['Ku', 'TuiBeTse', 'kam_haphuat', 'normalize_taibun']
