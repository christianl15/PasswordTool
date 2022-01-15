import random

from optparse import Option
from typing import Optional

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$']
words = []

good_result = f"""
    <html>
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="http://147.182.184.159/style.css">
        </head>
        <body>
            <div class="ending_page">
                <center>
                    Your password is secure <br>
                    <a href="http://127.0.0.1:5500/index.html">Go back to original site.</a>
                </center>
            </div>
        </body>
    </html>
    """

bad_result = f"""
    <html>
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="http://147.182.184.159/style.css">
        </head>
        <body>
            <div class="ending_page">
                <center>
                    Your password is not secure go and change it <br>
                    <a href="http://127.0.0.1:5500/index.html">Go back to the original site.</a>
                </center>
            </div>
        </body>
    </html>
    """

passwords_parsed = []

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.on_event("startup")
async def startup_event():
    password1_file = open("/home/christian/Documents/Christian/Projects/password-tool/passwords.txt", "r")
    password2_file = open("/home/christian/Documents/Christian/Projects/password-tool/passwords2.txt", "r")
    password3_file = open("/home/christian/Documents/Christian/Projects/password-tool/passwords3.txt", "r")

    for _password in password1_file:
        strip_line = _password.strip()
        passwords_parsed.append(strip_line)

    for _password2 in password2_file:
        strip_line2 = _password2.strip()
        passwords_parsed.append(strip_line2)

    for _password3 in password3_file:
        strip_line3 = _password3.strip()
        passwords_parsed.append(strip_line3)
    
    password1_file.close()
    password2_file.close()
    password3_file.close()

@app.get("/check_password/", response_class=HTMLResponse)
def check_password( password: Optional[str] = None):
    
    bad_password = False

    for __password in passwords_parsed:
        if __password == password:
            bad_password = True
            break

    if not bad_password:
        return good_result
    elif bad_password:
        return bad_result
 
    # return_value = "<html><body>numberOfLetters:" + nochar + " <br>" + "numberOfNumbers:" + nonum + " <br>" + "nunberOfSchar:" + noscar + "</body></html>"
    return f"""
    <html>
        <body>
            Your password is: {password}<br>
            <a href="http://127.0.0.1:5500/index.html">Go back to the original page</a>
        </body>
    </html>
    """

@app.get("/genpassword/", response_class=HTMLResponse)
def genpassword( nochar: Optional[int] = None, nonum: Optional[int] = None, noscar: Optional[int] = None):

    password = ''

    for letter in range(1,nochar+1):
        rd_letters = random.choice(letters)
        password += rd_letters
    for symbol in range(1,nonum+1):
            rd_symbols = random.choice(symbols)
            password += rd_symbols
    for number in range(1,noscar+1):
        rd_numbers = random.choice(numbers)
        password += rd_numbers
    
    word_file = open("/home/christian/Documents/Christian/Projects/password-tool/26_words.txt", "r")

    for word in word_file:
        word_line = word.strip()
        words.append(word_line)

    backup = """ temp_char = ""
    password_rem_list = []
    password_rem = password.split()
    for password_r in password_rem:
        temp_char = password_r[:1]
        if temp_char.lower() == 'a':
            password_rem_list.append(words[0] + " ")
        if temp_char.lower() == 'b':
            password_rem_list.append(words[1] + " ")
        if temp_char.lower() == 'c':
            password_rem_list.append(words[2] + " ")
        if temp_char.lower() == 'd':
            password_rem_list.append(words[3] + " ")
        if temp_char.lower() == 'e':
            password_rem_list.append(words[4] + " ")
        if temp_char.lower() == 'f':
            password_rem_list.append(words[5] + " ")
        if temp_char.lower() == 'g':
            password_rem_list.append(words[6] + " ")
        if temp_char.lower() == 'h':
            password_rem_list.append(words[7] + " ")
        if temp_char.lower() == 'i':
            password_rem_list.append(words[8] + " ")
        if temp_char.lower() == 'j':
            password_rem_list.append(words[9] + " ")
        if temp_char.lower() == 'k':
            password_rem_list.append(words[10] + " ")
        if temp_char.lower() == 'l':
            password_rem_list.append(words[11] + " ")
        if temp_char.lower() == 'm':
            password_rem_list.append(words[12] + " ")
        if temp_char.lower() == 'n':
            password_rem_list.append(words[13] + " ")
        if temp_char.lower() == 'o':
            password_rem_list.append(words[14] + " ")
        if temp_char.lower() == 'p':
            password_rem_list.append(words[15] + " ")
        if temp_char.lower() == 'q':
            password_rem_list.append(words[16] + " ")
        if temp_char.lower() == 'r':
            password_rem_list.append(words[17] + " ")
        if temp_char.lower() == 's':
            password_rem_list.append(words[18] + " ")
        if temp_char.lower() == 't':
            password_rem_list.append(words[19] + " ")
        if temp_char.lower() == 'u':
            password_rem_list.append(words[20] + " ")
        if temp_char.lower() == 'v':
            password_rem_list.append(words[21] + " ")
        if temp_char.lower() == 'w':
            password_rem_list.append(words[22] + " ")
        if temp_char.lower() == 'x':
            password_rem_list.append(words[23] + " ")
        if temp_char.lower() == 'y':
            password_rem_list.append(words[24] + " ")
        if temp_char.lower() == 'z':
            password_rem_list.append(words[25] + " ") """

    # return_value = "<html><body>numberOfLetters:" + nochar + " <br>" + "numberOfNumbers:" + nonum + " <br>" + "nunberOfSchar:" + noscar + "</body></html>"
    return f"""
    <html>
        <body>
            Your password is: {password}<br>
            <a href="http://127.0.0.1:5500/index.html">Go back to the original page</a>
        </body>
    </html>
    """
