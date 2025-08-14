@REM Eğitim Paint Uygulaması - Sphinx Makefile (Windows)
@REM Bu dosya, Windows'ta Sphinx dokümantasyon oluşturma için kullanılır

@REM Minimal makefile for Sphinx documentation (Windows)

@REM You can set these variables from the command line.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

@REM Put it first so that "make" without argument is like "make help".
help:
	@echo.
	@echo 🎨 Eğitim Paint Uygulaması - Sphinx Makefile (Windows)
	@echo.
	@echo Kullanılabilir komutlar:
	@echo   help              - Bu yardım mesajını gösterir
	@echo   html              - HTML dokümantasyon oluşturur
	@echo   clean             - Build dosyalarını temizler
	@echo   clean-all         - Tüm dosyaları temizler
	@echo   build-quick       - Hızlı HTML build
	@echo   build-full        - Tam HTML build
	@echo   build-pdf         - PDF dokümantasyon oluşturur
	@echo   build-epub        - EPUB dokümantasyon oluşturur
	@echo   check             - Link ve doctest kontrolü
	@echo   spelling          - Yazım kontrolü
	@echo   serve             - Yerel sunucu başlatır
	@echo   install-deps      - Sphinx bağımlılıklarını yükler
	@echo   dev               - Geliştirme ortamı hazırlar
	@echo   prod              - Production build
	@echo   all               - Tam build ve temizlik
	@echo.
	@echo Örnek kullanım:
	@echo   make html         # HTML dokümantasyon oluştur
	@echo   make serve        # Yerel sunucu başlat
	@echo   make dev          # Geliştirme ortamı
	@echo.
	@echo Varsayılan komutlar:
	@echo   html              - HTML dokümantasyon oluşturur
	@echo   dirhtml           - Directory-style HTML dokümantasyon oluşturur
	@echo   singlehtml        - Tek HTML dosyası oluşturur
	@echo   pickle            - Pickle dosyası oluşturur
	@echo   json              - JSON dosyası oluşturur
	@echo   htmlhelp          - HTML Help dosyası oluşturur
	@echo   qthelp            - Qt Help dosyası oluşturur
	@echo   devhelp           - Devhelp dosyası oluşturur
	@echo   epub              - EPUB dosyası oluşturur
	@echo   latex             - LaTeX dosyası oluşturur
	@echo   text              - Text dosyası oluşturur
	@echo   man               - Manual page oluşturur
	@echo   texinfo           - Texinfo dosyası oluşturur
	@echo   gettext           - Gettext message catalog oluşturur
	@echo   changes           - Changelog oluşturur
	@echo   linkcheck         - Link kontrolü yapar
	@echo   doctest           - Doctest çalıştırır
	@echo   coverage          - Coverage report oluşturur
	@echo   xml               - XML dosyası oluşturur
	@echo   pseudoxml         - Pseudo-XML dosyası oluşturur
	@echo.
	@echo Detaylı yardım için:
	@echo   sphinx-build -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS%
	@echo.
	@REM Catch-all target: route all unknown targets to Sphinx using the new
	@REM "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
	@if "%1" == "" goto :html
	@%SPHINXBUILD% -M %1 "%SOURCEDIR%" "%BUILDDIR%" %SPHINXOPTS% %O%
	@goto :end
	:html
	@%SPHINXBUILD% -M html "%SOURCEDIR%" "%BUILDDIR%" %SPHINXOPTS% %O%
	:end

@REM Özel hedefler
clean-all:
	@echo 🧹 Tüm dosyalar temizleniyor...
	@if exist "%BUILDDIR%" rmdir /s /q "%BUILDDIR%"
	@if exist "*.log" del /q "*.log"
	@if exist "*.tmp" del /q "*.tmp"
	@echo ✅ Temizlik tamamlandı!

serve:
	@echo 🌐 Dokümantasyon sunucusu başlatılıyor...
	@echo 📖 Tarayıcıda http://localhost:8000 adresini açın
	@echo 🛑 Durdurmak için Ctrl+C tuşlayın
	@if exist "%BUILDDIR%\html" (
		cd "%BUILDDIR%\html" && python -m http.server 8000
	) else (
		@echo ❌ HTML dokümantasyon bulunamadı! Önce 'make html' çalıştırın.
	)

install-deps:
	@echo 📦 Sphinx bağımlılıkları yükleniyor...
	pip install sphinx sphinx-rtd-theme myst-parser
	@echo ✅ Bağımlılıklar yüklendi!

build-quick:
	@echo 🚀 Hızlı dokümantasyon oluşturuluyor...
	%SPHINXBUILD% -b html "%SOURCEDIR%" "%BUILDDIR%\html" %SPHINXOPTS%

build-full:
	@echo 🔨 Tam dokümantasyon oluşturuluyor...
	%SPHINXBUILD% -b html "%SOURCEDIR%" "%BUILDDIR%\html" %SPHINXOPTS% -W --keep-going

build-pdf:
	@echo 📄 PDF dokümantasyon oluşturuluyor...
	%SPHINXBUILD% -b latex "%SOURCEDIR%" "%BUILDDIR%\latex" %SPHINXOPTS%
	@echo 📚 PDF oluşturuluyor...
	@if exist "%BUILDDIR%\latex" (
		cd "%BUILDDIR%\latex" && make all-pdf
	) else (
		@echo ❌ LaTeX build bulunamadı!
	)

build-epub:
	@echo 📱 EPUB dokümantasyon oluşturuluyor...
	%SPHINXBUILD% -b epub "%SOURCEDIR%" "%BUILDDIR%\epub" %SPHINXOPTS%

check:
	@echo 🔍 Dokümantasyon kontrol ediliyor...
	%SPHINXBUILD% -b linkcheck "%SOURCEDIR%" "%BUILDDIR%\linkcheck" %SPHINXOPTS%
	%SPHINXBUILD% -b doctest "%SOURCEDIR%" "%BUILDDIR%\doctest" %SPHINXOPTS%

spelling:
	@echo 📝 Yazım kontrolü yapılıyor...
	%SPHINXBUILD% -b spelling "%SOURCEDIR%" "%BUILDDIR%\spelling" %SPHINXOPTS%

@REM Varsayılan hedef
all: clean-all build-full
	@echo ✅ Dokümantasyon başarıyla oluşturuldu!
	@echo 📁 Çıktı: %BUILDDIR%\html\index.html

@REM Geliştirici hedefleri
dev: install-deps build-quick serve

@REM Production hedefleri
prod: clean-all build-full check
	@echo 🚀 Production dokümantasyon hazır!

@REM Yardım
help-extended:
	@call :help

@REM Catch-all target: route all unknown targets to Sphinx using the new
@REM "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@%SPHINXBUILD% -M $@ "%SOURCEDIR%" "%BUILDDIR%" %SPHINXOPTS% %O%
