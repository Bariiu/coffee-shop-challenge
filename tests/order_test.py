import unittest
from order import Order
from customer import Customer
from coffee import Coffee

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Alice")
        self.coffee = Coffee("Cappuccino")

    def test_init_valid(self):
        order = Order(self.customer, self.coffee, 5.0)
        self.assertEqual(order.price, 5.0)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, self.coffee)

    def test_price_validation(self):
        with self.subTest("Test low price"):
            with self.assertRaises(ValueError):
                Order(self.customer, self.coffee, 0.9)



if __name__ == '__main__':
    unittest.main()