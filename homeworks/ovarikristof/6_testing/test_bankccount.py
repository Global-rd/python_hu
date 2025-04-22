import pytest
from bankaccount import BankAccount  # Importáljuk a BankAccount osztályt, amelyet tesztelni fogunk

# Fixtures létrehozása két különböző BankAccount példányhoz
@pytest.fixture
def account1():
    return BankAccount("Alice", 500.0)

@pytest.fixture
def account2():
    return BankAccount("Bob", 300.0)

# Deposit method tesztelése különböző inputokkal, hogy biztosítsuk az elvárt viselkedést
@pytest.mark.parametrize("amount, expected_exception", [
    (0, ValueError),           # Ha a deposit amount 0, ValueError-t várunk
    (-50, ValueError),         # Negatív deposit esetén is ValueError-ra számítunk
])
def test_deposit_invalid_amount(account1, amount, expected_exception):
    with pytest.raises(expected_exception):
        account1.deposit(amount)

# Érvényes befizetés tesztelése
def test_deposit_valid_amount(account1):
    account1.deposit(100)
    assert account1.get_balance() == 600.0  # Az egyenlegnek 600-nak kell lennie

# Withdraw method tesztelése különböző inputokkal
@pytest.mark.parametrize("amount, expected_exception", [
    (0, ValueError),           # Ha a withdraw amount 0, ValueError-t várunk
    (-50, ValueError),         # Negatív withdraw esetén is ValueError-ra számítunk
    (600, ValueError),         # Több mint a rendelkezésre álló egyenleg esetén ValueError-ra számítunk
])
def test_withdraw_invalid_amount(account1, amount, expected_exception):
    with pytest.raises(expected_exception):
        account1.withdraw(amount)

# Érvényes kifizetés tesztelése
def test_withdraw_valid_amount(account1):
    account1.withdraw(200)
    assert account1.get_balance() == 300.0  # Az egyenlegnek 300-nak kell lennie

# Transfer method tesztelése, hogy a megfelelő exception raise-elődik-e nem BankAccount célra
def test_transfer_invalid_target(account1):
    with pytest.raises(TypeError):
        account1.transfer(100, "not_a_bank_account")  # Nem BankAccount objektum, TypeError-ra számítunk

# Transfer method érvényes esetének tesztelése
def test_transfer_valid_amount(account1, account2):
    account1.transfer(200, account2)
    assert account1.get_balance() == 300.0  # Az account1 egyenlegének 300-nak kell lennie
    assert account2.get_balance() == 500.0  # Az account2 egyenlegének 500-nak kell lennie

# Balance ellenőrzés, hogy az alapértelmezett érték megfelelő
def test_initial_balance():
    account = BankAccount("Charlie")
    assert account.get_balance() == 0.0  # Az alapértelmezett balance-nak 0.0-nak kell lennie

# Exception tesztelése negatív kezdeti egyenleg esetén
def test_initial_negative_balance():
    with pytest.raises(ValueError):
        BankAccount("Charlie", -100)  # Negatív egyenleg nem megengedett

# __str__ method tesztelése
def test_str_method(account1):
    assert str(account1) == "Account owner: Alice, Balance: 500.00"  # A __str__ method outputjának ezt kellene adnia
