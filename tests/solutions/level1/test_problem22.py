from solutions.level1.problem22 import names_scores
import unittest

class TestProblem22(unittest.TestCase):

    def test_problem(self):
        self.assertEqual(names_scores(), 871198282)
