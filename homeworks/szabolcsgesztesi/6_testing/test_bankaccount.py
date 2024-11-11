import pytest
from bankaccount import BankAccount

# Tesztelés fixture-el
@pytest.fixture
def account_1():
    return BankAccount("Alice", 100.0)

@pytest.fixture
def account_2():
    return BankAccount("Bob", 50.0)

# Teszt parametrize-al
@pytest.mark.parametrize("amount, expected_exception", [
    (0, ValueError),  # ValueError 0-ával
    (-50, ValueError),  # Negatív számmal
    (20, None)  # Helyes összeggel
])
def test_deposit(account_1, amount, expected_exception):
    if expected_exception:
        with pytest.raises(expected_exception):
            account_1.deposit(amount)
    else:
        initial_balance = account_1.get_balance()
        account_1.deposit(amount)
        assert account_1.get_balance() == initial_balance + amount

# Teszt túl nagy felvett összegre
def test_withdraw_insufficient_funds(account_1):
    with pytest.raises(ValueError, match="Insufficient funds."):
        account_1.withdraw(200)

# Teszt helytelen bankszámlára
def test_transfer_to_non_bank_account(account_1):
    with pytest.raises(TypeError, match="Target must be a BankAccount instance."):
        account_1.transfer(50, "Not a BankAccount")

# Test helytelen felvett összegre
def test_withdraw_negative_amount(account_1):
    with pytest.raises(ValueError, match="Withdraw amount must be positive."):
        account_1.withdraw(-20)

# Teszt sikeres átutalásra
def test_successful_transfer(account_1, account_2):
    amount = 30
    initial_balance_1 = account_1.get_balance()
    initial_balance_2 = account_2.get_balance()
    
    account_1.transfer(amount, account_2)
    
    assert account_1.get_balance() == initial_balance_1 - amount
    assert account_2.get_balance() == initial_balance_2 + amount

# Lekértezés tesztje
def test_get_balance(account_1):
    assert account_1.get_balance() == 100.0

# Teszt __str__ method-ra
def test_str_method(account_1):
    assert str(account_1) == "Account owner: Alice, Balance: 100.00"