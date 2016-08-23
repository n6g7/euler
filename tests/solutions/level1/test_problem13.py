from solutions.level1.problem13 import first_digits_of_sum
import unittest

class TestProblem13(unittest.TestCase):

    def test_problem(self):
        self.assertEqual(first_digits_of_sum(10), '5537376230')
