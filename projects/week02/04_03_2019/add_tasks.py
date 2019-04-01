def anagrams():
    w1 = str(input())
    w2 = str(input())

    if sorted(w1) == sorted(w2):
        return "ANAGRAMS"

    else:
        return "NOT ANAGRAMS"

# anagrams()

def to_digits(n):
	n = abs(n)

	return [int(char) for char in str(n)]

def is_credit_card_valid(number):
    arr = to_digits(number)
    str_number = ""

    if len(arr) % 2 == 0:
        return False

    for index in range(len(arr)):
        if index % 2 != 0:
            arr[index] *= 2
            str_number += str(arr[index])
        else:
            str_number += str(arr[index])

    sum_of_dig_in_arr = 0

    for digit in str_number:
        sum_of_dig_in_arr += int(digit)

    return sum_of_dig_in_arr % 10 == 0

# print(79927398713, is_credit_card_valid(79927398713))
# print(79927398715, is_credit_card_valid(79927398715))

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0: 
            return False
  
    return True

def goldbach(n):
    result = []

    for number in range(2, n + 1):
        if is_prime(number) and is_prime(n - number):
            result.append((number, n - number))

    if len(result) % 2 == 0:
        return result[:(len(result) // 2)]

    elif len(result) % 3 == 0:
        return result[:(len(result) // 2) + 1]

    return result

# print(goldbach(8))