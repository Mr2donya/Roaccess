import os
import time


class color:

    firoze = '\033[96m'
    white = '\033[0m'


try:

    from RoacessLib import *

except:

    print("Roaccess don't found your lib :(")
    exit()

try:

    import mysql.connector

except:

    try:

        os.system('pip3 install mysql-connector-python')

    except:

        print("Roaccess don't install mysql connector :(")


os.system('clear')

print(color.firoze + """                             
  _____                                   
 |  __ \                                  
 | |__) |___   __ _  ___ ___ ___  ___ ___ 
 |  _  // _ \ / _` |/ __/ __/ _ \/ __/ __|
 | | \ \ (_) | (_| | (_| (_|  __/\__ \__ \\
 |_|  \_\___/ \__,_|\___\___\___||___/___/ Ver 0.1
                                                                         
""")


if ini_file():

    print(color.white + "[!] Your information finded we use this information :)")

    flag_information = True

else:

    print(color.white + "[!] we don't found your information :(")

    FILE = open("user.ini", mode="w")

    username = str(input("Enter your mysql username : "))
    password = stdiomask.getpass(prompt = '[?] Enter your mysql user password : ')

    FILE_WRITE = FILE.write(username + "\n")
    FILE_WRITE = FILE.write(password)

    FILE.close()

    flag_information = False

print("""
[1] - Create new database

[2] - Open databse

[3] - Show your databases

Note : For exit Ctrl + C 
""")

while True:

    try:

        choice_oprions = str(input("[?] Enter your option : "))

    except KeyboardInterrupt:

        os.system('clear')
        print("Bye ;)\n")
        time.sleep(2)
        exit(os.system('clear'))


    if choice_oprions == "1":

        create_new_database(flag_information)

    elif choice_oprions == "2":

        open_database()
        names = str(input("Enter your names : "))
        create_new_table(names=names)

    elif choice_oprions == "3":

        show_databasess(flag_information)

