class ShoppingCart:
    def __init__(self):
        self.items = []

    def total_price(self):
        total = 0
        for item in self.items:
            total += item["price"]
        return total


cart = ShoppingCart()
cart.items.append({"name": "Peanut butter", "price":1.0})
cart.items.append({"name": "Bread", "price": 2.0})
cart.items.append({"name": "Maize", "price":3.0})
cart.items.append({"name": "Eggs", "price": 4.0})
cart.items.append({"name": "Whey Protein", "price":5.0})

print(cart.total_price())