from TFS_classes import *
import csv

massiv_products = []
product = None

def create_massiv_products(product):
    global massiv_products
    massiv_products.append(product)

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

def import_to_csv(clmnq):
    products_csv = []
    for i in range(len(massiv_products)):
        products_csv.append(massiv_products[i].return_dict())
        print()
    file_name = "products.csv"
    name_columns = ['id', 'name', 'price', 'vendercode', 'quantity']
    colums_csv = []
    for i in range(clmnq):
        colums_csv.append(name_columns[i])
    with open(file_name, 'w', newline='') as file:
        wrinter = csv.DictWriter(file, fieldnames=colums_csv, delimiter=';')
        wrinter.writeheader()
        wrinter.writerows(products_csv)