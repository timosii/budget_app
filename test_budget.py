food = Category("Food")
clothing = Category("Clothing")
food.deposit(1000.00, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more foo')
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
food.transfer(50.00, clothing)

clothing.deposit(180.00, 'initial deposit')
clothing.withdraw(10.25, 'skirt')
clothing.withdraw(23.09, 'trousers')

print(food)
print(create_spend_chart([food, clothing]))
