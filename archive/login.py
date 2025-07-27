def giris_yap(kullanici_adi, sifre):
    dogru_kullanici = "emine"
    dogru_sifre = "1234"
    
    if not sifre :
        raise ValueError("Şifre boş olamaz.")
    
    if kullanici_adi == dogru_kullanici and sifre == dogru_sifre:
        return "Giriş Başarılı"
    else: 
        return "Giriş Başarısız"