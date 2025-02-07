from coe_number.number_utils import is_prime_list

import unittest

class PrimeListTest(unittest.TestCase):
    def test_all_prime_numbers(self):
        prime_list = [2, 3, 5, 7, 11, 13, 17]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)