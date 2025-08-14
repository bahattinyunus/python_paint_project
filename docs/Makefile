# Eğitim Paint Uygulaması - Sphinx Makefile
# Bu dosya, Sphinx dokümantasyon oluşturma için kullanılır

# Minimal makefile for Sphinx documentation

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Özel hedefler
clean-all:
	rm -rf $(BUILDDIR)
	rm -rf *.log
	rm -rf *.tmp

serve:
	@echo "🌐 Dokümantasyon sunucusu başlatılıyor..."
	@echo "📖 Tarayıcıda http://localhost:8000 adresini açın"
	@echo "🛑 Durdurmak için Ctrl+C tuşlayın"
	cd $(BUILDDIR)/html && python -m http.server 8000

install-deps:
	@echo "📦 Sphinx bağımlılıkları yükleniyor..."
	pip install sphinx sphinx-rtd-theme myst-parser

build-quick:
	@echo "🚀 Hızlı dokümantasyon oluşturuluyor..."
	$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS)

build-full:
	@echo "🔨 Tam dokümantasyon oluşturuluyor..."
	$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS) -W --keep-going

build-pdf:
	@echo "📄 PDF dokümantasyon oluşturuluyor..."
	$(SPHINXBUILD) -b latex "$(SOURCEDIR)" "$(BUILDDIR)/latex" $(SPHINXOPTS)
	@echo "📚 PDF oluşturuluyor..."
	cd "$(BUILDDIR)/latex" && make all-pdf

build-epub:
	@echo "📱 EPUB dokümantasyon oluşturuluyor..."
	$(SPHINXBUILD) -b epub "$(SOURCEDIR)" "$(BUILDDIR)/epub" $(SPHINXOPTS)

check:
	@echo "🔍 Dokümantasyon kontrol ediliyor..."
	$(SPHINXBUILD) -b linkcheck "$(SOURCEDIR)" "$(BUILDDIR)/linkcheck" $(SPHINXOPTS)
	$(SPHINXBUILD) -b doctest "$(SOURCEDIR)" "$(BUILDDIR)/doctest" $(SPHINXOPTS)

spelling:
	@echo "📝 Yazım kontrolü yapılıyor..."
	$(SPHINXBUILD) -b spelling "$(SOURCEDIR)" "$(BUILDDIR)/spelling" $(SPHINXOPTS)

# Varsayılan hedef
all: clean-all build-full
	@echo "✅ Dokümantasyon başarıyla oluşturuldu!"
	@echo "📁 Çıktı: $(BUILDDIR)/html/index.html"

# Geliştirici hedefleri
dev: install-deps build-quick serve

# Production hedefleri
prod: clean-all build-full check
	@echo "🚀 Production dokümantasyon hazır!"

# Yardım
help-extended:
	@echo "🎨 Eğitim Paint Uygulaması - Sphinx Makefile"
	@echo ""
	@echo "Kullanılabilir komutlar:"
	@echo "  help              - Bu yardım mesajını gösterir"
	@echo "  html              - HTML dokümantasyon oluşturur"
	@echo "  clean             - Build dosyalarını temizler"
	@echo "  clean-all         - Tüm dosyaları temizler"
	@echo "  build-quick       - Hızlı HTML build"
	@echo "  build-full        - Tam HTML build"
	@echo "  build-pdf         - PDF dokümantasyon oluşturur"
	@echo "  build-epub        - EPUB dokümantasyon oluşturur"
	@echo "  check             - Link ve doctest kontrolü"
	@echo "  spelling          - Yazım kontrolü"
	@echo "  serve             - Yerel sunucu başlatır"
	@echo "  install-deps      - Sphinx bağımlılıklarını yükler"
	@echo "  dev               - Geliştirme ortamı hazırlar"
	@echo "  prod              - Production build"
	@echo "  all               - Tam build ve temizlik"
	@echo ""
	@echo "Örnek kullanım:"
	@echo "  make html         # HTML dokümantasyon oluştur"
	@echo "  make serve        # Yerel sunucu başlat"
	@echo "  make dev          # Geliştirme ortamı"
