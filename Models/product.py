class Product :

    def __init__ (self , id_product , name , barcode , ingredient , quantity , unit):
        self.id_product = id_product
        self.name = name
        self.barcode = barcode
        self.ingredient = ingredient
        self.quantity = quantity
        self.unit = unit 

    def __repr__ (self):
        return f"Product (id_product = {self.id_product} , name = {self.name} , barcode= {self.barcode}, ingredient = {self.ingredient}, quantity = {self.quantity} , unit = {self.unit})"
    