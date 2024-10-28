from datetime import datetime as dt

class InvalidAmountError(Exception):
    """ Custom exception for invalid transaction amount."""
    pass


class InsufficientFundsError(Exception):
    """ Custom exception for insufficient funds"""
    pass


class BankAccount:

    def __init__(self, account_holder:str, account_number:str, balance:float=0.0):
        self.account_holder = account_holder
        self.account_number = account_number
        self._balance = balance
        self._transactions = []

    def deposit(self, amount: int):
        
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be positive")
        self._balance += amount
        self._record_transaction(transaction_type="deposit", amount=amount)
        return True

    def withdraw(self, amount):
        
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise InsufficientFundsError("Insufficent funds for transaction")
        self._record_transaction(transaction_type="withdraw", amount=amount)
        self._balance -= amount
        return True

    def get_balance(self):
        return self._balance
    
    def _record_transaction(self, transaction_type, amount):
        transaction = {"type": transaction_type,
                       "amount": amount,
                       "date": dt.now().strftime("%Y-%m-%d %H:%M:%S")}
        self._transactions.append(transaction)


    def get_transaction_history(self):
        
        if not self._transactions:
            return "There are no transactions yet"

        history = f"Transaction history for {self.account_holder}-{self.account_number}: \n"
        for transaction in self._transactions:
            history += (f"{transaction['date']} - {transaction['type']:} "
                        f"${transaction['amount']}\n")
        return history
