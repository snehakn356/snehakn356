class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}, New Balance: {self.__balance}")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}, Remaining Balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds")

account = BankAccount(500)
account.deposit(200)
account.withdraw(100)
