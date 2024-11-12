import pytest
from bankaccount import BankAccount

@pytest.fixture
def empty_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account_1():
    account_1 = BankAccount(owner= "Zsóka", balance= 50000)
    return account_1

@pytest.fixture
def bank_account_2():
    account_2 = BankAccount(owner= "Csenge", balance= 1000)
    return account_2

@pytest.mark.parametrize("amount, expected_exception", [
    (-10000, ValueError), #negative amount
    (0, ValueError), #zero amount
])
def test_deposit_invalid_input(empty_bank_account, amount, expected_exception):
    with pytest.raises(expected_exception):
        empty_bank_account.deposit(amount)

def test_valid_transfer(bank_account_1, bank_account_2):
    bank_account_1.transfer(1000, bank_account_2)
    assert bank_account_1.get_balance() == 49000
    assert bank_account_2.get_balance() == 2000

def test_invalid_transfer(bank_account_1):
    with pytest.raises(TypeError):
        bank_account_1.transfer(4000, "bank_account")
    