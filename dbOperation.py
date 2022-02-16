import mysql.connector
from datetime import datetime
import sys

#database connection
try:
	connection = mysql.connector.connect(
		host = "localhost",
		user = "paramont",
		password = "Monaliza!360",
		database = "warehouse",
		auth_plugin='mysql_native_password')
	print("DB  Connected.")
except:
	print("Unable to connect to the database.")

cursor = connection.cursor()
datenow = datetime.now()
#inserting data to db
def addProduct(pname,pprice,pamount):
	cursor.execute("INSERT INTO Products(name, price,amount,created_at,updated_at) VALUES (%s, %s, %s, %s, %s)", (pname,pprice,pamount,datenow,datenow))
	connection.commit()
	return 1

def addCustomer(cfirstname, clastname, cstreet, cpostcode, cage):
    cursor.execute("INSERT INTO Customers(first_name, last_name, street, post_code, age,created_at,updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s)", (cfirstname, clastname, cstreet, cpostcode, cage,datenow,datenow))
    connection.commit()
    return 1

def addStuffs(sfirstname, slastname, ssempsince, sage):
    cursor.execute("INSERT INTO Staffs(first_name, last_name, employee_since, age,created_at,updated_at) VALUES (%s, %s, %s, %s, %s, %s)", (sfirstname, slastname, ssempsince, sage,datenow,datenow))
    connection.commit()
    return 1

def addOrders(opid,ocid,osid,ocount):
    cursor.execute("INSERT INTO Orders(product_id, customer_id, staff_id, count, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s)", (opid,ocid,osid,ocount,datenow,datenow))
    connection.commit()
    return 1

def showProduct():
    cursor.execute("SELECT * FROM Products")
    rows = cursor.fetchall()
    return rows

def showCustomer():
    cursor.execute("SELECT * FROM Customers")
    rows = cursor.fetchall()
    return rows

def showStaff():
    cursor.execute("SELECT * FROM Staffs")
    rows = cursor.fetchall()
    return rows

def showOrder():
    cursor.execute("SELECT p.name as product_name,c.last_name as customer_name,s.last_name as staff_name,o.* FROM Orders as o inner join Products as p, Customers as c, Staffs as s where o.product_id=p.id and o.customer_id=c.id and o.staff_id=s.id;")
    rows = cursor.fetchall()
    return rows
