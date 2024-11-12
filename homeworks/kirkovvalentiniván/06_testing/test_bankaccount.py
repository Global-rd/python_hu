import pytest
from bankaccount import BankAccount
from unittest.mock import patch

@pytest.fixture
def bankaccount_1():
    return BankAccount("David", 200)

@pytest.fixture
def bankaccount_2():
    return BankAccount("Emma", 550)

@pytest.fixture
def invalid_bankaccount():
    return BankAccount("Invalid Account", -100)

@pytest.mark.parametrize("deposit_amount, expected_balance, expected_exception", [
    (30, 230, None), #normal case
    (0, 200, ValueError), #Error: adding zero to the actual balance 
    (-30, 200, ValueError) #Error: adding negative number to the actual balance
])

def test_deposit(bankaccount_1, deposit_amount, expected_balance, expected_exception):
    if expected_exception:
        with pytest.raises(expected_exception):
            bankaccount_1.deposit(deposit_amount)
    else:
        bankaccount_1.deposit(deposit_amount)
        assert bankaccount_1.get_balance() == expected_balance

def test_withdraw(bankaccount_1):
    bankaccount_1.withdraw(50)
    assert bankaccount_1.get_balance() == 150

    with pytest.raises(ValueError):
        bankaccount_1.withdraw(2000)

    with pytest.raises(ValueError):
        bankaccount_1.withdraw(0)

def test_transfer(bankaccount_1, bankaccount_2):
    with pytest.raises(TypeError):
        bankaccount_1.transfer(50, "not a bank account")

    assert bankaccount_1.get_balance() ==150
    assert bankaccount_2.get_balance() ==600

def test_transfer_to_self(bankaccount_1):
    initial_balance = bankaccount_1.get_balance()

    bankaccount_1.transfer(50, bankaccount_1)
    assert bankaccount_1.get_balance() == initial_balance
