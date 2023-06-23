import random
import os

print("Welcome To The Number Guessing Game System!")
print("Bot VS You")
print("Begins!")

nuke = random.randint(1, 100)
limit = float('inf')  # Setting limit to infinity for unlimited guesses

while True:
    ask = int(input("Enter Your Guess: "))

    if nuke < ask:
        print("Guessed Number Is Too Big!")
    elif nuke > ask:
        print("Guessed Number Is Too Small!")
    else:
        print("Wow! You Guessed it Correctly!")
        break

    limit -= 1

    if limit == 0:
        print("Game Over!")
        choice = input("Do you want to restart the game? (yes/no): ")
        if choice.lower() == "yes":
            os.system("python Guess_The_Number.py")  # Restart the game by executing the script again
        else:
            print("Exiting the game...")
            break
