# Nakliye Sistemi - Landing Page

Modern ve profesyonel bir nakliye hizmetleri landing page uygulaması.

## Özellikler
- Responsive tasarım (Bootstrap 5)
- Hizmetler vitrin sayfası
- İletişim formu
- Modern gradient arka plan
- Türkçe arayüz

## Başlangıç

1. Python 3.10+ kurulu olmalı
2. `python -m venv venv && venv\Scripts\activate`
3. `pip install -r requirements.txt`
4. `python run.py` ile başlat
5. http://localhost:5000 adresinden ziyaret edin

## Dosya Yapısı
```
app/
├── __init__.py          # Flask app konfigürasyonu
├── models.py            # Veritabanı modelleri
├── auth/               # Kimlik doğrulama modülü
│   ├── __init__.py
│   └── routes.py
├── templates/          # HTML şablonları
│   ├── base.html       # Temel şablon
│   ├── index.html      # Ana sayfa
│   └── contact.html    # İletişim sayfası
config.py              # Uygulama konfigürasyonu
run.py                 # Başlangıç dosyası
requirements.txt       # Bağımlılıklar
```

## Teknolojiler
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Bootstrap 5
- SQLite

## Lisans
MIT
