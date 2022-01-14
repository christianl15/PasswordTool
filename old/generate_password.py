import random

def gen_password():
    keep_running = True


    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$']

    password = ''

    for letter in range(1,nr_letters+1):
        rd_letters = random.choice(letters)
        password += rd_letters
    for symbol in range(1,nr_symbols+1):
            rd_symbols = random.choice(symbols)
            password += rd_symbols
    for number in range(1,nr_numbers+1):
        rd_numbers = random.choice(numbers)
        password += rd_numbers

    print(f"Your password is: {password}")
