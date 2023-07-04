class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []


    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})


    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
        return True if self.check_funds(amount) else False

    
    def get_balance(self):
        balance = 0
        for note in self.ledger:
            for _, v in note.items():
                if type(v) == int:
                    balance += v

        return balance


    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False


    def check_funds(self, amount):
        self.amount = amount
        return False if self.amount > self.get_balance() else True





food = Category("food")
sport = Category('sport')



