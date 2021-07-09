from .butkian.ku import Ku
from .butkian.ku import TuiBeTse
from .butkian.kongiong import normalize_taibun
from .butkian.kongiong import 標點符號 as PIAUTIAM
from .susia.kongke import thiah, SuSiaTshoNgoo


def kam_haphuat(tsit_ji_lomaji):
    try:
        thiah(tsit_ji_lomaji)
    except SuSiaTshoNgoo:
        return False
    return True


__all__ = [
    'Ku', 'TuiBeTse', 'normalize_taibun',
    'kam_haphuat', PIAUTIAM,
]
