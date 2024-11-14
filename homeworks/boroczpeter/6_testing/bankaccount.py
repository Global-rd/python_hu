class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        if not isinstance(balance, (int, float)): # balance must be a number
            raise TypeError("Balance must be a number.")
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount: float):       
        if not isinstance(amount, (int, float)): # deposited amount must be number
            raise TypeError("Deposit amount must be a number.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
    
    def withdraw(self, amount: float):
        if not isinstance(amount, (int, float)): # withdrawed amount must be number
            raise TypeError("Withdraw amount must be a number.")        
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def transfer(self, amount: float, target_account: 'BankAccount'):
        if not isinstance(amount, (int, float)): # transfered amount must be number
            raise TypeError("Transfer amount must be a number.")
        if amount <= 0: # only positive number can be transfered
            raise ValueError("Transfer amount must be positive.")
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount instance.")
        if self == target_account: # transfer to own account not possible
            raise ValueError("Cannot transfer to own account.")
        self.withdraw(amount)
        target_account.deposit(amount)
    
    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance:.2f}"