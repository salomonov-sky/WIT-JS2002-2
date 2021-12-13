from exc2 import Employee

import unittest


class TestMain2(unittest.TestCase):
    def setUp(self):
        self.w1 = Employee("John", "Smith", 35, 7500)
        self.w2 = Employee("Andrew", "Miller", 26, 6500)
        self.w3 = Employee("Kendall", "Evans",26 , 5500)

    def test_introduce_self(self):
        self.assertTrue(Employee.introduce_self(self.w1))
        self.assertEqual(Employee.introduce_self(self.w1), Employee.introduce_self(self.w2))

    def test_raise_salary(self):
        self.assertIsNone(Employee.raise_salary(self.w1, 1.2))
        self.assertEqual(Employee.raise_salary(self.w1, 1), Employee.raise_salary(self.w2, 10))

    def test_check_age(self):
        self.assertTrue(Employee.check_age(self.w2))
        self.assertFalse(Employee.check_age(self.w3))
        self.assertEqual(Employee.check_age(self.w2), Employee.check_age(self.w3))

    def test_get_email(self):
        self.assertTrue(Employee.get_email(self.w1))
        self.assertEqual(Employee.get_email(self.w1), Employee.get_email(self.w2))

unittest.main()

