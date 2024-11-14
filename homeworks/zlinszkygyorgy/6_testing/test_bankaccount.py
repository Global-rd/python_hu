import pytest
from bankaccount import BankAccount

# Creating fixtures
@pytest.fixture
def account_zero_balance():
    return BankAccount("Gyorgy")

@pytest.fixture
def account_with_balance():
    return BankAccount("Judit", 112.0)

# Parametrized test for testing deposit method
@pytest.mark.parametrize("amount, expected_exceptions", [
                         (0, ValueError),    # Zero deposit
                         (-20, ValueError)  # Negative deposit
                         ])
def test_deposit_invalid_amount(account_zero_balance, amount, expected_exceptions):
    with pytest.raises(expected_exceptions):
        account_zero_balance.deposit(amount)

# Edge case: transfer to non bank account
def test_transfer_to_non_bank_account(account_with_balance):
    with pytest.raises(TypeError):
        account_with_balance.transfer(25, "not a bank account")

# Testing exceptions
def test_withdraw_insufficient_fund(account_with_balance):
    with pytest.raises(ValueError):
        account_with_balance.withdraw(120)

def test_withdraw_negative_amount(account_with_balance):
    with pytest.raises(ValueError):
        account_with_balance.withdraw(-20)

# Testing deposit method
def test_deposit(account_zero_balance):
    account_zero_balance.deposit(10)
    assert account_zero_balance.get_balance() == 10

# Testing withdraw method
def test_withdraw(account_with_balance):
    account_with_balance.withdraw(50)
    assert account_with_balance.get_balance() == 62

# Testing transfer method
def test_transfer(account_with_balance, account_zero_balance):
    account_with_balance.transfer(50, account_zero_balance)
    assert account_with_balance.get_balance() == 62
    assert account_zero_balance.get_balance() == 50