from Models.ingredient import Ingredient
from Models.product import Product
from Models.pantry_item import Pantry_Item
test_ingredient = Ingredient(1 , "Tomato" , "Vegetable")
test_product = Product ( 1 , "Tomato Sauce" , "1234567890123" , test_ingredient , 500 , "ml")

print(test_ingredient)
print(test_product)