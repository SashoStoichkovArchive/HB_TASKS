import math

def rpn_calc(expr):
    expr_arr = expr.split(' ')

    operators = ['+', '-', '*', '/', 'SQRT']

    if operators not in expr_arr and len(expr_arr) == 1:
        return float(expr_arr[0])

    for i in range(len(expr_arr)):
        if expr_arr[i] in operators:
            if expr_arr[i] == '+':
                expr_arr[i-1] = str(int(expr_arr[i-2]) + int(expr_arr[i-1]))
                expr_arr.pop(0)
                expr_arr.pop(i-1)

            elif expr_arr[i] == '-':
                expr_arr[i-1] = str(int(expr_arr[i-2]) - int(expr_arr[i-1]))
                expr_arr.pop(0)
                expr_arr.pop(i-1)

            elif expr_arr[i] == '*':
                expr_arr[i-1] = str(int(expr_arr[i-2]) * int(expr_arr[i-1]))
                expr_arr.pop(0)
                expr_arr.pop(i-1)

            elif expr_arr[i] == '/':
                expr_arr[i-1] = str(int(expr_arr[i-2]) / int(expr_arr[i-1]))
                expr_arr.pop(0)
                expr_arr.pop(i-1)

            elif expr_arr[i] == 'SQRT':
                expr_arr[i-1] = str(math.sqrt(int(expr_arr[i-1])))
                expr_arr.pop(i)

    return float(expr_arr[0])

if __name__ == "__main__":
    print(rpn_calc('20 4 /'))
    print(rpn_calc('9 SQRT'))
    print(rpn_calc('4 2 + 3 -'))
    print(rpn_calc('3 5 8 * 7 + *'))
