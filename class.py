name = input('enter name')
age = input('enter age')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello my name is {self.name} and I'm  {self.age} years old.")

person = Person(name, age)

print("Name: ", person.name)
print("Age: ", person.age)
person.greet() # Outputs "Hello my name is John and am 25 years old
