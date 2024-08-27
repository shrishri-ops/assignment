import re

def check_password_strength(password):
    """
   Check the strength of the password based on the following criteria:
    - Minimum length of 8 characters.
    - Contains both uppercase and lowercase letters.
    - Contains at least one digit.
    - Contains at least one special character.

    Args:
    password (str): The password string to check.

    Returns:
    bool: True if the password meets all the criteria, False otherwise.
    """
    # Check the length of the password
    if len(password) < 8:
        return False

    # Check for uppercase and lowercase letters
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False

    # Check for at least one digit
    if not re.search(r'[0-9]', password):
        return 

    # Check for at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False

    # If all criteria are met, return True
    return True

if __name__ == "__main__":
    # Take user input for the password
    password = input("Enter a password to check its strength: ")

    # Validate the password using the check_password_strength function
    if check_password_strength(password):
        print("Your password is strong.")
    else:
        print("Your password is weak. It must be at least 8 characters long, contain both uppercase and lowercase letters, include at least one digit, and have at least one special character.")
