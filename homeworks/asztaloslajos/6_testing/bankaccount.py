
# def Class
class BankAccount:
# init
    def __init__(self, owner: str, balance: float = 0.0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner
        self.balance = balance
# deposit method  
    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
# withdraw method    
    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
# transfer method
    def transfer(self, amount: float, target_account: 'BankAccount'):
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount instance.")
        elif self.balance < amount:
            raise ValueError("Insufficient funds.")
        self.withdraw(amount)
        target_account.deposit(amount)
# get balance method    
    def get_balance(self):
        return self.balance
# str method overwrite
    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance:.2f}"

