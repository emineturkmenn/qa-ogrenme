# Login Modülü Test Dokümantasyonu

## Test Edilen Fonksiyon
`giris_yap(kullanici_adi, sifre)`

## Amaç
Kullanıcı adı ve şifre ile giriş işlemini test etmek.

## Test Senaryoları

1. ✅ Doğru kullanıcı adı ve şifre girildiğinde "Giriş başarılı" dönmeli.
2. ❌ Hatalı şifre girildiğinde "Giriş başarısız" dönmeli.
3. ❌ Hatalı kullanıcı adı girildiğinde "Giriş başarısız" dönmeli.
4. ⚠️ Şifre boş bırakıldığında `ValueError` hatası fırlatmalı.

## Kullanılan Test Aracı
- pytest 7.3.1

## Sonuç
Tüm testler başarıyla geçmiştir.
