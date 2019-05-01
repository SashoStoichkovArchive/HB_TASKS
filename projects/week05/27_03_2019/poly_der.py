import re

class Monomial:
    def __init__(self, monomial):
        self._sign = Monomial.parse_sign(monomial)
        self._variable = Monomial.parse_variable(monomial)
        self._exponent = Monomial.parse_exponent(monomial, self._variable)
        self._coefficient = Monomial.parse_coefficient(monomial, self._variable)

    def __str__(self):
        monomial_str = ''
        if self.coefficient != 1:
            monomial_str += str(self.coefficient)
        if self.variable != '':
            monomial_str += self.variable
        elif self.variable == '' and self.coefficient == 1:
            monomial_str += str(self.coefficient)
        if self.exponent > 1:
            monomial_str += '^' + str(self.exponent)
        return monomial_str

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.coefficient == other.coefficient and self.exponent == other.exponent

    def __gt__(self, other):
        return self.exponent > other.exponent

    @property
    def sign(self):
        return self._sign

    @property
    def variable(self):
        return self._variable

    @property
    def exponent(self):
        return self._exponent

    @property
    def coefficient(self):
        return self._coefficient

    @staticmethod
    def parse_sign(monomial):
        pattern = re.compile(r'[-+]')
        sign = pattern.search(monomial)
        return sign[0] if sign else '+'

    @staticmethod
    def parse_variable(monomial):
        pattern = re.compile(r'[a-zA-Z]')
        variable = pattern.search(monomial)
        return variable[0] if variable else ''

    @staticmethod
    def parse_exponent(monomial, variable):
        if variable == '':
            return 0
        else:
            pattern = re.compile(r'({})\^?(\d*)'.format(variable))
            match = pattern.search(monomial)
            if match:
                try:
                    exponent = int(match.group(2))
                except ValueError:
                    exponent = 1
        return exponent

    @staticmethod
    def parse_coefficient(monomial, variable):
        pattern = re.compile(r'\+?-?(\d*)\*?{}?'.format(variable))
        match = pattern.search(monomial)
        return int(match.group(1)) if match.group(1) else 1

    def get_first_derivative(self):
        if self.variable is '':
            return __class__('0')
        derivative = ''
        coefficient = self.coefficient * self.exponent
        exponent = self.exponent - 1
        if coefficient == 0:
            return __class__('')
        elif coefficient >= 1:
            derivative += str(coefficient) + '*'
        if exponent == 0:
            return __class__(self.sign + derivative)
        if exponent == 1:
            derivative += self.variable
        elif exponent > 1:
            derivative += self.variable + '^' + str(exponent)
        return __class__(self.sign + derivative)

class Polynomial:
    def __init__(self, polynomial):
        self.monomial_list = polynomial

    @property
    def monomial_list(self):
        return self._monomial_list

    @monomial_list.setter
    def monomial_list(self, polynomial):
        pattern = re.compile(r'\+?-?[0-9a-zA-Z*^]*')
        self._monomial_list = [Monomial(monomial)
                               for monomial in re.findall(pattern, polynomial)[:-1:]]

    def get_first_derivative(self):
        deriv_list = [monomial.get_first_derivative()
                      for monomial in self.monomial_list]
        return deriv_list

    def print_first_derivative(self):
        deriv_list = self.get_first_derivative()
        deriv_list.sort(key=lambda monomial: monomial.exponent, reverse=True)
        try:
            first_deriv = str(deriv_list[0]) if str(deriv_list[0]) != '0' else ''
            for deriv in deriv_list[1:]:
                if str(deriv) != '0':
                    first_deriv += deriv.sign + str(deriv)
        except IndexError:
            pass
        else:
            return first_deriv

if __name__ == "__main__":
    p = Polynomial('x^3+x+2*x+x^10')
    print(p.print_first_derivative())