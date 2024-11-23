#Homework 6. - Nagy Norbert
import pytest
from bankaccount import BankAccount
from bankaccount import InvalidBankaccountOwner
from bankaccount import BalanceNotPositiveError
from bankaccount import SameBankAccountsError

@pytest.fixture
def bankaccount_0():
    return BankAccount("Aladar")

@pytest.fixture
def bankaccount_100():
    return BankAccount("Bela",100)

def test_bankaccount_create(bankaccount_0,bankaccount_100):
    with pytest.raises(InvalidBankaccountOwner):
        BankAccount("",100)
        BankAccount(" ")
    with pytest.raises(BalanceNotPositiveError):
        BankAccount("X",-1)
    with pytest.raises(TypeError):
        BankAccount("X","a")

    assert bankaccount_0.owner == "Aladar"
    assert bankaccount_0.balance == 0
    assert bankaccount_100.owner == "Bela"
    assert bankaccount_100.balance == 100

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

@pytest.mark.parametrize("bankaccount_owner, balance, withdraw_amount, expected_exception",[
    ("TT",100,200,ValueError), #withdrawal_amount > balance
    ("TT",100,-5,ValueError), #ithdrawal_amount < 0
    ("TT",100,"test",TypeError), #ithdrawal_amount < 0
])

def test_withdraw_errors(bankaccount_owner,balance,withdraw_amount,expected_exception):
    with pytest.raises(expected_exception):
        ac = BankAccount(bankaccount_owner,balance)
        ac.withdraw(withdraw_amount)

@pytest.mark.parametrize("bankaccount_owner, balance, withdraw_amount,expected_balance",[
    ("TT",100,1,99),
    ("TI",100,0,100),
    ("TJ",100,100,0),
    ("TK",415,4.5,410.5),
    ("TL",0,0,0),
])

def test_withdraw_success(bankaccount_owner,balance,withdraw_amount,expected_balance):
    ac = BankAccount(bankaccount_owner,balance)
    ac.withdraw(withdraw_amount)
    assert ac.get_balance() == expected_balance

def test_money_transfer(bankaccount_0,bankaccount_100):
    with pytest.raises(TypeError):
        bankaccount_100.transfer(10,"string")
        bankaccount_100.transfer("test",bankaccount_0)
    bankaccount_100.transfer(10,bankaccount_0)
    assert bankaccount_100.get_balance() == 90
    assert bankaccount_0.get_balance() == 10
    with pytest.raises(SameBankAccountsError):
        bankaccount_100.transfer(10,bankaccount_100)
