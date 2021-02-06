from core.library._math import Math


def test_ceil():
    assert Math.ceil('2.5') == 3
    assert Math.ceil('2.45') == 2
    assert Math.ceil('3343.53432432432') == 3344


