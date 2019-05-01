import unittest
import matrix_bombing as mb

class TestMatrixBombing(unittest.TestCase):
    def test_when_matrix_and_coordinates_are_passed_then_return_matrix_with_numbers_after_a_bomb_drop(self):
        m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        exp = [[0, 0, 0], [0, 5, 1], [2, 3, 4]]

        self.assertEqual(mb.drop_bomb(m, 1, 1), exp)

    def test_when_matrix_is_passed_then_return_the_sum_of_the_numbers_in_it(self):
        m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        
        self.assertEqual(mb.sum_of_el_in_matrix(m), 45)

    def test_when_matrix_is_passed_then_return_a_dictionary_of_the_bombing_plan(self):
        m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        exp = {(0, 0): 42, (0, 1): 36, (0, 2): 37, (1, 0): 30, (1, 1): 15,
               (1, 2): 23, (2, 0): 29, (2, 1): 15, (2, 2): 26}

        self.assertEqual(mb.matrix_bombing_plan(m), exp)

if __name__ == "__main__":
    unittest.main()