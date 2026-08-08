
import random
import string

print("=" * 50)
print("           RANDOM PASSWORD GENERATOR")
print("=" * 50)

while True:

    # Get password length
    length = int(input("\nEnter password length: "))

    # Get character preferences
    upper = input("Include uppercase letters? (yes/no): ").lower()
    lower = input("Include lowercase letters? (yes/no): ").lower()
    numbers = input("Include numbers? (yes/no): ").lower()
    symbols = input("Include symbols? (yes/no): ").lower()

    # Create character set
    characters = ""

    if upper == "yes":
        characters += string.ascii_uppercase

    if lower == "yes":
        characters += string.ascii_lowercase

    if numbers == "yes":
        characters += string.digits

    if symbols == "yes":
        characters += string.punctuation

    # Check character selection
    if characters == "":
        print("\nPlease select at least one character type.")
        continue

    # Generate password
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\n" + "-" * 50)
    print("Generated Password:", password)
    print("-" * 50)

    # Ask whether to generate another password
    again = input("\nGenerate another password? (yes/no): ").lower()

    if again != "yes":
        print("\nThank you for using Password Generator!")
        break

print("=" * 50)
