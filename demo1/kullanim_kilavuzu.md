# 🎨 Eğitim Paint Uygulaması - Kullanım Kılavuzu

## 📖 Giriş

Bu kılavuz, Python programlama öğrenmek isteyenler için hazırlanmış Paint uygulamasının nasıl kullanılacağını açıklar. Uygulama, Tkinter kütüphanesi kullanılarak geliştirilmiştir ve temel çizim işlemlerini öğrenmek için idealdir.

## 🚀 Uygulamayı Başlatma

1. Terminal veya komut istemcisini açın
2. Proje klasörüne gidin: `cd demo1`
3. Uygulamayı çalıştırın: `python main.py`

## 🎯 Ana Özellikler

### 📁 Dosya Menüsü
- **Yeni**: Yeni bir tuval oluşturur (mevcut çizimi siler)
- **Aç**: Bilgisayarınızdan resim dosyası açar
- **Kaydet**: Çiziminizi otomatik olarak kaydeder
- **Farklı Kaydet**: Çiziminizi istediğiniz konuma kaydeder
- **Temizle**: Tuvali temizler
- **Çıkış**: Uygulamayı kapatır

### ✏️ Düzenle Menüsü
- **Geri Al**: Son yapılan çizimi geri alır
- **Tümünü Sil**: Tüm çizimleri siler

### 🔧 Ekle Menüsü
- **Resim Ekle**: Tuvalinize resim ekler
- **Çizgi**: Düz çizgi çizer
- **Dikdörtgen**: Dikdörtgen şekli çizer
- **Çember**: Çember şekli çizer
- **Oval**: Oval şekli çizer

### 🛠️ Araç Çubuğu
- **Kalem**: İnce çizimler için
- **Fırça**: Kalın çizimler için
- **Silgi**: Hataları düzeltmek için
- **Renk**: Renk seçici açar
- **+/-**: Araç kalınlığını artırır/azaltır

## 🎨 Çizim Yapma

### 1. Basit Çizim
1. Kalem aracını seçin
2. İstediğiniz rengi seçin
3. Kalınlığı ayarlayın
4. Tuvalde fare ile çizim yapın

### 2. Şekil Çizimi
1. Ekle menüsünden istediğiniz şekli seçin
2. Tuvalde fare ile sürükleyerek şekli çizin
3. Fare bırakıldığında şekil tamamlanır

### 3. Resim Ekleme
1. Ekle menüsünden "Resim Ekle" seçin
2. Bilgisayarınızdan resim dosyası seçin
3. Resim tuvalinize eklenir ve taşınabilir

## 🔍 Detaylı Özellikler

### Renk Seçimi
- Renk butonuna tıklayarak renk paleti açılır
- İstediğiniz rengi seçin ve "Tamam" deyin
- Seçilen renk aktif araç için kullanılır

### Boyut Ayarlama
- "+" butonu ile araç kalınlığını artırın
- "-" butonu ile araç kalınlığını azaltın
- Mevcut kalınlık menüde gösterilir

### Geri Alma
- Düzenle menüsünden "Geri Al" seçin
- Son yapılan çizim silinir
- Birden fazla kez kullanılabilir

## 💾 Dosya İşlemleri

### Kaydetme
- **Otomatik Kaydet**: "Kaydet" ile timestamp ile kaydedilir
- **Manuel Kaydet**: "Farklı Kaydet" ile konum seçebilirsiniz
- Desteklenen format: JPG

### Açma
- Mevcut resim dosyalarını açabilirsiniz
- Desteklenen formatlar: JPG, PNG, GIF, BMP

## 🎓 Eğitim İpuçları

### Python Öğrenimi İçin
1. **Kod İnceleme**: Her fonksiyonun ne yaptığını anlamaya çalışın
2. **Değişiklik Yapma**: Renkleri, boyutları değiştirmeyi deneyin
3. **Yeni Özellik**: Kendi araçlarınızı eklemeyi deneyin
4. **Hata Ayıklama**: Hataları anlamaya ve düzeltmeye çalışın

### Tkinter Öğrenimi İçin
- **Widget'lar**: Canvas, Menu, Button gibi bileşenleri inceleyin
- **Event Handling**: Fare ve klavye olaylarını nasıl yönettiğini öğrenin
- **Layout Management**: Pencere düzenini nasıl yönettiğini anlayın

## 🔧 Sorun Giderme

### Yaygın Sorunlar
1. **Uygulama açılmıyor**: Python ve gerekli kütüphanelerin yüklü olduğundan emin olun
2. **Resim kaydedilemiyor**: Klasör yazma izinlerini kontrol edin
3. **Araçlar çalışmıyor**: Fare olaylarının doğru bağlandığından emin olun

### Hata Mesajları
- Hata mesajlarını okuyun ve anlamaya çalışın
- Python konsolunda hata detaylarını kontrol edin
- Gerekli kütüphanelerin yüklü olduğundan emin olun

## 📚 İleri Seviye

### Geliştirme Önerileri
- [ ] Yeni çizim araçları ekleme
- [ ] Katman sistemi
- [ ] Filtreler ve efektler
- [ ] Çoklu tuval desteği
- [ ] Kısayol tuşları
- [ ] Ayarlar menüsü

### Kod İnceleme
- `main.py`: Ana uygulama mantığı
- `tools.py`: Araç sınıfları
- `canvas_image.py`: Resim işlemleri
- `about.py`: Yardım ve hakkında pencereleri

## 🤝 Destek

Eğer sorun yaşıyorsanız:
1. README.md dosyasını okuyun
2. Kod yorumlarını inceleyin
3. Python dokümantasyonunu kontrol edin
4. GitHub issues'da sorun bildirin

## 🎯 Sonuç

Bu Paint uygulaması, Python programlama öğrenmek için mükemmel bir başlangıç projesidir. Temel GUI kavramlarını, olay yönetimini ve dosya işlemlerini öğrenirken eğlenceli bir uygulama geliştirmiş olursunuz.

**İyi çalışmalar ve eğlenceli öğrenmeler! 🚀**
