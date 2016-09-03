from tools.divisors import count_divisors, get_divisors, sum_divisors, is_perfect, is_deficient, is_abundant
import unittest

class TestCountDivisors(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(count_divisors(1), 1)
        self.assertEqual(count_divisors(2), 2)
        self.assertEqual(count_divisors(3), 2)
        self.assertEqual(count_divisors(4), 3)
        self.assertEqual(count_divisors(5), 2)
        self.assertEqual(count_divisors(18), 6)

class TestGetDivisors(unittest.TestCase):

    def test_simple(self):
        iter = get_divisors(12)

        self.assertEqual(next(iter), 1)
        self.assertEqual(next(iter), 12)
        self.assertEqual(next(iter), 2)
        self.assertEqual(next(iter), 6)
        self.assertEqual(next(iter), 3)
        self.assertEqual(next(iter), 4)
        self.assertRaises(StopIteration, lambda: next(iter))

    def test_proper(self):
        iter = get_divisors(20, True)

        self.assertEqual(next(iter), 1)
        self.assertEqual(next(iter), 2)
        self.assertEqual(next(iter), 10)
        self.assertEqual(next(iter), 4)
        self.assertEqual(next(iter), 5)
        self.assertRaises(StopIteration, lambda: next(iter))

class TestSumDivisors(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(sum_divisors(220), 504)
        self.assertEqual(sum_divisors(284), 504)

    def test_proper(self):
        self.assertEqual(sum_divisors(220, True), 284)
        self.assertEqual(sum_divisors(284, True), 220)

class TestIsPerfect(unittest.TestCase):

    def test_below_twenty(self):
        self.assertTrue(is_perfect(6))

    def test_more_cases(self):
        self.assertTrue(is_perfect(28))
        self.assertTrue(is_perfect(496))
        self.assertTrue(is_perfect(8128))
        self.assertTrue(is_perfect(33550336))

class TestIsDeficient(unittest.TestCase):

    def test_below_twenty(self):
        for n in [1,2,3,4,5,7,8,9,10,11,13,14,15,16,17,19]:
            self.assertTrue(is_deficient(n))

    def test_more_cases(self):
        self.assertTrue(is_deficient(49))
        self.assertTrue(is_deficient(50))

class TestIsAbundant(unittest.TestCase):

    def test_below_twenty(self):
        for n in [12,18,20]:
            self.assertTrue(is_abundant(n))

    def test_more_cases(self):
        self.assertTrue(is_abundant(24))
        self.assertTrue(is_abundant(100))
        self.assertTrue(is_abundant(120))
        self.assertTrue(is_abundant(196))
        self.assertTrue(is_abundant(945))
        self.assertTrue(is_abundant(1575))
        self.assertTrue(is_abundant(7425))
