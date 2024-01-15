import csv
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.load_menu(source_path)

    def load_menu(self, source_path: str) -> None:
        with open(source_path, newline='') as csvfile:
            menu_reader = csv.DictReader(csvfile)
            dishes_bibl = {}

            for row in menu_reader:
                dish_name = row['dish']
                dish_ingredient = row['ingredient']
                amount = int(row['recipe_amount'])
                price = float(row['price'])

                if dish_name not in dishes_bibl:
                    dish = Dish(dish_name, price)
                    dishes_bibl[dish_name] = dish
                    self.dishes.add(dish)
                else:
                    dish = dishes_bibl[dish_name]

                ingredient = Ingredient(dish_ingredient)
                dish.add_ingredient_dependency(ingredient, amount)
