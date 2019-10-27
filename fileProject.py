#!/usr/bin/python
#^[0-9]+\s[0-9]+\s[0-9]+\s[0-9]+$
import sqlite3

conn = sqlite3.connect('SWADatabase.db')
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS users([username] VARCHAR PRIMARY KEY, [password] VARCHAR, [address] VARCHAR)")
c.execute("INSERT INTO users([username], [password], [address]) VALUES('admin', 'admin', '12345 Example Road Starkville, MS 54321')")
c.execute("INSERT INTO users([username], [password], [address]) VALUES('username', 'password', '98765 Sample Street Starkville, MS 43210')")

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

c.execute("CREATE TABLE IF NOT EXISTS purchaseHistory([orderNum] VARCHAR, [total] VARCHAR, [card] VARCHAR, [address] VARCHAR, [username] VARCHAR)")

c.close()

conn.row_factory = sqlite3.Row
c = conn.cursor()

def login():
    retArray = []
    username = input ("Input your Username: ")
    password = input ("Input your Password: ")

    result = c.execute("SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "';")
    check = result.fetchone()

    retArray.append(check[0])

    if not check:
        retArray.append(False)
        return retArray
    else:
        retArray.append(True)
        return retArray

success = login()
while(success[1] == False):
    print("Invalid Username/Password Combo. Please Retry.\n")
    success = login()

print("Successful Login\n")
username = success[0]
runningTotal = 0
opt = ""
num = ""
option = ""
container = ['', '', '']
cart = []
i = 0
x = 0

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
        add = ""

        while add != 'back':

            for row in rows:
                print(row[0] + '     ' + row[1] + '     ' + row[2] + '     ' + row[3] + '     ' + row[4])

            add = input("\nPlease select item to add to cart (Use the number)(Type back to go back): ")
            adding = c.execute("SELECT * FROM products WHERE productNum = '" + add +"';")
            res = adding.fetchall()

            if add == 'back':
                break
            elif add != '1' and add != '2' and add != '3' and add != '4' and add != '5' and add != '6' and add != '7' and add != '8' and add != '9' and add != '10' and add != '11' and add != '12':
                print("Invalid Selection\n")
            else:
                for row in res:
                    container[0] = 0
                    container[1] = row[1]
                    container[2] = row[2]
                    transfer = container.copy()
                    cart.append(transfer)
                    runningTotal = runningTotal + float(row[2])
                    i = i + 1
    
    if opt == '2':
        option = ''

        while option != 'back':
            for j in range(0, len(cart)):
                cart[j][0] = j
                print(cart[j])
            print('Total Price: ' + str(runningTotal))
            print('')

            print('Please Select an Action:')
            print('1. Checkout')
            print('2. Remove Item')
            option = input(': ')

            if option == '1':
                cardnum = ''
                while cardnum != 'back':
                    print('')
                    cardnum = input('Please input a 10-digit OSC card number (type back to go back): \n')

                    if len(cardnum) != 10:
                        print('')

                    elif len(cardnum) == 10:
                        if cardnum.isdigit():
                            confirmation = ''
                            print('')

                            while confirmation != 'back':
                                confirmation = input("Please type 'confirm' to confirm your purchase or back to go back: \n")

                                if confirmation == 'back':
                                    cardnum = 'back'
                                    option = 'back'
                                    break

                                elif confirmation != 'confirm':
                                    print("")

                                else:
                                    input('Thank you for your purchase. Hit enter to go back to the home page\n')
                                    confirmation = 'back'
                                    option = 'back'

                                    r = c.execute("SELECT address FROM users WHERE username = '" + username + "'")
                                    rows = r.fetchone()

                                    address = rows[0]

                                    c.execute("INSERT INTO purchaseHistory([orderNum], [total], [card], [address], [username]) VALUES('" + str(x) + "', '" + str(runningTotal) + "', '" + cardnum + "', '" + address + "', '" + username + "')")

                                    cardnum = 'back'
                                    cart = []
                                    runningtotal = 0.0
                                    x = x + 1

            elif option == '2':
                num = ''
                while num != 'back':
                    for j in range(0, len(cart)):
                        cart[j][0] = j
                        print(cart[j])
                    print("")
                    num = input("Pick the number of the item to remove(type back to go back): ")

                    if num == 'back':
                        break
                    elif int(num) not in range(0, len(cart)):
                        print("Number not in the cart. Please try again.")
                    elif num != 'back':
                        runningTotal = runningTotal - float(cart[int(num)][2])
                        cart.pop(int(num))


    if opt == '3':
        hist = c.execute("SELECT * FROM purchaseHistory WHERE username = '" + username + "'")
        histList = hist.fetchall()

        if histList == None:
            input("No purchase history found. Press enter to return to home.")
        
        else:
            for row in histList:
                print(row[0] + "     " + row[1] + "     " + row[2] + "     " + row[3] + "     " + row[4])

    if opt == '4':
        exit
            