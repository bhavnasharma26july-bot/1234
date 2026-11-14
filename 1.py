

secret = 35

lives = 5

while lives > 0:
    guess = int(input("Enter Your Guess:"))

    if guess == secret:
        print("Congratulations! You Won!")
    else:
        lives = lives - 1

    if guess > secret:
        print("guess is more than the secret number")
    else:
        print("guess is less than the secret number")