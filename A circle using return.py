#use return to calc area of a circle
from math import pi

class Circle:
    def __init__(self, radius):
        self.radius =radius

    def area(self):
        Area = pi * self.radius **2
        return Area
    
    def perimeter(self):
        Circum = pi * self.radius *2
        return Circum
    
rad = int(input("Enter Radius: "))
circle1 = Circle(rad)
print("The Area is: ", circle1.area())
print("The Perimeter is: ", circle1.perimeter())