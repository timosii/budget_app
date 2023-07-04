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
                if type(v) in (int,float):
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


    def display(self):
        first_string = self.name.center(30, '*')
        res = first_string + '\n'
        for action in self.ledger:
            res += \
            f"{action['description'].ljust(23)}{str(action['amount']).rjust(7)}\n" 
        res += f"Total: {self.get_balance()}"

        return res

    


food = Category("Food")
clothing = Category("Clothing")
food.deposit(1000.00, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more foo')
food.transfer(50.00, clothing)

clothing.deposit(180.00, 'initial deposit')
clothing.withdraw(10.25, 'skirt')
clothing.withdraw(23.09, 'trousers')


print(food.display())
print(clothing.display())


def create_spend_chart(lst):
    '''
    Принимает список категорий, возвращает строку
    '''
    first_string = "Percentage spent by category"
    hash_table_of_strings = {1:'100| ',2:'90| ',3:'80| ',4:'70| ',5:'60| ',6:'50| ',7:'40| ',8:'30| ',9:'20| ',10:'10| ',11:' 0| '}
    return hash_table_of_strings

print(create_spend_chart([1]))


