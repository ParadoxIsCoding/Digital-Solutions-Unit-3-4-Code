class Triangle:
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
        self.number_of_sides = 3 
    
    def check_angles(self):
       
        return self.angle1 + self.angle2 + self.angle3 == 180

my_triangle = Triangle(90, 30, 60)

print("Exercise 1 Output:")
print(f"Number of sides: {my_triangle.number_of_sides}") 
print(f"Do angles sum to 180?: {my_triangle.check_angles()}")  

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

my_vehicle = Vehicle(240, 15000)

print("\nExercise 2 Output:")
print(f"Vehicle Max Speed: {my_vehicle.max_speed} km/h")  
print(f"Vehicle Mileage: {my_vehicle.mileage} km")        

class Bus(Vehicle):
    def __init__(self, max_speed, mileage):
        
        super().__init__(max_speed, mileage)

school_bus = Bus(120, 50000)

print("\nExercise 3 Output:")
print(f"Bus Max Speed: {school_bus.max_speed} km/h")  
print(f"Bus Mileage: {school_bus.mileage} km")        
