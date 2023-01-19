# -------------------------------------------- class Product_base ------------------------------------------------------
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

# ----------------------------------------- class Product_property4 ----------------------------------------------------
class Product_property4(Product_base):
    def __init__(self, st1, st2, st3, st4):
        Product_base.__init__(self, st1, st2, st3)
        self.vendercode = st4
        self.dict = {'id': self.id, 'name': self.name, 'price': self.price, 'vendercode': self.vendercode}

    def printInfo(self):
        Product_base.printInfo(self)
        print("vendercode: ", self.vendercode)

# ----------------------------------------- class Product_property5 ----------------------------------------------------
class Product_property5(Product_property4):
    def __init__(self, st1, st2, st3, st4, st5):
        Product_property4.__init__(self, st1, st2, st3, st4)
        self.quantity = st5
        self.dict = {'id': self.id, 'name': self.name, 'price': self.price, 'vendercode': self.vendercode,
                     'quantity': self.quantity}

    def printInfo(self):
        Product_property4.printInfo(self)
        print("quantity: ", self.quantity)