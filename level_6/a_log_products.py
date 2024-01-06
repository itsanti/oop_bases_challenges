"""
У нас есть различные типы классы для различных типов продуктов. Но мы ничего не знаем о том что происходит, когда мы вызываем
эти методы, хотелось бы простейшего логирования

Задания:
    1. Создайте класс PrintLoggerMixin и метод log у него, который будет принтить переданное в него сообщение.
    2. Используйте этот миксин, чтобы залогировать все методы у PremiumProduct и DiscountedProduct.
       Добавьте миксин и используйте новый метод во всех методах основных классов.
    3. Вызовите у экземпляров PremiumProduct и DiscountedProduct все возможные методы и убедитесь, что вызовы логируются.
"""


class PrintLoggerMixin:
    def log(self, msg):
        print(msg)


class Product(PrintLoggerMixin):
    def __init__(self, title: str, price: float):
        self.log(f'Call {self.__class__.__name__}::__init__')
        self.title = title
        self.price = price

    def get_info(self):
        self.log(f'Call {self.__class__.__name__}::get_info')
        return f'Product {self.title} with price {self.price}'


class PremiumProduct(Product):
    def increase_price(self):
        self.log(f'Call {self.__class__.__name__}::increase_price')
        self.price *= 1.2

    def get_info(self):
        base_info = super().get_info()
        return f'{base_info} (Premium)'

class DiscountedProduct(Product):
    def decrease_price(self):
        self.log(f'Call {self.__class__.__name__}::decrease_price')
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
    
    Call Product::__init__
    Call Product::get_info
    Call PremiumProduct::__init__
    Call PremiumProduct::increase_price
    Call PremiumProduct::get_info
    Call DiscountedProduct::__init__
    Call DiscountedProduct::decrease_price
    Call DiscountedProduct::get_info
'''