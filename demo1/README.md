# 🎨 Paint Tkinter

Python 3 ve Tkinter ile hazırlanmış basit ama güçlü bir Paint uygulaması. Hem eğlenceli hem öğretici. Kendi dijital tuvalinde özgürce çiz!

## 🚀 Özellikler

### 🛠️ Araçlar
- **Kalem (Pen)**  
  - Renk ve kalınlık seçilebilir  
- **Fırça (Brush)**  
  - Renk ve kalınlık ayarlanabilir  
- **Silgi (Eraser)**  
  - Çizimleri kolayca sil  
- **Şekiller (Shapes)**  
  - Dörtgen  
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

<p align="center">
  <img src="ss.png" height="400" width="712" />
</p>

---

## 🧰 Gereksinimler

```bash
pip install -r requirements.txt




# Reposu klonlanır
git clone https://github.com/swaroopmaddu/Paint-Tkinter.git

# Klasöre girilir
cd Paint-Tkinter/

# (İsteğe bağlı) sanal ortam oluştur
python -m venv venv
# Ortamı aktifleştir
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Gereken modüller yüklenir
pip install -r requirements.txt

# Uygulama çalıştırılır
python main.py
