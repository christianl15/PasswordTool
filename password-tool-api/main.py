from json.encoder import ESCAPE
import random
import os 

from optparse import Option
from tokenize import String

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
                    Your password was not found in the database, but may still be vulnerable <br>
                    <a href="http://pwdtool.ddns.net/index.html">Go back to original site.</a>
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
                    Your password was found in the database, go and change it. <br>
                    <a href="http://pwdtool.ddns.net/index.html">Go back to the original site.</a>
                </center>
            </div>
        </body>
    </html>
    """

passwords_parsed = []

@app.on_event("startup")
async def startup_event():
    pwd_files_dir = os.getenv("PWD_FILES_DIR")
    files = os.listdir(pwd_files_dir)
    for file in files:
        print(file)
        full_file_path = pwd_files_dir + file
        print(full_file_path)
        password_file = open(full_file_path, "r")

        for _password in password_file:
            strip_line = _password.strip()
            passwords_parsed.append(strip_line.lower())
        password_file.close()
    
@app.get("/check_password/", response_class=HTMLResponse)
def check_password( password: Optional[str] = None):
    
    bad_password = False

    for __password in passwords_parsed:
        if __password == password.lower():
            bad_password = True
            break

    if not bad_password:
        return good_result
    elif bad_password:
        return bad_result

char_dict = { 'a' : '@', 'A' : '@', 'i' : '!', 'I' : '1', 'e' : '3', 'E' : '3',  's' : '$', 'S' : '$', 'o' : '0', 'O' : '0'}

@app.get("/make_secure/", response_class=HTMLResponse)
def check_password( c_password: Optional[str] = None):
    blank = ""
    secure_pass = list(c_password)
    length = len(secure_pass)
    short_pass = False

    if length < 16:
        short_pass = True

    for i in range(1,5):
    
        char = random.choice(secure_pass)
        char_index = secure_pass.index(char)
        secure_pass[char_index] = str(char).upper()

    for i in range(len(secure_pass)):
        if char_dict.get(secure_pass[i]):
            secure_pass[i] = char_dict.get(secure_pass[i])
        #elif str(secure_pass[i]).isalpha() == True:
        #    if str(secure_pass[i]).isupper() == True:
        #        secure_pass[i] = str(secure_pass[i]).lower()
        #    else:
        #        secure_pass[i] = str(secure_pass[i]).upper()

    return_pass = blank.join(secure_pass)

    regular_result =  f"""
    <html>
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="http://localhost:5500/style.css">
        </head>
        <body>
            <div class="ending_page">
                <center>
                    Your more secured password is: {return_pass}<br>
                    <a href="http://pwdtool.ddns.net/index.html">Go back to the original page</a>
                </center>
            </div>
        </body>
    </html>
    """

    short_result = f"""
    <html>
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="http://localhost:5500/style.css">
        </head>
        <body>
            <div class="ending_page">
                <center>
                    Your more secured password is: {return_pass}<br>
                        <div class=text_red><br>WARNING: your password is less than 16 characters long. <br>We recommend you to change it to 16 characters or longer. <br></div>
                        <a href="http://pwdtool.ddns.net/index.html">Go back to the original page</a>
                    </div>
                </center>
            </div>
        </body>
    </html>
    """

    if short_pass == True:
        return short_result
    else:
        return regular_result

@app.get("/genpassword/", response_class=HTMLResponse)
def genpassword( nochar: Optional[int] = None, nonum: Optional[int] = None, noscar: Optional[int] = None):

    password = ''

    for letter in range(1,nochar+1):
        rd_letters = random.choice(letters)
        password += rd_letters
    for symbol in range(1,noscar+1):
            rd_symbols = random.choice(symbols)
            password += rd_symbols
    for number in range(1,nonum+1):
        rd_numbers = random.choice(numbers)
        password += rd_numbers

    # return_value = "<html><body>numberOfLetters:" + nochar + " <br>" + "numberOfNumbers:" + nonum + " <br>" + "nunberOfSchar:" + noscar + "</body></html>"
    return f"""
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
                    Your password is: {password}<br>
                    <a href="http://pwdtool.ddns.net/index.html">Go back to the original page</a>
                </center>
            </div>
        </body>
    </html>
    """
