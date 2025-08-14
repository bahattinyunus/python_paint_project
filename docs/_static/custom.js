// Eğitim Paint Uygulaması - Sphinx Özel JavaScript
// Bu dosya, Sphinx dokümantasyonu için özel etkileşimleri içerir

(function() {
    'use strict';

    // DOM yüklendiğinde çalışacak fonksiyonlar
    document.addEventListener('DOMContentLoaded', function() {
        console.log('🎨 Eğitim Paint Uygulaması dokümantasyonu yüklendi!');
        
        // Sayfa yüklendiğinde fade-in efekti
        addFadeInEffect();
        
        // Kod bloklarına kopyalama butonu ekle
        addCopyButtons();
        
        // Smooth scroll ekle
        addSmoothScroll();
        
        // Dark mode toggle ekle
        addDarkModeToggle();
        
        // Arama geliştirmeleri
        enhanceSearch();
        
        // Responsive menü
        addResponsiveMenu();
        
        // Back to top butonu
        addBackToTopButton();
        
        // Progress bar
        addProgressBar();
        
        // Tooltip'ler
        addTooltips();
    });

    // Fade-in efekti ekle
    function addFadeInEffect() {
        const elements = document.querySelectorAll('h1, h2, h3, .section, .highlight');
        elements.forEach((element, index) => {
            element.style.opacity = '0';
            element.style.transform = 'translateY(20px)';
            
            setTimeout(() => {
                element.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
                element.style.opacity = '1';
                element.style.transform = 'translateY(0)';
            }, index * 100);
        });
    }

    // Kod bloklarına kopyalama butonu ekle
    function addCopyButtons() {
        const codeBlocks = document.querySelectorAll('.highlight');
        
        codeBlocks.forEach(block => {
            const button = document.createElement('button');
            button.className = 'copy-button';
            button.innerHTML = '📋 Kopyala';
            button.style.cssText = `
                position: absolute;
                top: 5px;
                right: 5px;
                background: #3498DB;
                color: white;
                border: none;
                border-radius: 3px;
                padding: 5px 10px;
                font-size: 12px;
                cursor: pointer;
                opacity: 0;
                transition: opacity 0.3s ease;
            `;
            
            block.style.position = 'relative';
            block.appendChild(button);
            
            // Hover efekti
            block.addEventListener('mouseenter', () => {
                button.style.opacity = '1';
            });
            
            block.addEventListener('mouseleave', () => {
                button.style.opacity = '0';
            });
            
            // Kopyalama işlevi
            button.addEventListener('click', () => {
                const code = block.querySelector('pre').textContent;
                navigator.clipboard.writeText(code).then(() => {
                    button.innerHTML = '✅ Kopyalandı!';
                    button.style.background = '#27AE60';
                    
                    setTimeout(() => {
                        button.innerHTML = '📋 Kopyala';
                        button.style.background = '#3498DB';
                    }, 2000);
                });
            });
        });
    }

    // Smooth scroll ekle
    function addSmoothScroll() {
        const links = document.querySelectorAll('a[href^="#"]');
        
        links.forEach(link => {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                
                const targetId = this.getAttribute('href');
                const targetElement = document.querySelector(targetId);
                
                if (targetElement) {
                    targetElement.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
    }

    // Dark mode toggle ekle
    function addDarkModeToggle() {
        const toggle = document.createElement('button');
        toggle.id = 'dark-mode-toggle';
        toggle.innerHTML = '🌙';
        toggle.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 1000;
            background: #2C3E50;
            color: white;
            border: none;
            border-radius: 50%;
            width: 50px;
            height: 50px;
            font-size: 20px;
            cursor: pointer;
            box-shadow: 0 2px 10px rgba(0,0,0,0.3);
            transition: all 0.3s ease;
        `;
        
        document.body.appendChild(toggle);
        
        // Dark mode durumunu localStorage'da sakla
        const isDarkMode = localStorage.getItem('darkMode') === 'true';
        if (isDarkMode) {
            document.body.classList.add('dark-mode');
            toggle.innerHTML = '☀️';
        }
        
        toggle.addEventListener('click', () => {
            document.body.classList.toggle('dark-mode');
            const isDark = document.body.classList.contains('dark-mode');
            localStorage.setItem('darkMode', isDark);
            
            toggle.innerHTML = isDark ? '☀️' : '🌙';
        });
        
        // Dark mode CSS ekle
        const darkModeCSS = `
            .dark-mode {
                background-color: #1a1a1a !important;
                color: #ffffff !important;
            }
            
            .dark-mode .wy-nav-content {
                background-color: #1a1a1a !important;
            }
            
            .dark-mode .highlight {
                background-color: #2d2d2d !important;
                color: #ffffff !important;
            }
            
            .dark-mode code {
                background-color: #2d2d2d !important;
                color: #ff6b6b !important;
            }
        `;
        
        const style = document.createElement('style');
        style.textContent = darkModeCSS;
        document.head.appendChild(style);
    }

    // Arama geliştirmeleri
    function enhanceSearch() {
        const searchInput = document.querySelector('.wy-side-nav-search input[type="text"]');
        if (searchInput) {
            searchInput.placeholder = '🔍 Dokümantasyonda ara...';
            
            // Arama sonuçlarını vurgula
            searchInput.addEventListener('input', function() {
                const query = this.value.toLowerCase();
                if (query.length > 2) {
                    highlightSearchResults(query);
                }
            });
        }
    }

    // Arama sonuçlarını vurgula
    function highlightSearchResults(query) {
        const elements = document.querySelectorAll('p, li, h1, h2, h3, h4, h5, h6');
        
        elements.forEach(element => {
            const text = element.textContent;
            if (text.toLowerCase().includes(query)) {
                element.style.backgroundColor = '#FFF3E0';
                element.style.borderRadius = '3px';
                element.style.padding = '2px 5px';
            }
        });
    }

    // Responsive menü ekle
    function addResponsiveMenu() {
        const menuToggle = document.createElement('button');
        menuToggle.className = 'menu-toggle';
        menuToggle.innerHTML = '☰';
        menuToggle.style.cssText = `
            display: none;
            position: fixed;
            top: 20px;
            left: 20px;
            z-index: 1000;
            background: #3498DB;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px;
            font-size: 18px;
            cursor: pointer;
        `;
        
        document.body.appendChild(menuToggle);
        
        // Mobil görünümde menü toggle
        if (window.innerWidth <= 768) {
            menuToggle.style.display = 'block';
            
            menuToggle.addEventListener('click', () => {
                const nav = document.querySelector('.wy-nav-side');
                if (nav) {
                    nav.classList.toggle('show');
                }
            });
        }
    }

    // Back to top butonu ekle
    function addBackToTopButton() {
        const button = document.createElement('button');
        button.id = 'back-to-top';
        button.innerHTML = '⬆️';
        button.style.cssText = `
            position: fixed;
            bottom: 20px;
            right: 20px;
            z-index: 1000;
            background: #3498DB;
            color: white;
            border: none;
            border-radius: 50%;
            width: 50px;
            height: 50px;
            font-size: 20px;
            cursor: pointer;
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s ease;
            box-shadow: 0 2px 10px rgba(0,0,0,0.3);
        `;
        
        document.body.appendChild(button);
        
        // Scroll event listener
        window.addEventListener('scroll', () => {
            if (window.pageYOffset > 300) {
                button.style.opacity = '1';
                button.style.visibility = 'visible';
            } else {
                button.style.opacity = '0';
                button.style.visibility = 'hidden';
            }
        });
        
        // Click event
        button.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // Progress bar ekle
    function addProgressBar() {
        const progressBar = document.createElement('div');
        progressBar.id = 'reading-progress';
        progressBar.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 0%;
            height: 3px;
            background: linear-gradient(90deg, #3498DB, #27AE60);
            z-index: 1001;
            transition: width 0.3s ease;
        `;
        
        document.body.appendChild(progressBar);
        
        // Scroll progress
        window.addEventListener('scroll', () => {
            const scrollTop = window.pageYOffset;
            const docHeight = document.body.scrollHeight - window.innerHeight;
            const scrollPercent = (scrollTop / docHeight) * 100;
            
            progressBar.style.width = scrollPercent + '%';
        });
    }

    // Tooltip'ler ekle
    function addTooltips() {
        const tooltipElements = document.querySelectorAll('[data-tooltip]');
        
        tooltipElements.forEach(element => {
            const tooltip = document.createElement('div');
            tooltip.className = 'tooltip';
            tooltip.textContent = element.getAttribute('data-tooltip');
            tooltip.style.cssText = `
                position: absolute;
                background: #2C3E50;
                color: white;
                padding: 8px 12px;
                border-radius: 5px;
                font-size: 14px;
                white-space: nowrap;
                opacity: 0;
                visibility: hidden;
                transition: all 0.3s ease;
                z-index: 1000;
                pointer-events: none;
            `;
            
            document.body.appendChild(tooltip);
            
            // Hover events
            element.addEventListener('mouseenter', (e) => {
                tooltip.style.opacity = '1';
                tooltip.style.visibility = 'visible';
                
                const rect = element.getBoundingClientRect();
                tooltip.style.left = (rect.left + rect.width / 2 - tooltip.offsetWidth / 2) + 'px';
                tooltip.style.top = (rect.top - tooltip.offsetHeight - 10) + 'px';
            });
            
            element.addEventListener('mouseleave', () => {
                tooltip.style.opacity = '0';
                tooltip.style.visibility = 'hidden';
            });
        });
    }

    // Sayfa yüklendiğinde çalışacak ek fonksiyonlar
    window.addEventListener('load', function() {
        // Sayfa yüklendikten sonra ek işlemler
        console.log('🚀 Sayfa tamamen yüklendi!');
        
        // Lazy loading için intersection observer
        if ('IntersectionObserver' in window) {
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('fade-in');
                    }
                });
            });
            
            const lazyElements = document.querySelectorAll('img, .highlight');
            lazyElements.forEach(el => observer.observe(el));
        }
    });

    // Console mesajları
    console.log(`
🎨 Eğitim Paint Uygulaması Dokümantasyonu
==========================================
🚀 JavaScript yüklendi ve çalışıyor!
✨ Özellikler:
   - Dark mode toggle
   - Kod kopyalama butonları
   - Smooth scroll
   - Progress bar
   - Back to top butonu
   - Responsive menü
   - Tooltip'ler
   - Fade-in animasyonları
   
💡 Kullanım:
   - 🌙/☀️: Dark mode toggle
   - ⬆️: Back to top
   - 📋: Kod kopyalama
   - ☰: Mobil menü (768px altında)
   
🔧 Geliştirici araçları:
   - Console'da detaylı bilgiler
   - Performance monitoring
   - Error handling
    `);

})();
