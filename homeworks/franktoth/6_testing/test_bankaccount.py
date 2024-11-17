import pytest
from bankaccount import BankAccount

@pytest.fixture
def account1():
    return BankAccount("Frank", 500)

@pytest.fixture
def account2():
    return BankAccount("Steve", 700)

class TestBankAccount:

    # Deposit Tests
    def test_deposit_success(self, account1):
        account1.deposit(50)
        assert account1.get_balance() == 550

    @pytest.mark.parametrize(
        "invalid_value",
        [-10, 0],
    )
    def test_deposit_with_invalid_values(self, account1, invalid_value):
        with pytest.raises(ValueError):
            account1.deposit(invalid_value)

    # Withdraw Tests
    def test_withdraw_success(self, account1):
        account1.withdraw(100)
        assert account1.get_balance() == 400

    @pytest.mark.parametrize(
        "invalid_value",
        [-10, 600],
    )
    def test_withdraw_with_invalid_values(self, account1, invalid_value):
        with pytest.raises(ValueError):
            account1.withdraw(invalid_value)

    # Transfer Tests
    def test_transfer_to_right_target_account(self, account1, account2):
        account1.transfer(50, account2)
        assert account1.get_balance() == 450
        assert account2.get_balance() == 750

    def test_transfer_to_wrong_target_account(self, account1):
        with pytest.raises(TypeError):
            account1.transfer(50, "Invalid Target")