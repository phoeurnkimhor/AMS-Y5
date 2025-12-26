import pytest
from unittest.mock import Mock
from shopping_cart import Cart, CartFullError


@pytest.fixture
def sample_cart():
    """Fixture to create a new cart with 3 capacity."""
    return Cart(capacity=3)

def test_add_item(sample_cart):
    sample_cart.add_item("Apple", 2)
    sample_cart.add_item("Banana", 3)
    assert len(sample_cart.items) == 2
    assert sample_cart.items[0] == ("Apple", 2)


def test_total_price(sample_cart):
    sample_cart.add_item("Apple", 2)
    sample_cart.add_item("Banana", 3)
    assert sample_cart.total_price() == 5


def test_cart_full_error(sample_cart):
    sample_cart.add_item("A", 1)
    sample_cart.add_item("B", 1)
    sample_cart.add_item("C", 1)
    with pytest.raises(CartFullError):
        sample_cart.add_item("D", 1)

def test_external_dependency_mock(sample_cart):
    price_fetcher = Mock(return_value=10)

    price = price_fetcher("Apple")
    sample_cart.add_item("Apple", price)

    assert sample_cart.total_price() == 10
    price_fetcher.assert_called_once_with("Apple")
