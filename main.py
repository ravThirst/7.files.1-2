import codecs
from dataclasses import dataclass, field


@dataclass
class CookBook:
    def __str__(self) -> str:
        return str(self.cook_book)

    cook_book: dict = field(default_factory=dict)

    def get_recipes_from_file(self, path: str):
        with codecs.open(path, 'r', 'utf-8') as f:
            while True:
                dish = f.readline().strip()
                if not dish:
                    break
                ingredients_num = int(f.readline().strip())
                ingredients = []
                for i in range(ingredients_num):
                    ingredient = f.readline().strip().split(' | ')
                    ingredients.append(
                        {'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]), 'measure': ingredient[2]})
                self.cook_book[dish] = ingredients
                f.readline()

    def get_shop_list_by_dishes(self, dishes, person_count):
        shop_list = {}
        for dish in dishes:
            ingredients = self.cook_book[dish]
            for ingredient in ingredients:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']
                if ingredient_name not in shop_list:
                    shop_list[ingredient_name] = {'quantity': quantity, 'measure': measure}
                else:
                    shop_list[ingredient_name]['quantity'] += quantity
        return shop_list


if __name__ == "__main__":
    cook_book = CookBook()
    cook_book.get_recipes_from_file("recipes.txt")
    print(cook_book)
    shop_list = cook_book.get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)
    print(shop_list)

