from solutions.level1.problem15 import lattice_paths
import unittest

class TestProblem15(unittest.TestCase):

    def test_example(self):
        self.assertEqual(lattice_paths(2, 2), 6)

    def test_problem(self):
        self.assertEqual(lattice_paths(20, 20), 137846528820)
