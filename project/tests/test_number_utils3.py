from coe_number.number_utils import is_prime_list

import unittest

class PrimeListTest(unittest.TestCase):
    def test_contains_non_prime(self):
        prime_list = [2, 3, 4, 5, 6, 7]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)