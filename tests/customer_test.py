import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Alice")
        self.coffee = Coffee("Latte")

    def test_init_valid(self):
        customer = Customer("Bob")
        self.assertEqual(customer.name, "Bob")




if __name__ == '__main__':
    unittest.main()