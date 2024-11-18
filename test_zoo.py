import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_error_ticket_price(self):
        # C1b1: error
        self.assertEqual(self.zoo.get_ticket_price(-1), "error")

    def test_child_ticket_price(self):
        # C1b2: 0 <= age <= 12
        self.assertEqual(self.zoo.get_ticket_price(5), 50)

    def test_teen_ticket_price(self):
        # C1b3: 13 <= age <= 20
        self.assertEqual(self.zoo.get_ticket_price(18), 100)

    def test_adult_ticket_price(self):
        # C1b4: 21 <= age <= 60
        self.assertEqual(self.zoo.get_ticket_price(30), 150)

    def test_senior_ticket_price(self):
        # C1b5: age > 60
        self.assertEqual(self.zoo.get_ticket_price(65), 100)

if __name__ == '__main__':
    unittest.main()
