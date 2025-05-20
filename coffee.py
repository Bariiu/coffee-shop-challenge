class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            raise AttributeError("Coffee name cannot be changed")
        if not isinstance(value, str):
            raise TypeError("Name must bea string")
        if len(value) < 3:
            raise ValueError("Coffee name must be greater or equal to 3 characters")
        self._name = value

    def orders(self):
        return self._orders.copy()

    def customers(self):
        return list({order.customer for order in self._orders})

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        return sum(o.price for o in self._orders)/len(self._orders) if self._orders else 0