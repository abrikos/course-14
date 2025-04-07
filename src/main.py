import json

from src.category import Category
from src.product import Product


def load_products() -> None:
    with open("../data/products.json") as f:
        data = json.load(f)
        for cat in data:
            products = []
            for prod in cat["products"]:
                products.append(Product(prod["name"], prod["description"], prod["price"], prod["quantity"]))
            c = Category(cat["name"], cat["description"], products)
            print(c.products)
    print(Category.category_count)
    print(Category.product_count)
    print(Product.new_product({"name": "aaaa", "description": "zzz", "price": 5, "quantity": 10}))


load_products()
