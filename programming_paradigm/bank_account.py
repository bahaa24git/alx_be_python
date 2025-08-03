class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return f"Deposited {amount}. New balance is {self.account_balance}."
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            return True
        elif amount > self.account_balance:
            return False

    def display_balance(self):
        return f"Account balance is {self.account_balance}."
