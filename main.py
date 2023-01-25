from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import re
from TFS_funcs import *
from tkinter import filedialog


# -----------------------------------------= Окно с таблицей данных =---------------------------------------------------
def window_with_table():
    global window_table
    # определяем данные для отображения
    products = []
    for i in range(len(massiv_products)):
        products.append(list(massiv_products[i].return_dict().values()))
    if window_table:
        window_table.destroy()
    window_table = Tk()
    window_table.title("Данные товаров:")
    window_table.geometry("900x300+200+400")
    # определяем столбцы
    columns = ['id', 'name', 'price', 'vendercode', 'quantity']
    columns_of_table = []
    for i in range(len(massiv_products[0].return_dict())):
        columns_of_table.append(columns[i])
    tree = ttk.Treeview(window_table, columns=columns_of_table, show="headings")
    tree.pack()
    # определяем заголовки
    for i in range(len(columns_of_table)):
        tree.heading(columns_of_table[i], text=columns_of_table[i], anchor=S)
    # настраиваем столбцы
    for i in range(1, len(columns_of_table) + 1):
        n = '#' + str(i)
        tree.column(n, stretch=YES, width=100, anchor=S)
    # добавляем данные
    for product in products:
        tree.insert("", END, values=product)

# ----------------------------------------------= Кнопка добавить =-----------------------------------------------------
def add_to_massiv():
    global massiv_products
    global clnmq
    global window_table
    global massiv_entry

    if check_field(massiv_entry) == False:
        messagebox.showinfo("Добавление товара", "Данные о товаре не добавлены. Заполните все поля")
    else:
        creating_product(massiv_entry, clnmq)
        massiv_products = return_massiv()
        window_with_table()

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
                import_to_csv(clnmq, filepath)

# -------------------------------------= Функции валидации полей ввода =------------------------------------------------
def is_valid_Id(newval):
    return re.match("\d{0,}$", newval) is not None  # регулярное выражение от 0 до бесконечности

def is_valid_Name(newval):
    return re.match("[a-zA-Zа-яА-Я\s.]{0,30}$", newval) is not None  # только буквы и пробелы 0-30

def is_valid_Price(newval):
    return re.match("[0-9.]{0,10}$", newval) is not None  # 10 символов, цифры и точки

def is_valid_Vendercode(newval):
    return re.match("\d{0,7}$", newval) is not None  # 0-9999999

def is_valid_Quantity(newval):
    return re.match("\d{0,3}$", newval) is not None  # 0-999

# --------------------------------------= Функция закрытия всех окон =--------------------------------------------------
def close_windows():
    global window_create_new_table
    global window_edit_old_table
    if window_table:
        window_table.destroy()
    if window_create_new_table:
        window_create_new_table.destroy()
    if window_edit_old_table:
        window_edit_old_table.destroy()

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

        # Кнопка Закрыть окна:
        close_button = Button(root, text='Закрыть окно', command=close_windows, fg="#eee", bg="#333", height=1, width=20)
        close_button.grid(row=4, column=3, padx=5, pady=40)

# -------------------------------------= Окно заполнения данными новой таблицы =----------------------------------------
def create_new_table():
    global clmns_quantity
    global quantity
    global window_create_new_table
    global clnmq
    if (clmns_quantity.get()).isdigit() == False:
        messagebox.showinfo("Ошибка", "Введите цифры")
    elif check_quantity(clmns_quantity.get()) == False:
        messagebox.showinfo("Ошибка", "Количество столбцов должно быть от 3 до 5")
    else:
        clnmq = int(quantity.get())         # получаем кол-во столбцов
        window_new_table.destroy()                    # закрытие первого окна
        window_create_new_table = Tk()                         # создаем новое окно
        window_create_new_table.title("Таблица товаров")       # заголовок
        window_create_new_table.geometry("830x300+250+100")
        lbl2 = Label(text="Введите данные о товарах", fg="#eee", bg="#333", height=2)
        lbl2.grid(row=0, column=0, padx=5, pady=0, sticky="w")
        # Изображение:
        canvas = Canvas(window_create_new_table, height=60, width=55)
        img = PhotoImage(file='image.png')
        image = canvas.create_image(5, 10, anchor='nw', image=img)
        canvas.grid(row=0, column=4, padx=5, pady=5, sticky="e")
        create_fields_in_gui(clnmq, window_create_new_table)
        window_create_new_table.mainloop()

# -------------------------------------= Окно редактирования старой таблицы =----------------------------------------
def editing_table():
    global clnmq
    global quantity
    global start_window
    global window_edit_old_table
    global massiv_products
    clnmq = len(massiv_products[0].return_dict())
    start_window.destroy()
    window_edit_old_table = Tk()  # создаем новое окно
    window_edit_old_table.title("Таблица товаров")  # заголовок
    window_edit_old_table.geometry("830x300+250+100")
    lbl2 = Label(text="Введите данные о товарах", fg="#eee", bg="#333", height=2)
    lbl2.grid(row=0, column=0, padx=5, pady=0, sticky="w")
    # Изображение:
    canvas = Canvas(window_edit_old_table, height=60, width=55)
    img = PhotoImage(file='image.png')
    image = canvas.create_image(5, 10, anchor='nw', image=img)
    canvas.grid(row=0, column=4, padx=5, pady=5, sticky="e")

    create_fields_in_gui(clnmq, window_edit_old_table)
    window_with_table()
    window_edit_old_table.mainloop()

# -----------------------------= Создание новой таблицы. Окно запроса количества столбцов =-----------------------------
def new_table():
    global quantity
    global clmns_quantity
    global window_new_table
    start_window.destroy()
    window_new_table = Tk()
    window_new_table.title("Основное окно")
    window_new_table.geometry("300x200+500+200")
    lbl_choice = Label(text="Введите количество необходимых столбцов", pady=10)
    lbl_choice.pack()
    lbl_choice2 = Label(text="(Id, Name, Price, Vendercode, Quantity):")
    lbl_choice2.pack()
    quantity = StringVar()
    clmns_quantity = ttk.Entry(textvariable=quantity, width=20)
    clmns_quantity.pack(pady=10)
    create_button = Button(text="Создать", fg="#eee", bg="#333", height=1, width=16, pady=-10, command=create_new_table)
    create_button.pack()
    window_new_table.mainloop()

# ------------------------------------= Функция выбора файла для редактирвоания =---------------------------------------
def old_table():
    global clmns_quantity
    global massiv_products
    global clnmq
    try:
        filepath = filedialog.askopenfilename()
        if filepath[-4:] != '.csv':
            raise Exception("Выберите файл c расширением csv")
    except Exception as e:
        messagebox.showinfo("Ошибка", e)
    else:
        try:
            result = read_file(filepath)
            if result == False:
                raise Exception("В выбранном файле неверное кол-во столбцов. Должно быть от 3 до 5")
        except Exception as fail:
            messagebox.showinfo("Ошибка", fail)
        else:
            massiv_products = return_massiv()
            print("прочитали: ",massiv_products)
            clmns_quantity = massiv_products[0].return_dict()
            clnmq = clmns_quantity
            editing_table()

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
window_new_table = None
window_table = None
window_create_new_table = None
window_edit_old_table = None
# -----------------------= Стартовое окно с запросом Новой или Существующей таблицы =-----------------------------------
start_window = Tk()
start_window.title("Работа с таблицами")
start_window.geometry("300x200+500+200")
lbl_choice = Label(text="С какой таблицей вы хотите работать?", pady=10)
lbl_choice.pack(pady=10)
new_table = Button(text="Создать новую таблицу", fg="#eee", bg="#333", height=1, width=25, pady=5, command=new_table)
new_table.pack()
edit_table = Button(text="Загрузить существующую таблицу", fg="#eee", bg="#333", height=1, width=30, pady=5, command=old_table)
edit_table.pack(pady=10)
start_window.mainloop()