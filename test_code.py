from core.library._math import Math


def test_ceil():
    assert Math.ceil('2.5') == 3
    assert Math.ceil('2.45') == 2
    assert Math.ceil('3343.53432432432') == 3344

def test_module():
    assert Math.math_module('-3') == 3.0
    assert Math.math_module('3') == 3.0
    assert Math.math_module('-435434534') == 435434534.0


