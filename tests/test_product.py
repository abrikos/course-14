from typing import Any
from unittest.mock import patch

import pytest

from src.product import LawnGrass, Product, Smartphone


@pytest.fixture
def product_1() -> Product:
    return Smartphone("a", "b", 1, 2, 22, "zzz", 3, "red")


@pytest.fixture
def product_2() -> Product:
    return LawnGrass("a", "b", 1, 2, "RRR", "zzz", "grr")


@pytest.fixture
def product_3() -> Product:
    return Smartphone("aAA", "bbb", 12, 22, 222, "zzz2222", 32, "red222")


def test_new_product() -> None:
    prod = Product.new_product({"name": "aaaa", "description": "bbbbb", "price": 10, "quantity": 20})
    assert str(prod) == "aaaa, 10 руб. Остаток: 20 шт."


def test_str(product_1: Product) -> None:
    assert str(product_1) == "a, 1 руб. Остаток: 2 шт."


def test_add(product_1: Product, product_3: Product) -> None:
    assert product_1 + product_3 == 266


def test_wrong_add(product_1: Smartphone, product_2: LawnGrass) -> None:
    with pytest.raises(TypeError, match='Only same types allowed'):
        product_1 + product_2

def test_zero_quantity() -> None:
    with pytest.raises(ValueError, match='Товар с нулевым количеством не может быть добавлен'):
        Smartphone("aAA", "bbb", 12, 0, 222, "zzz2222", 32, "red222")


def test_print_product(capsys: Any) -> None:
    Product.new_product({"name": "ZZZZ", "description": "bbbbb", "price": 10, "quantity": 20})
    captured = capsys.readouterr()
    assert (
        captured.out
        == "[Product created]:  {'name': 'ZZZZ', 'description': 'bbbbb', '_Product__price': 10, 'quantity': 20}\n"
    )


def test_init(product_1: Product) -> None:
    assert product_1.name == "a"
    assert product_1.description == "b"
    assert product_1.quantity == 2
    assert product_1.price == 1


def test_add_product(product_2: Product) -> None:
    assert product_2.name == "a"
    assert product_2.description == "b"
    assert product_2.quantity == 2
    assert product_2.price == 1


@patch("builtins.input")
def test_price(mock_data: Any, product_1: Product) -> None:
    product_1.price = 0
    assert product_1.price == 1
    product_1.price = -2
    assert product_1.price == 1
    product_1.price = 4
    assert product_1.price == 4
    mock_data.return_value = "y"
    product_1.price = 0.5
    assert product_1.price == 0.5


@patch("builtins.input")
def test_price_no(mock_data: Any, product_1: Product) -> None:
    mock_data.return_value = "n"
    product_1.price = 0.5
    assert product_1.price == 1
