import random
import tkinter as tk
from tkinter import *
from tkinter import ttk, font as tkFont
from tkinter import messagebox
from PIL import ImageTk, Image

def close_app(event):
    root.quit()

def clear_canva(width, height):
    main_canva.delete("all")
    root.geometry(str(width) + "x" + str(height) + "+500+100")
    main_canva.configure(width= width, height= height)

def load_image(url, width, height):
    img = Image.open(url)
    img_resized = img.resize((width, height))
    converted_img = ImageTk.PhotoImage(img_resized)
    return converted_img

def new_circle(x, y, radio, color="#E0E0E0"):
    main_canva.create_oval(
        x - radio, y - radio, 
        x + radio, y + radio, 
        outline="black", fill=color, width=2
    )
    
def val_second_game_num_entry(value):
    if not value.isdigit() or not (1 <= int(value) <= 200):
        show_error("Entrada inválida", "Por favor, introduce\nun número entre 1 y 200.")
        num_entry.focus_set()
        return
    second_game_logic(int(value))

def show_error(title, text):
    error_box = tk.Toplevel()
    error_box.title(title)
    error_box.geometry("400x200")
    error_box.configure(bg="#1E1E2F")

    message_label = tk.Label(error_box, text=text, font=text_font, fg=btn_text_color, bg="#33334D", justify="center")
    message_label.pack(pady=20)

    ok_btn = ttk.Button(error_box, text="OK", command=error_box.destroy)
    ok_btn.pack(pady=10)

    error_box.transient(root)
    error_box.grab_set()
    root.wait_window(error_box)


def first_game_screen():
    # Limpiamos el canva y lo redimensionamos
    clear_canva(800, 400)

    # Boton volver al menu principal y cerrar juego
    main_menu_bg = main_canva.create_rectangle(0, 350, 400, 400, fill="#33334D", outline="")
    main_menu_text = main_canva.create_text(200, 375, text="🏠 Menu Principal", fill=btn_text_color, font=btn_text_font)
    exit_bg = main_canva.create_rectangle(400, 350, 800, 400, fill="#33334D", outline="")
    exit_text = main_canva.create_text(600, 375, text="❌ Cerrar Juego", fill=btn_text_color, font=btn_text_font)
    main_canva.tag_bind(main_menu_bg, "<Button-1>", lambda e: main_menu())
    main_canva.tag_bind(main_menu_text, "<Button-1>", lambda e: main_menu())
    main_canva.tag_bind(exit_bg, "<Button-1>", close_app)
    main_canva.tag_bind(exit_text, "<Button-1>", close_app)

    # Imagenes Piedra, Papel o Tijeras
    global stone_img_l, scisors_img_l, paper_img_l
    stone_img_l = load_image("stone.png",150,150)
    stone_img = main_canva.create_image(80,125,anchor=NW,image=stone_img_l)
    scisors_img_l = load_image("scisors.png",150,150)
    scisors_img = main_canva.create_image(320,125,anchor=NW,image=scisors_img_l)
    paper_img_l = load_image("paper.png",150,150)
    paper_img = main_canva.create_image(570,125,anchor=NW,image=paper_img_l)

    main_canva.tag_bind(stone_img, "<Button-1>", lambda e: first_game_logic("piedra"))
    main_canva.tag_bind(paper_img, "<Button-1>", lambda e: first_game_logic("papel"))
    main_canva.tag_bind(scisors_img, "<Button-1>", lambda e: first_game_logic("tijeras"))

    # Titulo
    main_canva.create_text(400, 50, text="¿Que eliges?", fill=title_color, font=title_font)

def first_game_logic(player_option):
    options = ["piedra", "papel", "tijeras"]
    robot_option = random.choice(options)

    if player_option == "piedra" and robot_option == "tijeras":
        first_game_final_screem("Has Ganado!", player_option, robot_option)
        return
    if player_option == "tijeras" and robot_option == "papel":
        first_game_final_screem("Has Ganado!", player_option, robot_option)
        return
    if player_option == "papel" and robot_option == "piedra":
        first_game_final_screem("Has Ganado!", player_option, robot_option)
        return
    if player_option == robot_option:
        first_game_final_screem("Has Empatado!", player_option, robot_option)
        return
    first_game_final_screem("Has Perdido!", player_option, robot_option)

def first_game_final_screem(title, player_option, robot_option):
    options_img = {
        "piedra" : stone_img_l, 
        "papel" : paper_img_l, 
        "tijeras" : scisors_img_l
    }

    main_canva.delete("all")

    main_canva.create_text(400, 50, text=title, fill=title_color, font=title_font)

    main_canva.create_text(200, 125, text="Tu sacaste", fill=btn_text_color, font=btn_text_font)
    main_canva.create_image(125,150,anchor=NW,image=options_img[player_option])

    main_canva.create_text(600, 125, text="La maquina saco", fill=btn_text_color, font=btn_text_font)
    main_canva.create_image(525,150,anchor=NW,image=options_img[robot_option])

    main_menu_bg = main_canva.create_rectangle(0, 350, 250, 400, fill="#33334D", outline="")
    main_menu_text = main_canva.create_text(125, 375, text="🏠 Menú Principal", fill=btn_text_color, font=small_btn_text_font)
    regame_bg = main_canva.create_rectangle(275, 350, 525, 400, fill="#33334D", outline="")
    regame_text = main_canva.create_text(400, 375, text="⟳ Volver a Jugar", fill=btn_text_color, font=small_btn_text_font)
    exit_bg = main_canva.create_rectangle(550, 350, 800, 400, fill="#33334D", outline="")
    exit_text = main_canva.create_text(675, 375, text="❌ Cerrar Juego", fill=btn_text_color, font=small_btn_text_font)
    main_canva.tag_bind(main_menu_bg, "<Button-1>", lambda e: main_menu())
    main_canva.tag_bind(main_menu_text, "<Button-1>", lambda e: main_menu())
    main_canva.tag_bind(regame_bg, "<Button-1>", lambda e: first_game_screen())
    main_canva.tag_bind(regame_text, "<Button-1>", lambda e: first_game_screen())
    main_canva.tag_bind(exit_bg, "<Button-1>", close_app)
    main_canva.tag_bind(exit_text, "<Button-1>", close_app)

def second_game_screen():
    global interrogant_img_l, games_trys, num_entry_var, num_entry, first_num, second_num, third_num, second_game_text, secret_num

    # Limpiamos el canva y lo redimensionamos
    clear_canva(1000, 700)

    games_trys = 0
    secret_num = random.randint(1, 200)

    main_canva.create_text(500, 50, text="Adivina el Número Oculto", fill=title_color, font=title_font)

    new_circle(500,175,75)

    second_game_text = main_canva.create_text(500, 300, text="Introduce un número para empezar", fill=btn_text_color, font=text_font)

    interrogant_img_l = load_image("interrogant.png",75,75)
    interrogant_img = main_canva.create_image(460,135,anchor=NW,image=interrogant_img_l)

    new_circle(225,450,75, "#33334D")
    first_num = main_canva.create_text(225, 450, text="--", fill=btn_text_color, font=title_font)

    new_circle(500,450,75, "#33334D")
    second_num = main_canva.create_text(500, 450, text="--", fill=btn_text_color, font=title_font)

    new_circle(775,450,75, "#33334D")
    third_num = main_canva.create_text(775, 450, text="--", fill=btn_text_color, font=title_font)

    main_canva.create_text(400, 600, text="Introduce un número", fill=btn_text_color, font=text_font)

    num_entry_var = tk.StringVar()
    num_entry = tk.Entry(root, textvariable=num_entry_var, font=text_font, width=10, bg="#33334D", fg=btn_text_color, justify="center")
    main_canva.create_window(650, 600, anchor="center", window=num_entry)

    num_entry.bind("<Return>", lambda event: val_second_game_num_entry(num_entry_var.get()))

    # Boton volver al menu principal y cerrar juego
    main_menu_bg = main_canva.create_rectangle(0, 650, 500, 700, fill="#33334D", outline="")
    main_menu_text = main_canva.create_text(250, 675, text="🏠 Menu Principal", fill=btn_text_color, font=btn_text_font)
    exit_bg = main_canva.create_rectangle(500, 650, 1000, 700, fill="#33334D", outline="")
    exit_text = main_canva.create_text(700, 675, text="❌ Cerrar Juego", fill=btn_text_color, font=btn_text_font)
    main_canva.tag_bind(main_menu_bg, "<Button-1>", lambda e: main_menu())
    main_canva.tag_bind(main_menu_text, "<Button-1>", lambda e: main_menu())
    main_canva.tag_bind(exit_bg, "<Button-1>", close_app)
    main_canva.tag_bind(exit_text, "<Button-1>", close_app)

def second_game_logic(num):
    global games_trys, secret_num
    games_trys += 1
    if games_trys <= 3:
        if games_trys == 1:
            main_canva.itemconfig(first_num, text=num)
        if games_trys == 2:
            main_canva.itemconfig(second_num, text=num)
        if games_trys == 3:
            main_canva.itemconfig(third_num, text=num)
            if num != secret_num:
                second_game_final_screem("Has Perdido")
                return
        if num < secret_num:
            main_canva.itemconfig(second_game_text, text="Tu número es más pequeño que el número oculto")
            return
        if num > secret_num:
            main_canva.itemconfig(second_game_text, text="Tu número es más grande que el número oculto")
            return
        if num == secret_num:
            second_game_final_screem("Has Ganado")
            return
    second_game_final_screem("Has Perdido")
        
def second_game_final_screem(title):
    clear_canva(800, 500)

    main_canva.create_text(400, 50, text=title, fill=title_color, font=title_font)

    main_canva.create_text(400, 160, text="El número secreto era:", fill=btn_text_color, font=text_font)

    new_circle(400,280,75, "#33334D")
    second_num = main_canva.create_text(400, 280, text=secret_num, fill=btn_text_color, font=title_font)

    main_menu_bg = main_canva.create_rectangle(0, 450, 250, 500, fill="#33334D", outline="")
    main_menu_text = main_canva.create_text(125, 475, text="🏠 Menú Principal", fill=btn_text_color, font=small_btn_text_font)
    regame_bg = main_canva.create_rectangle(275, 450, 525, 500, fill="#33334D", outline="")
    regame_text = main_canva.create_text(400, 475, text="⟳ Volver a Jugar", fill=btn_text_color, font=small_btn_text_font)
    exit_bg = main_canva.create_rectangle(550, 450, 800, 500, fill="#33334D", outline="")
    exit_text = main_canva.create_text(675, 475, text="❌ Cerrar Juego", fill=btn_text_color, font=small_btn_text_font)
    main_canva.tag_bind(main_menu_bg, "<Button-1>", lambda e: main_menu())
    main_canva.tag_bind(main_menu_text, "<Button-1>", lambda e: main_menu())
    main_canva.tag_bind(regame_bg, "<Button-1>", lambda e: second_game_screen())
    main_canva.tag_bind(regame_text, "<Button-1>", lambda e: second_game_screen())
    main_canva.tag_bind(exit_bg, "<Button-1>", close_app)
    main_canva.tag_bind(exit_text, "<Button-1>", close_app)

def third_game_screen():
    global third_game_words, selected_words, first_word_entry_var, second_word_entry_var, third_word_entry_var, fourth_word_entry_var, fifth_word_entry_var
    third_game_words = {
        "Apple": "manzana",
        "Book": "libro",
        "House": "casa",
        "Sun": "sol",
        "Moon": "luna",
        "Tree": "árbol",
        "Car": "coche",
        "Water": "agua",
        "Fire": "fuego",
        "Earth": "tierra",
        "Sky": "cielo",
        "Dog": "perro",
        "Cat": "gato",
        "Bird": "pájaro",
        "Flower": "flor",
        "Food": "comida",
        "School": "escuela",
        "Road": "camino",
        "Wind": "viento",
        "Star": "estrella"
    }
    
    # Dejar el canva vacio y redimensionar ventana
    clear_canva(700, 850)

    selected_words = random.sample(list(third_game_words.keys()), 5)

    main_canva.create_text(350, 100, text="Traduce las palabras\n al español", fill=title_color, font=title_font, justify="center")

    main_canva.create_text(250, 250, text=selected_words[0], fill=btn_text_color, font=text_font)
    first_word_entry_var = tk.StringVar()
    first_word_entry = tk.Entry(root, textvariable=first_word_entry_var, font=text_font, width=10, bg="#33334D", fg=btn_text_color, justify="center")
    main_canva.create_window(400, 250, anchor="center", window=first_word_entry)

    main_canva.create_text(250, 350, text=selected_words[1], fill=btn_text_color, font=text_font)
    second_word_entry_var = tk.StringVar()
    second_word_entry = tk.Entry(root, textvariable=second_word_entry_var, font=text_font, width=10, bg="#33334D", fg=btn_text_color, justify="center")
    main_canva.create_window(400, 350, anchor="center", window=second_word_entry)

    main_canva.create_text(250, 450, text=selected_words[2], fill=btn_text_color, font=text_font)
    third_word_entry_var = tk.StringVar()
    third_word_entry = tk.Entry(root, textvariable=third_word_entry_var, font=text_font, width=10, bg="#33334D", fg=btn_text_color, justify="center")
    main_canva.create_window(400, 450, anchor="center", window=third_word_entry)

    main_canva.create_text(250, 550, text=selected_words[3], fill=btn_text_color, font=text_font)
    fourth_word_entry_var = tk.StringVar()
    fourth_word_entry = tk.Entry(root, textvariable=fourth_word_entry_var, font=text_font, width=10, bg="#33334D", fg=btn_text_color, justify="center")
    main_canva.create_window(400, 550, anchor="center", window=fourth_word_entry)

    main_canva.create_text(250, 650, text=selected_words[4], fill=btn_text_color, font=text_font)
    fifth_word_entry_var = tk.StringVar()
    fifth_word_entry = tk.Entry(root, textvariable=fifth_word_entry_var, font=text_font, width=10, bg="#33334D", fg=btn_text_color, justify="center")
    main_canva.create_window(400, 650, anchor="center", window=fifth_word_entry)

    third_game_next_btn = main_canva.create_rectangle(200, 700, 500, 750, fill="#33334D", outline="")
    third_game_next_text = main_canva.create_text(350, 725, text="Continuar ➤", fill=btn_text_color, font=btn_text_font)
    main_canva.tag_bind(third_game_next_btn, "<Button-1>", lambda e: third_game_logic())
    main_canva.tag_bind(third_game_next_text, "<Button-1>", lambda e: third_game_logic())

    main_menu_bg = main_canva.create_rectangle(0, 800, 350, 850, fill="#33334D", outline="")
    main_menu_text = main_canva.create_text(175, 825, text="🏠 Menu Principal", fill=btn_text_color, font=btn_text_font)
    exit_bg = main_canva.create_rectangle(350, 800, 700, 850, fill="#33334D", outline="")
    exit_text = main_canva.create_text(525, 825, text="❌ Cerrar Juego", fill=btn_text_color, font=btn_text_font)
    main_canva.tag_bind(main_menu_bg, "<Button-1>", lambda e: main_menu())
    main_canva.tag_bind(main_menu_text, "<Button-1>", lambda e: main_menu())
    main_canva.tag_bind(exit_bg, "<Button-1>", close_app)
    main_canva.tag_bind(exit_text, "<Button-1>", close_app)

def third_game_logic():
    global selected_words
    score = 0
    title = "Has Aprobado"

    user_answers = [
        first_word_entry_var.get(),
        second_word_entry_var.get(),
        third_word_entry_var.get(),
        fourth_word_entry_var.get(),
        fifth_word_entry_var.get()
    ]

    for i, word in enumerate(selected_words):
        if user_answers[i].lower() == third_game_words[word]:
            score += 1

    if score < 3 :
        title = "Has suspendido"

    third_game_final_screem(score, title)

def third_game_final_screem(score, title):
    clear_canva(600, 420)

    main_canva.create_text(300, 50, text=title, fill=title_color, font=title_font)

    score_text = "Tu púntuacion total,\nha sido "+ str(score) +"/5"
    main_canva.create_text(300, 150, text=score_text, fill=btn_text_color, font=btn_text_font, justify="center")

    main_menu_bg = main_canva.create_rectangle(0, 250, 600, 300, fill="#33334D", outline="")
    main_menu_text = main_canva.create_text(300, 275, text="🏠 Menú Principal", fill=btn_text_color, font=btn_text_font)
    regame_bg = main_canva.create_rectangle(0, 310, 600, 360, fill="#33334D", outline="")
    regame_text = main_canva.create_text(300, 335, text="⟳ Volver a Jugar", fill=btn_text_color, font=btn_text_font)
    exit_bg = main_canva.create_rectangle(0, 370, 600, 420, fill="#33334D", outline="")
    exit_text = main_canva.create_text(300, 390, text="❌ Cerrar Juego", fill=btn_text_color, font=btn_text_font)
    main_canva.tag_bind(main_menu_bg, "<Button-1>", lambda e: main_menu())
    main_canva.tag_bind(main_menu_text, "<Button-1>", lambda e: main_menu())
    main_canva.tag_bind(regame_bg, "<Button-1>", lambda e: third_game_screen())
    main_canva.tag_bind(regame_text, "<Button-1>", lambda e: third_game_screen())
    main_canva.tag_bind(exit_bg, "<Button-1>", close_app)
    main_canva.tag_bind(exit_text, "<Button-1>", close_app)

def main_menu():
    # Dejar el canva vacio y redimensionar ventana
    clear_canva(500, 800)

    global bg_img, option_img
    bg_img = ImageTk.PhotoImage(Image.open("bg.jpeg"))
    option_img = load_image("menu_option.png",390,100)

    # Imagen de fondo menu principal
    main_canva.create_image(0,0,anchor=NW,image=bg_img)

    # Titulo menu principal
    main_canva.create_text(250, 180, text="Menu Principal", fill=title_color, font=title_font)

    # Botones seleccion minijuego
    first_game_img = main_canva.create_image(55,230,anchor=NW,image=option_img)
    first_game_text = main_canva.create_text(250, 275, text="Piedra, Papel o Tijeras", fill=btn_text_color, font=btn_text_font)
    second_game_img = main_canva.create_image(55,340,anchor=NW,image=option_img)
    second_game_text = main_canva.create_text(250, 385, text="Adivina el Número", fill=btn_text_color, font=btn_text_font)
    third_game_img = main_canva.create_image(55,450,anchor=NW,image=option_img)
    third_game_text = main_canva.create_text(250, 495, text="Traducir Palabras", fill=btn_text_color, font=btn_text_font)
    exit_game_img = main_canva.create_image(55,560,anchor=NW,image=option_img)
    exit_game_text = main_canva.create_text(250, 605, text="Salir", fill=btn_text_color, font=btn_text_font)

    # Bindeamos cada boton a su minijuego
    main_canva.tag_bind(first_game_img, "<Button-1>", lambda e: first_game_screen())
    main_canva.tag_bind(first_game_text, "<Button-1>", lambda e: first_game_screen())
    main_canva.tag_bind(second_game_img, "<Button-1>", lambda e: second_game_screen())
    main_canva.tag_bind(second_game_text, "<Button-1>", lambda e: second_game_screen())
    main_canva.tag_bind(third_game_img, "<Button-1>", lambda e: third_game_screen())
    main_canva.tag_bind(third_game_text, "<Button-1>", lambda e: third_game_screen())
    main_canva.tag_bind(exit_game_img, "<Button-1>", close_app)
    main_canva.tag_bind(exit_game_text, "<Button-1>", close_app)


# Ventena Principal
root = tk.Tk()
root.title("Minijuegos")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.resizable(width = False, height = False)

# Precargamos algunas globales necesarias
global title_font, title_color, btn_text_font, small_btn_text_font, btn_text_color
title_font = tkFont.Font(family='Lucida Console', size=32, weight='bold')
title_color = "#E0E0E0"
btn_text_font = tkFont.Font(family='Lucida Console', size=18, weight='bold')
small_btn_text_font = tkFont.Font(family='Lucida Console', size=14, weight='bold')
btn_text_color = "#FFFFFF"
text_font= tkFont.Font(family='Lucida Console', size=16)

main_canva = Canvas(root, width=500, height=800)
main_canva.pack()
main_canva.configure(background="#1E1E2F")

main_menu()

root.mainloop()