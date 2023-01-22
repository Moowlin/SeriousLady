from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import re
from TFS_funcs import *
from tkinter import filedialog

# ----------------------------------------------= Кнопка добавить =-----------------------------------------------------
def add_to_massiv():
    global massiv_products
    global clnmq
    if check_field(massiv_entry) == False:
        messagebox.showinfo("Добавление товара", "Данные о товаре не добавлены. Заполните все поля")
    else:
        creating_product(massiv_entry, clnmq)
        massiv_products = return_massiv()
        print(massiv_products)
        #for i in range(len(massiv_entry)):
        #    label = ttk.Label()
        #    label.grid(row=5, column=i, sticky="w", padx=5, pady=40)
        #    label["text"] = massiv_entry[i].get()  # получаем введенный текст
        messagebox.showinfo("Добавление товара", "Данные о товаре добавлены")

# ------------------------------------------= Кнопка Очистить =---------------------------------------------------------
def clear():
    for i in range(len(massiv_entry)):
        massiv_entry[i].delete(0, END)

# ----------------------------------------= Кнопка Вывод в файл =-------------------------------------------------------
def import_to_file():
    global massiv_products
    global clnmq
    if len(massiv_products) == 0:
        messagebox.showinfo("Ошибка", "Нет данных для вывода в файл")
    else:
        try:
            filepath = filedialog.asksaveasfilename()
            if '.' in filepath:
                raise Exception("Имя файла не должно содержать точку")
        except Exception as e:
            messagebox.showinfo("Ошибка", e)
        else:
            if filepath != "":
                print(type(filepath))
                print(filepath)
                import_to_csv(clnmq, filepath)

# -------------------------------------= Функции валидации полей ввода =------------------------------------------------
def is_valid_Id(newval):
    return re.match("\d{0,}$", newval) is not None  # регулярное выражение от 0 до бесконечности

def is_valid_Name(newval):
    return re.match("[a-zA-Zа-яА-Я\s]{0,30}$", newval) is not None  # только буквы и пробелы 0-30

def is_valid_Price(newval):
    return re.match("[0-9.]{0,10}$", newval) is not None  # 10 символов, цифры и точки

def is_valid_Vendercode(newval):
    return re.match("\d{0,7}$", newval) is not None  # 0-9999999

def is_valid_Quantity(newval):
    return re.match("\d{0,3}$", newval) is not None  # 0-999

# ---------------------------------------= Поля ввода данных товара =---------------------------------------------------
def create_fields_in_gui(clnmq, root):
    name_columns = ['Id', 'Name', 'Price', 'Vendercode', 'Quantity']
    for i in range(clnmq):
        name_st = name_columns[i]
        lbl = Label(text=name_st)
        lbl.grid(row=2, column=i, pady=10)
        message_nimi = StringVar()
        # Валидация полей:
        if i == 0:
            # Pегистрируем функцию, которая производит валидацию со значением "%P"
            check = (root.register(is_valid_Id), "%P")
            # Свяжем текст с переменной message_nimi
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
        massiv_entry.append(textentry)              # Создение массива с содержимым полей
        textentry.grid(row=3, column=i, padx=3)     # Отображение полей ввода на окне

        # Кнопка Добавить:
        add_button = Button(text="Добавить", command=add_to_massiv, fg="#eee", bg="#333", height=1, width=20)
        add_button.grid(row=4, column=0, padx=5, pady=40)

        # Кнопка Очистить:
        clear_button = Button(text="Очистить", command=clear, fg="#eee", bg="#333", height=1, width=20)
        clear_button.grid(row=4, column=1, padx=5, pady=40)

        # Кнопка Вывод в файл:
        import_button = Button(text="Вывод в файл", command=import_to_file, fg="#eee", bg="#333", height=1, width=20)
        import_button.grid(row=4, column=2, padx=5, pady=40)

        # Кнопка Закрыть окно:
        close_button = Button(root, text='Закрыть окно', command=root.destroy, fg="#eee", bg="#333", height=1, width=20)
        close_button.grid(row=4, column=3, padx=5, pady=40)

# -------------------------------------= Окно заполнения данными новой таблицы =----------------------------------------
def create_new_table():
    global clmns_quantity
    global quantity
    global window
    global clnmq
    if (clmns_quantity.get()).isdigit() == False:
        messagebox.showinfo("Ошибка", "Введите цифры")
    elif check_quantity(clmns_quantity.get()) == False:
        messagebox.showinfo("Ошибка", "Количество столбцов должно быть от 3 до 5")
    else:
        clnmq = int(quantity.get())         # получаем кол-во столбцов
        window.destroy()                    # закрытие первого окна
        root = Tk()                         # создаем новое окно
        root.title("Таблица товаров")       # заголовок
        root.geometry("830x300+250+100")
        #root.maxsize(900, 1000)
        #root.minsize(830, 500)
        lbl2 = Label(text="Введите данные о товарах", fg="#eee", bg="#333", height=2)
        lbl2.grid(row=0, column=0, padx=5, pady=0, sticky="w")
        # Изображение:
        canvas = Canvas(root, height=60, width=55)
        img = PhotoImage(file='image.png')
        image = canvas.create_image(5, 10, anchor='nw', image=img)
        canvas.grid(row=0, column=4, padx=5, pady=5, sticky="e")
        create_fields_in_gui(clnmq, root)
        root.mainloop()

# -----------------------------= Создание новой таблицы. Окно запроса количества столбцов =-----------------------------
def new_table():
    global quantity
    global clmns_quantity
    global window
    global root
    root.destroy()
    window = Tk()
    window.title("Основное окно")
    window.geometry("300x200+500+200")
    lbl_choice = Label(text="Введите количество необходимых столбцов", pady=10)
    lbl_choice.pack()
    lbl_choice2 = Label(text="(Id, Name, Price, Vendercode, Quantity):")
    lbl_choice2.pack()
    quantity = StringVar()
    clmns_quantity = ttk.Entry(textvariable=quantity, width=20)  # , validate="key", validatecommand=check)
    clmns_quantity.pack(pady=10)
    create_button = Button(text="Создать", fg="#eee", bg="#333", height=1, width=16, pady=-10, command=create_new_table)
    create_button.pack()
    window.mainloop()

# ----------------------------------------= ФУНКЦИЯ ЗАГЛУШКА!!!!! =-----------------------------------------------------
def pizda():
    messagebox.showinfo("Заглушка", "Ну пиздец! Еще работать и работать =(")
# ----------------------------------------------------------------------------------------------------------------------
#                                   .___  ___.      ___       __  .__   __.
#                                   |   \/   |     /   \     |  | |  \ |  |
#                                   |  \  /  |    /  ^  \    |  | |   \|  |
#                                   |  |\/|  |   /  /_\  \   |  | |  . `  |
#                                   |  |  |  |  /  _____  \  |  | |  |\   |
#                                   |__|  |__| /__/     \__\ |__| |__| \__|
# ----------------------------------------------------------------------------------------------------------------------
massiv_products = []
massiv_entry = []
clnmq = None
clmns_quantity = None
quantity = None
window = None
# -----------------------= Стартовое окно с запросом Новой или Существующей таблицы =-----------------------------------
root = Tk()
root.title("Работа с таблицами")
root.geometry("300x200+500+200")
lbl_choice = Label(text="С какой таблицей вы хотите работать?", pady=10)
lbl_choice.pack(pady=10)
new_table = Button(text="Создать новую таблицу", fg="#eee", bg="#333", height=1, width=25, pady=5, command=new_table)
new_table.pack()
edit_table = Button(text="Загрузить существующую таблицу", fg="#eee", bg="#333", height=1, width=30, pady=5, command=pizda)
edit_table.pack(pady=10)
root.mainloop()