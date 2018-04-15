from tools.maximum_path import maximum_path_pyramid
import unittest


class TestMaximumPathPyramid(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(maximum_path_pyramid([[1], [2, 3]]), 4)
