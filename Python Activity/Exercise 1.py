
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    def __init__(self, max_speed, mileage):

        super().__init__(max_speed, mileage)


school_bus = Bus(120, 50000)


print(f"Bus Max Speed: {school_bus.max_speed} km/h")  
print(f"Bus Mileage: {school_bus.mileage} km")        
