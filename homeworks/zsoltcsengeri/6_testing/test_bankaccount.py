import pytest
from bankaccount import BankAccount


# Fixture for bankaccount1 account
@pytest.fixture
def bankaccount_1():
    # A BankAccount for Zsolt with $100 balance
    return BankAccount("Zsolt", 100)


# Fixture for bankaccount2 account
@pytest.fixture
def bankaccount_2():
    # A BankAccount for Maryna with $50 balance
    return BankAccount("Maryna", 50)


# Test for valid deposit
def test_deposit(bankaccount_1, bankaccount_2):
    bankaccount_1.deposit(600)
    bankaccount_2.deposit(200)
    assert bankaccount_1.balance == 700
    assert bankaccount_2.balance == 250


# Parametrized test for invalid deposit inputs
@pytest.mark.parametrize(
    "amount, expected_exception",
    [
        (-100, ValueError),  # negative deposit
        (0, ValueError),  # zero deposit
    ],
)
def test_deposit_invalid_input(
    bankaccount_1, bankaccount_2, amount, expected_exception
):
    with pytest.raises(expected_exception):
        bankaccount_1.deposit(amount)
        bankaccount_2.deposit(amount)
