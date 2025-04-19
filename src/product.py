from typing import Any, Self


class Product:
    """класс Товар"""

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> Any:
        return self.quantity * self.price + other.quantity * other.price

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_dict: dict) -> Self:
        return cls(product_dict["name"], product_dict["description"], product_dict["price"], product_dict["quantity"])

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, p: float) -> None:
        if p <= 0:
            print("Цена не должна быть нулевая или отрицательна")
        else:
            if p < self.__price:
                confirm = input("Цена ниже текущей. Подтверждаете? y/n")
                if confirm.lower() == "y":
                    self.__price = p
            else:
                self.__price = p
