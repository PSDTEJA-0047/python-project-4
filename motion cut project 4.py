import random
import string

def generate_password(length=12):
    """Generate a random password."""
    # Define characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        num_passwords = int(input("How many passwords do you want to generate? "))
        length = int(input("Enter the length of each password: "))
        for _ in range(num_passwords):
            password = generate_password(length)
            print(password)
    except ValueError:
        print("Please enter valid numeric values for length and number of passwords.")

if __name__ == "__main__":
    main()
