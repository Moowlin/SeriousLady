from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import re
from TFS_funcs import *

# ----------------------------------------------= Кнопка добавить =-----------------------------------------------------
def show_message():
    global clnmq

    if len(massiv_entry) == 3:
        cl_id = massiv_entry[0]
        cl_name = massiv_entry[1]
        cl_price = massiv_entry[2]
        create_product(clnmq, cl_id.get(), cl_name.get(), cl_price.get())

    if len(massiv_entry) == 4:
        cl_id = massiv_entry[0]
        cl_name = massiv_entry[1]
        cl_price = massiv_entry[2]
        cl_vendercode = massiv_entry[3]
        create_product(clnmq, cl_id.get(), cl_name.get(), cl_price.get(), cl_vendercode.get())

    if len(massiv_entry) == 5:
        cl_id = massiv_entry[0]
        cl_name = massiv_entry[1]
        cl_price = massiv_entry[2]
        cl_vendercode = massiv_entry[3]
        cl_quantity = massiv_entry[4]
        create_product(clnmq, cl_id.get(), cl_name.get(), cl_price.get(), cl_vendercode.get(), cl_quantity.get())


    for i in range(len(massiv_entry)):
        label = ttk.Label()
        label.grid(row=5, column=i, sticky="w", padx=5, pady=40)
        label["text"] = massiv_entry[i].get()  # получаем введенный текст

    messagebox.showinfo("Добавление товара", "Данные о товаре добавлены")

# ------------------------------------------= Функции кнопки Очистить =-------------------------------------------------
def clear():
    for i in range(len(massiv_entry)):
        massiv_entry[i].delete(0, END)

# ---------------------------------------= Функции кнопки вывод в файл =------------------------------------------------
def import_to_file():
    global clnmq
    import_to_csv(clnmq)

# -------------------------------------= Функции валидации полей ввода =------------------------------------------------
def is_valid1(newval):
    result = re.match("[3-5]$", newval) is not None #3-5
    # -------Вывод ошибки
    if not result:
        errmsg.set("Количество столбцов должно быть от 3 до 5")
    else:
        errmsg.set("")
    return result

def is_valid_Id(newval):
    return re.match("\d{0,}$", newval) is not None  #регулярное выражение от 0 до бесконечности

def is_valid_Name(newval):
    return re.match("[a-zA-Zа-яА-Я\s]{0,30}$", newval) is not None #только буквы и пробелы 0-30

def is_valid_Price(newval):
    return re.match("[0-9.]{0,10}$", newval) is not None #10 символов, цифры и точки

def is_valid_Vendercode(newval):
    return re.match("\d{0,7}$", newval) is not None #0-9999999

def is_valid_Quantity(newval):
    return re.match("\d{0,3}$", newval) is not None #0-999


# ----------------------------------= Вывод столбцов в графическом интерфейсе =--------------------------------------
massiv_entry = []

def do_message(clnmq, root):
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

# ---------------------------------------------= Кнопка Вывод в файл =--------------------------------------------------
        import_button = Button(text="Вывод в файл", command=import_to_file, fg="#eee", bg="#333", height=1, width=16)
        import_button.grid(row=5, column=0, sticky="e", padx=5, pady=20)

# ----------------------------------------------------------------------------------------------------------------------
#                                   .___  ___.      ___       __  .__   __.
#                                   |   \/   |     /   \     |  | |  \ |  |
#                                   |  \  /  |    /  ^  \    |  | |   \|  |
#                                   |  |\/|  |   /  /_\  \   |  | |  . `  |
#                                   |  |  |  |  /  _____  \  |  | |  |\   |
#                                   |__|  |__| /__/     \__\ |__| |__| \__|
#
# ----------------------------= Нажатие на кнопку открывает новое окно с таблицей =-------------------------------------
clnmq = None
def click_button():
    global clnmq
# -------------------------------------------= Запрос кол-ва столбцов =-------------------------------------------------
    clnmq = int(quantity.get())
    window.destroy() #закрытие первого окна
# -----------------------------------------------= Создание окна =------------------------------------------------------
    root = Tk()
    root.title("Таблица товаров")  # заголовок
    root.geometry("830x500+250+100")
    root.maxsize(900,1000)
    root.minsize(830,500)
    lbl2 = Label(text="Введите данные о товарах:", fg="#eee", bg="#333", height=2, pady=-10)
    lbl2.grid(row=1, column=0, padx=10, pady=0, sticky="w")

# ------------------------------------------------= Изображение =-------------------------------------------------------
    canvas = Canvas(root, height=60, width=55)
    img = PhotoImage(file='image.png')
    image = canvas.create_image(5, 10, anchor='nw', image=img)
    canvas.grid(row=1, column=4, padx=5, pady=5, sticky="e")

# ----------------------------------------------= Старт программы =-----------------------------------------------------
    do_message(clnmq, root)
    root.mainloop()

# -----------------------------= Создание первого окна с запросом количества столбцов =---------------------------------
window = Tk()
window.title("Основное окно")
window.geometry("300x200+500+200")
 
lbl_choice = Label(text="Введите количество необходимых столбцов", pady=10)
lbl_choice.pack()
lbl_choice2 = Label(text="(Id, Name, Price, Vendercode, Quantity):")
lbl_choice2.pack()

# ----------------------------------= Окно ввода количества столбцов с валидацией =-------------------------------------
check = (window.register(is_valid1), "%P") 
errmsg = StringVar()
quantity = StringVar()
clmns_quantity = ttk.Entry(textvariable=quantity, width=20, validate="key", validatecommand=check)
clmns_quantity.pack(pady=10)

# ----------------------------------------= Вывод ошибки при валидации =------------------------------------------------
error_label = ttk.Label(foreground="red", textvariable=errmsg, wraplength=250)
error_label.pack(padx=5, pady=5)

button1 = Button(text="Создать", fg="#eee", bg="#333", height=1, width=16, pady=-10, command=click_button)
button1.pack()

window.mainloop()
