from solutions.level1.problem17 import number_letter_counts
import unittest


class TestProblem17(unittest.TestCase):

    def test_example(self):
        self.assertEqual(number_letter_counts(5), 19)
