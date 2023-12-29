class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelx = Vehicle(60, 10)
print(modelx.max_speed, modelx.mileage)
