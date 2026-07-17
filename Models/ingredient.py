class Ingredient :
    
    def __init__(self , id_ingredient , name , category):
        self.id_ingredient = id_ingredient 
        self.name = name 
        self.category = category

    def __repr__(self):
        return f"Ingredient (id_ingredient = {self.id_ingredient} , name = {self.name} , category = {self.category})"