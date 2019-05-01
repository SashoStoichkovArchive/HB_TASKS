import unittest
import filter


class TestFilter(unittest.TestCase):
    data = [['full_name', 'favourite_color', 'company_name', 'email', 'phone_number', 'salary'],
            ['Michael Olson', 'olive', 'Scott, Young and King', 'zacharymcdonald@yahoo.com', '114-116-1124x315',
             '2151'],
            ['Diana Harris', 'lime', 'Martin-Barnes', 'timothy81@gmail.com', '1-860-251-9980x6941', '5354'],
            ['Marilyn Maldonado', 'black', 'Walker PLC', 'gmcintosh@yahoo.com', '+49(1)7897611670', '7158'],
            ['David Frye', 'silver', 'Willis Inc', 'stricklandjessica@gmail.com', '422.395.8104', '5090'],
            ['David Lopez', 'purple', 'Singh Ltd', 'hcrosby@yahoo.com', '853.603.6658x134', '7266']]

    def test_validate_keys_with_existing_keys_given_return_true(self):
        kwargs = {'full_name': '', 'favourite_color': '',
                  'company_name': '', 'email': '',
                  'phone_number': '', 'salary': ''}
        self.assertTrue(filter.validate_keys(TestFilter.data, kwargs))

    def test_if_full_name_passed_return_people_with_full_name(self):
        expected_result = [['Diana Harris', 'lime', 'Martin-Barnes',
                           'timothy81@gmail.com', '1-860-251-9980x6941', '5354']]
        self.assertEqual(filter.filter(TestFilter.data, full_name='Diana Harris'), expected_result)

    def test_if_favourite_color_is_passed_return_people_with_that_color(self):
        expected_result = [['Marilyn Maldonado', 'black', 'Walker PLC',
                            'gmcintosh@yahoo.com', '+49(1)7897611670', '7158']]
        self.assertEqual(filter.filter(TestFilter.data, favourite_color='black'), expected_result)

    def test_if_company_name_is_passed_return_people_from_that_company(self):
        expected_result = [['Marilyn Maldonado', 'black', 'Walker PLC',
                            'gmcintosh@yahoo.com', '+49(1)7897611670', '7158']]
        self.assertEqual(filter.filter(TestFilter.data, company_name='Walker PLC'), expected_result)

    def test_if_email_is_passed_return_people_with_that_email(self):
        expected_result = [['Diana Harris', 'lime', 'Martin-Barnes',
                            'timothy81@gmail.com', '1-860-251-9980x6941', '5354']]
        self.assertEqual(filter.filter(TestFilter.data, email='timothy81@gmail.com'), expected_result)

    def test_if_phone_number_is_passed_return_people_with_that_phone_number(self):
        expected_result = [['Diana Harris', 'lime', 'Martin-Barnes',
                           'timothy81@gmail.com', '1-860-251-9980x6941', '5354']]
        self.assertEqual(filter.filter(TestFilter.data, phone_number='1-860-251-9980x6941'), expected_result)

    def test_if_a_non_existent_argument_is_passed_return_an_empty_list(self):
        expected_result = []
        self.assertEqual(filter.filter(TestFilter.data, non_existing_arg=''), expected_result)

if __name__ == '__main__':
    unittest.main()