# Create a Pizza class that accepts a list of ingredients.
#
# The class supports:
#
# - the order_number attribute, which returns the current order numberBe
#
# - the ingredients attribute, which returns the list accepted in the constructor
#
# - functions (garden_feast, hawaiian, meat_festival) for creating types of pizzas, the ingredients of which are known in advance

class Pizza:
    order = 0

    def __init__(self, ingredients):
        self.ingredients = ingredients
        Pizza.order += 1
        self.order_number = Pizza.order

    @classmethod
    def garden_feast(cls):
        return cls(['spinach', 'olives', 'mushroom'])

    @classmethod
    def hawaiian(cls):
        return cls(['ham', 'pineapple'])

    @classmethod
    def meat_festival(cls):
        return cls(['beef', 'meatball', 'bacon'])


p1 = Pizza(['bacon', 'parmesan', 'ham'])  # order 1
p2 = Pizza.garden_feast()  # order 2
print(p1.ingredients)  # ['bacon', 'parmesan', 'ham']
print(p2.ingredients)  # ['spinach', 'olives', 'mushroom']
print(p1.order_number)  # 1
print(p2.order_number)  # 2
