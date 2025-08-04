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

## 🧪 Allure ile Gelişmiş Test Raporu Oluşturma
Bu projede [Allure Test Report](https://docs.qameta.io/allure/) entegrasyonu yapılmıştır. Allure, test süreçlerini daha anlaşılır ve görsel hale getiren güçlü bir raporlama aracıdır.

### 1. Allure için testleri çalıştırma
```bash
pytest --alluredir=allure-results
```
Bu komut, Allure için gerekli ham test sonuçlarını ```allure-results/``` klasörüne oluşturur.
### 2. Allure raporunu oluşturup tarayıcıda açma
```bash
allure serve allure-results
```
```serve``` komutu, Allure raporunu derler ve varsayılan tarayıcıda açar.

### 3. Statik HTML raporu oluşturma (opsiyonel)
```bash
allure generate allure-results --clean -o allure-report
```
Oluşan ```allure-report/``` klasörü taşınabilir, paylaşılabilir bir statik HTML raporu içerir.

### Kurulum Notu
Allure komutu sisteminizde çalışmıyorsa, ```allure``` binary'sinin bulunduğu klasörü sistem ```PATH``` değişkeninize eklemeniz gerekir. Ayrıca Java kurulu olmalı ve ```JAVA_HOME``` tanımlanmalıdır.
```bash
JAVA_HOME=C:\Program Files\Java\jdk-XX
PATH=C:\allure\allure-2.34.1\bin
```

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
