#!/usr/bin/python3

import tkinter
import pyglet
from tkinter import *
from tkinter.ttk import *
from tkinter.colorchooser import askcolor
import io
import datetime
import time
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
from tkinter.filedialog import asksaveasfile
from math import sqrt
# defined
from canvas_image import CreateCanvasObject
from tools import Tool
from about import *

pen = Tool('Pen', 'black', 2)
brush = Tool('Brush', 'green', 5)
eraser = Tool('Eraser', 'white', 5)
shapes = Tool('Shape', 'black', 2)

tools = [pen, brush, eraser, shapes]

global selectedindex
selectedindex = 0

lastx, lasty = None, None

topx, topy, botx, boty = 0, 0, 0, 0
global shape_id

global count
global shape
count = 0


def get_mouse_posn(event):
    global topy, topx
    topx, topy = event.x, event.y


def update_selection(event):
    global shape_id
    global topy, topx, botx, boty
    botx, boty = event.x, event.y
    cv.coords(shape_id, topx, topy, botx, boty)


def activate_paint(e):
    global lastx, lasty
    cv.bind('<B1-Motion>', paint)
    lastx, lasty = e.x, e.y
    cv.bind('<ButtonRelease-1>', newshape)


def paint(e):
    global count
    global lastx, lasty
    global shape
    x, y = e.x, e.y
    tag = "shape" + str(count)
    if shape != 7:
        cv.create_line((lastx, lasty, x, y), width=tools[selectedindex].size, fill=tools[selectedindex].color, tags=tag)
    lastx, lasty = x, y


def donothing():
    filewin = Toplevel(window)
    button = Button(filewin, text="Do nothing button")
    button.pack()


def activeTool():
    for i in range(0, 5):
        menubar.entryconfig(4 + i, foreground='black', background='#F0F0F0')
    if selectedindex != 3:
        menubar.entryconfig(selectedindex + 4, foreground='green', background='white')


def usepen():
    global shape
    global selectedindex
    selectedindex = 0
    shape = 4
    eraser.size = 0
    activeTool()
    menubar.entryconfig(9, label=tools[selectedindex].size)
    window.config(cursor="pencil")
    cv.bind('<1>', activate_paint)
    cv.pack(expand=YES, fill=BOTH)


def usebrush():
    global selectedindex
    global shape
    shape = 5
    selectedindex = 1
    eraser.size = 0
    activeTool()
    menubar.entryconfig(9, label=tools[selectedindex].size)
    window.config(cursor="dot")
    cv.bind('<1>', activate_paint)
    cv.pack(expand=YES, fill=BOTH)


def newcolor():
    tools[selectedindex].color = askcolor(color=tools[selectedindex].color)[1]
    # outline_color = tools[selectedindex].color


def erase():
    global shape
    global selectedindex
    shape = 6
    selectedindex = 2
    eraser.size = 2
    try:
        cv.delete(circle)
    except Exception:
        pass
    window.config(cursor="circle")
    activeTool()
    menubar.entryconfig(9, label=tools[selectedindex].size)
    cv.bind('<1>', activate_paint)
    cv.pack(expand=YES, fill=BOTH)
    cv.bind("<Motion>", motion)


def openfilename():
    filename = filedialog.askopenfilename(title='Open')
    return filename


def fopen():
    x = openfilename()
    if x:
        img = Image.open(x)
        cv.image = ImageTk.PhotoImage(img)
        cv.create_image(0, 0, image=cv.image, anchor=NW)
        cv.pack()


def insert_image():
    global shape
    shape = 7
    window.config(cursor='fleur')
    x = openfilename()
    if x:
        CreateCanvasObject(cv, x, 0, 0)


global circle
circle = 0


def motion(event):
    x, y = event.x + 3, event.y + 7
    global circle
    cv.delete(circle)  # to refresh the circle each motion
    radius = eraser.size  # size of eraser cursor
    x_min = x - radius
    x_max = x + radius
    y_min = y - radius
    y_max = y + radius
    circle = cv.create_oval(x_min, y_min, x_max, y_max, outline="black")


def newshape(event):
    global count
    count += 1
    global shape
    if shape == 0:
        drawLine()
    elif shape == 1:
        drawrect()
    elif shape == 2:
        drawcircle()
    elif shape == 3:
        drawoval()
    elif shape == 4:
        usepen()
    elif shape == 5:
        usebrush()
    elif shape == 6:
        erase()
    elif shape == 7:
        insert_image()


def drawrect():
    global count
    global shape
    global topx, topy, botx, boty
    global shape_id
    global selectedindex
    selectedindex = 3
    activeTool()
    topx, topy, botx, boty = 0, 0, 0, 0
    window.config(cursor="crosshair")
    shape = 1
    tag = "shape" + str(count)
    cv.bind('<Button-1>', get_mouse_posn)
    shape_id = cv.create_rectangle(topx, topy, topx, topy, width=tools[selectedindex].size, fill='', outline='black', tags=tag)
    cv.bind('<B1-Motion>', update_selection)
    cv.bind('<ButtonRelease-1>', newshape)


def drawcircle():
    global shape
    global topx, topy, botx, boty
    global shape_id
    global count
    global selectedindex
    selectedindex = 3
    activeTool()
    menubar.entryconfig(9, label=tools[selectedindex].size)
    shape = 2
    tag = "shape" + str(count)
    topx, topy, botx, boty = 0, 0, 0, 0
    window.config(cursor="crosshair")
    shape_id = cv.create_oval(topx, topy, botx, boty, width=tools[selectedindex].size,
                              fill='', outline='black', tags=tag)
    cv.bind('<Button-1>', get_mouse_posn)
    cv.bind('<B1-Motion>', update_selection)
    cv.bind('<ButtonRelease-1>', newshape)


def drawoval():
    global shape
    global topx, topy, botx, boty
    global shape_id
    global count
    global selectedindex
    selectedindex = 3
    activeTool()
    menubar.entryconfig(9, label=tools[selectedindex].size)
    shape = 3
    tag = "shape" + str(count)
    topx, topy, botx, boty = 0, 0, 0, 0
    window.config(cursor="crosshair")
    shape_id = cv.create_oval(topx, topy, botx, boty, width=tools[selectedindex].size, fill='', outline='black', tags=tag)
    cv.bind('<Button-1>', get_mouse_posn)
    cv.bind('<B1-Motion>', update_selection)
    cv.bind('<ButtonRelease-1>', newshape)


def drawLine():
    global shape
    global topx, topy, botx, boty
    global shape_id
    global count
    global selectedindex
    selectedindex = 3
    activeTool()
    menubar.entryconfig(9, label=tools[selectedindex].size)
    window.config(cursor="crosshair")
    shape = 0
    tag = "shape" + str(count)
    topx, topy, botx, boty = 0, 0, 0, 0
    shape_id = cv.create_line(topx, topy, botx, boty, width=tools[selectedindex].size, fill=tools[selectedindex].color, tags=tag)
    cv.bind('<Button-1>', get_mouse_posn)
    cv.bind('<B1-Motion>', update_selection)
    cv.bind('<ButtonRelease-1>', newshape)


def reset():
    cv.delete("all")


def increase():
    if tools[selectedindex].size < 50:
        tools[selectedindex].size += 1
    menubar.entryconfig(9, label=tools[selectedindex].size)


def decrease():
    if tools[selectedindex].size > 1:
        tools[selectedindex].size -= 1
    menubar.entryconfig(9, label=tools[selectedindex].size)


def getImage():
    ps = cv.postscript(colormode='color')
    img = Image.open(io.BytesIO(ps.encode('utf-8')))
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H%M%S')
    filename = 'Canvas' + st + '.jpg'
    img.save(filename, 'jpeg')
    messagebox.showinfo("Successfull", "Image saved as " + filename)


def file_saveas():
    ps = cv.postscript(colormode='color')
    img = Image.open(io.BytesIO(ps.encode('utf-8')))
    files = [('JPG FIle', '*.jpg*')]
    f = asksaveasfile(mode='w', defaultextension=".jpg", filetypes=files)
    if f is None:
        return
    img.save(f, 'jpeg')
    messagebox.showinfo("Successfull", "Image saved as " + str(f))


def undo():
    global count
    if count > 0:
        count -= 1
        cv.delete("shape" + str(count))


def exit_function():
    if messagebox.askyesno("Close the window", "Do you want to close the window ?", icon='warning'):
        window.destroy()


window = tkinter.Tk()
window.title("Paint Board")
photo = PhotoImage(file="icon.png")
window.iconphoto(False, photo)
h = window.winfo_screenheight()
w = window.winfo_screenwidth()
window.geometry(str(w) + 'x' + str(h))


menubar = Menu(window, activeborderwidth=2, activebackground='white', activeforeground='green', bg='#F0F0F0', relief=RAISED)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=reset)
filemenu.add_command(label="Open", command=fopen)
filemenu.add_command(label="Save", command=getImage)
filemenu.add_command(label="Save as", command=file_saveas)
filemenu.add_command(label="Close", command=reset)
filemenu.add_command(label="Exit", command=exit_function)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=undo)
editmenu.add_command(label="Delete All", command=reset)
menubar.add_cascade(label="Edit", menu=editmenu)

insertmenu = Menu(menubar, tearoff=0)
insertmenu.add_command(label='Add Image', command=insert_image)
insertmenu.add_command(label='Line', command=drawLine)
insertmenu.add_command(label='Rectangle', command=drawrect)
insertmenu.add_command(label='Circle', command=drawcircle)
insertmenu.add_command(label='Oval', command=drawoval)
menubar.add_cascade(label='Insert', menu=insertmenu)

menubar.add_command(label="Pen", command=usepen)
menubar.add_command(label="Brush", command=usebrush)
menubar.add_command(label="Eraser", command=erase)
menubar.add_command(label="Color", command=newcolor)

menubar.add_command(label="-", command=decrease)
menubar.add_command(label=tools[selectedindex].size, state=DISABLED)
menubar.add_command(label="+", command=increase)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=help)
helpmenu.add_command(label="Author", command=author)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

cv = Canvas(window, bg='white', width=300, height=300)
cv.pack(expand=YES, fill=BOTH)

window.config(menu=menubar)
window.mainloop()
