class Contract:
    def __init__(self, car, person, money):
        self.car = car
        self.person = person
        self._money = money

    # def get_money(self):
    #     return self._money * 1.95

    # def set_money(self, value):
    #     self._money = value

    # def del_money(self):
    #     del self._money

    # money = property(get_money, set_money, del_money)

    @property
    def get_money(self):
        return self._money * 1.95

    # @money.setter
    # def money(self, value):
    #     self._money = value

contract_mazda = Contract('Mazda', 'Pesho', 7500)

# contract_mazda.set_money(9400)
contract_mazda.money = 9452
print(contract_mazda.money)