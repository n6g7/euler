from solutions.level1.problem11 import greatest_diagonal_product
import unittest

class TestProblem11(unittest.TestCase):

    def test_problem(self):
        self.assertEqual(greatest_diagonal_product(4), 70600674)
