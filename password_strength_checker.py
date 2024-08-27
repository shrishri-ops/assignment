"""
This module provides functionality to check the strength of a password
based on criteria such as length, uppercase, lowercase, digits, and special characters.
"""

# Function to check the password criteria
def check_password_strength(password):
    """
    Function to check the password strength based on several criteria:
    - Minimum length: 8 characters
    - Contains both uppercase and lowercase letters
    - Contains at least one digit (0-9)
    - Contains at least one special character
    """

    # Lists of different character types
    lowercase_letters = list("abcdefghijklmnopqrstuvwxyz")
    uppercase_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    special_characters = list("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")

    # Initialize flags to track if conditions are met
    password_contain_lower = False
    password_contain_upper = False
    password_contain_digit = False
    password_contain_special = False

    # Check if the password is long enough
    if len(password) < 8:
        print("Password is too short. It should be at least 8 characters long.")
        return False

    # Iterate through the password to check for all criteria
    for char in password:
        if char in lowercase_letters:
            password_contain_lower = True
        if char in uppercase_letters:
            password_contain_upper = True
        if char.isdigit():  # Checks if the character is a digit
            password_contain_digit = True
        if char in special_characters:
            password_contain_special = True

    # Final check: ensure all criteria are met
    if password_contain_lower and password_contain_upper \
        and password_contain_digit and password_contain_special:
        return True

    # Provide feedback on which criteria are missing
    if not password_contain_lower:
        print("Password should contain at least one lowercase letter.")
    if not password_contain_upper:
        print("Password should contain at least one uppercase letter.")
    if not password_contain_digit:
        print("Password should contain at least one digit (0-9).")
    if not password_contain_special:
        print("Password should contain at least one special character (e.g., !, @, #, $, %).")
    return False

# Check the password strength function as per pylint
def main():
    """Prompt user to enter a password and check its strength."""
    password = input("Enter the password without using space: ")

    # Check the password strength
    if check_password_strength(password):
        print("Your password is strong.")
    else:
        print("Your password is weak. Please follow the guidelines to create a strong password.")

if __name__ == "__main__":
    main()
