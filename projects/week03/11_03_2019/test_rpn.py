import unittest
import rpn

class TestReversedPolishNotation(unittest.TestCase):
    def test_when_float_number_has_no_remainder_return_int(self):
        n = 9.0
        expected_result = 9
        self.assertEqual(rpn.int_or_float(n), expected_result)

    def test_when_float_number_has_no_remainder_return_float(self):
        n = 9.5
        expected_result = 9.5
        self.assertEqual(rpn.int_or_float(n), expected_result)

    def test_when_two_integers_are_passed_to_evaluate_return_their_sum(self):
        op1 = '2'
        op2 = '4'
        operator = '+'
        expected_result = 6
        self.assertEqual(rpn._evaluate(op1, op2, operator), expected_result)
    
    def test_when_two_integers_are_passed_to_evaluate_return_their_difference(self):
        op1 = '2'
        op2 = '4'
        operator = '-'
        expected_result = -2
        self.assertEqual(rpn._evaluate(op1, op2, operator), expected_result)

    def test_when_two_integers_are_passed_to_evaluate_return_their_product(self):
        op1 = '2'
        op2 = '4'
        operator = '*'
        expected_result = 8
        self.assertEqual(rpn._evaluate(op1, op2, operator), expected_result)

    def test_when_two_integers_are_passed_to_evaluate_return_their_quotient(self):
        op1 = '2'
        op2 = '4'
        operator = '/'
        expected_result = 0.5
        self.assertEqual(rpn._evaluate(op1, op2, operator), expected_result)
    
    def test_when_single_digit_is_passed_then_return_same_digit(self):
        expr = '2'
        expected_result = 2
        self.assertEqual(rpn.rpn_calculate(expr), expected_result)

    def test_when_two_numbers_are_passed_then_return_sum_of_them(self):
        expr = '4 2 +'
        expected_result = 6
        self.assertEqual(rpn.rpn_calculate(expr), expected_result)

    def test_when_operator_is_subtraction_of_two_numbers_then_return_the_difference(self):
        expr = '4 2 -'
        expected_result = 2
        self.assertEqual(rpn.rpn_calculate(expr), expected_result)

    def test_when_operator_is_muliplication_of_two_numbers_then_return_the_product(self):
        expr = '4 2 *'
        expected_result = 8
        self.assertEqual(rpn.rpn_calculate(expr), expected_result)

    def test_when_operator_is_division_of_two_numbers_then_return_the_quotient(self):
        expr = '4 2 /'
        expected_result = 2
        self.assertEqual(rpn.rpn_calculate(expr), expected_result)

    def test_when_operator_is_SQRT_and_operand_is_nine_then_return_three(self):
        expr = '9 SQRT'
        expected_result = 3
        self.assertEqual(rpn.rpn_calculate(expr), expected_result)

    def test_with_three_operands_and_two_operators_then_return_result(self):
        expr = '4 2 + 3 -'
        expected_result = 3
        self.assertEqual(rpn.rpn_calculate(expr), expected_result)

    def test_with_four_operands_and_three_operators_then_return_result(self):
        expr = '3 5 8 * 7 + *'
        expected_result = 141
        self.assertEqual(rpn.rpn_calculate(expr), expected_result)

    def test_with_SQRT_and_a_expression_then_return_result(self):
        expr = '1 4 SQRT +'
        expected_result = 3
        self.assertEqual(rpn.rpn_calculate(expr), expected_result)

    def test_with_three_operands_and_MAX_return_the_biggest(self):
        expr = '1 2 3 MAX'
        expected_result = 3
        self.assertEqual(rpn.rpn_calculate(expr), expected_result)

    def test_with_subtraction_operand_and_MAX_return_negative_of_biggest(self):
        expr = '1 2 3 MAX -'
        expected_result = -3
        self.assertEqual(rpn.rpn_calculate(expr), expected_result)
    
    def test_with_three_operands_and_MIN_return_the_biggest(self):
        expr = '1 2 3 MIN'
        expected_result = 1
        self.assertEqual(rpn.rpn_calculate(expr), expected_result)

    def test_with_subtraction_operand_and_MIN_return_negative_of_biggest(self):
        expr = '1 2 3 MIN -'
        expected_result = -1
        self.assertEqual(rpn.rpn_calculate(expr), expected_result)

    def test_with_expr_with_MIN_adn_MIN_chained_return_MIN(self):
        expr = '1 2 3 MAX MIN'
        expected_result = 3
        self.assertEqual(rpn.rpn_calculate(expr), expected_result)

    def test_with_expr_with_MIN_adn_MAX_chained_return_MIN(self):
        expr = '1 2 3 MIN MAX'
        expected_result = 1
        self.assertEqual(rpn.rpn_calculate(expr), expected_result)
    

if __name__ == '__main__':
    unittest.main()