"""
Author: Gaál István Tamás
Task: Homework-6
"""

import pytest
from bankaccount import BankAccount

@pytest.fixture
def bela_bankaccount():
    bela = BankAccount("Béla", 0.0)
    return bela

@pytest.fixture
def tom_bankaccount():
    return BankAccount("Tom", 100.0)

#testing name
def test_name_type(bela_bankaccount,tom_bankaccount):
    assert bela_bankaccount.owner is not None
    assert tom_bankaccount.owner is not None

#testing deposit function
def test_deposit_to_bankaccount(bela_bankaccount):
    assert bela_bankaccount.balance == 0.0
    bela_bankaccount.deposit(100.0)
    assert bela_bankaccount.balance == 100.0

#testing deposit function to exceptions
@pytest.mark.parametrize("amount, expected_exception", [
    (0, ValueError),
    (-1, ValueError)
])
def test_deposit(bela_bankaccount, amount, expected_exception):
    with pytest.raises(expected_exception):
        bela_bankaccount.deposit(amount)

#testing transfer function
@pytest.mark.parametrize("amount, target_account, expected_exception", [
    (10, 10, TypeError),
    (20, "hello", TypeError),
    (10, True, TypeError)
])
def test_transfer(bela_bankaccount, amount, target_account, expected_exception):
    with pytest.raises(expected_exception):
        bela_bankaccount.transfer(amount, target_account)
