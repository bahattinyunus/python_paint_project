import tkinter as tk
from tkinter import messagebox
from tkinter import Label, Canvas
import webbrowser
from urllib.request import urlopen
from PIL import Image, ImageTk
from io import BytesIO

# === 1. Hakkında (About) Penceresi ===
def show_about(master=None):
    """
    Kullanıcıya uygulama hakkında kısa bilgi verir.
    Bu fonksiyon her yerden çağrılabilir.
    """
    messagebox.showinfo(
        "About Tkinter Paint",
        "This is the newest version of the Paint application using Tkinter.\n"
        "Tkinter Paint v1.00"
    )

# === 2. Yardım Penceresi ===
def show_help(master=None):
    """
    Uygulamanın özelliklerini listeleyen Yardım penceresini açar.
    Bu pencere ayrı bir Tk penceresi yerine Toplevel olarak açılır.
    """
    help_window = tk.Toplevel(master)
    help_window.title('Help - Paint App')
    help_window.geometry("500x500")
    help_window.resizable(False, False)

    canvas = Canvas(help_window, bg='white', width=500, height=500)
    canvas.pack(expand=tk.YES, fill=tk.BOTH)

    help_text = """
    === Paint App Features ===

    ✏️ Tools:
        • Pen  → Custom size & color
        • Brush → Adjustable size & color
        • Shapes → Rectangle, Circle, Oval, Line

    🖼️ Image:
        • Add images to your canvas
        • Open existing images
        • Save your work as an image file
    """

    canvas.create_text(250, 30, anchor=tk.CENTER, font=("Helvetica", 16, "bold"), text="How to Use?")
    canvas.create_text(20, 70, anchor=tk.NW, width=460, font=("Courier", 10), text=help_text)

# === 3. Yazar Bilgi Penceresi ===
def show_author(master=None):
    """
    Uygulamanın geliştiricisine dair bilgileri ve görselini gösterir.
    """
    author_window = tk.Toplevel(master)
    author_window.title('About the Author')
    author_window.geometry("500x500")
    author_window.resizable(False, False)

    canvas = Canvas(author_window, bg='white', width=500, height=500)
    canvas.pack(expand=tk.YES, fill=tk.BOTH)

    # Profil fotoğrafı URL'si
    img_url = "https://pbs.twimg.com/profile_images/1151493893030068225/cBzeDrmJ_400x400.jpg"

    try:
        # Fotoğrafı internetten al ve yeniden boyutlandır
        raw_data = urlopen(img_url).read()
        image = Image.open(BytesIO(raw_data))
        image = image.resize((150, 150), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image, master=author_window)
        canvas.create_image(250, 100, image=photo, anchor=tk.CENTER)
        canvas.image = photo  # Referans tutmazsak Python resmi silebilir
    except Exception as e:
        print(f"Resim yüklenemedi: {e}")

    # Açıklama metni
    description = (
        "This application was built using Tkinter.\n"
        "Tkinter is a Python binding to the Tk GUI toolkit.\n"
        "You can draw shapes, lines, text, and more using canvas."
    )
    canvas.create_text(250, 280, anchor=tk.CENTER, width=460, font=("Arial", 11), text=description)

    # Tıklanabilir GitHub bağlantısı
    def open_github(event=None):
        webbrowser.open_new("https://github.com/swaroopmaddu/")

    github_link = tk.Label(author_window, text="Visit GitHub Profile", fg="blue", cursor="hand2", bg="white", font=("Arial", 10, "underline"))
    github_link.place(x=180, y=450)
    github_link.bind("<Button-1>", open_github)
