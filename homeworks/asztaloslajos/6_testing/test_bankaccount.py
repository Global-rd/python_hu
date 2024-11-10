import pytest
from bankaccount import BankAccount

#test 1
@pytest.fixture
def test1_account():
    return BankAccount("Számla1", 2000.0)

@pytest.fixture
def test2_account():
    return BankAccount("Számla2", 1000.0)

#test2
@pytest.mark.parametrize("deposit, expected_exception", [
    (0.0, ValueError), #zero deposit
    (-1000.0, ValueError), #negative deposit
])
def test_deposit_invalid_input(test1_account,deposit,expected_exception):
    with pytest.raises(expected_exception):
        test1_account.deposit(deposit)

def test_transfer(test1_account,test2_account):
    test1_account.transfer(1000.0, test2_account)
    assert test1_account.balance == 1000.0 and test2_account.balance == 2000.0

#test3
def test_use_bankaccount_instance(test1_account):
    test3_account = "valami"
    test1_account.transfer(1.0, test3_account)    

#test4
def test_withdraw_insufficient_amount(test2_account):
    test2_account.withdraw(2000.0)

def test_transfer_insufficient_amount(test1_account,test2_account):
    test2_account.transfer(2000.0,test1_account)



