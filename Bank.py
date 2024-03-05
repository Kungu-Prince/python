# bank code using classes, define class 
class FinancialAccount:
    def __init__(self, account_number, balance, opening_date, account_holder):
        self.account_number = account_number
        self.balance = balance
        self.opening_date = opening_date
        self.account_holder = account_holder

    def deposit_funds(self, amount):
        self.balance += amount
        return f"Successfully deposited {amount} into your account."

    def withdraw_funds(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        else:
            self.balance -= amount
            return f"Withdrew {amount} from your account successfully."

    def check_account_balance(self):
        return f"Your current account balance is {self.balance}."

    def account_information(self):
        return f"Account Holder: {self.account_holder}\nAccount Number: {self.account_number}\nAccount Balance: {self.balance}\nAccount Opening Date: {self.opening_date}"

# Creating an instance of the FinancialAccount class
financial_account = FinancialAccount(123456, 100000, "01-03-2022", "Jane Smith")

# User interaction loop
while True:
    print("\nSelect an option:")
    print("1. Deposit Funds")
    print("2. Check Account Balance")
    print("3. Withdraw Funds")
    print("4. Exit")

    user_choice = input("Enter your choice (1/2/3/4): ")

    if user_choice == '1':
        deposit_amount = float(input("Enter the amount to deposit: "))
        print(financial_account.deposit_funds(deposit_amount))
    elif user_choice == '2':
        print(financial_account.check_account_balance())
    elif user_choice == '3':
        withdrawal_amount = float(input("Enter the amount to withdraw: "))
        print(financial_account.withdraw_funds(withdrawal_amount))
    elif user_choice == '4':
        break
    else:
        print("Invalid choice. Please select a valid option.")
