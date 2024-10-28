from bank_account import BankAccount

def main():
    account_1 = BankAccount(account_holder="X", account_number="1", balance=500.0)

    print(account_1.get_balance())
    if account_1.deposit(200):
        print("Deposit Succesful!")
    
    if account_1.withdraw(700):
        print("Withdrawal successful")

    print(account_1.get_transaction_history())

if __name__ == "__main__":
    main()