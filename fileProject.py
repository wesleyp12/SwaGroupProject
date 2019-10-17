#!/usr/bin/python
#^[0-9]+\s[0-9]+\s[0-9]+\s[0-9]+$
import mysql.connector as mariadb
import sys

argOne = sys.argv[1]
argTwo = sys.argv[2]

currentUser = ""
userLogedIn = False

mariadb_connection = mariadb.connect(user="root", password = "", database="swaProject")
cursor = mariadb_connection.cursor()

def createLogin(userName, password):
    cursor.execute("INSERT INTO userLogin(userName, password) values ('"+ userName+ "', '"+ password + "')")
    currentUser + userName
    return currentUser


def logedInUser():
    print(currentUser)


def results():
    cursor.execute("select * from userLogin")
    getResults = cursor.fetchall()
    print(getResults)


def()
createLogin(argOne, argTwo)
results()
logedInUser()
