print("example 1 -------")
print()
#example 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name + " and I am" + str(self.age) + " years old.")

person1 = Person("Alice", 30)
person1.greet()


print()
print("example 2 -------")
print()
#example 2
class Car:
    def __init__(self, make, model, year, speed):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed
    
    def print_accelerate(self):
        print("the car is now accelareating to " + str(self.speed) + " miles per hour.")

my_car = Car("Toyota", "Camry", 2020 , 60)
my_car.print_accelerate()
