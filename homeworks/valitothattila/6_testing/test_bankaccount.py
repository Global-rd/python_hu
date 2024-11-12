import pytest
from unittest.mock import patch
from bankaccount import BankAccount

@pytest.fixture
def P_account():
    return BankAccount("Peter")
   
def test_deposit(P_account):
    assert P_account.balance == 0.0
    P_account.deposit(20.0)
    assert P_account.balance == 20.0

@pytest.fixture
def R_account():
    return BankAccount("Robi",200)
    
def test_owner(R_account):
    assert R_account.owner == "Robi"

def test_withdraw(R_account):
    R_account.withdraw(20)
    assert R_account.owner == "Robi"
    assert R_account.balance == 180

@pytest.mark.parametrize("amount, expected_exception", [
    (-100.0, ValueError),
])                   #negative balance
    
def invalid_withdraw_value(R_account, amount, expected_exception):
    with pytest.raises(expected_exception):
        #R_account = BankAccount(owner, balance)
        R_account.withdraw(amount)   





