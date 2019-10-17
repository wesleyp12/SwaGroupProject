#!/usr/bin/python
#^[0-9]+\s[0-9]+\s[0-9]+\s[0-9]+$
import mysql.connector as mariadb

currentUser = ""
userLogedIn = False

mariadb_connection = mariadb.connect(user="root", password = "", database="swaProject")
cursor = mariadb_connection.cursor()

def createLogin(userName, password):
    if(login(userName, password) == False):
        cursor.execute("INSERT INTO userLogin(userName, password) values ('"+ userName+ "', '"+ password + "')")
    else:
        print ("Username and Password combination already exists.")
    return

def login(username, password):
    result = cursor.execute("SELECT * FROM userLogin WHERE userName = '" + username + "' AND password = '" + password + "'")
    if not result:
        return False
    else:
        return True

def logedInUser():
    print(currentUser)


def results():
    cursor.execute("select * from userLogin")
    getResults = cursor.fetchall()
    print(getResults)


input username = "Input your Username: "
input password = "Input your Password: "

if( login(username, password) == True ):
    print ()"login successful"()
    break
else:
    print ()"invalid username/password combo")
    break