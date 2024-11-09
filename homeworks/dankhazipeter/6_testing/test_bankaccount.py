import pytest
from bankaccount import BankAccount


@pytest.fixture
def account_1():
    return BankAccount("Alice", 100.0)


@pytest.fixture
def account_2():
    return BankAccount("Bob", 50.0)


def test_initial_balance(account_1):
    assert account_1.get_balance() == 100.0


def test_deposit(account_1):
    account_1.deposit(50.0)
    assert account_1.get_balance() == 150.0


@pytest.mark.parametrize("amount, expected_exception", [
    (0, ValueError),
    (-10, ValueError)
])
def test_deposit_invalid(amount, expected_exception, account_1):
    with pytest.raises(expected_exception):
        account_1.deposit(amount)


def test_withdraw(account_1):
    account_1.withdraw(50.0)
    assert account_1.get_balance() == 50.0


@pytest.mark.parametrize("amount, expected_exception", [
    (0, ValueError),
    (-10, ValueError),
    (200, ValueError)
])
def test_withdraw_invalid(amount, expected_exception, account_1):
    with pytest.raises(expected_exception):
        account_1.withdraw(amount)


def test_transfer(account_1, account_2):
    account_1.transfer(50.0, account_2)
    assert account_1.get_balance() == 50.0
    assert account_2.get_balance() == 100.0


def test_transfer_invalid_target(account_1):
    with pytest.raises(TypeError):
        account_1.transfer(50.0, "not_a_bank_account")


def test_transfer_insufficient_funds(account_1, account_2):
    with pytest.raises(ValueError):
        account_1.transfer(200.0, account_2)
