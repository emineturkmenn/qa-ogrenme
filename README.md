# QA Öğrenme - Selenium ile Test Otomasyonu

Bu proje, Python programlama dili ve Selenium kütüphanesi kullanılarak hazırlanmış basit bir web test otomasyon uygulamasıdır. Otomasyon testi örnekleri üzerinden yazılım testi öğrenme ve pratik yapma amacı taşımaktadır.

## Proje Yapısı

```
│
├── drivers/                    # ChromeDriver dosyası burada tutulur (Git'e eklenmez)
│ └── chromedriver-win64/
├── pages/                      # Sayfa objeleri (Page Object Model yapısı)
│ └── duckduckgo_result_page.py
| └── duckduckgo_search_page.py
├── tests/                      # Test senaryoları
│ └── test_duckduckgo_search.py
├── conftest.py                 # Pytest için fixture yapılandırması
├── requirements.txt            # Bağımlılıkları listeler
├── .gitignore                  # Gereksiz dosyaların takibini engeller
└── README.md                   # Proje dokümantasyonu
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

> **Not:** Testler şu anda **headless mod kapalı** olarak çalışmaktadır...


## Katkıda Bulunmak

Katkılarınızı memnuniyetle karşılıyorum. Sorun bildirebilir veya yeni test senaryoları ekleyebilirsiniz.
