import random
import os

is_secure = True

def db_check(password):
    password_txt = open("passwords.txt", "r")
    passwords_parsed = []

    for _password in password_txt:
        strip_line = _password.strip()
        passwords_parsed.append(strip_line)

    for __password in passwords_parsed:
        if __password == password:
            print("Insecure")
            break
            

if __name__ == "__main__":
    db_check(password="password1")
