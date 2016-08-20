from problem8 import greatest_product
import unittest

class TestProblem8(unittest.TestCase):

    def test_example(self):
        self.assertEqual(greatest_product(4), 5832)

    def test_problem(self):
        self.assertEqual(greatest_product(13), 23514624000)
