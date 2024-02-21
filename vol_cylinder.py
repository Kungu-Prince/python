#volume of a cylinder
import math
def volume():
    radius = float(input("Enter radius of the cylinder: "))
    height = float(input("Enter height of the cylinder"))
    volume = math.pi * height * radius**2
    print("Volume of cylinder", volume)

volume()