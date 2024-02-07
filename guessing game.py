#guessing game by randomly picking the number
import random
print (" WELCOME😊 ")
print ("Lets have some fun😎🎶")
winning_number = int(input("Please enter number: "))
random_number = random.randint(1,10)
print ("Random number: ", random_number)
if winning_number == random_number:
    print (" YOU JUST WON A TRIP TO SAROVA WHITESANDS🙂")
else:
    print ("SORRY! TRY AGAIN LATER😞")
