#!/usr/bin/python
#^[0-9]+\s[0-9]+\s[0-9]+\s[0-9]+$
import databaseFile

def login():
    username = input ("Input your Username: ")
    password = input ("Input your Password: ")

    result = databaseFile.query("SELECT * FROM userLogin WHERE userName = '" + username + "' AND password = '" + password + "';")
    check = result.fetchone

    if not check:
        return False
    else:
        return True

databaseFile.createTable()

success = login()
while(success == False):
    print("Invalid Username/Password Combo. Please Retry.\n")
    success = login()

print("Successful Login\n")