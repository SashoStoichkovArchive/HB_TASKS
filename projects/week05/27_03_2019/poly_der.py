import sys

class Monomial:
    def __init__(self, mono):
        self.mono = mono

    def get_derivative(self):
        if self.mono[0] in '-123456789':
            c = self.mono[0]
        
        for i in range(1, len(self.mono)):
            if self.mono[i] in '0123456789':
                c += self.mono[i]
                if i == len(self.mono) - 1:
                    return str(0)
            else:
                if self.mono[i] in 'qwertyuiopasdfghjklzxcvbnm':
                    x = self.mono[i]
                    if i == len(self.mono) - 1:
                        return c
                    else:
                        i += 1
                        if self.mono[i] == '^':
                            i += 1
                            num = ''
                            while i <= len(self.mono) - 1:
                                num += self.mono[i]
                                i += 1

                            return str(int(c) * int(num)) + '*x^' + str(int(num) - 1)

class Polynomial(Monomial):
    def __init__(self, poly):
        self.poly = poly

    def get_monomials(self):
        arr = []
        i = 0

        while i <= len(self.poly)-1:
            string = ''

            if self.poly[i] == '-':
                string += self.poly[i]
                i += 1

            while i <= len(self.poly)-1 and self.poly[i] not in '+-':
                string += self.poly[i]
                i += 1

            arr.append(string)

            if i <= len(self.poly) - 1 and self.poly[i] == '+':
                i += 1
            else:
                continue

        return arr

    def get_derivatives(self):
        arr = self
        der = []

        for mono in arr:
            mon = Monomial(mono)
            der.append(mon.get_derivative())

        return der

    def get_result(self):
        der = self
        result = ''

        for deriv in der:
            if deriv == '0':
                continue
            else:
                if deriv[0] in '123456789':
                    result = result + '+' + deriv
                else:
                    result += deriv

        return result
