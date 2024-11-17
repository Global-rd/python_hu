import pytest
from bank_account import BankAccount

# Fixtures
@pytest.fixture
def account1():
    return BankAccount("Alice", 100.0)

@pytest.fixture
def account2():
    return BankAccount("Bob", 50.0)

# Test deposit with parameterize
@pytest.mark.parametrize("amount", [0, -50])
def test_deposit_invalid(account1, amount):
    with pytest.raises(ValueError, match="Deposit amount must be positive."):
        account1.deposit(amount)

# Test withdraw with parameterize 
@pytest.mark.parametrize("amount, expected_balance", [ 
    (50, 50.0), 
    (100, 0.0), 
]) 
def test_withdraw(account1, amount, expected_balance): 
    account1.withdraw(amount) 
    assert account1.get_balance() == expected_balance 

@pytest.mark.parametrize("amount, exception, message", [ 
    (0, ValueError, "Withdraw amount must be positive."), 
    (200, ValueError, "Insufficient funds."), 
]) 
def test_withdraw_invalid(account1, amount, exception, message): 
    with pytest.raises(exception, match=message): 
        account1.withdraw(amount)

# Test transfer with valid accounts
def test_transfer_valid(account1, account2):
    account1.transfer(30, account2)
    assert account1.get_balance() == 70
    assert account2.get_balance() == 80

# Test transfer with invalid target
def test_transfer_invalid_target(account1):
    with pytest.raises(TypeError, match="Target must be a BankAccount instance."):
        account1.transfer(30, "not_a_bank_account")

# Test initial balance
def test_initial_balance_invalid():
    with pytest.raises(ValueError, match="Initial balance cannot be negative."):
        BankAccount("Charlie", -100)

# Test valid deposit
def test_deposit_valid(account1):
    account1.deposit(50)
    assert account1.get_balance() == 150.0

    