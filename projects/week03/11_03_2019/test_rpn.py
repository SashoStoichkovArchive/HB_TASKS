import unittest
from rpn import rpn_calc

class TestReversedPolishNotation(unittest.TestCase):
    def test_when_single_digit_is_passed_then_return_the_same_digit(self):
        expr = '45'
        expected_result = 45.0
        
        self.assertEqual(rpn_calc(expr), expected_result)

    def test_when_two_numbers_are_passed_then_return_sum_of_them(self):
        expr = '4 8 +'
        expected_result = 12.0

        self.assertEqual(rpn_calc(expr), expected_result)

    def test_when_substraction_of_two_numbers_then_return_the_difference(self):
        expr = '7 3 -'
        expected_result = 4.0

        self.assertEqual(rpn_calc(expr), expected_result)

    def test_when_two_numbers_are_passed_then_return_multi_of_them(self):
        expr = '4 5 *'
        expected_result = 20.0

        self.assertEqual(rpn_calc(expr), expected_result)

    def test_when_two_numbers_are_passed_then_return_deletion_of_them(self):
        expr = '20 5 /'
        expected_result = 4.0

        self.assertEqual(rpn_calc(expr), expected_result)

    def test_when_number_is_passed_then_return_SQRT_of_it(self):
        expr = '9 SQRT'
        expected_result = 3.0

        self.assertEqual(rpn_calc(expr), expected_result)

if __name__ == "__main__":
    unittest.main()