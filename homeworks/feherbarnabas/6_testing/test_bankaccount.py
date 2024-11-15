import pytest
from bankaccount import BankAccount

#Test 1 - Creating objects
@pytest.fixture
def account_1():
    return BankAccount("Géza", 210.12)

@pytest.fixture 
def account_2():
    return BankAccount("Gergő", 30.50 )

#Test 2 - Deposit method() 
def test_balance(account_1):
    assert account_1.get_balance() == 210.12

def test_top_up(account_1):
    account_1.deposit(39.88)
    assert account_1.get_balance() == 250

def test_withdraw_valid(account_1):
    account_1.withdraw(50)
    assert account_1.get_balance() == 160.12
 
@pytest.mark.parametrize("amount, expected_exception", [
    (0,ValueError),
    (-1, ValueError),
    (220, ValueError),
    ("string", TypeError)
])

def test_withdraw_invalid_input(account_1, amount, expected_exception):
    with pytest.raises(expected_exception):
        account_1.withdraw(amount) 

def test_transfer(account_1, account_2):
    account_1.transfer(20, account_2)
    assert account_1.get_balance() == 190.12 and account_2.get_balance() == 50.50

#Test 3
def test_transfer_invalid_account(account_1):
    with pytest.raises(TypeError):
        account_1.transfer(10, "Dzsúlió")

#Test 4
def test_transfer_insufficient_funds(account_1, account_2):
    with pytest.raises(ValueError):
        account_1.transfer(220, account_2)

def test_transfer_to_self(account_1):
    with pytest.raises(TypeError):
        account_1.transfer(20, account_1)