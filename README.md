# password-tool
My Tech Fair 2022 project.

# demonstration
Try a finished project at pwdchecker.ddns.net

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
into it. Then run `git clone https://github.com/csleecsl/password-tool/edit/main/README.md`.

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
