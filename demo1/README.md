# 🎨 Eğitim Paint Uygulaması

Python 3 ve Tkinter ile hazırlanmış basit ama güçlü bir Paint uygulaması. Bu proje, Python programlama öğrenmek isteyenler için ideal bir eğitim projesidir. Kendi dijital tuvalinde özgürce çiz ve programlama becerilerini geliştir!

## 🚀 Özellikler

### 🛠️ Araçlar
- **Kalem (Pen)**  
  - Renk ve kalınlık seçilebilir  
- **Fırça (Brush)**  
  - Renk ve kalınlık ayarlanabilir  
- **Silgi (Eraser)**  
  - Çizimleri kolayca sil  
- **Şekiller (Shapes)**  
  - Dikdörtgen  
  - Çember  
  - Oval  
  - Düz çizgi

### 🖼️ Görsel İşlemleri
- Resim ekleyebilme  
- Mevcut bir resmi açma  
- Tuvali `.jpg` olarak kaydetme  

### 🧩 Diğer Özellikler
- Geri alma (Undo)  
- Tuvali sıfırlama  
- Renk paletiyle özelleştirme  
- Seçilen aracın kalınlığını artırma/azaltma  

## 🎯 Eğitim Hedefleri

Bu proje ile öğrenebileceğiniz konular:

- **Tkinter GUI Kütüphanesi**: Python'da grafik arayüz geliştirme
- **Canvas Widget**: Çizim ve grafik işlemleri
- **Event Handling**: Fare ve klavye olaylarını yönetme
- **Menu System**: Menü çubuğu oluşturma
- **File Operations**: Dosya açma, kaydetme işlemleri
- **Image Processing**: PIL kütüphanesi ile resim işleme
- **Object-Oriented Programming**: Sınıf ve nesne yapıları

## 🧰 Gereksinimler

```bash
pip install -r requirements.txt
```

## 📥 Kurulum

### 1. Projeyi İndirin
```bash
# Reposu klonlayın
git clone https://github.com/kullaniciadi/paint_proje.git

# Klasöre girin
cd paint_proje/demo1
```

### 2. Sanal Ortam Oluşturun (Önerilen)
```bash
# Sanal ortam oluşturun
python -m venv .venv

# Ortamı aktifleştirin
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate
```

### 3. Gerekli Kütüphaneleri Yükleyin
```bash
# Gereken modülleri yükleyin
pip install -r requirements.txt

# Veya manuel olarak:
pip install Pillow pyglet
```

### 4. Uygulamayı Çalıştırın
```bash
# Sanal ortam ile:
& "c:/github repolarım/paint_proje/.venv/Scripts/python.exe" "c:/github repolarım/paint_proje/demo1/main.py"

# Veya doğrudan:
python main.py
```

## 📚 Öğrenme Rehberi

### 1. Temel Kavramlar
- **Tkinter**: Python'un standart GUI kütüphanesi
- **Canvas**: Çizim yapılabilecek dikdörtgen alan
- **Event Binding**: Olayları fonksiyonlara bağlama

### 2. Proje Yapısı
```
demo1/
├── main.py          # Ana uygulama dosyası
├── tools.py         # Araç sınıfları
├── canvas_image.py  # Canvas resim işlemleri
├── about.py         # Hakkında ve yardım pencereleri
├── baslat.py        # Akıllı başlatma scripti
├── kullanim_kilavuzu.md  # Detaylı kullanım kılavuzu
├── requirements.txt # Gerekli kütüphaneler
└── icon.png         # Uygulama ikonu
```

### 3. Kod Analizi
- **Tool Class**: Her çizim aracı için ayrı sınıf
- **Event Handlers**: Fare olaylarını yöneten fonksiyonlar
- **Menu System**: Menü çubuğu ve alt menüler

## 🎨 Kullanım Örnekleri

### Basit Çizim
1. Kalem aracını seç
2. İstediğin rengi seç
3. Kalınlığı ayarla
4. Tuvalde çizim yap

### Şekil Çizimi
1. Şekil menüsünden istediğin şekli seç
2. Tuvalde fare ile sürükleyerek şekli çiz

### Resim Kaydetme
1. Dosya menüsünden "Kaydet" seç
2. Otomatik olarak timestamp ile kaydedilir

## 🔧 Geliştirme Önerileri

Bu projeyi geliştirmek için yapabilecekleriniz:

- [ ] Yeni çizim araçları ekleme (spray, text, etc.)
- [ ] Katman sistemi ekleme
- [ ] Filtreler ve efektler ekleme
- [ ] Çoklu tuval desteği
- [ ] Kısayol tuşları ekleme
- [ ] Ayarlar menüsü ekleme

## 📖 Öğrenme Kaynakları

- [Python Tkinter Dokümantasyonu](https://docs.python.org/3/library/tkinter.html)
- [PIL/Pillow Dokümantasyonu](https://pillow.readthedocs.io/)
- [Python GUI Programming](https://realpython.com/python-gui-tkinter/)

## 🤝 Katkıda Bulunma

Bu eğitim projesine katkıda bulunmak istiyorsanız:

1. Projeyi fork edin
2. Yeni özellik ekleyin
3. Pull request gönderin
4. Kod kalitesini artırın

## 📄 Lisans

Bu proje eğitim amaçlı hazırlanmıştır ve açık kaynak kodludur.

## 🚀 Hızlı Başlangıç

```bash
# 1. Projeyi klonlayın
git clone https://github.com/kullaniciadi/paint_proje.git

# 2. Klasöre girin
cd paint_proje/demo1

# 3. Kütüphaneleri yükleyin
pip install Pillow pyglet

# 4. Çalıştırın
python main.py
```

---

**🎯 Hedef**: Python programlama becerilerinizi geliştirin ve güzel bir Paint uygulaması oluşturun!

**💡 İpucu**: Kodu satır satır inceleyin, her fonksiyonun ne yaptığını anlamaya çalışın ve kendi özelliklerinizi eklemeyi deneyin.

**⭐ Star**: Bu projeyi beğendiyseniz GitHub'da star vermeyi unutmayın!
