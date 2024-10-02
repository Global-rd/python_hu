import dotenv
import os
dotenv.load_dotenv()

account_balance = 500 #current balance in dollars
correct_pin = os.environ.get("PIN")

pin = int(input("Please enter your PIN: "))

if pin == correct_pin:
    print("PIN accepted.")
    print(f"Your current balance is {account_balance:.2f}")

    withdrawal_amount = float(input("Enter the amount you want to withdraw: "))

    if withdrawal_amount > 0:
        if withdrawal_amount <= account_balance:
            account_balance -= withdrawal_amount # account_balance - withdrawal amount
            print(f"Withdrawal successful! Current balance is: ${account_balance:.2f}")
        else:
            print("Insufficient funds for this withdrawal.")
    else:
        print("Invalid amount. Please enter a positive number!")
else:
    print("Incorrect PIN, please try again.")
