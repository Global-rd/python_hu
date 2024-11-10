import pytest

from bankaccount import BankAccount

@pytest.fixture
def ures_account():
    return BankAccount("Marty McFly")

@pytest.fixture
def account_egyenleggel():
    return BankAccount("Egon Spengler", 1000)

@pytest.mark.parametrize("osszeg", [0, -10])
def test_befizetes_ervenytelen_osszeg(osszeg, ures_account):
    with pytest.raises(ValueError):
        ures_account.deposit(osszeg)

def test_kivetel(ures_account):
    with pytest.raises(ValueError):
        ures_account.withdraw(100)

def test_utalas(ures_account):
    with pytest.raises(TypeError):
        ures_account.transfer(100, "Nincs számla")

def test_utalas_nincs_penz(ures_account, account_egyenleggel):
    with pytest.raises(ValueError):
        account_egyenleggel.transfer(2000, ures_account)

def test_negativ_egyenleg():
    with pytest.raises(ValueError, match="Az egyenleg nem lehet negatív!"):
        BankAccount("Imi", -10.0)