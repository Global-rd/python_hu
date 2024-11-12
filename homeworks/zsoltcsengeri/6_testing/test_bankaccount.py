import pytest
from bankaccount import BankAccount

# Fixture for an empty account
@pytest.fixture
def empty_account():
    return BankAccount()

# Fixture for an account with initial balance
@pytest.fixture
def account_with_data():
    account = BankAccount("Zsolt", 100)
    return account

# Test for valid deposit
def test_deposit(account_with_data):
    account_with_data.deposit(600)
    assert account_with_data.balance == 700

# Parametrized test for invalid deposit inputs
@pytest.mark.parametrize(
    "amount, expected_exception",
    [
        (-100, ValueError),  # negative deposit
        (0, ValueError),     # zero deposit
    ],
)
def test_deposit_invalid_input(account_with_data, amount, expected_exception):
    with pytest.raises(expected_exception):
        account_with_data.deposit(amount)
