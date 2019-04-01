class Bill:
    def __init__(self, amount):
        if type(amount) is not int:
            raise TypeError("String is not integer")
        if amount < 0:
            raise ValueError("Integer is less than 0")
        
        self.amount = amount
    
    def __str__(self):
        return "A {0}$ {1}".format(self.amount, "Bill")

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return True

    def __hash__(self):
        return hash(self.amount*(self.amount^2)*(self.amount*(self.amount + (self.amount*365))))

    def __int__(self):
        return self.amount

class BillBatch:
    def __init__(self, batch):
        self.batch = batch

    def __len__(self):
        return len(self.batch)

    def total(self):
        result = 0

        for i in range(self.__len__()):
            result += self.batch[i]

        return result

    def __getitem__(self, index):
        return self.batch[index]

class CashDesk:
    def __init__(self):
        self.desk = {}
        self.all_money = []

    def take_money(self, money):
        count = 1
        if isinstance(money, Bill):
            self.all_money.append(money)
            if "{0}$ bills".format(money) not in self.desk:
                self.desk.update({"{0}$ bills".format(money): count})
            else:
                self.desk.update({"{0}$ bills".format(money): count+1})
        else:
            for i in range(money.__len__()):
                self.all_money.append(money[i])
                if "{0}$ bills".format(money[i]) not in self.desk:
                    self.desk.update({"{0}$ bills".format(money[i]): count})
                else:
                    self.desk.update({"{0}$ bills".format(money[i]): count+1})

    def __len__(self):
        return len(self.desk)

    def total(self):
        result = 0

        for el in self.all_money:
            result += int(el)

        return result

    def inspect(self, money):
        print("We have a total of {0}$ in the desk".format(self.total()))
        print("We have the following count of bills")
        
if __name__ == "__main__":
    values = [10, 20, 50, 100, 100, 100]
    bills = [Bill(value) for value in values]

    batch = BillBatch(bills)

    desk = CashDesk()

    desk.take_money(batch)
    desk.take_money(Bill(10))

    print(desk.total()) # 390
    desk.inspect(values)

    # We have a total of 390$ in the desk
    # We have the following count of bills, sorted in ascending order:
    # 10$ bills - 2
    # 20$ bills - 1
    # 50$ bills - 1
    # 100$ bills - 3