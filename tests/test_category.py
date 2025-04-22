import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def category_1() -> Category:
    p1 = Product("a", "b", 1, 2)
    p2 = Product("a1", "b1", 1, 2)
    return Category("a", "b", [p1, p2])


def test_cat_str(category_1: Category) -> None:
    assert str(category_1) == "a, количество продуктов: 2 шт."


def test_cat_1(category_1: Category) -> None:
    assert category_1.name == "a"
    assert category_1.description == "b"
    assert category_1.category_count == 2
    assert category_1.product_count == 2


@pytest.fixture
def category_2() -> Category:
    p1 = Product("a", "b", 1, 2)
    p2 = Product("a1", "b1", 1, 2)
    category = Category("a", "b", [])
    category.add_product(p1)
    category.add_product(p2)
    return category


def test_cat_2(category_2: Category) -> None:
    assert category_2.name == "a"
    assert category_2.description == "b"
    assert category_2.category_count == 3
    assert category_2.product_count == 2


def test_cat_props(category_2: Category) -> None:
    assert category_2.products == ["a, 1 руб. Остаток 2 шт.", "a1, 1 руб. Остаток 2 шт."]


def test_wrong_add(category_2: Category) -> None:
    try:
        category_2.add_product("String")
        assert False
    except TypeError:
        assert True
