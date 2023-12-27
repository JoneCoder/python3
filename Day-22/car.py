# class Car:
#     name = 'Toyota'
#     model = 'Supra mk4'
#     color = 'orange'
#
#     def start():
#         print('Starting the engine')
#
#
# print('Name of the car:', Car.name)
# print('Color:', Car.color)
#
# Car.start()


class Car:
    name = ''
    model = ''
    color = ''

    def start(self):
        print(self.name, ' car starting the engine')


# Creating a car object
myCar = Car()
myCar.name = 'Toyota'
myCar.model = 'Supra mk4'
myCar.color = 'orange'

print(myCar.name)
myCar.start()

myCar2 = Car()
myCar2.name = 'BMW'
myCar2.color = 'white'
print(myCar2.name)
myCar2.start()



