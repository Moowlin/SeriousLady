import csv


class Product_base:
    def __init__(self, st1, st2, st3):
        self.id = st1
        self.name = st2
        self.price = st3
        self.dict = {'id': self.id, 'name': self.name, 'price': self.price}

    def printInfo(self):
        print("id: ", self.id)
        print("name: ", self.name)
        print("price: ", self.price)

    def return_dict(self):
        return self.dict


class Product_property4(Product_base):
    def __init__(self, st1, st2, st3, st4):
        Product_base.__init__(self, st1, st2, st3)
        self.vendercode = st4
        self.dict = {'id': self.id, 'name': self.name, 'price': self.price, 'vendercode': self.vendercode}

    def printInfo(self):
        Product_base.printInfo(self)
        print("vendercode: ", self.vendercode)


class Product_property5(Product_property4):
    def __init__(self, st1, st2, st3, st4, st5):
        Product_property4.__init__(self, st1, st2, st3, st4)
        self.quantity = st5
        self.dict = {'id': self.id, 'name': self.name, 'price': self.price, 'vendercode': self.vendercode, 'quantity': self.quantity}

    def printInfo(self):
        Product_property4.printInfo(self)
        print("quantity: ", self.quantity)

massiv_products = []
clmnq = None


def create_massiv_products(product):
    global massiv_products
    massiv_products.append(product)


product = None
def create_product():
    global product
    global clmnq
    clmnq = int(input('укажи число: '))
    if clmnq == 3:
        product = Product_base(2342, "sdfsf", "wfwaqf")
        #product = Product_base(id.get(), name.get(), price.get())
        #product.printInfo()
        create_massiv_products(product)
    elif clmnq == 4:
        product = Product_property4(456, 'второе св-во', '3 сво-во', "4 св-во")
        #product = Product_property4(id.get(), name.get(), price.get(), vendercode.get())
        #product.printInfo()
        create_massiv_products(product)
    elif clmnq == 5:
        product = Product_property5(65745, 'второе св-во', '3 сво-во', "4 св-во", "5 сво-во")
        #product = Product_property5(id.get(), name.get(), price.get(), vendercode.get(), quantity.get())
        #product.printInfo()
        create_massiv_products(product)
    else:
        print("doesn't work")



def button_count_products():
    x = int(input('Сколько товаров вести: '))
    for i in range(x):
        create_product()

button_count_products()

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------



print()

products_csv = []
for i in range(len(massiv_products)):
    products_csv.append(massiv_products[i].return_dict())
    print()

print(products_csv)

file_name = "products.csv"

name_columns = ['id', 'name', 'price', 'vendercode', 'quantity']
colums_csv = []

for i in range(clmnq):
    colums_csv.append(name_columns[i])



with open(file_name, 'w', newline='') as file:
    wrinter = csv.DictWriter(file, fieldnames=colums_csv, delimiter=';')
    wrinter.writeheader()

    wrinter.writerows(products_csv)

