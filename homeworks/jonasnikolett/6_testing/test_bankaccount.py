import pytest
from bankaccount import BankAccount


@pytest.fixture
def bankaccount_0():
    return BankAccount("Xaver")

@pytest.fixture
def bankaccount_100():
    return BankAccount("Julia",1500)

def test_bankaccount_create(bankaccount_0,bankaccount_100):
    with pytest.raises(InvalidBankaccountOwner):
        BankAccount("",100)
        BankAccount(" ")
    with pytest.raises(BalanceNotPositiveError):
        BankAccount("X",-1)
    with pytest.raises(TypeError):
        BankAccount("X","a")

    assert bankaccount_0.owner == "Xaver"
    assert bankaccount_0.balance == 0
    assert bankaccount_100.owner == "Julia"
    assert bankaccount_100.balance == 1500

def test_deposit_positive_amounts(bankaccount_0,bankaccount_100):
    bankaccount_0.deposit(500)
    bankaccount_100.deposit(100)
    assert bankaccount_0.balance == 500
    assert bankaccount_100.balance == 200

def test_deposit_non_positive_amounts(bankaccount_0,bankaccount_100):
    
    with pytest.raises(ValueError):
        bankaccount_0.deposit(0)
        bankaccount_100.deposit(-2)
    
    with pytest.raises(TypeError):
        bankaccount_0.deposit("a")


@pytest.mark.parametrize("amount, expected_exception", [
    (0,ValueError),
    (-100, ValueError),
    (1500, ValueError),
    ("string", TypeError),
    ([100], TypeError)
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
        account1.transfer(50, "Xaver")

def test_transfer_insufficient_funds(account1, account2):
    with pytest.raises(ValueError):
        account1.transfer(1500, account2)

def test_transfer_to_self(account1):
    with pytest.raises(TypeError):
        account1.transfer(500, account1)
