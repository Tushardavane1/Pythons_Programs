class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount >= 0 :
            self.balance += amount
            print(f"Deposit of {amount} successful. New balance: {self.balance}")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if 0 <= amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. New balance: {self.balance}")
        else:
            print("Invalid amount for withdrawal.")

    def get_balance(self):
        return self.balance


# Example usage
account1 = BankAccount("123456789", 1000)
print("how much do you deposit")
account1.deposit(int(input()))
print("how much do you the withdraw the cash")
account1.withdraw(int(input()))
print("Account balance:", account1.get_balance())
