from solutions.level1.problem23 import non_abundant_sums
import unittest

class TestProblem23(unittest.TestCase):

    def test_problem(self):
        self.assertEqual(non_abundant_sums(28123), 4179871)
