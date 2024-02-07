#guessing game by randomly picking the number
import random
print("WELCOME😊")
print("Let's have some fun😎🎶")

remaining_attempts = 3

while remaining_attempts > 0:
    winning_number = int(input("Please enter a number between 1 and 10: "))
    random_number = random.randint(1, 10)

    print("Random number: ", random_number)

    if winning_number == random_number:
        print("Congratulations! You just won a trip to Sarova Whitesands🙂.")
        break
    else:
        print("Sorry! Try again😞.")
        remaining_attempts -= 1
        print(f"Remaining attempts: {remaining_attempts}")

    if remaining_attempts == 0:
        print("Sorry, out of tokens. See you next time😞.")
