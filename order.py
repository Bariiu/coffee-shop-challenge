from customer import Customer
from coffee import Coffee

class Order:
    def __init__(self, customer, coffee, price):
        self._customer = None
        self._coffee = None
        self._price = None
        
        self.customer = customer
        self.coffee = coffee
        self.price = price

        customer._orders.append(self)
        coffee._orders.append(self)

    def get_price(self):
        return self._price
    
    def set_price(self, value):
        if self._price is not None:
            raise AttributeError("Price cannot be changed after creation")
        if not isinstance(value, float):
            raise TypeError("Price must be a float")
        if not (1.0 <= value <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0")
        self._price = value
    
    price = property(get_price, set_price)

    def get_customer(self):
        return self._customer
    
    def set_customer(self, value):
        if not isinstance(value, Customer):
            raise TypeError("Must be a Customer instance")
        if self._customer is not None:
            raise AttributeError("Customer cannot be changed after creation")
        self._customer = value
    
    customer = property(get_customer, set_customer)

    def get_coffee(self):
        return self._coffee
    
    def set_coffee(self, value):
        if not isinstance(value, Coffee):
            raise TypeError("Must be a Coffee instance")
        if self._coffee is not None:
            raise AttributeError("Coffee cannot be changed after creation")
        self._coffee = value
    
    coffee = property(get_coffee, set_coffee)