import pytest
from bankaccount import BankAccount

@pytest.mark.parametrize("owner, balance, error", [
    ("Barnabas", -110, ValueError),
    (None, "Zero", TypeError),
    # ("Christina", 4/3, ValueError) -> Nincs raiselve???
])
def test__init__(owner, balance, error):
    with pytest.raises(error):
        BankAccount(owner=owner, balance=balance)

@pytest.fixture
def empty_account():
    return BankAccount()

@pytest.fixture
def own_account():
    account = BankAccount(owner="Peter", balance=500)
    return account

@pytest.fixture
def outher_account():
    accounnt = BankAccount(owner="Anna", balance=0)
    return accounnt

def test_deposit(own_account):
    own_account.deposit(500)
    assert own_account.balance == 1000

@pytest.mark.parametrize("amount, error", [
    (-100, ValueError),
    (0, ValueError),
    ("Zero", TypeError)
])
def test_deposit_with_parametrize(own_account, amount, error):
    with pytest.raises(error):
        own_account.deposit(amount)

def test_withdraw(own_account):
    own_account.withdraw(500)
    assert own_account.balance == 0

@pytest.mark.parametrize("amount, error", [
    (600, ValueError),
    (-100, ValueError),
    ("Total balance", TypeError) 
])
def test_withdrow_with_parametrize(own_account, amount, error):
    with pytest.raises(error):
        own_account.withdraw(amount=amount)

def test_transfer(own_account, outher_account):
    own_account.transfer(amount=500, target_account=outher_account)
    assert own_account.balance == 0
    assert outher_account.balance ==500
    outher_account.transfer(amount=200, target_account=own_account)
    assert outher_account.balance == 300
    assert own_account.balance == 200
    own_account.transfer(amount=200, target_account=own_account)
    assert own_account.balance == 200

#def test_transfet_to_invalid_bankaccount(own_account):
#    assert own_account.transfer(amount=200, target_account="Elon Musk") == pytest.raises(TypeError)
# -> pénz küldése nem BankAccount object -> pass :(

@pytest.mark.parametrize("amount, error", [
    (600, ValueError), # többet utal mint a keret
    (-300, ValueError) # negatív összeget utal
])
def test_transfer_with_parametrize(own_account, outher_account, amount, error):
    with pytest.raises(error):
        own_account.transfer(amount=amount, target_account=outher_account)

def test_get_balance(own_account):
    own_account.get_balance()
