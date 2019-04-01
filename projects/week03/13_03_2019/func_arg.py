def sum_in_range(s_index, e_index, step=1):
    return sum(list(range(s_index, e_index, step)))

def sum_of_numbers(number1, *args, number2=10, **kwargs):
    # print(args)
    # print(len(args))
    return number1 + sum(args) + number2 + sum(kwargs.values())

def append_to_list(number, lst=[]):
    lst.append(number)
    return lst

if __name__ == "__main__":
    # print(sum_in_range(0, 10, 2))
    # print(sum_of_numbers(1, **{'number3':3}))
    print(append_to_list(7, [2, 3]))