"""
6. HÁZI FELADAT: Értelmezd a kódot, és írj unit test-eket pytest segítségével. A unit testeknél a következőket vedd figyelembe:

- OK Írj legalább 2 fixture-t (2 különböző BankAccount object), amiket a tesztjeidben használsz.
- OK Írj legalább egy tesztet ami @pytest.mark.parametrize-t használ annak érdekében, hogy a tesztet több input-ra is lefuttassa (pl: teszteld a deposit() method-ot pontosan 0 és negatív szám inputtal is).
- OK Tesztelj edge case-eket (pl: pénz küldése nem BankAccount object-nek).
- OK Írj teszteket amik arra irányulnak, hogy a megfelelő Exception raise-elődik- e a megadott input-ra.
"""
import pytest
import os
from datetime import datetime

#BankAccount osztály importálása bankaccount.py állományból:
from bankaccount import BankAccount

###############################################################################################
### Írj legalább 2 fixture-t (2 különböző BankAccount object), amiket a tesztjeidben használsz.
###############################################################################################
@pytest.fixture
def account_one():
    return BankAccount(owner="Kata", balance=100.0)

@pytest.fixture
def account_two():
    return BankAccount(owner="Peti", balance=200.0)


# Test1: Unit test PASSED:
def test_deposit(account_one):
    account_one.deposit(50)
    assert account_one.get_balance() == 150.0 

# Test2: Unit test FAILED:
def test_withdraw(account_two):
    account_two.withdraw(30)
    assert account_two.get_balance() == 171.0

# Test3: Unit test PASSED:
def test_transfer(account_one, account_two):
    account_one.transfer(50, account_two)
    assert account_one.get_balance() == 50.0
    assert account_two.get_balance() == 250.0


###############################################################################################
### Írj legalább egy tesztet ami @pytest.mark.parametrize-t használ annak érdekében, hogy #####
### a tesztet több input-ra is lefuttassa (pl: teszteld a deposit() method-ot pontosan 0 és ###
### negatív szám inputtal is). ################################################################
###############################################################################################
@pytest.mark.parametrize("amount, expected_exception", [

# Test4: PASSED: Így ValueError hibára fut a main kód -> a unit test NEM fut hibára:
    (-25, ValueError), 
 
# Test5: PASSED: Így ValueError hibára fut a main kód -> a unit test NEM fut hibára:
    (0, ValueError),

# Test6: FAILED: NEM fut ValueError hibára a main kód -> a unit test hibára fut.
    (50, ValueError)
])
def test_invalid_deposit(account_one, amount, expected_exception):
    with pytest.raises(expected_exception):
        account_one.deposit(amount)


#######################################################################################################
### Tesztelj edge case-eket (pl: pénz küldése nem BankAccount object-nek). ############################
### Írj teszteket amik arra irányulnak, hogy a megfelelő Exception raise-elődik- e a megadott input-ra.
#######################################################################################################
@pytest.mark.parametrize("amount, target_account, expected_exception", [
# Test7: PASSED: Így TypeError hibára fut a main kód, így itt a unit test NEM fut hibára:
    (50, account_two, TypeError),

# Test8: FAILED: Így NEM fut TypeError hibára fut a main kód, így itt a unit test hibára fut:
    (50, BankAccount(owner="Peti", balance=140), TypeError), 

# Test9: PASSED: Így ValueError hibára fut a main kód, így itt a unit test NEM fut hibára.
    (5000, BankAccount(owner="Peti", balance=140), ValueError) ,

# Test10: FAILED: Így NEM fut ValueError hibára a main kód, így itt a unit test hibára fut.
    (50, BankAccount(owner="Peti", balance=140), ValueError) 
])
def test_invalid_transfer(account_one, amount, target_account, expected_exception):
    with pytest.raises(expected_exception):
        account_one.transfer(amount, target_account)


#######################################################################################################
### Kiegészítések #####################################################################################
#######################################################################################################

# K1: a program futásakor a képernyő törlése ##########################################################
current_datetime = datetime.now()
os.system("cls")
print(f"(Előző futási eredmény törölve a képernyőről ekkor: {current_datetime})")
print("----------------------------")

# K2: saját, relatív útvonal megadása, hogy csak az én kódomra futtassa a pytest-et ###################
# pytest homeworks/veizerattila/6_testing