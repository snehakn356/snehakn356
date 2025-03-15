class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative")

account = BankAccount(500)
print("Balance:", account.get_balance())
account.set_balance(1000)
print("Updated Balance:", account.get_balance())
