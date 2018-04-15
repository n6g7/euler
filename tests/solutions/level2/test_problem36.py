from solutions.level2.problem36 import double_base_palindromes
import unittest


class TestProblem36(unittest.TestCase):

    def test_problem(self):
        self.assertEqual(double_base_palindromes(1000000), 872187)
