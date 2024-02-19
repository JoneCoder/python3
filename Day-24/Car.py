class Car:
    def __init__(self, name, manufacture, color, year, cc):
        self.name = name
        self.manufacture = manufacture
        self.color = color
        self.year = year
        self.cc = cc

    def start(self):
        return f"Starting the {self.name}"

    def brake(self):
        print('Brake the car')

    def drive(self):
        print('Driving car')

    def turn(self, side):
        return f"Turn on the {self.name} {side} side"

    def changeGear(self):
        print('Changing the gear')


car1 = Car('Car 1', 'BD', 'red', '2011', '300')
car2 = Car('Car 2', 'BD', 'white', '2014', '350')

car1.model = 'M20'

carTurn = car1.turn('Right')

print(car1.model)
