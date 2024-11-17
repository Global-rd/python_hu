class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
    
    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def transfer(self, amount: float, target_account: 'BankAccount'):
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount instance.")
        self.withdraw(amount)
        target_account.deposit(amount)
    
    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance:.2f}"




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

# Test withdraw
def test_withdraw(account1):
    account1.withdraw(50)
    assert account1.get_balance() == 50.0

def test_withdraw_invalid(account1):
    with pytest.raises(ValueError, match="Withdraw amount must be positive."):
        account1.withdraw(0)
    with pytest.raises(ValueError, match="Insufficient funds."):
        account1.withdraw(200)

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