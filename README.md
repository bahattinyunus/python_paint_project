# 🎨 Eğitim Paint Uygulaması

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange.svg)](https://docs.python.org/3/library/tkinter.html)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Language](https://img.shields.io/badge/Language-Turkish-red.svg)](https://github.com/bahattinyunuscetin/python_paint_project)

> **Türkçe arayüzlü, eğitim odaklı Paint uygulaması** - Python ve Tkinter ile geliştirilmiş, öğrenciler için ideal çizim aracı.

## 🌟 Proje Hakkında

Bu proje, Python programlama öğrenenler için tasarlanmış, Türkçe arayüzlü bir Paint uygulamasıdır. Tkinter kütüphanesi kullanılarak geliştirilmiş olup, temel çizim araçları ve kullanıcı dostu arayüz sunar.

### 🎯 Eğitim Hedefleri
- **Python GUI programlama** öğrenimi
- **Tkinter kütüphanesi** kullanımı
- **Event handling** ve **canvas** yönetimi
- **Dosya işlemleri** ve **görsel programlama**
- **Türkçe arayüz** geliştirme

## 🚀 Hızlı Başlangıç

### 📋 Gereksinimler
- Python 3.6 veya üzeri
- Windows, macOS veya Linux

### ⚡ Tek Komutla Çalıştırma
```bash
# Projeyi klonlayın
git clone https://github.com/bahattinyunuscetin/python_paint_project.git

# Klasöre girin
cd python_paint_project

# Uygulamayı çalıştırın
python demo1/main.py
```

## 📁 Proje Yapısı

```
python_paint_project/
├── 📁 demo1/                    # Ana uygulama klasörü
│   ├── 🎨 main.py              # Ana uygulama dosyası
│   ├── 🛠️ tools.py             # Çizim araçları sınıfı
│   ├── 🖼️ canvas_image.py      # Resim işleme modülü
│   ├── ℹ️ about.py              # Hakkında ve yardım pencereleri
│   ├── 🚀 baslat.py            # Akıllı başlatma scripti
│   ├── 📖 README.md             # Detaylı kullanım kılavuzu
│   ├── 📚 kullanim_kilavuzu.md # Kullanım rehberi
│   ├── 📦 requirements.txt      # Gerekli kütüphaneler
│   └── 🖼️ icon.png             # Uygulama ikonu
├── 📄 README.md                 # Bu dosya (genel proje bilgisi)
├── 📄 LICENSE                   # MIT lisans dosyası
├── 📄 CONTRIBUTING.md           # Katkıda bulunma rehberi
├── 📄 CHANGELOG.md              # Değişiklik günlüğü
└── 📄 .gitignore                # Git ignore dosyası
```

## 🎨 Özellikler

### ✏️ Çizim Araçları
- **Kalem**: Serbest çizim
- **Fırça**: Farklı boyutlarda çizim
- **Silgi**: Çizim silme
- **Şekiller**: Çizgi, dikdörtgen, çember, oval

### 🎛️ Arayüz Özellikleri
- **Türkçe menü sistemi**
- **Renk seçici**
- **Boyut ayarları**
- **Geri alma özelliği**
- **Dosya işlemleri** (aç, kaydet, farklı kaydet)

### 📱 Kullanıcı Deneyimi
- **Hoş geldin mesajı**
- **Detaylı yardım sistemi**
- **Kullanım kılavuzu**
- **Responsive tasarım**

## 🛠️ Kurulum

### 1. Projeyi İndirin
```bash
git clone https://github.com/bahattinyunuscetin/python_paint_project.git
cd python_paint_project
```

### 2. Sanal Ortam Oluşturun (Önerilen)
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Gerekli Kütüphaneleri Yükleyin
```bash
pip install -r demo1/requirements.txt
```

### 4. Uygulamayı Çalıştırın
```bash
python demo1/main.py
```

## 📚 Öğrenme Rehberi

### 🎯 Başlangıç Seviyesi
- **Python temelleri** bilgisi
- **Tkinter widget'ları** anlayışı
- **Event handling** kavramları

### 🔧 Orta Seviye
- **Canvas yönetimi** ve **çizim işlemleri**
- **Dosya işlemleri** ve **görsel programlama**
- **Arayüz tasarımı** ve **kullanıcı deneyimi**

### 🚀 İleri Seviye
- **Kod organizasyonu** ve **modüler yapı**
- **Hata yönetimi** ve **güvenlik**
- **Performans optimizasyonu**

## 🎨 Kullanım Örnekleri

### Basit Çizim
1. Uygulamayı başlatın
2. Kalem aracını seçin
3. Canvas'ta çizim yapın
4. Farklı renkler deneyin

### Şekil Çizimi
1. Şekil aracını seçin
2. İstediğiniz şekli seçin
3. Canvas'ta sürükleyerek çizin

### Resim Kaydetme
1. **Dosya → Kaydet** menüsünü kullanın
2. Dosya adı ve konum belirleyin
3. JPG formatında kaydedin

## 🔧 Geliştirme

### Katkıda Bulunma
Bu proje açık kaynak kodludur ve katkılarınızı bekler! Detaylar için [CONTRIBUTING.md](CONTRIBUTING.md) dosyasını inceleyin.

### Geliştirme Ortamı
```bash
# Geliştirme için gerekli araçlar
pip install black flake8 pytest
```

### Test Etme
```bash
# Kod kalitesi kontrolü
black demo1/
flake8 demo1/

# Uygulama testi
python demo1/main.py
```

## 📖 Dokümantasyon

- **[demo1/README.md](demo1/README.md)**: Detaylı kullanım kılavuzu
- **[demo1/kullanim_kilavuzu.md](demo1/kullanim_kilavuzu.md)**: Kullanım rehberi
- **[CONTRIBUTING.md](CONTRIBUTING.md)**: Katkıda bulunma rehberi
- **[CHANGELOG.md](CHANGELOG.md)**: Değişiklik günlüğü

## 🌟 Öne Çıkan Özellikler

### 🎯 Eğitim Odaklı
- **Türkçe arayüz** ile kolay öğrenim
- **Detaylı açıklamalar** ve yardım sistemi
- **Adım adım kullanım** kılavuzu

### 🚀 Kullanıcı Dostu
- **Sezgisel arayüz** tasarımı
- **Hızlı başlatma** scripti
- **Kapsamlı dokümantasyon**

### 🔧 Teknik Kalite
- **Modüler kod yapısı**
- **Hata yönetimi** ve güvenlik
- **Cross-platform** uyumluluk

## 🤝 Topluluk

### 📞 İletişim
- **GitHub Issues**: [Bug raporları ve öneriler](https://github.com/bahattinyunuscetin/python_paint_project/issues)
- **Discussions**: [Genel sorular ve tartışmalar](https://github.com/bahattinyunuscetin/python_paint_project/discussions)

### 🌟 Destekleyin
Bu projeyi beğendiyseniz:
- ⭐ **Star** verin
- 🔄 **Fork** edin
- 💬 **Issue** açın
- 🚀 **Pull Request** gönderin

## 📄 Lisans

Bu proje [MIT License](LICENSE) altında lisanslanmıştır. Detaylar için lisans dosyasını inceleyin.

## 🙏 Teşekkürler

- **Python topluluğu** - Harika programlama dili için
- **Tkinter geliştiricileri** - GUI kütüphanesi için
- **Açık kaynak topluluğu** - İlham ve destek için

---

<div align="center">

**🎨 Eğitim Paint Uygulaması ile Python GUI programlamayı öğrenin!**

[🚀 Başlayın](demo1/README.md) • [📚 Dokümantasyon](demo1/kullanim_kilavuzu.md) • [🤝 Katkıda Bulunun](CONTRIBUTING.md)

</div>
