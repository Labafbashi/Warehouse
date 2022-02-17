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
    cursor.execute("SELECT o.id, \
			p.name as product_name, \
			Concat(c.first_name,' ',c.last_name) as customer_name, \
			Concat(s.first_name,' ',s.last_name) as staff_name, \
			o.count, p.price, \
			round(o.count*p.price,2) as total_price \
			FROM Orders as o inner join Products as p, Customers as c, Staffs as s \
			where o.product_id=p.id and o.customer_id=c.id and o.staff_id=s.id;")
    rows = cursor.fetchall()
    return rows

def showExacProduct(pid):
	sql="select * from Products where id=%s ;" % pid
	cursor.execute(sql)
	row = cursor.fetchall()
	return row

def delExacProduct(pid):
	sql="delete from Products where id=%s ;" % pid
	cursor.execute(sql)
	connection.commit()
	return 1

def showExacCustomer(cid):
  sql="select * from Customers where id=%s ;" % cid
  cursor.execute(sql)
  row = cursor.fetchall()
  return row

def delExacCustomer(cid):
  sql="delete from Customers where id=%s ;" % cid
  cursor.execute(sql)
  connection.commit()
  return 1

def showExacStaff(sid):
  sql="select * from Staffs where id=%s ;" % sid
  cursor.execute(sql)
  row = cursor.fetchall()
  return row

def delExacStaff(sid):
  sql="delete from Staffs where id=%s ;" % sid
  cursor.execute(sql)
  connection.commit()
  return 1

def showExacOrder(oid):
  sql="SELECT o.id, \
		p.name as product_name, \
    Concat(c.first_name,' ',c.last_name) as customer_name, \
    Concat(s.first_name,' ',s.last_name) as staff_name, \
    o.count, p.price, \
    round(o.count*p.price,2) as total_price \
		FROM Orders as o inner join Products as p, Customers as c, Staffs as s  \
    where o.product_id=p.id and o.customer_id=c.id and o.staff_id=s.id \
    and o.id = %s ;" % oid 
  cursor.execute(sql)
  row = cursor.fetchall()
  return row

def delExacOredr(oid):
  sql="delete from Orders where id=%s ;" % oid
  cursor.execute(sql)
  connection.commit()
  return 1
