# QA Öğrenme - Selenium ile Test Otomasyonu

Bu proje, Python programlama dili ve Selenium kütüphanesi kullanılarak hazırlanmış basit bir web test otomasyon uygulamasıdır. Otomasyon testi örnekleri üzerinden yazılım testi öğrenme ve pratik yapma amacı taşımaktadır.

## Proje Yapısı

```
|
├── pages/                      # Sayfa objeleri (Page Object Model yapısı)
| └── duckduckgo_search_page.py
├── reports/                    # HTML raporlar burada
│   └── report.html
├── tests/                      # Test senaryoları
│ └── test_search.py
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
- (Yakında: Allure, GitHub Actions)


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


Testler `webdriver-manager` kullanılarak otomatik olarak güncel ChromeDriver ile çalışır.
Her test için tarayıcı açılır ve temiz şekilde kapatılır.

## Test Raporları

Aşağıdaki komut ile HTML formatında test raporu oluşturulur:

```bash
pytest --html=reports/report.html --self-contained-html
```
`report.html` dosyasını tarayıcıda açarak sonuçları görselleştirilmiş şekilde inceleyebilirsiniz.

## Notlar

- Tarayıcı penceresi kısa sürede açılıp kapanabilir. Gözle görülemeyebilir ama test geçmişi terminalden takip edilebilir.
- Testler şu anda **headless mod kapalı** olarak çalışmaktadır...

## 📈 Geliştirme Planı
 - [x] Webdriver-manager ile otomatik sürücü yönetimi
 - [x] Page Object Model yapısı
 - [x] Pytest ile parametrik testler
 - [x] HTML test raporu oluşturma
 - [ ] Allure ile gelişmiş raporlama (sıradaki adım)
 - [ ] GitHub Actions ile CI/CD entegrasyonu
 - [ ] Test verilerinin dış kaynaklardan alınması (JSON, CSV vs.)
 - [ ] API test otomasyonuna başlangıç

## Katkıda Bulunmak

Katkılarınızı memnuniyetle karşılıyorum. Sorun bildirebilir veya yeni test senaryoları ekleyebilirsiniz.

## 👤 Yazar

**Emine Türkmen**  
[GitHub Profili](https://github.com/emineturkmenn)
