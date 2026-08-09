from solutions.level1.problem6 import squares_difference
import unittest


class TestProblem6(unittest.TestCase):

    def test_example(self):
        self.assertEqual(squares_difference(10), 2640)
