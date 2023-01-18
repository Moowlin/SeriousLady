import csv


class Product_base:
    def __init__(self, st1, st2, st3):
        self.id = st1
        self.name = st2
        self.price = st3

    def printInfo(self):
        print("id: ", self.id)
        print("name: ", self.name)
        print("price: ", self.price)


class Product_property4(Product_base):
    def __init__(self, st1, st2, st3, st4):
        Product_base.__init__(self, st1, st2, st3)
        self.vendercode = st4

    def printInfo(self):
        Product_base.printInfo(self)
        print("vendercode: ", self.vendercode)


class Product_property5(Product_property4):
    def __init__(self, st1, st2, st3, st4, st5):
        Product_property4.__init__(self, st1, st2, st3, st4)
        self.quantity = st5

    def printInfo(self):
        Product_property4.printInfo(self)
        print("quantity: ", self.quantity)

massiv_products = []

def create_massiv_products(product):
    global massiv_products
    massiv_products.append(product)
    print(massiv_products)

product = None
def create_product():
    global product
    clmnq = int(input('укажи число: '))
    if clmnq == 3:
        product = Product_base(2342, "sdfsf", "wfwaqf")
        #product = Product_base(id.get(), name.get(), price.get())
        product.printInfo()
        create_massiv_products(product)
    elif clmnq == 4:
        product = Product_property4(456, 'второе св-во', '3 сво-во', "4 св-во")
        #product = Product_property4(id.get(), name.get(), price.get(), vendercode.get())
        product.printInfo()
        create_massiv_products(product)
    elif clmnq == 5:
        product = Product_property5(65745, 'второе св-во', '3 сво-во', "4 св-во", "5 сво-во")
        #product = Product_property5(id.get(), name.get(), price.get(), vendercode.get(), quantity.get())
        product.printInfo()
        #create_massiv_products(product)
    else:
        print("doesn't work")



def button_count_products():
    x = int(input('Сколько товаров вести: '))
    for i in range(x):
        create_product()


#button_count_products()

create_product()
print(product)

print((type(product)))
print(dir(product))



# --------------- Обработка массива
#for i in range(len(massiv_products)):
#    for values, key in massiv_products[i].dict.items():
#        print(values, key)




file_name = "products.csv"


# https://qna.habr.com/q/967195