print()
print("example 1 Single Inheritance -------")
print()
#example 1
class Animal:
    def eat(self):
        print("I am eating.")
class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")
dog = Dog()
dog.eat() # Output: I am eating.
dog.bark() # Output: Woof! Woof!


print()
print("example 2 Multiple Inheritance  -------")
print()
#example 2

class Animal:
    def eat(self):
        print("I am eating.")
class Mammal:
    def breathe(self):
        print("I am breathing.")
class Dog(Animal, Mammal):
    def bark(self):
        print("Woof! Woof!")
dog = Dog()
dog.eat() # Output: I am eating.
dog.breathe() # Output: I am breathing
dog.bark() # Output: Woof! Woof!



print()
print("example 3.1 super() -------")
print()
#example 3.1
class Animal:
    def make_sound(self):
        print("Generic animal sound.")
class Dog(Animal):
    def make_sound(self):
        super().make_sound() # Call the parent class method
        print("Woof! Woof!")
dog = Dog()
dog.make_sound()


print()
print("example 3.2 super() -------")
print()
#example 3.2
class AquaticAnimal:
    def swim(self):
        print(f"{self.name} is swimming.")
class Bird:
    def fly(self):
        print(f"{self.name} is flying.")
class Penguin(AquaticAnimal, Bird):
    def __init__(self, name):
        self.name = name

penguin = Penguin('Pengu')
penguin.swim() # Output: Pengu is swimming.
penguin.fly() # Output: Pengu is flying.


