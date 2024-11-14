import pytest
from bankaccount import BankAccount


@pytest.fixture
def empty_bank_account():
    return BankAccount("Tom", 0)

@pytest.fixture
def bank_account_with_deposit():
    return BankAccount("Joe", 500)

def test_current_account_balance():
    if BankAccount is empty_bank_account:
        assert empty_bank_account.get_balance() == 0
    if BankAccount is bank_account_with_deposit:
        assert bank_account_with_deposit.get_balance() == 500
 
def test_add_deposit_with_zero_balance(empty_bank_account):
    empty_bank_account.deposit(250)
    assert empty_bank_account.get_balance() == 250

def test_withdraw_from_banck_account_with_deposit(bank_account_with_deposit):
    bank_account_with_deposit.withdraw(300)
    assert bank_account_with_deposit.get_balance() == 200

def test_transfer(bank_account_with_deposit, empty_bank_account):
    bank_account_with_deposit.transfer(100, empty_bank_account)
    assert empty_bank_account.get_balance() == 100

@pytest.mark.parametrize("amount, expected_error", [
    (-1, ValueError), # Deposit amount must be positive.
    (0, ValueError), # Deposit amount must be positive. Other than 0
    ("ten", TypeError) # Deposit amount must be numeric. 
])

def test_invalid_amount_of_deposit(bank_account_with_deposit, amount, expected_error):
    with pytest.raises(expected_error):
        bank_account_with_deposit.deposit(amount)

@pytest.mark.parametrize("amount, expected_error",[
    (-50, ValueError), # Withdraw amount must be positive.
    (200, ValueError), #Insufficient funds
    ("ten", TypeError) # Withdraw amount must be numeric. 
]) 

def test_withdraw_errors(empty_bank_account, amount, expected_error):
        with pytest.raises(expected_error):
            empty_bank_account.withdraw(amount)

@pytest.mark.parametrize("owner,balance, expected_error", [
    ("Jill",-100, ValueError)
])
def test_initial_balance_error(owner, balance, expected_error):
    with pytest.raises (expected_error):
        BankAccount(owner, balance)

@pytest.mark.parametrize("amount, target_account, expected_error", [
    (100, "fakeaccount",  TypeError), # Target must be a BankAccount instance
    (100, bank_account_with_deposit, TypeError), # You cannot have the same account for initiate and receive transfer
    ("ten", empty_bank_account, TypeError), # Please use numeric values for amount for transfer
    (-100, empty_bank_account, TypeError), # Please add a positive amount for transfer
    (0,empty_bank_account, TypeError), # Please add a positive amount for transfer. Other than 0
    (1000, empty_bank_account, TypeError), #Insufficient fund for transfer
])

def test_transfer_errors(amount, target_account, expected_error):
    with pytest.raises(expected_error):
        BankAccount.transfer(bank_account_with_deposit,amount, target_account)




    