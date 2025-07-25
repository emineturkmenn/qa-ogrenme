import pytest
from login import giris_yap

def test_dogru_bilgiler():
    assert giris_yap("emine", "1234") == "Giriş Başarılı"
    
def test_yanlis_sifre():
    assert giris_yap("emine", "0000") == "Giriş Başarısız"
    
def test_yanlis_kullanici():
    assert giris_yap("mucahit", "1234")
    
def test_bos_sifre():
    with pytest.raises(ValueError):
        giris_yap("emine", "")