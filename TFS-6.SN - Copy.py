from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import re


# -------------------------------------= Всплывающее окно при нажатии Добавить =----------------------------------------
def show_message():
    messagebox.showinfo("Добавление товара", "Данные о товаре добавлены")

    for i in range(len(massiv_entry)):
        label = ttk.Label()
        label.grid(row=5, column=i, sticky="w", padx=5, pady=40)
        label["text"] = massiv_entry[i].get()  # получаем введенный текст

# ------------------------------------------= Функции кнопки Очистить =-------------------------------------------------
def clear():
    for i in range(len(massiv_entry)):
        massiv_entry[i].delete(0, END)

# -------------------------------------= Функции валидации полей ввода =------------------------------------------------
def is_valid_Id(newval):
    return re.match("\d{0,}$", newval) is not None  # регулярное выражение


def is_valid_Name(newval):
    return re.match("\d{0,}$", newval) is not None


def is_valid_Price(newval):
    return re.match("\d{0,}$", newval) is not None


def is_valid_Vendercode(newval):
    return re.match("\d{0,}$", newval) is not None


def is_valid_Quantity(newval):
    return re.match("\d{0,}$", newval) is not None


# -------------------------------------= Вывод столбцов в графическом интерфейсе =--------------------------------------
massiv_entry = []

def do_message():
    name_columns = ['Id', 'Name', 'Price', 'Vendercode', 'Quantity']

    for i in range(clnmq):
        name_st = name_columns[i]
        lbl = Label(text=name_st)
        lbl.grid(row=2, column=i, pady=10)

        message_nimi = StringVar()
        if i == 0:
            # ----Pегистрируем функцию, которая производит валидацию со значением "%P"
            check = (root.register(is_valid_Id), "%P")
            # ----Свяжем текст с переменной message_nimi
            textentry = ttk.Entry(textvariable=message_nimi, width=25, validate="key", validatecommand=check)

        if i == 1:
            check = (root.register(is_valid_Name), "%P")
            textentry = ttk.Entry(textvariable=message_nimi, width=25, validate="key", validatecommand=check)

        if i == 2:
            check = (root.register(is_valid_Price), "%P")
            textentry = ttk.Entry(textvariable=message_nimi, width=25, validate="key", validatecommand=check)

        if i == 3:
            check = (root.register(is_valid_Vendercode), "%P")
            textentry = ttk.Entry(textvariable=message_nimi, width=25, validate="key", validatecommand=check)

        if i == 4:
            check = (root.register(is_valid_Quantity), "%P")
            textentry = ttk.Entry(textvariable=message_nimi, width=25, validate="key", validatecommand=check)

        massiv_entry.append(textentry)
        textentry.grid(row=3, column=i, padx=3)

# -----------------------------------------------= Кнопка Добавить =----------------------------------------------------
        add_button = Button(text="Добавить", command=show_message, fg="#eee", bg="#333", height=1, width=16)
        add_button.grid(row=4, column=0, sticky="e", padx=5, pady=40)

# -----------------------------------------------= Кнопка Очистить =----------------------------------------------------
        clear_button = Button(text="Очистить", command=clear, fg="#eee", bg="#333", height=1, width=16)
        clear_button.grid(row=4, column=1, sticky="w", padx=5, pady=40)


# ----------------------------------------------------------------------------------------------------------------------#
#                                   .___  ___.      ___       __  .__   __.
#                                   |   \/   |     /   \     |  | |  \ |  |
#                                   |  \  /  |    /  ^  \    |  | |   \|  |
#                                   |  |\/|  |   /  /_\  \   |  | |  . `  |
#                                   |  |  |  |  /  _____  \  |  | |  |\   |
#                                   |__|  |__| /__/     \__\ |__| |__| \__|
# -------------------------------------------= Запрос кол-ва столбцов =-------------------------------------------------
try:
    clnmq = int(input("Введите количество необходимых столбцов (Id, Name, Price, Vendercode, Quantity):"))
    if clnmq < 3 and clnmq > 5:
        raise Exception("Столбцов должно быть не менее 3 и не более 5")
except ValueError:
    print("Введены некорректные данные")
except Exception as e:
    print(e)
else:
    print("Запуск программы")

# -----------------------------------------------= Создание окна =------------------------------------------------------
    root = Tk()
    root.title("Таблица товаров")  # заголовок
    root.geometry("830x500+200+200")
    lbl2 = Label(text="Введите данные о товарах:", fg="#eee", bg="#333", height=2, pady=-10)
    lbl2.grid(row=1, column=0, padx=10, pady=0, sticky="w")

# ------------------------------------------------= Изображение =-------------------------------------------------------
    canvas = Canvas(root, height=60, width=55)
    img = PhotoImage(file='image.png')
    image = canvas.create_image(5, 10, anchor='nw', image=img)
    canvas.grid(row=1, column=4, padx=5, pady=5, sticky="e")

# ----------------------------------------------= Старт программы =-----------------------------------------------------
    do_message()
    root.mainloop()
