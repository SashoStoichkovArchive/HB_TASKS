def sum_of_digits(n):
	return sum(to_digits(n))

# print(sum_of_digits(1325132435356))

def to_digits(n):
	n = abs()

	return [int(char) for char in str(n)]

# print(to_digits(9999))

def to_number(arr):
	chars = [str(digit) for digit in arr]

	return int(''.join(chars))

# print(to_number(['1', '2', '3']))

def factorial(n):
	if n == 0:
		return 1
	else:
		return (n * factorial(n - 1))

def fact_digits(n):
	return sum([fact(digit) for digit in to_digits(n)])

# print(fact_digits(999))

def palindrome(n):
	s_index = 0

	if type(n) == int:
		arr = to_digits(n)
		e_index = len(arr) - 1

		while s_index < e_index or s_index == e_index:
			if (arr[s_index] != arr[e_index]):
				return False

			s_index += 1
			e_index -= 1

		return True

	else:
		e_index = len(n) - 1

		while s_index < e_index or s_index == e_index:
			if (n[s_index] != n[e_index]):
				return False

			s_index += 1
			e_index -= 1

		return True		

# print(palindrome('asds'))

def count_vowels(string):
	count = 0

	lower_vowels = ['a', 'o', 'e', 'i', 'u', 'y']
	upper_vowels = []

	for i in range(len(lower_vowels)):
		upper_vowels += [lower_vowels[i].upper()]

	for char in arr:
		if char in lower_vowels or char in upper_vowels:
			count += 1

	return count

# print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))

def count_consonants(string):
	count = 0

	lower_consonants = ['q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
	upper_consonants = []

	for i in range(len(lower_consonants)):
		upper_consonants += [lower_consonants[i].upper()]

	for char in arr:
		if char in lower_consonants or char in upper_consonants:
			count += 1

	return count

# print(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))

def char_histogram(string):
    result = {}

    for char in string:
        result[char] = result.get(char, 0) + 1

    return result

# print(char_histogram("asd `aasd"))

def sum_of_digits_in_arr(arr):
	result = 0

	for i in arr:
		result += i

	return result

def sum_matrix(m):
	result = 0

	for i in range(len(m)):
		result += sum_of_digits_in_arr(m[i])

	return result

# print(sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))

def nan_expand(times):
	return "Not a " * times + "NaN"

print(nan_expand(100))

def prime_factorization(num):
	factors = []
	result = []
	
	if num == 1:
		return [(1)]

	for i in range(2, num + 1):
		if num % i == 0:
			is_prime = 1

			for j in range(2, (i // 2) + 1):
				if i % j == 0:
					is_prime = 0
					break

			if is_prime == 1:
				factors.append(i)

	if len(factors) == 1 and factors[0] == num:
		return [(factors[0], 1)]

	for factor in factors:
		counter = 0

		while num % factor == 0:
			counter += 1
			num //= factor
			
			if num % factor != 0:
				result.append((factor, counter))

	return result

# print(prime_factorization(1000))

def group(arr):
	result = []
	counter = 1

	for i in range(len(arr)):

		if i == len(arr) - 1:
			result.append([arr[i]] * counter)

		else:
			if arr[i] == arr[i + 1]:
				counter += 1

			else:
				result.append([arr[i]] * counter)
				counter = 1

	return result

# print(group([1, 1, 1, 2, 3, 1, 1]))

def max_consecutive(items):
	counter = 1
	result = 1

	for i in range(1, len(items)):
		if items[i - 1] == items[i]:
			counter += 1
		else:
			counter = 1
		
		if counter > result:
			result = counter
		
	return result

# print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))

def word_counter():
	arr = [['i', 'v', 'a', 'n', 'q', 'h', 'r', 'e', 'z', 'g', 't', 'z', 'o', 'y', 'm'],
		   ['e', 'v', 'n', 'h', 't', 'r', 'x', 'e', 'k', 'y', 'd', 'a', 'i', 'l', 'c'],
		   ['i', 'a', 'c', 't', 'u', 'a', 'l', 'l', 'y', 'm', 'c', 'x', 'r', 'l', 'e'],
		   ['m', 'v', 'c', 'n', 'p', 'u', 'a', 'm', 'n', 't', 'l', 'u', 'e', 'a', 'a'],
		   ['q', 'r', 'i', 't', 'w', 'e', 'a', 'q', 'u', 'p', 'r', 'x', 't', 'u', 'z'],
		   ['p', 'e', 'a', 'c', 't', 'u', 'a', 'l', 'l', 'y', 'w', 'p', 'y', 't', 'm'],
		   ['o', 'y', 'h', 't', 'r', 'e', 'l', 'u', 'f', 'p', 'q', 'n', 'z', 'c', 's'],
		   ['p', 'a', 'c', 't', 'u', 'a', 'l', 'l', 'y', 'u', 'r', 'e', 'q', 'a', 'r']]
	word = "actually"
	arr_h = 8
	arr_w = 15
	word_index = 0
	result = 0
	
	if len(word) > arr_h and len(word) > arr_w:
		print("Invalid number of rows or columns!")

	for h in range(arr_h):
		for w in range(arr_w):
			if arr[h][w] == word[0]:
				# upwards
				word_index = 0
				if h >= len(word) - 1:
					word_index += 1
					for i in range(h - 1, h - len(word), -1):
						if arr[i][w] == word[word_index]:
							if word_index == len(word) - 1:
								result += 1
							else:
								word_index += 1
				# to the right
				word_index = 0
				if w <= arr_w - len(word):
					word_index += 1
					for i in range(w + 1, w + len(word)):
						if arr[h][i] == word[word_index]:
							if word_index == len(word) - 1:
								result += 1
							else:
								word_index += 1
				# downwards
				word_index = 0
				if h <= arr_h - len(word):
					word_index += 1
					for i in range(h + 1, h + len(word)):
						if arr[i][w] == word[word_index]:
							if word_index == len(word) - 1:
								result += 1
							else:
								word_index += 1
				# to the left
				word_index = 0
				if w >= len(word) - 1:
					word_index += 1
					for i in range(w - 1, w - len(word), -1):
						if arr[h][i] == word[word_index]:
							if word_index == len(word) - 1:
								result += 1
							else:
								word_index += 1
				# to the up-right
				word_index = 0
				if h >= len(word) - 1 and w <= arr_w - len(word):
					word_index += 1
					for i in range(1, len(word)):
						if arr[h - i][w + i] == word[word_index]:
							if word_index == len(word) - 1:
								result += 1
							else:
								word_index += 1
				# to the down-right
				word_index = 0
				if h <= arr_h - len(word) and w <= arr_w - len(word):
					word_index += 1
					for i in range(1, len(word)):
						if arr[h + i][w + i] == word[word_index]:
							if word_index == len(word) - 1:
								result += 1
							else:
								word_index += 1
				# to the down-left
				word_index = 0
				if h <= arr_h - len(word) and w >= len(word) - 1:
					word_index += 1
					for i in range(1, len(word)):
						if arr[h + i][w - i] == word[word_index]:
							if word_index == len(word) - 1:
								result += 1
							else:
								word_index += 1
				# to the up-left
				word_index = 0
				if h >= len(word) - 1 and w >= len(word) - 1:
					word_index += 1
					for i in range(1, len(word)):
						if arr[h - i][w - i] == word[word_index]:
							if word_index == len(word) - 1:
								result += 1
							else:
								word_index += 1


	print(result)
						

# word_counter()
