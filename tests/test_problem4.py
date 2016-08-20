from problem4 import largest_palindrome_by_magnitude
import unittest

class TestProblem4(unittest.TestCase):

    def test_example(self):
        self.assertEqual(largest_palindrome_by_magnitude(2), 9009)

    def test_problem(self):
        self.assertEqual(largest_palindrome_by_magnitude(3), 906609)
