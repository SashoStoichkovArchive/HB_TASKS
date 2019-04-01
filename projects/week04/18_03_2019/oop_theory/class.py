class Panda:
    def __init__(self, name, food, weight, age, city='Sofia'):
        self.panda_name = name
        self.fav_food = food
        self.curr_weight = weight
        self.age = age

    def celebrate_birthday(self):
        self.age += 1

    def __eq__(self, other):
        return True

    def __str__(self):
        return "Panda: {0}".format(self.panda_name)

panda = Panda('Ivo', 'ice_cream', 74, 23)

print(panda)

# print(panda == panda)
# print(panda is panda)

panda2 = Panda('Rosi', 'ice_cream', 74, 23)

print(panda2)