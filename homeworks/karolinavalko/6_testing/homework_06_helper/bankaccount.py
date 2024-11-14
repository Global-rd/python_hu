class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        if not isinstance(amount, (int,float)):
            raise TypeError ("Please use numeric values for deposit.")
    
    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        if not isinstance(amount, (int,float)):
            raise TypeError ("Please use numeric values for withdraw.")

    def transfer(self, amount: float, target_account: 'BankAccount'):
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount instance.")
        self.withdraw(amount)
        target_account.deposit(amount)
        if self == target_account:
            raise TypeError("You cannot have the same account for initiate and receive transfer.")
        if not isinstance (amount, (int,float)):
            raise TypeError ("Please use numeric values for amount for transfer.")
        if amount <= 0:
            raise ValueError("Please add a positive amount for transfer.")
        if amount > target_account.balance:
            raise ValueError("Insufficent fund for transfer.")
    
    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance:.2f}"




