# Importing Required Modules.
import random # For generating random characters.
import string # For using letters, digits, symbols.

minlength = 4  # Set a minimum password length for safety [You can customize it.]

# Function to generate a password 
def password_generate(length):
    characters= string.ascii_letters + string.digits + string.punctuation # Combine all possible characters A-Z, a-z, 0-9, symbols.
    password = ''.join(random.choice(characters) for _ in range(length)) # Randomly select a 'length' characters & join them into a string.
    return password

# Main rogram execution starts here.
if __name__ == "__main__":
    print("🔐 Random Password Geberator")
    try:
        length=int(input("Enter Password Length: ")) # Asks the user for desired password  length.
        # Checks if the entered number is less than minimum value or like too short.
        if length < minlength: 
            print(f"❌ Password length must be at least {minlength}.")
        else:
            # Generate & Display the password.
            password = password_generate(length)
            print(f"✅ Your Password : {password}")

    # Handles a invaild input (for example, if user enteres text instead of numbers it shows this error.)
    except ValueError:
        print("❌ Please enter valid number")
         
