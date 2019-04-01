import random

class Car:
    def __init__(self, car, model, max_speed):
        self.car = car
        self.model = model
        self.max_speed = max_speed

class Driver:
    def __init__(self, name, car):
        self.name = name
        if isinstance(car, Car()):
            self.car = car

class Race:
    def __init__(self, drivers=[], crash_chance=random.random()):
        for i in range(len(drivers)):
            if isinstance(drivers[i], Driver()):
                self.drivers = drivers.append(drivers[i])
        self.crash_chance = crash_chance

    @staticmethod
    def result():
        pass