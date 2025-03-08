import unittest
from fizzbuzz import fizzbuzz
from staircase import staircase
from cat_and_mouse import cat_and_mouse

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
    
    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), "Buzz")
    
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
    
    def test_number(self):
        self.assertEqual(fizzbuzz(7), "7")

class TestStaircase(unittest.TestCase):
    def test_staircase_4(self):
        expected = "   #\n  ##\n ###\n####"
        self.assertEqual(staircase(4), expected)
    
    def test_staircase_2(self):
        expected = " #\n##"
        self.assertEqual(staircase(2), expected)

class TestCatAndMouse(unittest.TestCase):
    def test_cat_a_wins(self):
        self.assertEqual(cat_and_mouse(1, 3, 2), "Cat A")
    
    def test_cat_b_wins(self):
        self.assertEqual(cat_and_mouse(1, 5, 4), "Cat B")
    
    def test_mouse_escapes(self):
        self.assertEqual(cat_and_mouse(1, 3, 2), "Mouse C")

if __name__ == "__main__":
    unittest.main()