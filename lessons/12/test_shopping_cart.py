import pytest
from shopping_cart import ShoppingCart
from unittest.mock import patch


@pytest.fixture
def empty_cart():
    return ShoppingCart()

@pytest.fixture
def cart_with_items():
    cart = ShoppingCart()
    cart.add_item("apple", 1, 3)
    cart.add_item("banana", 0.5, 5)
    return cart

def test_add_item(empty_cart):
    
    empty_cart.add_item("apple", 1, 2)
    assert empty_cart.items["apple"]["quantity"] == 2
    assert empty_cart.items["apple"]["price"] == 1


@pytest.mark.parametrize("item_name, price, quantity, expected_exception", [
    ("orange", -1, 1, ValueError), #negative price
    ("orange", 1, 0, ValueError), #zero quantity
    ("orange", 1, -2, ValueError), #negative quantity
])
def test_add_item_invalid_input(empty_cart, item_name, price, quantity, expected_exception):
    with pytest.raises(expected_exception):
        empty_cart.add_item(item_name, price, quantity)



@patch('shopping_cart.ShoppingCart.apply_discount', return_value=4.4)
def test_checkout(mock_apply_discount, cart_with_items):
    final_price = cart_with_items.checkout("SAVE10")

    assert final_price == 4.4
    mock_apply_discount.assert_called_once_with("SAVE10")