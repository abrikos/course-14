from src.product import Product


class Category:
    """класс Категория"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, descriptions: str, products: list[Product]):
        self.name = name
        self.description = descriptions
        self.products = products
        Category.category_count += 1
        self.product_count = len(products)
        Category.product_count += self.product_count
