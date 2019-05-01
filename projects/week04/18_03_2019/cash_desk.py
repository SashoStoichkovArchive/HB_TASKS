class Bill:
    def __init__(self, amount):
        self.validate_amount(amount)
        self.amount = amount

    def __str__(self):
        return 'A {} $ bill'.format(self.amount)

    def __int__(self):
        return self.amount

    def __eq__(self, other):
        return True if self.amount == other.amount else False

    def __repr__(self):
        return 'Bill object at {}'.format(id(self))

    def __hash__(self):
        return self.amount

    def validate_amount(self, amount):
        if not isinstance(amount, int):
            raise TypeError('Error, provided data not in correct format!')
        elif amount < 0:
            raise ValueError('Error, amount must be greater than 1!')


class BillBatch:
    def __init__(self, bill_list):
        self.bill_list = bill_list
    
    def __len__(self):
        return len(self.bill_list)

    def __getitem__(self, index):
        return self.bill_list[index]
    
    def total(self):
        return sum([int(bill) for bill in self.bill_list])


class CashDesk:
    def __init__(self):
        self.desk = []

    def take_money(self, bills):
        if isinstance(bills, BillBatch):
            self.desk += bills
        elif isinstance(bills, Bill):
            self.desk.append(bills)
        else:
            raise TypeError('Error, provided data is not and instance of BillBatch or Bill!')

    def __getitem__(self, index):
        return self.desk[index]

    def __len__(self):
        return len(self.desk)

    def total(self):
        return sum([int(bill) for bill in self.desk])

    def inspect(self):
        bill_table = {}
        for bill in desk:
            if bill not in bill_table:
                bill_table[bill] = 1
            else:
                bill_table[bill] += 1
        for bill, number in bill_table.items():
            print(bill, number)


if __name__ == '__main__':
    values = [10, 20, 50, 100, 100, 100]
    bills = [Bill(value) for value in values]

    batch = BillBatch(bills)

    desk = CashDesk()

    desk.take_money(batch)
    desk.take_money(Bill(10))

    print(desk.total()) # 390
    desk.inspect()

    values = [10, 20, 50, 100]
    bills = [Bill(value) for value in values]

    batch = BillBatch(bills)

    for bill in batch:
        print(bill)
    
    print(batch.total())

    a = Bill(10)
    b = Bill(5)
    c = Bill(8)

    money_holder = {}
    money_holder[c] = 1
    if c in money_holder:
        money_holder[c] += 1
    print(money_holder)