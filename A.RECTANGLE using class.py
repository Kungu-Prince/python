#calc area and perimeter of a rectangle
class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
        
    def perimeter(self):
        return 2*(self.length + self.width) 
        
len = int(input("Enter Length: "))
wid = int(input("Enter Width: "))
RECTANGLE = rectangle(len, wid)
print("Area is: ", RECTANGLE.area())
print("Perimeter is: ",RECTANGLE.perimeter())
RECTANGLE.perimeter()
RECTANGLE.area()
