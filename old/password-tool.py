import old.password_checker as password_checker
import old.generate_password as generate_password
import old.art as art
import sys
import webbrowser

docs = 'https://github.com/csleecsl/password-tool/wiki/Documentation'

print(art.logo)
print("Welcome to the password tool app!")

not_Quiting = True

while not_Quiting:
    directions = input("'g' to generate a secure password, 'c' to check your password, 'd' for documentation, 'q' to quit ")

    # TODO Find how to trip the is_secure variable in be_password_checker in the fe_init.py file

    if directions.lower() == 'g':
        generate_password.gen_password()
    elif directions.lower() == 'c':
        password = input("What is your password? ")

        password_checker.db_check(password=password)

        if password_checker.is_secure == False:
            print("Your password is not secure generate a new password!")
    elif directions.lower() == 'd':
        webbrowser.open(docs)
    elif directions.lower() == 'q':
        not_Quiting = False
