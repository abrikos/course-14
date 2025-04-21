from typing import Any
from unittest.mock import patch

import pytest

from src.product import Product


@pytest.fixture
def product_1() -> Product:
    return Product("a", "b", 1, 2)


@pytest.fixture
def product_2() -> Product:
    return Product.new_product({"name": "a", "description": "b", "price": 1, "quantity": 2})


@pytest.fixture
def product_3() -> Product:
    return Product.new_product({"name": "aaaa", "description": "bbbbb", "price": 10, "quantity": 20})


def test_str(product_1: Product) -> None:
    assert str(product_1) == "a, 1 руб. Остаток: 2 шт."


def test_add(product_1: Product, product_3: Product) -> None:
    assert product_1 + product_3 == 1 * 2 + 10 * 20


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
