#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Eğitim Paint Uygulaması - Setup Dosyası
Türkçe arayüzlü, eğitim odaklı Paint uygulaması
"""

from setuptools import setup, find_packages
import os

# README dosyasını oku
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Requirements dosyasını oku
def read_requirements():
    with open("demo1/requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="egitim-paint-uygulamasi",
    version="1.0.0",
    author="Bahattin Yunus Çetin",
    author_email="",  # E-posta adresinizi buraya ekleyin
    description="Türkçe arayüzlü, eğitim odaklı Paint uygulaması",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/bahattinyunuscetin/python_paint_project",
    project_urls={
        "Bug Tracker": "https://github.com/bahattinyunuscetin/python_paint_project/issues",
        "Documentation": "https://github.com/bahattinyunuscetin/python_paint_project/blob/main/demo1/README.md",
        "Source Code": "https://github.com/bahattinyunuscetin/python_paint_project",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "Topic :: Education",
        "Topic :: Multimedia :: Graphics :: Editors",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
        "Natural Language :: Turkish",
        "Natural Language :: English",
    ],
    python_requires=">=3.6",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "black>=22.0.0",
            "flake8>=4.0.0",
            "pytest>=6.0.0",
            "pytest-cov>=3.0.0",
        ],
        "docs": [
            "sphinx>=4.0.0",
            "sphinx-rtd-theme>=1.0.0",
            "myst-parser>=0.17.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "egitim-paint=demo1.main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "demo1": ["*.png", "*.md", "*.txt"],
    },
    keywords=[
        "paint",
        "drawing",
        "graphics",
        "tkinter",
        "gui",
        "education",
        "turkish",
        "python",
        "canvas",
        "art",
    ],
    platforms=["Windows", "macOS", "Linux"],
    license="MIT",
    zip_safe=False,
)
