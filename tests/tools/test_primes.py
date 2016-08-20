from tools.primes import is_prime, prime_factors
from types import GeneratorType
import unittest

class TestIsPrime(unittest.TestCase):

    def test_under_ten(self):
        primes = [2, 3, 5, 7]
        not_primes = [1, 4, 6, 8, 9]

        for n in primes:
            self.assertTrue(is_prime(n))

        for n in not_primes:
            self.assertFalse(is_prime(n))

class TestPrimeFactors(unittest.TestCase):

    def test_generator(self):
        self.assertIsInstance(prime_factors(20), GeneratorType)

    def test_values(self):
        self.assertEqual(list(prime_factors(20)), [2, 2, 5])

    def test_reverse(self):
        self.assertEqual(list(prime_factors(20, reverse=True)), [5, 2, 2])
