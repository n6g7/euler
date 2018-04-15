from tools.sequence.fibonacci import fibonacci
import unittest


class TestFibonacci(unittest.TestCase):

    def test_generator(self):
        iter = fibonacci()
        self.assertEqual(next(iter), 1)
        self.assertEqual(next(iter), 1)
        self.assertEqual(next(iter), 2)
        self.assertEqual(next(iter), 3)
        self.assertEqual(next(iter), 5)
        self.assertEqual(next(iter), 8)
        self.assertEqual(next(iter), 13)
