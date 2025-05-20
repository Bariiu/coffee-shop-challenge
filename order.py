class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        
        customer._orders.append(self)
        coffee._orders.append(self)

