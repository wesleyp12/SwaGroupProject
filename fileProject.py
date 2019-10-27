#!/usr/bin/python
#^[0-9]+\s[0-9]+\s[0-9]+\s[0-9]+$
import sqlite3

conn = sqlite3.connect('SWADatabase.db')
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS users([username] VARCHAR PRIMARY KEY, [password] VARCHAR)")
c.execute("INSERT INTO users([username], [password]) VALUES('admin', 'admin')")
c.execute("INSERT INTO users([username], [password]) VALUES('username', 'password')")

c.execute("CREATE TABLE IF NOT EXISTS products([productNum] VARCHAR PRIMARY KEY, [productName] CHAR , [price] VARCHAR, [stock] VARCHAR, [department] VARCHAR)")
c.execute("INSERT INTO products([productNum], [productName], [price], [stock], [department]) VALUES('1', 'Glad 13G Trash Bags', '16.37', '50', 'Household')")
c.execute("INSERT INTO products([productNum], [productName], [price], [stock], [department]) VALUES('2', '23pc. Kitchen Utensil Set', '24.99', '100', 'Household')")
c.execute("INSERT INTO products([productNum], [productName], [price], [stock], [department]) VALUES('3', '6-Quart Crock-Pot Slow Cooker', '24.71', '25', 'Household')")
c.execute("INSERT INTO products([productNum], [productName], [price], [stock], [department]) VALUES('4', 'The Great Gatsby', '9.89', '100', 'Book')")
c.execute("INSERT INTO products([productNum], [productName], [price], [stock], [department]) VALUES('5', 'Animal Farm', '7.19', '150', 'Book')")
c.execute("INSERT INTO products([productNum], [productName], [price], [stock], [department]) VALUES('6', 'The Catcher in the Rye', '8.59', '75', 'Book')")
c.execute("INSERT INTO products([productNum], [productName], [price], [stock], [department]) VALUES('7', 'Shrek Pulsh Toy', '17.88', '500', 'Toys')")
c.execute("INSERT INTO products([productNum], [productName], [price], [stock], [department]) VALUES('8', 'LEGO Bionicle Building Kit', '39.95', '100', 'Toys')")
c.execute("INSERT INTO products([productNum], [productName], [price], [stock], [department]) VALUES('9', 'Set of 3 Flingshot Monkeys', '14.99', '49', 'Toys')")
c.execute("INSERT INTO products([productNum], [productName], [price], [stock], [department]) VALUES('10', 'Apple AirPods', '144.00', '80', 'Electronics')")
c.execute("INSERT INTO products([productNum], [productName], [price], [stock], [department]) VALUES('11', '1byone Turntable w/ Speaker', '49.99', '50', 'Electronics')")
c.execute("INSERT INTO products([productNum], [productName], [price], [stock], [department]) VALUES('12', 'TI-30XS Scientific Calculator', '14.88', '30', 'Electronics')")

c.close()

conn.row_factory = sqlite3.Row
c = conn.cursor()

def login():
    username = input ("Input your Username: ")
    password = input ("Input your Password: ")

    result = c.execute("SELECT * FROM users WHERE userName = '" + username + "' AND password = '" + password + "';")
    check = result.fetchone()

    if not check:
        return False
    else:
        return True

success = login()
while(success == False):
    print("Invalid Username/Password Combo. Please Retry.\n")
    success = login()

print("Successful Login\n")
runningTotal = 0
opt = ""
container = ['', '']
cart = []
i = 0

while opt != '4':
    print("Please select an action: (type 1-4)")
    print("1. View Inventory")
    print("2. View Cart")
    print("3. View Purchase History")
    print("4. Exit")
    opt = input(": ")
    print("")

    if opt == "1":
        result = c.execute("SELECT * FROM products")
        rows = result.fetchall()
        for row in rows:
            print(row[0] + '     ' + row[1] + '     ' + row[2] + '     ' + row[3] + '     ' + row[4])

        add = ""
        while add != 'back':
            add = input("\nPlease select item to add to cart (Use the number): ")
            adding = c.execute("SELECT * FROM products WHERE productNum = '" + add +"';")
            rows = adding.fetchall()

            if add == 'back':
                break
            elif add != '1' and add != '2' and add != '3' and add != '4' and add != '5' and add != '6' and add != '7' and add != '8' and add != '9' and add != '10' and add != '11' and add != '12':
                print("Invalid Selection\n")
            else:
                for row in rows:
                    container[0] = row[1]
                    container[1] = row[2]
                    cart.append(container)
                    i = i + 1
    
    if opt == '2':
        for j in len(cart):
            for k in range(0, 2):
                print(cart[j][k])

    if opt == '3':
        break

    if opt == '4':
        exit
            