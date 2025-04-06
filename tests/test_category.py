import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def category_1():
    p1 = Product('a','b',1,2)
    p2 = Product('a1','b1',1,2)
    return Category('a','b',[p1, p2])

def test_init(category_1):
    assert category_1.name == 'a'
    assert category_1.description == 'b'
    assert category_1.category_count == 1
    assert category_1.product_count ==2