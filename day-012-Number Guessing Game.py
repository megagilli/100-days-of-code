import art
import random


print(art.logo)
print("Welcome to the number guessing game")
print("im thinking a number between 1 and 100! ")
diff=input("choose a difficulty, Type 'easy' or 'hard': ").strip().lower()
attempts=10 if diff=="easy" else 5
random_number=random.randint(1,100)

print(f"\nYou have {attempts} remaining to guess")
for attempts in range(1,attempts+1):
    guess = int(input("Make a guess: "))

    if guess==random_number:
        print("You guessed correct! ")
        break
    elif guess<random_number:
        print("Too low!")
        print("Guess again!")
    elif guess>random_number:
        print("Too high!")
        print("Guess again!")
else:
    print(f"Sorry , you've used up all your attempts, The correct number was {random_number}")



