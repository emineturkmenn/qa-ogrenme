import pytest
from calculator import topla, cikar, carp, bol

def test_topla():
    assert topla(10,5) == 15
    
def test_cikar():
    assert cikar(-2,5) == -7
    
def test_carp():
    assert carp(2,0) == 0
    
def test_bol():
    assert bol(6,3) == 2

def test_bol_sifirsa():
    with pytest.raises(ValueError):
        bol(5,0)