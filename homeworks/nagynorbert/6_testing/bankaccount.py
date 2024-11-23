#Homework 6. - Nagy Norbert
class InvalidBankaccountOwner(Exception):
    """Owner is missing."""
    pass

class BalanceNotPositiveError(Exception):
    """Balance < 0"""
    pass

class SameBankAccountsError(Exception):
    """Bank accounts equals."""
    pass

class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        if not (isinstance(balance,float) or isinstance(balance,int)):
            raise TypeError("Balance is not numeric.")
        if balance < 0:
            raise BalanceNotPositiveError("Initial balance cannot be negative.")
        # bankaccount without owner is invalid
        if not owner:
            raise InvalidBankaccountOwner("Owner can't be empty.") 
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount: float):
        if not (isinstance(amount,float) or isinstance(amount,int)):
            raise TypeError("Amount is not numeric.")
        if amount < 0: #if deposit is 0 it can be handled
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
    
    def withdraw(self, amount: float):
        if not (isinstance(amount,float) or isinstance(amount,int)):
            raise TypeError("Amount is not numeric")
        if amount < 0: # if withdraw is 0 it can be handled
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def transfer(self, amount: float, target_account: 'BankAccount'):
        if not (isinstance(amount,float) or isinstance(amount,int)):
            raise TypeError("Amount is not numeric")
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount instance.")
        if self == target_account:
            raise SameBankAccountsError("Target account has to be different from origin.")
        self.withdraw(amount)
        target_account.deposit(amount)
    
    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance:.2f}"

