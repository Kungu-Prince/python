#convert temp to and fro degrees and fahrenheit
#prompt user for input of temperature in celsius
class Temperature:
    def __init__(self, celscius, fahrenheit):
        self.celscius = celscius
        self.fahrenheit =fahrenheit
#convert to celscius
    def convert_Fahrenheit(self):
        fahrenheight = (self.celscius * 1.88) + 32
        return fahrenheight
    
    def convert_Celscius(self):
        celscius = (self.fahrenheit/ 1.88) -32
        return celscius
    
cels = float(input("Enter Temperature in celscius: "))
fahr = float(input("Enter temperature in fahrenheit: "))
temperature = Temperature(cels, fahr)
print("Fahrenheit is: ", temperature.convert_Fahrenheit())
print("Celscius is: ", temperature.convert_Celscius())
temperature.convert_Fahrenheit()
temperature.convert_Celscius()

