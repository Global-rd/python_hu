class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        # Konstruktor: beállítja a tulajdonost és az egyenleget, ellenőrzi, hogy az egyenleg nem negatív.
        if isinstance(balance, str):
            raise TypeError("Balance must be a number.")
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        # Befizetés: ellenőrzi, hogy az összeg numerikus és pozitív, majd hozzáadja az egyenleghez.
        if not isinstance(amount, (int, float)):
            raise TypeError("Deposit amount must be a number.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount: float):
        # Kivétel: ellenőrzi, hogy az összeg numerikus, pozitív és elérhető az egyenlegből, majd levonja az összeget.
        if not isinstance(amount, (int, float)):
            raise TypeError("Withdraw amount must be a number.")
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def transfer(self, amount: float, target_account: 'BankAccount'):
        # Átutalás: ellenőrzi, hogy a célfiók BankAccount típusú, és nem saját maga, majd átutalja az összeget.
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount instance.")
        if target_account == self:
            raise ValueError("You cannot transfer money to the same account.")
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        self.withdraw(amount)
        target_account.deposit(amount)

    def get_balance(self):
        # Egyenleg lekérdezése: visszaadja az aktuális egyenleget.
        return self.balance

    def __str__(self):
        # Szöveges reprezentáció: visszaadja az objektum szöveges formáját.
        return f"Account owner: {self.owner}, Balance: {self.balance:.2f}"