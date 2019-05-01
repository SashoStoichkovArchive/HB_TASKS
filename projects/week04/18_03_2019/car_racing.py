import json, sys, os, random


class ArgParser:
    def __init__(self):
        self.args = sys.argv

    def parse_arguments(self):
        if len(self.args) == 1:
            print("""\
Hello PyRacer!
Please, call command with the proper argument:
python3 race.py start <name> <races_count> -> This will start a new championship with the given name, races count.
python3 race.py standings -> This will print the standings for each championship that has ever taken place. 
""")
            exit(-1)
        try:
            if self.args[1].lower() == 'standings':
                return 'standings'
            if self.args[1] == 'start':
                return self.args[2], int(self.args[3])
        except IndexError:
            print('Error, missing arguments!')
            exit(-1)


class CrashChangeGenerator:
    def __init__(self, a=0, b=1):
        self.a = a
        self.b = b
    
    def generate_crash_chance(self):
        chance = f'{random.uniform(self.a, self.b):.2f}'
        return float(chance)

    def generate_chance_for_drivers(self, drivers):
        return [self.generate_crash_chance() 
                for _ in range(len(drivers))]


class JsonParser:
    def __init__(self, json_file):
        self.parsed_data = JsonParser.read_json_cars_data(json_file)

    def get_drivers_stats(self):
        people = self.parsed_data["people"]
        return [(person["name"], person["car"],
                 person["model"],person["max_speed"])
                for person in people]

    @staticmethod
    def read_json_cars_data(json_file):
        try:
            with open('cars.json') as jf:
                try:
                    cars_data = json.load(jf)
                    return cars_data
                except ValueError:
                    print('Error, file specified not in json format!')
                    exit(-1)
        except FileNotFoundError:
            print('Error, file specified not found!')
            exit(-1)


class Car:
    def __init__(self, car, model, max_speed):
        self.car = car
        self.model = model
        self.max_speed = max_speed

    def __str__(self):
        return f'{self.car}, {self.model}, {self.max_speed}'

    def __repr__(self):
        return str(self)


class Driver:
    def __init__(self, name, car):
        self.name = name
        self.car = car

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return str(self)

    def get_speed(self):
        return self.car.max_speed

    @classmethod
    def build_drivers_list(cls, drivers_data):
        drivers = []
        for name, car, model, ms in drivers_data:
            drivers.append(cls(name, Car(car, model, ms)))
        return drivers


class Race:
    POINTS = {0: 8,
              1: 6,
              2: 4}

    def __init__(self, drivers, crash_chances):
        self.drivers = drivers
        self.crash_chances = crash_chances

    def __getitem__(self, item):
        return self.drivers[item]

    def _determine_winners(self):
        drivers_with_chances = list(zip(self.drivers, self.crash_chances))
        avg = sum(self.crash_chances)/len(self.crash_chances)
        winners = Race._filter_drivers(avg, drivers_with_chances)
        winners.sort(key=lambda driver: driver.get_speed(), reverse=True)
        return winners

    def construct_result_data(self):
        results = []
        winners = self._determine_winners()
        for driver in self.drivers:
            try:
                points = Race.POINTS.get(winners.index(driver), 0)
            except ValueError:
                points = 0
            results.append({
                'name': driver.name,
                'car': driver.car.car,
                'model': driver.car.model,
                'max_speed': driver.get_speed(),
                'points': points,
                'crashed': driver not in winners
            })
        return results

    @staticmethod
    def _order_drivers_by_points(results):
        return sorted(results, key=lambda driver: driver['points'], reverse=True)

    @staticmethod
    def print_race_results(results):
        sorted_results = Race._order_drivers_by_points(results)
        print('###### START ######')
        for driver in sorted_results:
            if driver['crashed'] is True:
                print(f"Unfortunately, {driver['name']} has crashed.")
            else:
                print(f"{driver['name']} - {str(driver['points'])}")
        print('')

    @staticmethod
    def _filter_drivers(avg, drivers_with_chances):
        return [driver[0] for driver in drivers_with_chances
                if driver[1] > avg]


class Championship:
    FILE_NAME = 'championship_history.json'

    def __init__(self, name, race_count, drivers):
        self.name = name
        self.race_count = race_count
        self.drivers = drivers
        self.drivers_table = self.create_drivers_table()

    def create_drivers_table(self):
        drivers_table = []
        for driver in self.drivers:
            drivers_table.append({
                'name': driver.name,
                'car': driver.car.car,
                'model': driver.car.model,
                'max_speed': driver.get_speed(),
                'points': 0,
                'crashed': False
            })
        return drivers_table

    def start_races(self):
        gcc = CrashChangeGenerator()
        for i in range(self.race_count):
            crash_chances = gcc.generate_chance_for_drivers(self.drivers_table)
            race_results = Race(self.drivers, crash_chances).construct_result_data()
            for driver_stats in self.drivers_table:
                for driver in race_results:
                    if driver_stats['name'] == driver['name']:
                        driver_stats['points'] += driver['points']
                        driver_stats['crashed'] = driver['crashed']
            print(f'Race #{i+1}')
            Race.print_race_results(race_results)

    def order_drivers_by_points(self):
        self.drivers_table.sort(key=lambda driver: driver['points'], reverse=True)

    def save_to_json(self):
        print('saving..')
        championship = {self.name: self.drivers_table}
        if Championship._file_exists():
            with open(Championship.FILE_NAME) as jf:
                championships_table = json.load(jf)
                championships_table.update(championship)
            with open(Championship.FILE_NAME, 'w') as jf:
                json.dump(championships_table, jf, indent=4)
        else:
            with open(Championship.FILE_NAME, 'w') as jf:
                json.dump(championship, jf, indent=4)

    @staticmethod
    def _file_exists():
        path = os.path.dirname(sys.argv[0])
        path_to_file = os.path.join(path, Championship.FILE_NAME)
        return os.path.exists(path_to_file)

    @staticmethod
    def print_standings():
        if Championship._file_exists():
            with open(Championship.FILE_NAME) as jf:
                championship_data = json.load(jf)
            for championship in championship_data:
                print(f'###{championship}###')
                for driver in championship_data[championship]:
                    print(f"{driver['name']} - {driver['points']}")
                print('')
        else:
            print('No standings yet!')


def start_championship():
    parser = ArgParser()
    args = parser.parse_arguments()
    if args == 'standings':
        Championship.print_standings()
    elif isinstance(args, tuple):
        drivers_stats = JsonParser('cars.json')
        drivers_list = Driver.build_drivers_list(drivers_stats.get_drivers_stats())
        championship = Championship(args[0], args[1], drivers_list)
        championship.start_races()
        championship.order_drivers_by_points()
        championship.save_to_json()


if __name__ == '__main__':
    start_championship()