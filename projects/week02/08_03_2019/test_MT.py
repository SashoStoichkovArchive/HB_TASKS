import unittest
import money_tracker as mt


class TestMoneyTracker(unittest.TestCase):
    def test_when_if_correct_is_read_then_correct_data_struct_is_build_and_returned(self):
        user_data = ['=== 22-03-2019 ===\n',
                     '10, Deposit, New Income\n', "27.7, Food, New Expense\n",
                     '=== 23-03-2019 ===\n',
                     '700, Salary, New Income\n', '50, Savings, New Income\n',
                     '4, Eating Out, New Expense\n']
        expected_result = {'22-03-2019': {'income': [(10, 'Deposit')], 'expense': [(27.7, 'Food')]},
                           '23-03-2019': {'income': [(700, 'Salary'), (50, 'Savings')], 'expense': [(4, 'Eating Out')]}}
        self.assertEqual(mt.build_user_data(user_data), expected_result)

    def test_show_user_incomes(self):
        user_data = {'22-03-2019': {'income': [(10, 'Deposit')], 'expense': [(27.7, 'Food')]},
                     '23-03-2019': {'income': [(700, 'Salary'), (50, 'Savings')], 'expense': [(4, 'Eating Out')]}}
        expected_result = [(10, 'Deposit'), (700, 'Salary'), (50, 'Savings')]
        self.assertEqual(mt.show_user_incomes(user_data), expected_result)

    def test_show_user_savings(self):
        user_data = {'22-03-2019': {'income': [(10, 'Deposit')], 'expense': [(27.7, 'Food')]},
                     '23-03-2019': {'income': [(700, 'Salary'), (50, 'Savings')], 'expense': [(4, 'Eating Out')]}}
        expected_result = [(50, 'Savings')]
        self.assertEqual(mt.show_user_savings(user_data), expected_result)

    def test_show_user_deposits(self):
        user_data = {'22-03-2019': {'income': [(10, 'Deposit')], 'expense': [(27.7, 'Food')]},
                     '23-03-2019': {'income': [(700, 'Salary'), (50, 'Savings')], 'expense': [(4, 'Eating Out')]}}
        expected_result = [(10, 'Deposit')]
        self.assertEqual(mt.show_user_deposits(user_data), expected_result)

    def test_show_user_expenses(self):
        user_data = {'22-03-2019': {'income': [(10, 'Deposit')], 'expense': [(27.7, 'Food')]},
                     '23-03-2019': {'income': [(700, 'Salary'), (50, 'Savings')], 'expense': [(4, 'Eating Out')]}}
        expected_result = [(27.7, 'Food'), (4, 'Eating Out')]
        self.assertEqual(mt.show_user_expenses(user_data), expected_result)

    def test_list_user_expenses_ordered_by_categories(self):
        user_data = {'22-03-2019': {'income': [(10, 'Deposit')], 'expense': [(27.7, 'Food')]},
                     '23-03-2019': {'income': [(700, 'Salary'), (50, 'Savings')], 'expense': [(4, 'Eating Out')]}}
        expected_result = [(4, 'Eating Out'), (27.7, 'Food')]
        self.assertEqual(mt.list_user_expenses_ordered_by_categories(user_data), expected_result)

    def test_show_user_data_per_date(self):
        date = '23-03-2019'
        user_data = {'22-03-2019': {'income': [(10, 'Deposit')], 'expense': [(27.7, 'Food')]},
                     '23-03-2019': {'income': [(700, 'Salary'), (50, 'Savings')], 'expense': [(4, 'Eating Out')]}}
        expected_result = [(700, 'Salary', 'New Income'), (50, 'Savings', 'New Income'),
                           (4, 'Eating Out', 'New Expense')]
        self.assertEqual(mt.show_user_data_per_date(date, user_data), expected_result)

    def test_list_income_categories(self):
        user_data = {'22-03-2019': {'income': [(10, 'Deposit')], 'expense': [(27.7, 'Food')]},
                     '23-03-2019': {'income': [(700, 'Salary'), (50, 'Savings')], 'expense': [(4, 'Eating Out')]}}
        expected_result = ['Deposit', 'Salary', 'Savings']
        self.assertEqual(mt.list_income_categories(user_data), expected_result)

    def test_list_expense_categories(self):
        user_data = {'22-03-2019': {'income': [(10, 'Deposit')], 'expense': [(27.7, 'Food')]},
                     '23-03-2019': {'income': [(700, 'Salary'), (50, 'Savings')], 'expense': [(4, 'Eating Out')]}}
        expected_result = ['Food', 'Eating Out']
        self.assertEqual(mt.list_expense_categories(user_data), expected_result)

    def test_add_income_with_valid_input_when_date_given_in_user_data(self):
        label = 'Savings'
        amount = 100
        date = '22-03-2019'
        user_data = {'22-03-2019': {'income': [(10, 'Deposit')], 'expense': [(27.7, 'Food')]},
                     '23-03-2019': {'income': [(700, 'Salary'), (50, 'Savings')], 'expense': [(4, 'Eating Out')]}}
        mt.add_income(label, amount, date, user_data)
        incomes_in_data = user_data[date]['income']
        self.assertIn((amount, label), incomes_in_data)

    def test_add_income_with_valid_input_when_date_given_not_in_user_data(self):
        label = 'Savings'
        amount = 100
        date = '24-03-2019'
        user_data = {'22-03-2019': {'income': [(10, 'Deposit')], 'expense': [(27.7, 'Food')]},
                     '23-03-2019': {'income': [(700, 'Salary'), (50, 'Savings')], 'expense': [(4, 'Eating Out')]}}
        mt.add_income(label, amount, date, user_data)
        incomes_in_data = user_data[date]['income']
        self.assertIn((amount, label), incomes_in_data)

    def test_add_expense_with_valid_input_when_date_given_in_user_data(self):
        label = 'Club'
        amount = 20
        date = '22-03-2019'
        user_data = {'22-03-2019': {'income': [(10, 'Deposit')], 'expense': [(27.7, 'Food')]},
                     '23-03-2019': {'income': [(700, 'Salary'), (50, 'Savings')], 'expense': [(4, 'Eating Out')]}}
        mt.add_expense(label, amount, date, user_data)
        incomes_in_data = user_data[date]['expense']
        self.assertIn((amount, label), incomes_in_data)

    def test_add_expense_with_valid_input_when_date_given_not_in_user_data(self):
        label = 'Club'
        amount = 20
        date = '24-03-2019'
        user_data = {'22-03-2019': {'income': [(10, 'Deposit')], 'expense': [(27.7, 'Food')]},
                     '23-03-2019': {'income': [(700, 'Salary'), (50, 'Savings')], 'expense': [(4, 'Eating Out')]}}
        mt.add_expense(label, amount, date, user_data)
        incomes_in_data = user_data[date]['expense']
        self.assertIn((amount, label), incomes_in_data)


if __name__ == "__main__":
    unittest.main()