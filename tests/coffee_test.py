import unittest
from coffee import Coffee
from customer import Customer
from order import Order

class TestCoffee(unittest.TestCase):
    def setUp(self):
        self.coffee = Coffee("Mocha")

    def test_init_valid(self):
        coffee = Coffee("Espresso")
        self.assertEqual(coffee.name, "Espresso")




if __name__ == '__main__':
    unittest.main()