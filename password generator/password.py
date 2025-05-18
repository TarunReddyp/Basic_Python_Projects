import random
import string

def password_generator():
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Password length must be greater than zero.")
            return
    except ValueError:
        print("Invalid input. Please enter a whole number for the length.")
        return

    include_lower = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    include_upper = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    include_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    include_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

    characters = ''
    if include_lower:
        characters += string.ascii_lowercase
    if include_upper:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        print("You must select at least one character set to generate a password.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"\nGenerated password: {password}")

if __name__ == "__main__":
    password_generator()