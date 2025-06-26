import tkinter as tk
from PIL import Image, ImageTk


class CreateCanvasObject:
    def __init__(self, canvas, image_name, xpos, ypos):
        self.canvas = canvas
        self.image_name = image_name
        self.xpos, self.ypos = xpos, ypos

        pil_image = Image.open(image_name)
        self.tk_image = ImageTk.PhotoImage(pil_image)
        self.image_obj = canvas.create_image(xpos, ypos, image=self.tk_image, anchor='nw')

        canvas.tag_bind(self.image_obj, '<Button1-Motion>', self.move)
        canvas.tag_bind(self.image_obj, '<ButtonPress-1>', self.start_move)
        canvas.tag_bind(self.image_obj, '<ButtonRelease-1>', self.release)
        self.move_flag = False

    def start_move(self, event):
        self.move_flag = True
        self.canvas.tag_raise(self.image_obj)
        self.mouse_xpos = event.x
        self.mouse_ypos = event.y

    def move(self, event):
        if self.move_flag:
            new_xpos, new_ypos = event.x, event.y
            dx = new_xpos - self.mouse_xpos
            dy = new_ypos - self.mouse_ypos

            # sınır kontrolü (canvas boyutuna göre)
            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()
            bbox = self.canvas.bbox(self.image_obj)  # (x1, y1, x2, y2)

            if bbox:
                x1, y1, x2, y2 = bbox
                if x1 + dx < 0:
                    dx = -x1
                if y1 + dy < 0:
                    dy = -y1
                if x2 + dx > canvas_width:
                    dx = canvas_width - x2
                if y2 + dy > canvas_height:
                    dy = canvas_height - y2

            self.canvas.move(self.image_obj, dx, dy)

            self.mouse_xpos = new_xpos
            self.mouse_ypos = new_ypos

    def release(self, event):
        self.move_flag = False
