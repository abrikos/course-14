from abc import ABC
from typing import Any, Self


class PrintProduct:
    def __init__(self) -> None:
        self.print_product()

    def print_product(self) -> None:
        print(f"[{self.__class__.__name__} created]:  {self.__dict__}")


class BaseProduct(ABC):
    @classmethod
    def new_product(cls, product_dict: dict):
        pass


class Product(BaseProduct, PrintProduct):
    """класс Товар"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Self) -> Any:
        if type(self) is type(other):
            return self.quantity * self.price + other.quantity * other.price
        else:
            raise TypeError

    @classmethod
    def new_product(cls, product_dict: dict) -> Self:
        return cls(**product_dict)

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


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.germination_period = germination_period
        self.color = color
        self.country = country
