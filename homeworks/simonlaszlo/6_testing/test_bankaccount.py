
import pytest
from  bankaccount import BankAccount

@pytest.fixture
def account1():
    return BankAccount("Judit", 100)

@pytest.fixture
def account2():
    return BankAccount("Aniko", 50)

def test_initial_balance(account1):
    assert account1.get_balance() == 100

def test_deposit_valid(account1):
    account1.deposit(50)
    assert account1.get_balance() == 150

@pytest.mark.parametrize("amount, expected_exception", [
    (0, ValueError),
    (-10, ValueError),
    ("string", TypeError),
    ([10], TypeError)
])

def test_deposit_exceptions(account1, amount, expected_exception):
    with pytest.raises(expected_exception):
        account1.deposit(amount)

def test_withdraw_valid(account1):
    account1.withdraw(50)
    assert account1.get_balance() == 50

@pytest.mark.parametrize("amount, expected_exception", [
    (0,ValueError),
    (-10, ValueError),
    (150, ValueError),
    ("string", TypeError),
    ([10], TypeError)
])

def test_withdraw_exceptions(account1, amount, expected_exception):
    with pytest.raises(expected_exception):
        account1.withdraw(amount)

def test_transfer_valid(account1, account2):
    account1.transfer(50, account2)
    assert account1.get_balance() == 50
    assert account2.get_balance() == 100

def test_transfer_invalid_account(account1):
    with pytest.raises(TypeError):
        account1.transfer(50, "Bela")

def test_transfer_insufficient_funds(account1, account2):
    with pytest.raises(ValueError):
        account1.transfer(150, account2)

def test_transfer_to_self(account1):
    with pytest.raises(TypeError):
        account1.transfer(50, account1)
