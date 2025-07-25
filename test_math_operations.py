import pytest
from math_operations import bol, topla


def test_topla():
    assert topla(3,5) == 8
    assert topla(-1,1) == 0
    assert topla(0,0) == 0

def test_bolme():
    assert bol(10,2) == 5
    assert bol(-6,3) == -2
    
def test_bolme_sifira():
    with pytest.raises(ValueError, match="Sıfıra bölünemez"):
        bol(10,0)