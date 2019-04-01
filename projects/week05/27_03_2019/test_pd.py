import unittest, poly_der

class TestPolyDer(unittest.TestCase):
    def test_when_constant_is_passed_then_return_zero(self):
        mono = '1534310'
        expected_result = '0'

        self.assertEqual(poly_der.Monomial(mono).get_derivative(), expected_result)

    def test_when_number_and_x_is_passed_then_return_number(self):
        mono = '-10*x'
        expected_result = '-10'

        self.assertEqual(poly_der.Monomial(mono).get_derivative(), expected_result)

    def test_when_monomial_and_x_is_passed_then_return_derivative(self):
        mono = '-10*x^3'
        expected_result = '-30*x^2'

        self.assertEqual(poly_der.Monomial(mono).get_derivative(), expected_result)

    def test_when_polynomial_is_passed_then_return_list_of_monomials(self):
        poly = '-2x^3+3x-1'
        expected_result = ['-2x^3', '3x', '-1']

        self.assertEqual(poly_der.Polynomial(poly).get_monomials(), expected_result)

    def test_when_list_of_monomials_of_a_polynomial_is_passed_return_list_of_derivatives_of_each_monomial(self):
        poly = '-2x^3+3x-1'        
        expected_result = ['-6*x^2', '3', '0']

        self.assertEqual(poly_der.Polynomial.get_derivatives(poly_der.Polynomial(poly).get_monomials()), expected_result)


    def test_when_list_of_derivatives_of_the_monomials_of_a_polynomial_is_passed_then_return_result_string(self):
        poly = '-2x^3+3x-1'        
        expected_result = '-6*x^2+3'

        self.assertEqual(poly_der.Polynomial.get_result(poly_der.Polynomial.get_derivatives(poly_der.Polynomial(poly).get_monomials())), expected_result)

if __name__ == "__main__":
    unittest.main()