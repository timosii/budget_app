
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        return self.display()

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
        total = f"{self.get_balance():.2f}"
        for action in self.ledger:
            edited_amount = f"{action['amount']:.2f}"
            res += \
            f"{action['description'][:23].ljust(23)}{edited_amount.rjust(7)}\n" 
        res += f"Total: {total}"

        return res

    def spent(self):
        res = 0
        for action in self.ledger:
            if action['amount'] < 0:
                res += abs(action['amount'])
        return round(res, 2)

def create_spend_chart(lst):
    count_categories = len(lst)
    sum_spent = 0 
    for cat in lst:
        sum_spent += cat.spent()

    first_string = "Percentage spent by category"
    hash_table_of_strings = {100:'100| ',\
                             90:' 90| ',\
                             80:' 80| ',\
                             70:' 70| ',\
                             60:' 60| ',\
                             50:' 50| ',\
                             40:' 40| ',\
                             30:' 30| ',\
                             20:' 20| ',\
                             10:' 10| ',\
                             0:'  0| '}
    for cat in lst:
        for k in hash_table_of_strings.keys():
            if cat.spent() / sum_spent * 100 <= k:
                hash_table_of_strings[k] += '   '
            else:
                hash_table_of_strings[k] += 'o  '

    medium_string = '    -' + '---' * count_categories

    lower_block = []
    names = []
    for cat in lst:
        names.append(cat.name)
    max_len = max(map(len, names))
    for i in range(max_len):
        block = '     '
        for cat in lst:
            if i in range(len(cat.name)):
                block += f'{cat.name[i]}  '
            else:
                block += '   '
        lower_block.append(block)

    res = first_string + '\n'
    for k, v in hash_table_of_strings.items():
        res += v + '\n'

    res += medium_string + '\n'
    for el in lower_block:
        res += el + '\n'
    
    return res[:-2]


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
# print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
# print(clothing.get_balance())
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)
education = Category('Education')
education.deposit(300, 'initial deposit')
education.withdraw(80, 'Udemy')
education.withdraw(88, 'Coursera')
# print(education.get_balance())
# print(auto.get_balance())

# print(education)
# print(food)
# print(clothing)

print(create_spend_chart([food, clothing, auto, education]))
