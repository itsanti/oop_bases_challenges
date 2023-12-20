"""
Мы используем константу EBAY_TITLE только в классе EbayProduct и хочется чтобы она жила в классе, а не где-то отдельно

Задания:
    1. Сделайте так, чтобы тайтл ебэя жил в классе
    2. Создайте экземпляр класса EbayProduct, вызовите у него метод get_product_info и убедитесь, что метод отдает
       то что вы ожидаете.
"""

class EbayProduct:
    ebay_title = 'eBay'

    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price

    def get_product_info(self):
        return f'Product {self.title} with price {self.price} from {self.ebay_title} marketplace'


if __name__ == '__main__':
    product = EbayProduct('Apple', 20)
    assert product.get_product_info() == 'Product Apple with price 20 from eBay marketplace'
