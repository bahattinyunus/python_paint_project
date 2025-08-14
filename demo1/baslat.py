#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🎨 Eğitim Paint Uygulaması - Başlatma Scripti

Bu script, Paint uygulamasını başlatır ve gerekli kontrolleri yapar.
Python programlama öğrenmek isteyenler için hazırlanmıştır.

Kullanım:
    python baslat.py

Gereksinimler:
    - Python 3.6+
    - Tkinter (genellikle Python ile birlikte gelir)
    - PIL/Pillow
    - pyglet
"""

import sys
import os
import subprocess
import importlib.util

def check_python_version():
    """Python sürümünü kontrol eder"""
    if sys.version_info < (3, 6):
        print("❌ Hata: Python 3.6 veya üstü gerekli!")
        print(f"   Mevcut sürüm: {sys.version}")
        return False
    print(f"✅ Python sürümü: {sys.version.split()[0]}")
    return True

def check_module(module_name, package_name=None):
    """Belirtilen modülün yüklü olup olmadığını kontrol eder"""
    if package_name is None:
        package_name = module_name
    
    try:
        importlib.import_module(module_name)
        print(f"✅ {package_name} yüklü")
        return True
    except ImportError:
        print(f"❌ {package_name} yüklü değil!")
        return False

def install_requirements():
    """Gerekli kütüphaneleri yükler"""
    print("\n📦 Gerekli kütüphaneler yükleniyor...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Kütüphaneler başarıyla yüklendi!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Kütüphane yükleme hatası!")
        return False

def main():
    """Ana fonksiyon"""
    print("🎨 Eğitim Paint Uygulaması - Başlatma Kontrolü")
    print("=" * 50)
    
    # Python sürüm kontrolü
    if not check_python_version():
        return
    
    print("\n🔍 Gerekli kütüphaneler kontrol ediliyor...")
    
    # Gerekli kütüphaneleri kontrol et
    required_modules = [
        ("tkinter", "Tkinter"),
        ("PIL", "Pillow (PIL)"),
        ("pyglet", "Pyglet")
    ]
    
    missing_modules = []
    for module, name in required_modules:
        if not check_module(module, name):
            missing_modules.append(name)
    
    # Eksik kütüphaneler varsa yükle
    if missing_modules:
        print(f"\n⚠️  Eksik kütüphaneler: {', '.join(missing_modules)}")
        print("📦 requirements.txt dosyasından yükleniyor...")
        
        if os.path.exists("requirements.txt"):
            if install_requirements():
                print("\n🔍 Kütüphaneler tekrar kontrol ediliyor...")
                for module, name in required_modules:
                    check_module(module, name)
            else:
                print("❌ Kütüphane yükleme başarısız!")
                print("💡 Manuel olarak yüklemeyi deneyin:")
                print("   pip install -r requirements.txt")
                return
        else:
            print("❌ requirements.txt dosyası bulunamadı!")
            return
    
    print("\n✅ Tüm gerekli kütüphaneler mevcut!")
    
    # Uygulamayı başlat
    print("\n🚀 Paint uygulaması başlatılıyor...")
    try:
        import main
        print("✅ Uygulama başarıyla başlatıldı!")
    except Exception as e:
        print(f"❌ Uygulama başlatma hatası: {e}")
        print("💡 Manuel olarak başlatmayı deneyin:")
        print("   python main.py")

if __name__ == "__main__":
    main()
