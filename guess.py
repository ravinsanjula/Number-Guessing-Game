import random
print("I am thinking of a number from 1 to 100")
number = random.randint(1,100)
print(f"Number is {number}")

level = input("Enter 'easy' or 'hard'....")


if level == 'easy':
    health = 10
if level == 'hard':
    health = 5


def checker():
    if number > guess:
        print("Too low...")
    elif number < guess:
        print("Too high...")
    else:
        print("Your guess is correct...")
    
game_over = False


while not game_over:
    for i in range(health):
        guess = int(input("Enter the number..."))
        checker()
        health -= 1
        print(f"You have only {health} left")
        if number == guess:
            game_over = True
    print("Game over you have lost...")
    game_over = True


