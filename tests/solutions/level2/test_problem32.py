from solutions.level2.problem32 import pandigital_products
import unittest


class TestProblem32(unittest.TestCase):

    def test_problem(self):
        self.assertEqual(pandigital_products(), 45228)
