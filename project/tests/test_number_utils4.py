from coe_number.number_utils import is_prime_list

import unittest

class PrimeListTest(unittest.TestCase):
    def test_contains_zero_and_negative_numbers(self):
        prime_list = [-3, -2, 0, 2, 3, 5]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)