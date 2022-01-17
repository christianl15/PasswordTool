# password-tool
My Tech Fair 2022 project.

# demonstration
Try a finished project at pwdtool.ddns.net

# installing dependancies
This program only works on Linux based servers (although I will only be showing how to install on Debian based Linux distros) and if you want to go really deep 
Macos computers. Also, it is possible to run it locally without nginx. More of that at the end of the installation process.
Install python3.
Install FastApi universally with `pip install fastapi`.
Install Uvicorn universally with `pip install uvicorn[standard]`.
Install nginx on Linux with `sudo apt install nginx` and for MacOS follow this guide: https://bit.ly/3I7ynhP
Install git.

Python3 is the language that the back-end was written in. FastApi is the framework that the back-end uses to communicate with the front-end. Uvicorn will act as our 
server. Nginx is the webserver for our front-end, Apache can also be used. And git is for source code management.

# 1 installing the base files
First we have to install the files to our webserver's HTML directory. With Nginx the HTML files are located at `/var/www/html/`. In a terminal, change directory 
into it. Then run `git clone https://github.com/csleecsl/password-tool`.

# 2 putting the files where they should be
Change directory into the password-tool directory and move the files and folders inside of passwordtool-api/ and passwordtool-client/ to the directory before it. 
Then delete both directories along with notes/. 

# 3 creating an enviroment variable (so it is easier to setup the back-end)
So that we don't have to it the file directly we have to setup an enviorment variable. Note that this will only work in the same terminal window that the command is run in. Run `export PWD_FILES_DIR=<PASSWORD_FILES>` but replace <PASSWORD_FILES> with the FULL path to the directory password_files/ (example: /var/www/html/password_files). 

# 4 running the program
Now you are setup up! Run `uvicorn main:app --reload` to run it! If you are running it locally type localhost into a web browser and the front-end will come up!

# OTHER running without nginx locally
To make running it locally easy, I recommend install VSCode to use the "Live Server" extention. Follow step 2 to organize the project. Then right click index.html 
and select "Open with Live Server". Then open a terminal window inside of VSCode and follow step 3 and 4.

# OTHER troubleshooting
If the program cannot import the module "main" then make sure you are in the /var/www/html directory first.
If you are running it on a server and the functionality of the project is not available then open port 8000.

# OTHER where did the password database come from
All the password files are from either leaked or hacked databases from companies that were not hashing their passwords. When passwords are stored hopefully the 
company that is storing them are hashing them and not storing them in plain text. Hashing algorithms are algorithms that mix the password into a unreadable 
string. Hackers who hacked companies and got passwords dumped them online. passwords.txt is from the RockYou 2009 hack and the NordVPN hack. passwords2.txt is 
from random companies that were hacked. The cool thing about passwords2.txt is that the passwords were originally hashed but were cracked by unknown hackers. 
passwords3.txt is from the hotmail.com hack. 
