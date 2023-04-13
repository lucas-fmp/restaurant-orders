# Req 3
import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self._load_menu_data(source_path)

    def _load_menu_data(self, source_path):
        with open(source_path) as menu_data:
            menu = csv.reader(menu_data)
            next(menu)
            for row in menu:
                dish_name, dish_price, ingredient_name, ingredient_qty = row
                ingredient = Ingredient(ingredient_name)
                dish = next(
                    (dish for dish in self.dishes if dish.name == dish_name),
                    None,
                )
                if dish is None:
                    dish = Dish(dish_name, float(dish_price))
                    self.dishes.add(dish)
                dish.add_ingredient_dependency(ingredient, int(ingredient_qty))
