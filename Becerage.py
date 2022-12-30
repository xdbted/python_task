# Create a Beverage class that, when constructed, takes a list of ingredients
#
# - supports the ingredients attribute, which returns a list of the ingredients passed when constructing the class instance
#
# - supports the get_cost function, which calculates the total cost of all ingredients of the drink
#
# - supports the get_price function, which calculates the price of a drink by multiplying the cost by 2.5
#
# - supports the get_name function, which returns a string listing the ingredients sorted alphabetically. If there is more than one ingredient, then add the word 'Fusion' at the end, otherwise add the word 'Smoothie'. This function should also replace 'berries' with 'berry'.
ingredients_price = {"Strawberries": 1.50, "Banana": 0.50, "Mango": 2.50, "Blueberries": 1.00,
                     "Raspberries": 1.00, "Apples": 1.75, "Pineapple": 3.50}


class Beverage:

    def __init__(self, ingredients):
        self.ingredients = ingredients

    def get_cost(self):
        cost = 0
        for x, y in ingredients_price.items():
            if x in [_ for _ in self.ingredients]:
                cost += y
        self.cost = cost
        return self.cost

    def get_price(self):
        return self.cost * 2.5

    def get_name(self):
        x = []
        for _ in self.ingredients:
            self.ingredients = _.replace('berries', 'berry')
            x.append(self.ingredients)
        self.name = sorted(x)
        if len(self.name) == 1:
            z = 'Smoothie'
        else:
            z = 'Fusion'
        return f'{(" ".join(self.name))} {z}'
