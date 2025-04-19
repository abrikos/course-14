from src.product import Product


class Category:
    """класс Категория"""

    category_count = 0
    product_count = 0

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

    @property
    def products(self) -> list:
        return list(map(lambda x: f"{x.name}, {x.price} руб. Остаток {x.quantity} шт.", self.__products))
