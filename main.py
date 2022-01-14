import random

from optparse import Option
from typing import Optional

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/", response_class=HTMLResponse)
def read_item( nochar: Optional[int] = None, nonum: Optional[int] = None, noscar: Optional[int] = None):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$']

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

 
    # return_value = "<html><body>numberOfLetters:" + nochar + " <br>" + "numberOfNumbers:" + nonum + " <br>" + "nunberOfSchar:" + noscar + "</body></html>"
    return_value = "<html><body>" + password + "</body></html>"
    return return_value
    