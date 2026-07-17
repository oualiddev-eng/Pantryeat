class Pantry_Item :

    def __init__(self , id_pantry_item , product , user , expiration_date , is_consumed):
        self.id_pantry_item = id_pantry_item
        self.product = product
        self.user = user
        self.expiration_date = expiration_date
        self.is_consumed = is_consumed

    def __repr__ (self) : 
        return f"Pantry_item (id_pantry_item = {self.id_pantry_item} , product = {self.product} , user = {self.user} , expiratio_date= {self.expiration_date} , is_consumed = {self.is_consumed})"
