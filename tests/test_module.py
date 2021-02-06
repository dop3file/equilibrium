from core.library._math import Math


def test_module():
    assert Math.math_module('-3') == 3.0
    assert Math.math_module('3') == 3.0
    assert Math.math_module('-435434534') == 435434534.0