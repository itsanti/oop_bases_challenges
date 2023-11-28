"""
У любого продукта есть такие свойства: название, описание, цена, вес

Задания:
    1. Создайте класс продукта.
    2. Создайте экземпляр этого продукта и наполинте своими данными.
    3. Распечатайте о нем иформацию в таком виде: Информация о продукте: название, описание, цена, вес
"""


class Product:
    def __init__(self, title: str, description: str, price: int, weight: float):
        self.title = title
        self.description = description
        self.price = price
        self.weight = weight

    def __str__(self):
        return (f'Информация о продукте: {self.title}\n'
                f'{self.description}.\n{(self.price / 100):0.2f} ₽, {self.weight} г.')


if __name__ == '__main__':
    product = Product('Пломбир «Из Лавки»',
                      ('К классическому сливочному пломбиру добавили солёную'
                       'карамель, сваренную по рецепту французских кондитеров'),
                      8900, 75)
    print(product)
