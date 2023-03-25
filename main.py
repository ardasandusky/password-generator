import random
import string
import pyperclip


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


if __name__ == '__main__':
    password_length = int(input("Enter the length of password: "))
    password = generate_password(password_length)
    print("Your password is: ", password)
    pyperclip.copy(password)
    print("Password copied to clipboard!")
