import unittest, fractions

class TestFractions(unittest.TestCase):
    def test_when_nominator_is_equal_to_denominator_then_return_tuple_containing_two_ones(self):
        t = (3, 3)
        expected_result = (1, 1)

        self.assertEqual(fractions.simplify_fraction(t), expected_result)

    def test_when_fraction_cannot_be_simplified_then_return_the_same_fraction(self):
        t = (7, 3)
        expected_result = (7, 3)

        self.assertEqual(fractions.simplify_fraction(t), expected_result)
    
    def test_when_fraction_can_be_simplified_then_return_simplified_fraction(self):
        t = (63, 462)
        expected_result = (3, 22)

        self.assertEqual(fractions.simplify_fraction(t), expected_result)

    def test_when_fractions_are_with_equal_denominators_then_return_simplified_fraction_with_summed_nominators_and_dominators(self):
        lst = [(1, 6), (2, 6), (3, 6)]
        expected_result = (1, 1)

        self.assertEqual(fractions.collect_fractions(lst), expected_result)

    def test_when_fractions_are_not_with_equal_denominators_then_return_simplified_fraction_with_summed_nominators_and_dominators(self):
        lst = [(1, 7), (2, 6), (4, 5)]
        expected_result = (134, 105)
        
        self.assertEqual(fractions.collect_fractions(lst), expected_result)

    def test_sort_fractions_function(self):
        lst = [(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]
        expected_result = [(22, 78), (15, 32), (5, 6), (7, 8), (9, 6), (22, 7)]

        self.assertEqual(fractions.sort_fractions(lst), expected_result)

if __name__ == "__main__":
    unittest.main()