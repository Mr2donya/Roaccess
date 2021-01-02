import mysql.connector
import stdiomask


def ini_file():

    try:

        FILE_INI = open("user.ini", mode="r")
        global FILE_READ 
        FILE_READ = FILE_INI.readlines()

        return True

    except:

        return False


def open_database():

    flag_information = ini_file()

    if flag_information:

        global host
        host = str(input("[?] Enter your host { empty for localhost } : "))

        if host == "":
            host = "localhost"

        global user 
        user = str(input("[?] Enter your database username : "))

        global password 
        password = stdiomask.getpass(prompt = '[?] Enter your database password : ')

        global database 
        database = str(input("[?] Enter your database name : "))

        try:

            mydb = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            print("Your Database successfully Opened")

        except:

            print("open Your Database filed")

    else:

        try:

            mydb = mysql.connector.connect(
                host=FILE_READ[0],
                user=FILE_READ[1],
                password=FILE_READ[2],
                database=FILE_READ[3]
            )

            print("Your Database successfully Opened")

        except:

            print("open Your Database filed")


def create_new_database(flag_information):


    if flag_information :

        ini_file()

        new_database_name = str(input("Enter your database name : "))

        mydb = mysql.connector.connect(
            
            host = FILE_READ[0],
            user = FILE_READ[1],
            password = FILE_READ[2]
        )

        mycursor = mydb.cursor()

        mycursor.execute("CREATE DATABASE " + new_database_name)

        print("Your Database successfully created")                


    else :

        host = str(input("[?] Enter your host { empty for localhost } : "))
        user = str(input("[?] Enter your database username : "))
        password = stdiomask.getpass(prompt = '[?] Enter your database password : ')
        new_database_name = str(input("Enter your database name : "))

        try :

            mydb = mysql.connector.connect(
                host=host,
                user=user,
                password=password
            )

            mycursor = mydb.cursor()

            mycursor.execute("CREATE DATABASE " + new_database_name)

            print("Your Database successfully created")

        except Exception as error_create_new_database:

            if "Access denied" in str(error_create_new_database) :

                print("You do not have the privilege to create a database :(")
            
            else : 

                print("Error : Create new database :(")




def show_databasess(flag_information):

    if flag_information:

        host = str(input("[?] Enter your host { empty for localhost } : "))

        mydb = mysql.connector.connect(

            host=host,
            user=FILE_READ[0],
            password=FILE_READ[1]
        )

        mycursor = mydb.cursor()

        mycursor.execute("SHOW DATABASES")

        for x in mycursor:

            print(x)
    else:

        host = str(input("[?] Enter your host { empty for localhost } : "))

        if host == "" :
            host = "localhost"

        user = str(input("[?] Enter your database username : "))
        password = stdiomask.getpass(prompt = '[?] Enter your database password : ')

        mydb = mysql.connector.connect(

            host=host,
            user=user,
            password=password
        )

        mycursor = mydb.cursor()

        mycursor.execute("SHOW DATABASES")

        for x in mycursor:

            print(x)


def create_new_table (names) :

    names_s = names.split()
    print(names_s[0])

    new_table_name = str(input("Enter your table name : "))

    mydb = mysql.connector.connect(

        host=host,
        user=user,
        password=password,
        database=database
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE TABLE " + new_table_name +
                     " (" + names_s[0] + " tinytext)")

    for x in range(len(names_s)) :
        
        if x != 0 :
            mycursor.execute("ALTER TABLE " + new_table_name + " ADD " + names_s[x] + " tinytext;")

    print("Your table ( " + new_table_name + " ) created on " + database)