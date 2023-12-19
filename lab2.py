print("example 1 -------")
print()
#example 1
class MyClass:
    x = 5
p1 = MyClass()
print(p1.x)

print()
print("example 2 -------")
print()
#example 2
class MyClass:
    i = 12345
    def f(self):
        return 'hello world'

X = MyClass()
print(X.f())


print()
print("example 3 -------")
print()
#example 3
class Dog:
    attr1 = "mammal"
    attr2 = "dog"
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)

Rodger = Dog()
# print(Rodger.attr1)
Rodger.fun()



print()
print("Exercise B -------")
print()
#Exercise B
# B. Create a class called Employee with two attributes: name and salary.
# Add a class-specific modifier to the salary attribute to ensure that it is
# always a positive value.

class Employee:
    name = None
    salary = None
    
    @classmethod
    def set_salary(cls, salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        else:
            cls.salary = salary
            
employee1 = Employee()
employee1.name = "Bob"

Employee.set_salary(5000)
print("Employee name: ", employee1.name)
print("Employee salay: ", employee1.salary)



print()
print("Exercise B -------")
print()
#Exercise c
# C. Create a class and object to represent a circle.


class Circle:
    def set_radius(self, radius):
        self.radius = radius
        
    def get_radius(self):
        return self.radius
    
    def circumference(self):
        return 2 * 3.14159 * self.radius
    
    def area(self):
        return 3.14159 * self.radius**2
    
circle = Circle()
circle.set_radius(7)
print("Radius: ", circle.get_radius())
print("Circumference: ", circle.circumference())
print("Area: ", circle.area())

