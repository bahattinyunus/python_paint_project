# Eğitim Paint Uygulaması - Makefile
# Bu dosya, proje yönetimi için çeşitli komutlar sağlar

.PHONY: help install install-dev test lint format clean build dist run docs

# Varsayılan hedef
help:
	@echo "🎨 Eğitim Paint Uygulaması - Makefile"
	@echo ""
	@echo "Kullanılabilir komutlar:"
	@echo "  install      - Temel bağımlılıkları yükler"
	@echo "  install-dev  - Geliştirme bağımlılıklarını yükler"
	@echo "  test         - Testleri çalıştırır"
	@echo "  lint         - Kod kalitesi kontrolü yapar"
	@echo "  format       - Kodu otomatik olarak formatlar"
	@echo "  clean        - Geçici dosyaları temizler"
	@echo "  build        - Projeyi derler"
	@echo "  dist         - Dağıtım paketi oluşturur"
	@echo "  run          - Uygulamayı çalıştırır"
	@echo "  docs         - Dokümantasyon oluşturur"
	@echo "  help         - Bu yardım mesajını gösterir"

# Temel bağımlılıkları yükle
install:
	@echo "📦 Temel bağımlılıklar yükleniyor..."
	pip install -r demo1/requirements.txt

# Geliştirme bağımlılıklarını yükle
install-dev:
	@echo "🔧 Geliştirme bağımlılıkları yükleniyor..."
	pip install -r demo1/requirements.txt
	pip install black flake8 pytest pytest-cov pre-commit

# Testleri çalıştır
test:
	@echo "🧪 Testler çalıştırılıyor..."
	python -m pytest tests/ -v --cov=demo1 --cov-report=html

# Kod kalitesi kontrolü
lint:
	@echo "🔍 Kod kalitesi kontrol ediliyor..."
	flake8 demo1/ --max-line-length=88 --extend-ignore=E203,W503
	@echo "✅ Lint kontrolü tamamlandı!"

# Kodu formatla
format:
	@echo "🎨 Kod formatlanıyor..."
	black demo1/ --line-length=88
	@echo "✅ Kod formatlandı!"

# Geçici dosyaları temizle
clean:
	@echo "🧹 Geçici dosyalar temizleniyor..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name "build" -exec rm -rf {} +
	find . -type d -name "dist" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name "htmlcov" -exec rm -rf {} +
	@echo "✅ Temizlik tamamlandı!"

# Projeyi derle
build:
	@echo "🔨 Proje derleniyor..."
	python setup.py build

# Dağıtım paketi oluştur
dist: clean
	@echo "📦 Dağıtım paketi oluşturuluyor..."
	python setup.py sdist bdist_wheel

# Uygulamayı çalıştır
run:
	@echo "🚀 Uygulama başlatılıyor..."
	cd demo1 && python main.py

# Dokümantasyon oluştur
docs:
	@echo "📚 Dokümantasyon oluşturuluyor..."
	cd docs && make html

# Sanal ortam oluştur
venv:
	@echo "🐍 Sanal ortam oluşturuluyor..."
	python -m venv .venv
	@echo "✅ Sanal ortam oluşturuldu!"
	@echo "💡 Aktifleştirmek için:"
	@echo "   Windows: .venv\\Scripts\\activate"
	@echo "   Unix/Mac: source .venv/bin/activate"

# Sanal ortamı aktifleştir (Windows)
activate-win:
	@echo "🐍 Windows sanal ortamı aktifleştiriliyor..."
	.venv\Scripts\activate

# Sanal ortamı aktifleştir (Unix/Mac)
activate-unix:
	@echo "🐍 Unix/Mac sanal ortamı aktifleştiriliyor..."
	source .venv/bin/activate

# Git hooks kur
hooks:
	@echo "🔗 Git hooks kuruluyor..."
	pre-commit install

# Geliştirme ortamını hazırla
dev-setup: install-dev hooks
	@echo "🚀 Geliştirme ortamı hazırlandı!"

# Hızlı başlangıç
quick-start: install run
	@echo "🎉 Hızlı başlangıç tamamlandı!"

# Windows için özel komutlar
windows:
	@echo "🪟 Windows için özel komutlar:"
	@echo "  make activate-win  - Sanal ortamı aktifleştir"
	@echo "  make run           - Uygulamayı çalıştır"

# Unix/Mac için özel komutlar
unix:
	@echo "🐧 Unix/Mac için özel komutlar:"
	@echo "  make activate-unix - Sanal ortamı aktifleştir"
	@echo "  make run           - Uygulamayı çalıştır"

# Proje durumunu kontrol et
status:
	@echo "📊 Proje durumu:"
	@echo "  Python sürümü: $(shell python --version)"
	@echo "  Pip sürümü: $(shell pip --version)"
	@echo "  Kurulu paketler:"
	@pip list --format=columns

# Bağımlılıkları güncelle
update-deps:
	@echo "🔄 Bağımlılıklar güncelleniyor..."
	pip install --upgrade -r demo1/requirements.txt
	@echo "✅ Bağımlılıklar güncellendi!"

# Güvenlik kontrolü
security-check:
	@echo "🔒 Güvenlik kontrolü yapılıyor..."
	pip-audit
	@echo "✅ Güvenlik kontrolü tamamlandı!"
