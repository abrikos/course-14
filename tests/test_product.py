import pytest

from src.product import Product


@pytest.fixture
def product_1():
    return Product('a','b',1,2)

def test_init(product_1):
    assert product_1.name == 'a'
    assert product_1.description == 'b'
    assert product_1.quantity == 2
    assert product_1.price == 1