class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        if not isinstance(balance, (int, float)): 
            raise TypeError("Balance must be a number.") # Számot várunk
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount: float):
        if not isinstance(amount, (int, float)):
            raise TypeError("Deposit amount must be a number.") # Szintén számot várunk
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
    
    def withdraw(self, amount: float):
        if not isinstance(amount, (int, float)):
            raise TypeError("Withdraw amount must be a number.") # Szintén számot várunk
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def transfer(self, amount: float, target_account: 'BankAccount'):
        if not isinstance(amount, (int, float)):
            raise TypeError("Transfer amount must be a number.")  # Szintén számot várunk
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount instance.") # Nincs számlája
        if self.balance < amount:
            raise ValueError("Insufficient funds.") # Nincs ennyije
        if self==target_account:
            raise TypeError("The account holder is the same.") # Nem küldhet magának
        self.withdraw(amount)
        target_account.deposit(amount)
    
    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance:.2f}"

