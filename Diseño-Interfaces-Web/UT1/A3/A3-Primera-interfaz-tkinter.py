import os
import random
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

dirname = os.path.dirname(__file__)
img_home_dir = dirname + '/hiragana'

# Cargamos todas las imagenes del directorio
filelist=os.listdir(str(img_home_dir))
for files in filelist[:]:
    if not(files.endswith(".png")):
        filelist.remove(files)

# Seleccionamos 10 imgs aleatorias de la carpeta
selected_imgs = []
img_num = 0
while len(selected_imgs) < 10:
    img_name = filelist[random.randrange(len(filelist))]
    if not img_name in selected_imgs:
        selected_imgs.append(img_name)

def open_img():
    global img_num
    if img_num < len(selected_imgs):
        img_url = img_home_dir + "/" + selected_imgs[img_num]
        img = Image.open(str(img_url))
        img = img.resize((400, 400), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        panel = Label(main_frame, image = img)
        panel.image = img
        panel.grid(row = 0, column = 0, sticky = "nsew")
        img_num += 1
        return img_num
    else:
        root.destroy()


# Ventena Principal
root = tk.Tk()
root.title("Hiragama Game")
root.geometry('400x500')
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.resizable(width = True, height = True)

# Frame Padre
main_frame = Frame(root,bg="#007c77")
main_frame.grid(row = 0, column = 0, sticky = "nsew")
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_columnconfigure(0, weight=1)

# Iniciar Juego
def start_game():
    global img_num
    start_btn.destroy()

    user_response = StringVar()
    user_input = tk.Entry(main_frame, textvariable= user_response, font=('Arial 24'), fg="#ff3cc7")
    user_input.configure(background="#4c1a57")
    user_input.grid(row = 1, column = 0, sticky = "nsew")

    next_btn = tk.Button(main_frame, 
                     text="Siguiente",
                     bg="#f0f600",
                     font=('Arial 24'),
                     command=start_game)
    next_btn.grid(row = 2, column = 0, sticky = "nsew")

    open_img()

start_btn = tk.Button(main_frame, 
                     text="Iniciar Juego",
                     bg="#f0f600",
                     font=('Arial 24'),
                     command=start_game)
start_btn.grid(row = 0, column = 0, sticky = "nsew")


root.mainloop()