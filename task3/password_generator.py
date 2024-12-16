import random
import string

# Step 1: Prompt the user for password length
print("Welcome to the Password Generator!")
length = int(input("Enter the desired length of the password: "))

# Step 2: Define the character set for the password
characters = string.ascii_letters + string.digits + string.punctuation

# Step 3: Generate a random password
password = ''.join(random.choice(characters) for i in range(length))

# Step 4: Display the generated password
print(f"Your generated password is: {password}")
