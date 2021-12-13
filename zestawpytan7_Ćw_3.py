from exc3 import is_numeric, is_negative, calculate_savings


import unittest
class TestMain3(unittest.TestCase):

    def test_is_numeric(self):
        self.assertFalse(is_numeric("x"))
        self.assertTrue(is_numeric(3))
       

    def test_is_negative(self):
        self.assertTrue(is_negative(-1))
        self.assertFalse(is_negative(1))

    def test_calculate_savings(self):
        self.assertFalse(calculate_savings("x", 20, 40))
        self.assertTrue(calculate_savings(30, 20, 10))
        self.assertFalse(calculate_savings(10, 20, -30))
        

unittest.main()
