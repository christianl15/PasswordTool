import random
import os
import old.art as art

is_secure = True

def db_check(password):
    password_txt = open("passwords.txt", "r")
    passwords_parsed = []

    for _password in password_txt:
        strip_line = _password.strip()
        line_list = strip_line.split()
        passwords_parsed.append(line_list)

    for __password in passwords_parsed:
        if __password == password:
            is_secure = False
            print("insecureTESTING")
            

if __name__ == "__main__":
    pass
