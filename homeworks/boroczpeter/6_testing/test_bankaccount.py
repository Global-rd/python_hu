import pytest
from bankaccount import BankAccount

@pytest.fixture
def account_1():
    return BankAccount("Alexa", 100.0)

@pytest.fixture
def account_2():
    return BankAccount("Brian", 300.0)

#test deposits
@pytest.mark.parametrize("amount", [100.0, 0.0, -100.0])
def test_deposit(account_1, amount):
    if amount > 0:
        account_1.deposit(amount)
        assert account_1.get_balance() == 100.0 + amount
    else:
        with pytest.raises(ValueError):
            account_1.deposit(amount)

# test withdrawals
def test_withdraw_over_balance(account_1):
    with pytest.raises(ValueError, match="Insufficient funds."):
        account_1.withdraw(200.0)

def test_withdraw_zero_or_negative_amount(account_1):
    with pytest.raises(ValueError, match="Withdraw amount must be positive."):
        account_1.withdraw(0)
    with pytest.raises(ValueError, match="Withdraw amount must be positive."):
        account_1.withdraw(-10)

# test bank transfers
def test_transfer_over_balance(account_1, account_2):
    with pytest.raises(ValueError, match="Insufficient funds."):
        account_1.transfer(200.0, account_2)

def test_transfer_negative_or_zero_amount(account_1, account_2):
    with pytest.raises(ValueError, match="Transfer amount must be positive."):
        account_1.transfer(0, account_2)
    with pytest.raises(ValueError, match="Transfer amount must be positive."):
        account_1.transfer(-10, account_2)

def test_transfer_non_bank_account(account_1):
    with pytest.raises(TypeError, match="Target must be a BankAccount instance."):
        account_1.transfer(10.0, "NotABankAccount")

def test_transfer_to_own_account(account_1):
    with pytest.raises(ValueError):
        account_1.transfer(10, account_1)

# test non-numeric inputs for depost, withdraw, transfer
def test_deposit_non_numeric(account_1):
    with pytest.raises(TypeError, match="Deposit amount must be a number."):
        account_1.deposit("not_a_number")

def test_withdraw_non_numeric(account_1):
    with pytest.raises(TypeError, match="Withdraw amount must be a number."):
        account_1.withdraw("not_a_number")

def test_transfer_non_numeric(account_1, account_2):
    with pytest.raises(TypeError, match="Transfer amount must be a number."):
        account_1.transfer("not_a_number", account_2)