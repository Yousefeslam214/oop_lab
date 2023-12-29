print()
print("example 1 -------")
print()
#example 1

class Shape:
    def __init__(self, name, color):
        self.name = name
        self.color = color
class Circle(Shape):
    def __init__(self, name, color, radius):
        super().__init__(name, color)
        self.radius = radius
    def calculate_area(self):
        return 3.14 * self.radius * self.radius
    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius
circle = Circle('Circle', 'red', 5)
print(f"Circle name: {circle.name}")
print(f"Circle color: {circle.color}")
print(f"Circle area: {circle.calculate_area()}")
print(f"Circle perimeter: {circle.calculate_perimeter()}")

print()
print("example 2 -------")
print()
#example 2

class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating.")
    def sleep(self):
        print(f"{self.name} is sleeping.")
# Parent class 2
class Bird:
    def __init__(self, name):
        self.name = name
    def fly(self):
        print(f"{self.name} is flying.")
# Child class inheriting from Animal and Bird
class Eagle(Animal, Bird):
    def __init__(self, name):
        super().__init__(name)
    def hunt(self):
        print(f"{self.name} is hunting.")
# Create an instance of Eagle
eagle = Eagle("Eagle")
eagle.eat() # Output: Eagle is eating.
eagle.sleep() # Output: Eagle is sleeping.
eagle.fly() # Output: Eagle is flying.
eagle.hunt() # Output: Eagle is hunting.
