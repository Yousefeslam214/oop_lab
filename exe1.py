# Write a python program to create a Vehicle class with 
# max_speed and mileage instance attributes

class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelx = Vehicle(60, 10)
print(modelx.max_speed, modelx.mileage)



# create a child class bus that will inherit all of the
# variables and methods of the Vehicle class

class Bus(Vehicle):
    pass

school_bus = Bus(180,13)
print(school_bus.mileage,school_bus.max_speed)



# Define a property that must have the same value for
# every class instance (object)

class Car(Vehicle):
    pass


# check type of an object

print(type(school_bus))


# Determine if School_bus is also an instance
# of the vehicle class


print(isinstance(school_bus, Vehicle))



