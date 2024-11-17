"""
A unit testeknél a következőket vedd figyelembe:
    -   Írj legalább 2 fixture-t (2 különböző BankAccount object), amiket a tesztjeidben használsz.
    -   Írj legalább egy tesztet ami @pytest.mark.parametrize-t használ annak érdekében, hogy a tesztet több input-ra is lefuttassa 
        (pl: teszteld a deposit() method-ot pontosan 0 és negatív szám inputtal is).
    -   Tesztelj edge case-eket (pl: pénz küldése nem BankAccount object-nek).
    -   Írj teszteket amik arra irányulnak, hogy a megfelelő Exception raise-elődik- e a megadott input-ra.

"""



import pytest
from bankaccount import BankAccount


# BankAccount-ok hozzáadása
@pytest.fixture
def account1():
    return BankAccount("Alice", 1000)

@pytest.fixture
def account2():
    return BankAccount("Bob", 500)


# teszt deposit() method 
@pytest.mark.parametrize("amount, expected_balance", [
    (100, 1100),  # pozitív 
    (0, 1000),    # 0 
    (-100, 1000), # negatív 
])
def test_deposit(account1, amount, expected_balance):
    if amount <= 0:
        with pytest.raises(ValueError):
            account1.deposit(amount)
    else:
        account1.deposit(amount)
        assert account1.get_balance() == expected_balance


# teszt withdraw 
@pytest.mark.parametrize("amount, expected_balance, should_raise", [
    (200, 800, False),        # helyes 
    (0, 1000, True),          # 0, hiba
    (-200, 1000, True),       # negatív, hiba
    (1500, 1000, True),       # több mint a balance, hiba
])
def test_withdraw(account1, amount, expected_balance, should_raise):
    if should_raise:
        with pytest.raises(ValueError):
            account1.withdraw(amount)
    else:
        account1.withdraw(amount)
        assert account1.get_balance() == expected_balance
        

# teszt transfer
def test_transfer(account1, account2):
    # jó tranzakció
    account1.transfer(200, account2)
    assert account1.get_balance() == 800
    assert account2.get_balance() == 700

    # pénz küldése nem BankAccount object-nek
    with pytest.raises(TypeError):
        account1.transfer(100, "not_a_bank_account")
    
    # nincs elég pénz
    with pytest.raises(ValueError):
        account1.transfer(1000, account2)


# teszt, negatív egyenleg
def test_negative_balance():
    with pytest.raises(ValueError):
        BankAccount("Invalid", -100)


