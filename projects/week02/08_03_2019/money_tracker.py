def int_or_float(n: float):
    return int(n) if n.is_integer() else n


def build_user_data(content):
    user_data = {}
    for line in content:
        if '=' in line:
            curr_date = line.strip('=\n ')
            user_data[curr_date] = {'income': [], 'expense': []}
        else:
            amount, label, category = line.split(', ')
            if 'income' in category.lower():
                user_data[curr_date]['income'].append((int_or_float(float(amount)), label))
            elif 'expense' in category.lower():
                user_data[curr_date]['expense'].append((int_or_float(float(amount)), label))
    return user_data


def list_user_data(all_user_data):
    INC_STR = 'New Income'
    EXP_STR = 'New Expense'
    for date in all_user_data:
        print('=== {} ==='.format(date))
        for category in all_user_data[date]:
            for amount, label in all_user_data[date][category]:
                print('{}, {}, {}'.format(amount, label, INC_STR if category == 'income' else EXP_STR))


def show_user_incomes(all_user_data):
    result = []
    for date in all_user_data:
         result += all_user_data[date]['income']
    return result


def show_user_savings(all_user_data):
    result = [(amount, category) for date in all_user_data
              for amount, category in all_user_data[date]['income']
              if category == 'Savings']
    return result

def show_user_deposits(all_user_data):
    result = [(amount, category) for date in all_user_data
              for amount, category in all_user_data[date]['income']
              if category == 'Deposit']
    return result


def show_user_expenses(all_user_data):
    result = []
    for date in all_user_data:
        try:
            result += all_user_data[date]['expense']
        except KeyError:
            pass
    return result


def list_user_expenses_ordered_by_categories(all_user_data):
    expenses = show_user_expenses(all_user_data)
    return sorted(expenses, key=lambda expense: expense[1])


def print_user_expenses_ordered_by_categories(all_user_data):
    print('Expenses by categories: ')
    for amount, category in list_user_expenses_ordered_by_categories(all_user_data):
        print(amount, category)


def show_user_data_per_date(date, all_user_data):
    INC_STR = 'New Income'
    EXP_STR = 'New Expense'
    result = [(amount, label, INC_STR if category == 'income' else EXP_STR)
              for category in all_user_data[date]
              for amount, label in all_user_data[date][category]]
    return result


def print_user_data_per_date(date, all_user_data):
    data_per_date = show_user_data_per_date(date, all_user_data)
    print('=== {} ==='.format(date))
    for amount, label, category in data_per_date:
        print('{}, {}, {}'.format(amount, label, category))


def list_income_categories(all_user_data):
    categories = [category for date in all_user_data
                  for amount, category in all_user_data[date]['income']]
    return categories


def list_expense_categories(all_user_data):
    categories = [category for date in all_user_data
                  for amount, category in all_user_data[date]['expense']]
    return categories


def add_income(income_category, money, date, all_user_data):
    _add_income_or_expense('income', income_category, money, date, all_user_data)


def add_expense(expense_category, money, date, all_user_data):
    _add_income_or_expense('expense', expense_category, money, date, all_user_data)


def _add_income_or_expense(inc_or_exp, category, money, date, all_user_data):
    if date in all_user_data:
        if inc_or_exp in all_user_data[date]:
            all_user_data[date][inc_or_exp].append((money, category))
        else:
            all_user_data[date][inc_or_exp] = [(money, category)]
    else:
        all_user_data[date] = {inc_or_exp: [(money, category)]}


def get_income_or_expense(inc_or_exp):
    prompt = 'New Income ' if inc_or_exp == 'income' else 'New Expense '
    amount = get_amount(prompt)
    label = input(prompt + 'type: ')
    date = get_date(prompt)
    return amount, label.capitalize(), date


def get_amount(prompt):
    while True:
        amount = input(prompt + 'amount: ')
        if validate_amount(amount):
            return int_or_float(float(amount))


def validate_amount(amount):
    try:
        amount = float(amount)
        if amount < 0:
            raise ValueError
        return True
    except ValueError:
        print("Error, amount must be a positive number!")
        return False


def get_date(prompt=''):
    while True:
        date = input(prompt + 'date: ')
        if validate_date(date):
            return date


def validate_date(date):
    from datetime import datetime
    try:
        datetime.strptime(date, '%d-%m-%Y')
        return True
    except ValueError:
        print("Error, provided date not in correct format, expected D-M-YYYY, got {}".format(date))
        return False


def read_data():
    try:
        with open('money_tracker.txt') as dbfile:
            content = dbfile.readlines()
        return content
    except FileNotFoundError:
        print("Error, database not found!")
        return None


def print_menu():
    print("""\nChoose one of the following options to continue:
1 - show all data
2 - show data for specific date
3 - show expenses, ordered by categories
4 - add new income
5 - add new expense
6 - exit\n""")


def get_input():
    print_menu()
    try:
        choice = int(input('Choice: '))
    except ValueError:
        print("\nError, provided value not a valid integer!\nPlease try again\n")
        return -1
    else:
        if choice < 1 or choice > 6:
            print("\nError, provided value not in range form 1 to 6!\nPlease try again\n")
            return -1
    return choice


def main():
    print("Hello!")
    content = read_data()
    all_user_data = build_user_data(content)
    while True:
        choice = get_input()
        if choice == 1:
            list_user_data(all_user_data)
        elif choice == 2:
            date = get_date()
            print_user_data_per_date(date, all_user_data)
        elif choice == 3:
            print_user_expenses_ordered_by_categories(all_user_data)
        elif choice == 4:
            amount, label, date = get_income_or_expense('income')
            add_income(label, amount, date, all_user_data)
        elif choice == 5:
            amount, label, date = get_income_or_expense('expense')
            add_expense(label, amount, date, all_user_data)
        elif choice == 6:
            break
        elif choice == -1:
            continue

if __name__ == '__main__':
    main()

