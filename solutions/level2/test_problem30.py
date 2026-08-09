from solutions.level2.problem30 import digit_power
import unittest


class TestProblem30(unittest.TestCase):

    def test_example(self):
        self.assertEqual(digit_power(4), 19316)
