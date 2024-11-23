'''
6. házi feladat

Tesztelés
'''



import pytest
import sys
import os

'''
For the first test:

# Add root dir
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
helper_path = os.path.join(root_dir, "extra_tasks", "homework_06_helper")

# adding helper_path to sys.path
sys.path.insert(0, helper_path)

from bankaccount import BankAccount  
'''

from bankaccount_corrected import BankAccount

##################### TESTING #################### 


# Creating Fixtures
@pytest.fixture
def account_empty():
    return BankAccount("Owner1")

@pytest.fixture
def account_with_balance():
    return BankAccount("Owner2", 1000.0)

# TTest the deposit method with different inputs
@pytest.mark.parametrize("amount", [0, -100, -1])
def test_deposit_invalid_amount(account_empty, amount):
    with pytest.raises(ValueError, match="Deposit amount must be positive."):
        account_empty.deposit(amount)

# Test for the withdraw method to see if the Exception works correctly with a negative amount
def test_withdraw_invalid_amount(account_with_balance):
    with pytest.raises(ValueError, match="Withdraw amount must be positive."):
        account_with_balance.withdraw(-50)

# Test for edge cases: sending money to a non-BankAccount object
def test_transfer_invalid_target(account_with_balance):
    with pytest.raises(TypeError, match="Target must be a BankAccount instance."):
        account_with_balance.transfer(100, "Not a BankAccount")

# Test whether the transfer method throws an exception when trying to refer to itself
def test_transfer_to_self(account_with_balance):
    with pytest.raises(ValueError, match="Cannot transfer to the same account."):
        account_with_balance.transfer(100, account_with_balance)

# Extra error handling: handling non-numeric values for deposit
def test_deposit_non_numeric(account_empty):
    with pytest.raises(TypeError, match="Amount must be a number."):
        account_empty.deposit("not a number")
