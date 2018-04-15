from solutions.level2.problem31 import coin_sums
import unittest


class TestProblem31(unittest.TestCase):

    def test_problem(self):
        self.assertEqual(
            coin_sums(200, [1, 2, 5, 10, 20, 50, 100, 200]),
            73682
        )
