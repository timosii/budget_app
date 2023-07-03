from typing import List


class Category:
    ledger: List = []

    def __init__(self, name):
        self.name = name


    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})


    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
        return True if self.check_funds(amount) else False

    
    def get_balance(self):
        balance = 0
        for note in self.ledger:
            for a, d in note:
                if a == "amount":
                    balance += d
        return balance


    def transfer(self, amount, category):
        self.category = category.Category()
        if self.check_funds(amount):
            self.category.withdraw(amount, f"Transfer to {self.category}")
            self.category.deposit(amount, f"Transfer from {self.category}")
            return True
        else:
            return False


    def check_funds(self, amount):
        self.amount = amount
        return True if self.amount > self.get_balance() else False

food = Category("food")
print(food)
