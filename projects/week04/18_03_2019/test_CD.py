import unittest
import cash_desk as cd


class TestBill(unittest.TestCase):
    def setUp(self):
        self.bill = cd.Bill(10)

    def test_if_str_method_returns_correct_string(self):
        self.assertEqual(str(self.bill), 'A 10 $ bill')

    def test_if_int_method_returns_bill_amount_as_int(self):
        self.assertEqual(int(self.bill), 10)

    def test_if_a_negative_number_is_given_as_init_argument_raise_value_error(self):
        self.assertRaises(ValueError, cd.Bill, -10)

    def test_if_a_different_type_from_int_is_given_return_TypeError(self):
        self.assertRaises(TypeError, cd.Bill, '10')

    def test_if_bills_with_same_amount_are_compared_then_return_true(self):
        bill1 = cd.Bill(1)
        bill2 = cd.Bill(1)
        self.assertTrue(bill1 == bill2)

    def test_if_bills_with_different_amount_are_compared_then_return_false(self):
        bill1 = cd.Bill(1)
        bill2 = cd.Bill(2)
        self.assertFalse(bill1 == bill2)

    def test_if_hash_method_works(self):
        temp_dict = {}
        temp_dict[self.bill] = 1
        self.assertEqual(temp_dict[self.bill], 1)


class TestBillBatch(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()