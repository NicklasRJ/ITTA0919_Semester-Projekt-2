import hashlib
import binascii
import os

"""
TODO: Skift hardcoded parameters til variabler som ligger i clouden / memory
"""


def hash_password(password):
    """ Hash a password for storing. """
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                  salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')


def verify_password(stored_password, provided_password):
    """ Verify a stored password against one provided by user. """
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password


def create_password():
    """ Insert docstring here """
    while True:
        print("Creating new password")
        input_password = input("Enter new password: ")
        saved_password = hash_password(input_password)
        print("Password created")
        make_more = input("Do you wish to add more passwords? ")
        if make_more == ("yes" or "y"):
            continue
        else:
            break
    return saved_password


def check_password(saved_password):
    """ Insert docstring here """
    try:
        while True:
            print("Going to login")
            input_password = input("Password: ")
            if verify_password(saved_password, input_password):
                print("Access Granted!\nWelcome to the server room")
                break
            else:
                print("\nAccess Denied!\nTry again")
    except NameError:
        print("No passwords in database\nExiting program")


if __name__ == "__main__":
    saved_password = create_password()
    check_password(saved_password)
