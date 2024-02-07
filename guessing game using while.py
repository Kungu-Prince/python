#guessing game by randomly picking the number
import random
print (" WELCOME😊 ")
print ("Lets have some fun😎🎶")
winning_number = int(input("Please enter a number between 1 and 20: "))
random_number = random.randint(1,20)

while winning_number != random_number:
    print ("Random number: ", random_number)
    print ("SORRY! TRY AGAIN LATER😞")

winning_number = int(input("Please enter a number between 1 and 20: "))
random_number = random.randint(1,20)

print (" YOU JUST WON A TRIP TO SAROVA WHITESANDS🙂")