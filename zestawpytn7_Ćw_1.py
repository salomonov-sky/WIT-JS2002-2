from exc1 import add, subtract, multiply, divide, is_numeric 


import unittest
class TestMain(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1,2), 3)
        self.assertNoEqual(add(2,2), 3)

    def tesr_subtract(self):
        self.assertEqual(subtract(5,2), 3)
        self.assertNotEqual(subtract(6,3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(3,3), 9)
        self.assertNotEqual(multiply(2,2), 6)

    def test_divide(self):
        self.assertEqual(divide(4,2), 2)
        self.assertNotEqual(divide(5,0))

    def is_numeric(self):
        self.assertFalse(is_numeric("x"))
        self.assertTrue(is_numeric(1))

unittest.main()
        
