class Coffee:
    def __init__(self, name):
        self.name = name 
        self._orders = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if hasattr(self, "_name"):
            raise AttributeError("Coffee names can't be changed")
        if not isinstance(new_name, str):
            raise TypeError("Name must bea string")
        if len(new_name) < 3:
            raise ValueError("Name must be more than or equal to 3 characters")
        self._name = new_name

    def orders(self):
        return self._orders.copy()
    
    def customers(self):
        return list({order.customer for order in self._orders})
    
    def num_orders(self):
        return len(self._orders)
    
    def average_price(self):
        if not self._orders:
            return 0
        total = sum(order.price for order in self._orders)
        return total / len(self._orders)