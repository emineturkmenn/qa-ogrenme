# QA Öğrenme - Selenium ile Test Otomasyonu

Bu proje, Python programlama dili ve Selenium kütüphanesi kullanılarak hazırlanmış basit bir web test otomasyon uygulamasıdır. Otomasyon testi örnekleri üzerinden yazılım testi öğrenme ve pratik yapma amacı taşımaktadır.

## Proje Yapısı

```
qa-ogrenme/
│
├── archive/                    # Eski çalışmalar (arşiv)
├── drivers/                   # ChromeDriver içeren dizin (Git'e eklenmez)
│   └── chromedriver-win64/
├── tests/                     # Test senaryoları
│   └── test_duckduckgo_search.py
├── conftest.py                # Pytest için fixture yapılandırması
├── requirements.txt           # Bağımlılık dosyası
└── .gitignore                 # Gereksiz dosyaların takibini engeller
```

## Kullanılan Teknolojiler

- Python 3.10
- Selenium
- Pytest
- Chrome ve ChromeDriver

## Kurulum

1. **Depoyu klonlayın:**

```bash
git clone https://github.com/emineturkmenn/qa-ogrenme.git
cd qa-ogrenme
```

2. **Gerekli kütüphaneleri yükleyin:**

```bash
pip install -r requirements.txt
```

3. **ChromeDriver’ı indirip `drivers/chromedriver-win64/` klasörüne yerleştirin.**

[ChromeDriver İndir (Sürümünüze uygun olanı seçin)](https://googlechromelabs.github.io/chrome-for-testing/)

## Testi Çalıştırma

```bash
pytest
```

Test başarıyla çalışırsa, DuckDuckGo'da "selenium python" araması yapılacak ve sonuçlar kontrol edilecektir.

## Notlar

- `chromedriver-win64/` klasörü `.gitignore` dosyasına eklenmiştir. Bu nedenle GitHub'a yüklenmez.
- Tarayıcı penceresi kısa sürede açılıp kapanabilir. Gözle görülemeyebilir ama test geçmişi terminalden takip edilebilir.

## Katkıda Bulunmak

Katkılarınızı memnuniyetle karşılıyorum. Sorun bildirebilir veya yeni test senaryoları ekleyebilirsiniz.
