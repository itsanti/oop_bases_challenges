"""
У нас есть различные типы классы для различных типов продуктов. Но мы ничего не знаем о том что происходит, когда мы вызываем
эти методы, хотелось бы простейшего логирования

Задания:
    1. Создайте класс PrintLoggerMixin и метод log у него, который будет принтить переданное в него сообщение.
    2. Используйте этот миксин, чтобы залогировать все методы у PremiumProduct и DiscountedProduct.
       Добавьте миксин и используйте новый метод во всех методах основных классов.
    3. Вызовите у экземпляров PremiumProduct и DiscountedProduct все возможные методы и убедитесь, что вызовы логируются.
"""

def PrintLoggerDecorator(cls):
    def logging(method):
        def inner_method(self, *args, **kwargs):
            print(f"Call {cls.__name__}::{method.__name__}")
            return method(self, *args, **kwargs)
        return inner_method
    methods = [attr for attr in cls.__dict__.keys()
               if not attr.startswith("__") and callable(getattr(cls, attr))]
    for method in methods:
        setattr(cls, method, logging(getattr(cls, method)))
    return cls


class Product():
    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price

    def get_info(self):
        return f'Product {self.title} with price {self.price}'


@PrintLoggerDecorator
class PremiumProduct(Product):
    def increase_price(self):
        self.price *= 1.2

    def get_info(self):
        base_info = super().get_info()
        return f'{base_info} (Premium)'


@PrintLoggerDecorator
class DiscountedProduct(Product):
    def decrease_price(self):
        self.price /= 1.2

    def get_info(self):
        base_info = super().get_info()
        return f'{base_info} (Discounted)'


if __name__ == '__main__':
    apple = Product('Apple', 20)
    assert apple.get_info() == 'Product Apple with price 20'

    apple15 = PremiumProduct('Apple 15', 200)
    apple15.increase_price()
    assert apple15.get_info() == 'Product Apple 15 with price 240.0 (Premium)'

    appleSE = DiscountedProduct('Apple SE', 12)
    appleSE.decrease_price()
    assert appleSE.get_info() == 'Product Apple SE with price 10.0 (Discounted)'

'''
    Out:
    
    Call PremiumProduct::increase_price
    Call PremiumProduct::get_info
    Call DiscountedProduct::decrease_price
    Call DiscountedProduct::get_info
'''