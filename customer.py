class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string")
        if not (1 <= len(new_name) <= 15):
            raise ValueError("Name must be 1-15 characters")
        self._name = new_name

    def orders(self):
        return self._orders.copy()
    
    def coffees(self):
        return list({order.coffee for order in self._orders})
    
    def create_order(self, coffee, price):
        from order import Order
        new_order = Order(self, coffee, price)
        return new_order