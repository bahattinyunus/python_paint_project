

# 🖌️ Python Paint Project

![Python Paint](https://img.shields.io/badge/Python-Paint-blue?style=for-the-badge\&logo=python)

## 📌 Proje Hakkında

Bu proje, Python kullanılarak yapılmış **basit bir Paint uygulamasıdır**. Eğitim amaçlı hazırlanmıştır ve özellikle **Python GUI (Tkinter)** konusunda deneyim kazanmak isteyenler için uygundur. Kullanıcı, uygulama üzerinde çizim yapabilir, renk seçebilir, fırça boyutunu değiştirebilir ve çizimlerini kaydedebilir.

Bu proje sayesinde öğrenebileceğiniz konular:

* Python ile GUI geliştirme
* Tkinter kütüphanesinin temel widget’ları
* Mouse ve klavye olaylarını yakalama
* Basit renk seçici ve fırça mekanizması oluşturma
* Canvas üzerinde çizim yapma

---

## 🛠️ Kullanılan Teknolojiler

* **Python 3.x**
* **Tkinter** (GUI için)
* **Pillow (PIL)** – Kaydetme ve resim işleme için

---

## 📥 Kurulum

### 1. Python Kurulumu

Python bilgisayarınızda yüklü değilse [Python resmi sitesinden](https://www.python.org/downloads/) en son sürümü indirip kurabilirsiniz.

### 2. Gerekli Kütüphaneleri Yükleme

Terminal veya komut istemcisine şu komutları yazın:

```bash
pip install pillow
```

Tkinter genellikle Python ile birlikte gelir. Eğer gelmediyse:

* Windows: Python yükleyici ile “Tkinter” seçeneğini işaretleyin
* Linux: `sudo apt-get install python3-tk`

---

## 🚀 Başlatma

Projeyi indirdikten sonra terminal veya IDE üzerinden şu şekilde çalıştırabilirsiniz:

```bash
python paint.py
```

Uygulama açıldığında bir pencere göreceksiniz. Artık çizim yapabilirsiniz!

---

## 🖍️ Özellikler

### 1. Çizim Yapma

* Sol fare tuşuna basılı tutarak çizim yapabilirsiniz.
* Fırça boyutu varsayılan olarak 5’tir ama ayarlanabilir.

### 2. Renk Seçme

* Renk paleti sayesinde fırçanın rengini değiştirebilirsiniz.
* Örnek renkler: kırmızı, mavi, yeşil, sarı, siyah.

### 3. Fırça Boyutu

* Küçük, orta ve büyük fırça seçenekleri ile çizimlerinizi özelleştirebilirsiniz.

### 4. Temizleme

* Canvas’ı tamamen temizlemek için “Clear” butonuna basabilirsiniz.

### 5. Kaydetme

* Çizimlerinizi `.png` formatında kaydedebilirsiniz.
* Pillow kütüphanesi sayesinde canvas içeriğini görüntü dosyası olarak saklar.

---

## 📚 Kod Yapısı ve Açıklamalar

Projede temel olarak **Tkinter Canvas** kullanılır. İşte kısa açıklama:

```python
import tkinter as tk
from tkinter import colorchooser
from PIL import ImageGrab
```

* **Canvas**: Çizim alanı sağlar.
* **Mouse events**: `<B1-Motion>` olayı ile kullanıcı fareyi hareket ettirirken çizim yapılır.
* **colorchooser.askcolor()**: Kullanıcıya renk seçme penceresi sunar.
* **ImageGrab**: Canvas’ı resim olarak kaydetmek için kullanılır.

Örnek çizim fonksiyonu:

```python
def paint(event):
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    canvas.create_oval(x1, y1, x2, y2, fill=current_color, outline=current_color)
```

* `event.x` ve `event.y` fare pozisyonunu verir.
* `create_oval` ile küçük daireler çizilir, bu da fırça efekti oluşturur.

---

## 💡 Eğitim Notları

* **Tkinter Widget’ları**: `Button`, `Canvas`, `Label`, `Scale`
* **Event Binding**: `canvas.bind("<B1-Motion>", paint)`
* **Global değişken kullanımı**: Fırça rengi ve boyut gibi değişkenleri global tutmak işleri kolaylaştırır.
* **Pillow ile kaydetme**: Tkinter canvas’ı direkt kaydedemez, ImageGrab ile ekran görüntüsü alınır.

Bu proje, **temel GUI ve event-driven programlama** kavramlarını pekiştirmek için mükemmeldir.

---

## 📌 Geliştirme Önerileri

* Farklı fırça şekilleri ekleyin (çizgi, kare, üçgen)
* Arka plan resimleri ekleyin
* Katman (layer) sistemi oluşturun
* Undo/Redo fonksiyonu ekleyin
* Daha fazla renk paleti ve özel renk seçici

---

## 📝 Lisans

Bu proje eğitim amaçlıdır. İstediğiniz gibi kullanabilir, geliştirebilir ve paylaşabilirsiniz.

