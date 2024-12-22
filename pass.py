# code that generates a list of 10 unique passwords, each 30 characters long
# created 12/22/2024

import random
import string

def generate_strong_password(length=30):
    """Generate a strong password with a given length."""
    
    # Define possible characters: uppercase, lowercase, digits, and special symbols
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    if length < 8:
        raise ValueError("Password length should be at least 8 characters for better security.")
    
    # Make sure the password contains at least one of each: lowercase, uppercase, digit, special character
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    # Fill the rest of the password length with random characters
    password += random.choices(all_characters, k=length - 4)
    
    # Shuffle the list to prevent predictable patterns and join into a string
    random.shuffle(password)
    
    return ''.join(password)

def generate_unique_passwords(count=10, length=30):
    """Generate a list of unique passwords."""
    passwords = set()
    
    while len(passwords) < count:
        passwords.add(generate_strong_password(length))
    
    return list(passwords)

# Example usage
if __name__ == "__main__":
    password_length = 30  # Fixed length of 30 characters
    unique_passwords = generate_unique_passwords(count=10, length=password_length)
    
    for i, password in enumerate(unique_passwords, start=1):
        print(f"Password {i}: {password}")



