import pytest
import sys
import os

# Hozzáadjuk a homeworks/nemethmate/6_testing mappát az import útvonalhoz
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from bankaccount import BankAccount  # Importáljuk a BankAccount osztályt

# Fixture 1: Egy teszt BankAccount objektumot adunk vissza
@pytest.fixture
def account1():
    return BankAccount(owner="John Doe", balance=1000.0)

# Fixture 2: Egy másik teszt BankAccount objektumot adunk vissza
@pytest.fixture
def account2():
    return BankAccount(owner="Jane Smith", balance=500.0)

# Teszt: nem numerikus balance (egyenleg) a konstruktorban
def test_invalid_initial_balance():
    # Ha nem számot adunk meg, TypeError-t kell dobni
    with pytest.raises(TypeError, match="Balance must be a number."):
        BankAccount(owner="Invalid Owner", balance="1000")

# Teszt: nem numerikus deposit (betét) összeg
def test_invalid_deposit(account1):
    # Ha nem számot próbálunk betenni, TypeError-t kell dobni
    with pytest.raises(TypeError, match="Deposit amount must be a number."):
        account1.deposit("invalid")

# Teszt: nem numerikus withdraw (kivétel) összeg
def test_invalid_withdraw(account1):
    # Ha nem számot próbálunk kivenni, TypeError-t kell dobni
    with pytest.raises(TypeError, match="Withdraw amount must be a number."):
        account1.withdraw("invalid")

# Teszt: nem BankAccount típusú objektumnak pénz küldése
def test_transfer_to_non_account(account1):
    # Ha nem BankAccount objektumnak próbálunk pénzt küldeni, TypeError-t kell dobni
    with pytest.raises(TypeError, match="Target must be a BankAccount instance."):
        account1.transfer(200, "not_a_bank_account")

# Teszt: saját magunknak pénz küldése
def test_transfer_to_self(account1):
    # Ha a saját számlánkra próbálunk pénzt küldeni, ValueError-t kell dobni
    with pytest.raises(ValueError, match="You cannot transfer money to the same account."):
        account1.transfer(200, account1)

# Teszt: transfer túl alacsony összeggel
def test_transfer_negative_amount(account1, account2):
    # Ha a transfer összeg negatív, ValueError-t kell dobni
    with pytest.raises(ValueError, match="Transfer amount must be positive."):
        account1.transfer(-100, account2)

# Teszt: túl alacsony withdraw (kivétel) összeg
def test_zero_withdraw(account1):
    # Ha nulla összeggel próbálunk pénzt kivenni, ValueError-t kell dobni
    with pytest.raises(ValueError, match="Withdraw amount must be positive."):
        account1.withdraw(0)

# Teszt: negatív withdraw (kivétel) összeg
def test_negative_withdraw(account1):
    # Ha negatív összeggel próbálunk pénzt kivenni, ValueError-t kell dobni
    with pytest.raises(ValueError, match="Withdraw amount must be positive."):
        account1.withdraw(-50)

# Teszt: transfer, amikor nincs elég pénz
def test_transfer_insufficient_funds(account1, account2):
    # Ha a számlánkon nincs elég pénz, ValueError-t kell dobni
    with pytest.raises(ValueError, match="Insufficient funds."):
        account1.transfer(2000, account2)
