import random
from enum import Enum


class CarType(Enum):
    COMPACT = 0
    REGULAR = 1
    SUV = 2
    ELECTRIC = 3
    HANDICAPPED = 4

class Car(object):
    def __init__(self, car_type):
        self.car_type = car_type


class ParkingSpace(object):
    def __init__(self, car_type):
        self.car_type = car_type
        self.parked_car = None

    def park(self, car):
        self.parked_car = car

    def release(self):
        self.parked_car = None

    def __str__(self):
        return "{}: {}".format(self.car_type, self.parked_car != None)


class ParkingLot(object):
    # single story
    def __init__(self):
        self.parking_spaces = [ParkingSpace(random.choice(list(CarType))) for _ in range(random.randint(2, 10))]

    def park(self, car):
        for space in self.parking_spaces:
            if space.car_type == car.car_type and not space.parked_car:
                space.park(car)
                return
        print("Unable to park the car")

    def __iter__(self):
        for space in self.parking_spaces:
            yield space

    def __str__(self):
        return 'Lot: \n' + '\n'.join([str(space) for space in self])
 

p = ParkingLot()
print(p)
c = Car(CarType.SUV)
p.park(c)
print(p)
c = Car(CarType.HANDICAPPED)
p.park(c)
print(p)
c = Car(CarType.HANDICAPPED)
p.park(c)
print(p)



