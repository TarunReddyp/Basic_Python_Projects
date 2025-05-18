import random
def number_guessing_game():
    secret_number = random.randint(1,100)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1
            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too High!")
            else :
                 print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
                 break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

if __name__ == "__main__":
    number_guessing_game()