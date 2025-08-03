# QA Öğrenme - Selenium ile Test Otomasyonu

Bu proje, Python programlama dili ve Selenium kütüphanesi kullanılarak hazırlanmış basit bir web test otomasyon uygulamasıdır. Otomasyon testi örnekleri üzerinden yazılım testi öğrenme ve pratik yapma amacı taşımaktadır.

## Proje Yapısı

```
|
├── pages/                      # Sayfa objeleri (Page Object Model yapısı)
│ └── duckduckgo_result_page.py
| └── duckduckgo_search_page.py
├── reports/                    # HTML raporlar burada
│   └── report.html
├── tests/                      # Test senaryoları
│ └── test_duckduckgo_search.py
├── conftest.py                 # Pytest için fixture yapılandırması
├── requirements.txt            # Bağımlılıkları listeler
├── .gitignore                  # Gereksiz dosyaların takibini engeller
└── README.md                   # Proje dokümantasyonu
```

## Kullanılan Teknolojiler

- Python 3.10+
- Selenium
- Pytest
- [webdriver-manager](https://pypi.org/project/webdriver-manager/)


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

## Testi Çalıştırma

```bash
pytest
```

Test başarıyla çalışırsa, DuckDuckGo'da `"selenium python"` araması yapılacak ve sonuçlar kontrol edilecektir.

## WebDriver Hakkında

Bu projede [`webdriver-manager`](https://pypi.org/project/webdriver-manager/) eklentisi kullanılarak ChromeDriver'ın sisteminize uygun sürümü **otomatik olarak indirilir ve kullanılır.**

Artık `chromedriver.exe` gibi dosyaları manuel indirmenize gerek yoktur. Bu nedenle `drivers/` klasörüne ihtiyaç kalmamıştır.

## Test Raporları

Aşağıdaki komut ile HTML formatında test raporu oluşturulur:

```bash
pytest --html=reports/report.html --self-contained-html
```

## Notlar

- `chromedriver-win64/` klasörü `.gitignore` dosyasına eklenmiştir. Bu nedenle GitHub'a yüklenmez.
- Tarayıcı penceresi kısa sürede açılıp kapanabilir. Gözle görülemeyebilir ama test geçmişi terminalden takip edilebilir.
- Testler şu anda **headless mod kapalı** olarak çalışmaktadır...


## Katkıda Bulunmak

Katkılarınızı memnuniyetle karşılıyorum. Sorun bildirebilir veya yeni test senaryoları ekleyebilirsiniz.
