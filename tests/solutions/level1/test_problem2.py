from solutions.level1.problem2 import sum_even_fibo
import unittest

class TestProblem2(unittest.TestCase):

    def test_problem(self):
        self.assertEqual(sum_even_fibo(4000000), 4613732)
