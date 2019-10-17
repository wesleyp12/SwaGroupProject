#!/usr/bin/python

import mysql.connector as mariadb
import sys

argOne = sys.argv[1]
argTwo = sys.argv[2]

currentUser = ""
userLogedIn = False

mariadb_connection = mariadb.connect(user="root", password = "", database="swaProject")
cursor = mariadb_connection.cursor()

def login(userName, password):
    cursor.execute("INSERT INTO userLogin(userName, password) values ('"+ userName+ "', '"+ password + "')")
    return currentUser + userName

def logedInUser():
    print(currentUser)

def results():
    cursor.execute("select * from userLogin")
    getResults = cursor.fetchall()
    print(getResults)



login(argOne, argTwo)
results()
logedInUser()
