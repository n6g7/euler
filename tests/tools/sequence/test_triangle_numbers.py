from tools.sequence.triangle_numbers import triangle_numbers
import unittest

class TestTriangleNumbers(unittest.TestCase):

    def test_generator(self):
        iter = triangle_numbers()
        self.assertEqual(next(iter), 1)
        self.assertEqual(next(iter), 3)
        self.assertEqual(next(iter), 6)
        self.assertEqual(next(iter), 10)
