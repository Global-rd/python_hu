import pytest
from bankaccount import BankAccount


# Fixture to create BankAccounts with different initial balances
@pytest.fixture(scope="class")
def accounts():
    account1 = BankAccount("Frank", 500)
    account2 = BankAccount("Steve", 700)
    invalid_account = BankAccount("Account Error", -250)
    return account1, account2, invalid_account


class TestBankAccount:
    # Test deposit with various inputs using parametrize
    @pytest.mark.parametrize("deposit_amount, expected_balance, expected_exception", [
        (50, 550, None), 
        (0, 330, None), 
        (-30, 100, ValueError)
    ])
    def test_deposit(self, accounts, deposit_amount, expected_balance, expected_exception):
        account = accounts[0] 

        if expected_exception:
            with pytest.raises(expected_exception):
                account.deposit(deposit_amount)
        else:
            account.deposit(deposit_amount)
            assert account.get_balance() == expected_balance

    # Test withdraw with different values
    def test_withdraw(self, accounts):
        account = accounts[0]

        account.withdraw(100)
        assert account.get_balance() == 400

        with pytest.raises(ValueError):
            account.withdraw(1000) 

        with pytest.raises(ValueError):
            account.withdraw(0) 

    # Test transfer with right and wrong account destinations
    def test_transfer(self, accounts):
        account1, account2, _ = accounts

        with pytest.raises(TypeError):
            account1.transfer(50, "Account Error")

        account1.transfer(50, account2)
        assert account1.get_balance() == 550
        assert account2.get_balance() == 750