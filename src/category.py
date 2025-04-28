from src.product import Product
from abc import ABC, abstractmethod


class CategoryOrder(ABC):
    @abstractmethod
    def print_info(self):
        pass


class Category(CategoryOrder):
    """класс Категория"""
    product_count = 0
    category_count = 0

    def __str__(self) -> str:
        return f"{self.name}, количество продуктов: {len(self.products)} шт."

    def __init__(self, name: str, descriptions: str, products: list[Product]):
        self.name = name
        self.description = descriptions
        self.__products = products
        Category.category_count += 1
        self.product_count = len(products)
        Category.product_count += self.product_count

    def add_product(self, product: Product) -> None:
        if isinstance(product, Product):
            self.__products.append(product)
            self.product_count += 1
            print(f"Product added: {product}")
        else:
            raise TypeError('Only products allowed')

    @property
    def products(self) -> list:
        return list(map(lambda x: f"{x.name}, {x.price} руб. Остаток {x.quantity} шт.", self.__products))

    @property
    def average_price(self):
        try:
            return sum(list(map(lambda x: x.price, self.__products))) / len(self.__products)
        except ZeroDivisionError:
            return 0

    def print_info(self):
        print(self.name, self.description)

class OrderError(Exception):
    """Order's exception class"""
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Unknown error"
    def __str__(self):
        return self.message

class Order(CategoryOrder):
    def __init__(self, product, count):
        if count <=0:
            raise OrderError('Quantity must be greater than zero')
        self.product = product
        self.count = count
        print(f"Product ordered: {product.name}, {self.count} шт.")

    def __str__(self):
        return f"Order for product: {self.product.name}. {self.count} шт."

    def print_info(self):
        print(self)


