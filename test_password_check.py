import pytest

from password_strength_checker import check_password_strength as checker

def test_checker():
    assert checker('R@jiv201992') == True

    assert checker('Rajiv12') == False