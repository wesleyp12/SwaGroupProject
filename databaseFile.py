import sqlite3
from sqlite3 import Error

conn = sqlite3.connect('SWADatabase.db')
c = conn.cursor()

def createTable():
    c.execute("DROP TABLE userLogin")
    c.execute("CREATE TABLE IF NOT EXISTS userLogin([username] VARCHAR PRIMARY KEY, [password] VARCHAR)")
    c.execute("INSERT INTO userLogin([username], [password]) VALUES('admin', 'admin')")
    c.execute("INSERT INTO userLogin([username], [password]) VALUES('username', 'password')")

    rows = c.fetchall()

    for row in rows:
        print(row)

def query(string):
    result = c.execute(string)
    return result

def dropTable():
    c.execute("DROP TABLE userLogin")
    print("Table Dropped\n")

createTable()