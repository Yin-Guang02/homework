import random

numbers_list = [10, 24, 33, 45, 50, 67, 88, 92, 100]

target_number = random.choice(numbers_list)

print("Welcome to the Quiz Competition, Harsh!")
print(f"The judge has picked a number from this list: {numbers_list}")

guessed_correctly = False

while not guessed_correctly:
    guess = int(input("\nGuess the number: "))
    
    if guess > target_number:
        print("Too high! Try a smaller number.")
    elif guess < target_number:
        print("Too low! Try a larger number.")
    else:
        print(f"Congratulations! You guessed it. The number was {target_number}.")
        guessed_correctly = True