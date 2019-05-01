import unittest
from poly_der import Monomial

class TestPolynomials(unittest.TestCase):
    def setUp(self):
        self.monomial = Monomial('3*x^2')

    def test_when_a_valid_monomial_is_given_return_variable(self):
        expected_result = 'x'
        self.assertEqual(self.monomial.variable, expected_result)

    def test_when_exponent_in_monomial_is_2_then_return_2(self):
        expected_result = 2
        self.assertEqual(self.monomial.exponent, expected_result)

    def test_when_no_exponent_in_monomial_then_return_1(self):
        expected_result = 1
        monomial = Monomial('2*x')
        self.assertEqual(monomial.exponent, expected_result)

    def test_when_coefficient_in_monomial_is_3_then_return_3(self):
        expected_result = 3
        self.assertEqual(self.monomial.coefficient, expected_result)

    def test_when_no_coefficient_in_monomial_then_return_1(self):
        monomial = Monomial('x')
        expected_result = Monomial('1')
        self.assertEqual(monomial.get_first_derivative(), expected_result)

    def test_when_monomial_is_x_to_the_power_of_2_then_return_2x(self):
        monomial = Monomial('x^2')
        expected_result = Monomial('2x')
        self.assertEqual(monomial.get_first_derivative(), expected_result)

if __name__ == '__main__':
    unittest.main()