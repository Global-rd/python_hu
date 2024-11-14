import pytest
from bankaccount import BankAccount

#--------------------------------- 1. tétel 2 fixture, 2 különböző BankAccount object

@pytest.fixture
def P_account():
    return BankAccount("Peter")
   
def test_deposit(P_account):
    assert P_account.balance == 0.0
    P_account.deposit(20.0)
    assert P_account.balance == 20.0

@pytest.fixture
def R_account():
    return BankAccount("Robi",200)

def test_withdraw(R_account):
    R_account.withdraw(20)
    assert R_account.owner == "Robi"
    assert R_account.balance == 180

@pytest.mark.parametrize("amount, expected_exception", [
    (-100.0, ValueError), #negative balance
])
    
def invalid_withdraw_value(R_account, amount, expected_exception):
    with pytest.raises(expected_exception):
        R_account.withdraw(amount)

 #--------------------------------- 2. tétel deposit() teszteld method-ot pontosan 0 és negatív szám inputtal
@pytest.fixture
def P_account():
    return BankAccount("Peti", 100.0)

@pytest.mark.parametrize("deposit_amount, expected_exception", [
    (-10.0, ValueError),      # Negatív összeg
    (0.0, ValueError),        # Nulla összeg
])
def test_deposit(P_account, deposit_amount, expected_exception):
        with pytest.raises(expected_exception):
            P_account.deposit(deposit_amount)

#--------------------------------- 3. tétel edge case-eket és küldés nem BankAccount object-nek
@pytest.fixture
def s_account():                            # forrás account
    return BankAccount("Peter")

@pytest.fixture
def t_account():                            # cél account
    return BankAccount("Robi")

@pytest.mark.parametrize(" s_balance_init, t_amount, t_balance_init, expected_s_balance, expected_t_balance, expected_exception", [
    (0.0, 0.1, 0.0, 0.0, 0.0, ValueError),  # Átutalás nulla egyenlegből
    (0.1, 0.1, 0.0, 0.0, 0.1, None),        # Átutalás pontosan az egyenleggel megegyező összeggel
    (0.1, 0.2, 0.0, 0.1, 0.0, ValueError),  # Átutalás nagyobb összeggel, mint az egyenleg
])
def test_transfer_edge_cases(s_account, t_account, s_balance_init, t_amount, t_balance_init, expected_s_balance, expected_t_balance, expected_exception):
    s_account.balance = s_balance_init
    t_account.balance = t_balance_init
    
    if expected_exception:
        with pytest.raises(expected_exception):
            s_account.transfer(t_amount, t_account)
    else:
        s_account.transfer(t_amount, t_account)
        assert s_account.get_balance() == expected_s_balance
        assert t_account.get_balance() == expected_t_balance

@pytest.mark.parametrize("s_balance_init, t_amount, t_balance_init, expected_s_balance, expected_t_balance, expected_exception", [
    (0.1, 0.1, 0.0, 0.0, 0.1, TypeError),   # pénz küldése nem BankAccount objectnek
])
def test_transfer_type_error(s_account, t_account, s_balance_init, t_amount, t_balance_init, expected_s_balance, expected_t_balance, expected_exception):
    s_account.balance = s_balance_init
    t_account.balance = t_balance_init

    with pytest.raises(expected_exception):
            s_account.transfer(t_amount, "Lajos")
            #s_account.transfer(t_amount, t_account)   #Raise hiba indukcióhoz

#--------------------------------- 4. tétel - megfelelő Exception raise-elődik
@pytest.fixture
def R_account():
    return BankAccount("Robi", 100.0)

@pytest.mark.parametrize("withdraw_amount, expected_balance, expected_exception", [
    (50.0, 50.0, None),              # Sikeres kifizetés
    (150.0, 100.0, ValueError),      # Elégtelen egyenleg
    (-10.0, 100.0, ValueError),      # Negatív összeg
    (0.0, 100.0, ValueError),        # Nulla összeg
])
def test_withdraw(R_account, withdraw_amount, expected_balance, expected_exception):
    if expected_exception:
        with pytest.raises(expected_exception):
            R_account.withdraw(withdraw_amount)
    else:
        R_account.withdraw(withdraw_amount)
        assert R_account.get_balance() == expected_balance






