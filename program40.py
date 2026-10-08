# Python Program using operator overloading with __add__() for + operator

class Account:
    def __init__(self, balance):
        self.balance = balance

    # Overloading the + operator to add balances of two Account objects
    def __add__(self, other):
        return Account(self.balance + other.balance)

# 1. Create two Account objects with initial balances
account1 = Account(1000)
account2 = Account(500)

# 2. Add the balances of the two Account objects using the + operator
total_balance = account1 + account2

# 3. Print the total balance
print(f"Total balance: {total_balance.balance}")