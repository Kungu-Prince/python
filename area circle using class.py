#area of a circle
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
        

    def area(self):
        #self.radius = float(input("Enter Radius"))
        area = self.radius**2 * math.pi
        print(f"area= {area}")

    def perimeter(self):
        perimeter = self.radius *2 *math.pi
        print(f"perimeter= {perimeter}")

Area = Circle(21) 
Perimeter = Circle(21)
Perimeter.perimeter()
Area.area()
