def simplify_fraction(fraction):
    if fraction[0] == fraction[1]:
        return (1, 1)

    nominator = fraction[0]
    denominator = fraction[1]

    for i in range(1, min(fraction) + 1):
        if nominator % i == 0 and denominator % i == 0:
            nominator //= i
            denominator //= i

    return (nominator, denominator)

def collect_fractions(fractions):
    denominators = []
    for i in range(len(fractions)):
        denominators.append(fractions[i][1])

    are_all_dominators_equal = True

    for i in range(len(denominators)):
        if denominators[i] != denominators[0]:
            are_all_dominators_equal = False

    result_nominator = 0
    mul_denominator = 1

    if are_all_dominators_equal:
        for i in range(len(fractions)):
            result_nominator += fractions[i][0]

        return simplify_fraction((result_nominator, denominators[0]))

    else:
        for i in range(len(fractions)):
            mul_denominator *= fractions[i][1]

        for i in range(len(fractions)):
            result_nominator += fractions[i][0] * (mul_denominator // fractions[i][1])

        return simplify_fraction((result_nominator, mul_denominator))

from collections import OrderedDict

def sort_fractions(fractions):
    results = {}

    for i in range(len(fractions)):
        results.update({fractions[i]: fractions[i][0]/fractions[i][1]})

    sorted_results = OrderedDict(sorted(results.items(), key=lambda x: x[1]))

    result = []

    for key in sorted_results:
        result.append(key)

    return result