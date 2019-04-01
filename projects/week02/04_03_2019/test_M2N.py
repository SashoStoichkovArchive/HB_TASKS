import unittest
from week2_solutions import message_to_numbers

class TestMessageToNumbers(unittest.TestCase):
    def test_when_capital_letter_is_passed_then_return_one_and_its_numbers(self):
        self.assertEquals(message_to_numbers('P'), [1, 7])

    def test_if_space_is_passed_then_zero_is_returned(self):
        self.assertTrue(0 in message_to_numbers('I am'))

    def test_when_two_consequtive_letters_on_one_key_then_minus_one_is_returned(self):
        self.assertTrue(-1 in message_to_numbers('aa'))

if __name__ == "__main__":
    unittest.main()