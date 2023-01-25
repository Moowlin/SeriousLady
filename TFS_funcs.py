from TFS_classes import *
import csv

massiv_products = []
product = None
# --------------------------------------= Функция возвращает массив продуктов =-----------------------------------------
def return_massiv():
    global massiv_products
    return massiv_products

# ---------------------------------------= Функция создания массива продуктов =-----------------------------------------
def create_massiv_products(product):
    global massiv_products
    massiv_products.append(product)

# -------------------------------------= Функция создания продукта как объекта =----------------------------------------
def create_product(clmnq, *data):
    global product
    if clmnq == 3:
        product = Product_base(data[0], data[1], data[2])
        create_massiv_products(product)
    if clmnq == 4:
        product = Product_property4(data[0], data[1], data[2], data[3])
        create_massiv_products(product)
    if clmnq == 5:
        product = Product_property5(data[0], data[1], data[2], data[3], data[4])
        create_massiv_products(product)

# ---------------------------------= Функция получения значений атрибутов продукта =------------------------------------
def creating_product(massiv_entry, clnmq):
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

# --------------------------------------= Функция импортирования данных в файл=-----------------------------------------
def import_to_csv(clmnq, filepath):
    products_csv = []
    for i in range(len(massiv_products)):
        products_csv.append(massiv_products[i].return_dict())
    file_name = filepath + ".csv"
    name_columns = ['id', 'name', 'price', 'vendercode', 'quantity']
    colums_csv = []
    for i in range(clmnq):
        colums_csv.append(name_columns[i])
    with open(file_name, 'w', newline='') as file:
        #wrinter = csv.DictWriter(file, fieldnames=colums_csv, delimiter=';')
        wrinter = csv.DictWriter(file, fieldnames=colums_csv)
        wrinter.writeheader()
        wrinter.writerows(products_csv)

# ------------------------------------------------= Функция чтения файла =----------------------------------------------
def read_file(filepath):
    with open(filepath, 'r+', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if len(row) not in (3, 4, 5):
                return False
                break
            if len(row) == 3:
                clnmq = 3
                data = list(row.values())
                create_product(clnmq, data[0], data[1], data[2])
            if len(row) == 4:
                clnmq = 4
                data = list(row.values())
                create_product(clnmq, data[0], data[1], data[2], data[3])
            if len(row) == 5:
                clnmq = 5
                data = list(row.values())
                create_product(clnmq, data[0], data[1], data[2], data[3], data[4])

# ----------------------------= Функция проверки заполнения полей данных о продукте =-----------------------------------
def check_field(massiv_entry):
    result_checking = False
    for i in range(len(massiv_entry)):
        if massiv_entry[i].get() == '':
            result_checking = False
            break
        else:
            result_checking = True
    return result_checking

# ------------------------------------= Функция проверки количества столбцов =------------------------------------------
def check_quantity(clmns_quantity):
    if int(clmns_quantity) not in (3, 4, 5):
            result = False
    else:
        result = True
    return result