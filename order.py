class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        
        customer._orders.append(self)
        coffee._orders.append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if hasattr(self, '_price'):
            raise AttributeError("Price cannot be changed")
        if not isinstance(value, float):
            raise TypeError("Price must be a float")
        if not (1.0 <= value <= 10.0):
            raise ValueError("Price must be 1.0-10.0")
        self._price = value

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise TypeError("Must be a Customer")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            raise TypeError("Must be a Coffee")
        self._coffee = value