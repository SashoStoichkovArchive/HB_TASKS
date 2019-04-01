def gas_stations(distance, tank_size, stations):
    gas_stations_in_route = []
    distance_traveled = 0

    while distance_traveled + tank_size < distance:
        gas_station = max([station for station in stations if station <= distance_traveled + tank_size])

        gas_stations_in_route.append(gas_station)

        distance_traveled = gas_station

    return gas_stations_in_route

def to_digits(n):
	n = abs(n)

	return [int(char) for char in str(n)]

def is_number_balanced(number):
    num = to_digits(number)

    middle_index = len(num) // 2

    if len(num) % 2 == 0:
        if sum(num[:(middle_index + 1)]) == sum(num[middle_index:]):
            return True
        else:
            return False

    else:
        if sum(num[:middle_index]) == sum(num[(middle_index + 1):]):
            return True
        else:
            return False

def increasing_or_decreasing(seq):
    lst = seq[1:]
    is_inc = all([lst[lst_index] > seq[lst_index] for lst_index in range(len(lst))])
    is_dec = all([lst[lst_index] < seq[lst_index] for lst_index in range(len(lst))])

    if is_inc:
        return "Up!"

    elif is_dec:
        return "Down!"

    return False

def get_largest_palindrome(n):
    pass

import re

def sum_of_numbers(input_string):
    result = 0
    numbers = re.findall("[0-9]+", input_string)

    for el in numbers:
        result += int(el)

    return result

def birthday_ranges(birthdays, ranges):
    result_ranges = []

    for tup in ranges:
        counter = 0

        for date in birthdays:
            if date >= tup[0] and date <= tup[1]:
                counter += 1

        result_ranges.append(counter)

    return result_ranges

def numbers_to_message(pressed_sequence):
    pass

def message_to_numbers(message):
    pass

def elevator_trips(people_weight, people_floors, max_people, max_weight):
    trips = 0
    # variant 1
    current_weight = 0
    start = 0

    for index, person_weight in enumerate(people_weight):
        current_weight += person_weight

        if current_weight > max_weight or len(people_weight[start:index]) >= max_people:
            trips += len(set(people_floors[start:index])) + 1
            current_weight = person_weight
            start = index

    trips += len(set(people_floors[start:])) + 1

    # variant 2
    # while len(people_weight) > 0:
    #     current_floors = [people_floors[index] for index, person in enumerate(people_weight)
    #                       if sum(people_weight[:index+1]) <= max_weight
    #                       and len(people_weight[:index+1]) <= max_people]

    #     trips += len(set(current_floors)) + 1

    #     people_weight = people_weight[len(current_floors):]
    #     people_floors = people_floors[len(current_floors):]

    return trips

if __name__ == "__main__":
    # print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]))
    # print(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]))
    # print(is_number_balanced(9))
    # print(increasing_or_decreasing([5, 4, 3, 2, 1])
    # print(sum_of_numbers("ab"))
    # print(birthday_ranges([5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15], [(4, 9), (6, 7), (200, 225), (300, 365)]))

    print(elevator_trips([40, 40, 100, 80, 60], [2, 3, 3, 2, 3], 5, 200))
    print(elevator_trips([80, 60, 40], [2, 3, 5], 2, 200))