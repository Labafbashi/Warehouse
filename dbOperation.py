import mysql.connector
from datetime import datetime
import sys

#database connection
try:
	connection = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "password",
		database = "warehouse",
		auth_plugin='mysql_native_password')
	print("DB  Connected.")
except:
	print("Unable to connect to the database.")

cursor = connection.cursor()
datenow = datetime.now()


def addProduct(pname,pprice,pamount):
	sql="select * from Products where name='" + pname + "';"
	cursor.execute(sql)
	row = cursor.fetchone()
	if cursor.rowcount == 0:
		cursor.execute("INSERT INTO Products(name, price,amount,created_at,updated_at) VALUES (%s, %s, %s, %s, %s)", (pname,pprice,pamount,datenow,datenow))
		connection.commit()
		return 1
	else:
		return -1

def addCustomer(cfirstname, clastname, cstreet, cpostcode, cage):
	sql = "SELECT * FROM Customers where first_name='" + cfirstname + "' and last_name='" + clastname + "';"
	cursor.execute(sql)
	row = cursor.fetchall()
	if cursor.rowcount == 0:
		cursor.execute("INSERT INTO Customers(first_name, last_name, street, post_code, age,created_at,updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s)", (cfirstname, clastname, cstreet, cpostcode, cage,datenow,datenow))
		connection.commit()
		return 1
	else:
		return -1

def addStuffs(sfirstname, slastname, ssempsince, sage):
	sql = "SELECT * FROM Staffs where first_name='" + sfirstname + "' and last_name='" + slastname + "';"
	cursor.execute(sql)
	row = cursor.fetchall()
	if cursor.rowcount == 0:
		cursor.execute("INSERT INTO Staffs(first_name, last_name, employee_since, age,created_at,updated_at) VALUES (%s, %s, %s, %s, %s, %s)", (sfirstname, slastname, ssempsince, sage,datenow,datenow))
		connection.commit()
		return 1
	else:
		return -1

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
    round(o.count*p.price,2) as total_price, p.id, c.id, s.id \
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

def editProduct(pID,pName,pPrice,pAmount):
	sql="select * from Products where name='" + pName + "';"
	cursor.execute(sql)
	row = cursor.fetchone()
	if cursor.rowcount == 0:
		cursor.execute("update Products set name= %s, price= %s, amount= %s, updated_at=%s where id=%s", (pName,pPrice,pAmount,datenow,pID))
		connection.commit()
		return 1
	else:
		return -1

def editCustomer(cID,fName,lName,cStreet,cPostCode,cAge):
	sql = "SELECT * FROM Customers where first_name='" + fName + "' and last_name='" + lName + "';"
	cursor.execute(sql)
	row = cursor.fetchall()
	if cursor.rowcount == 0:
		cursor.execute("update Customers set first_name= %s, last_name= %s, street= %s, post_code= %s, age= %s, updated_at=%s where id=%s", (fName,lName,cStreet,cPostCode,cAge,datenow,cID))
		connection.commit()
		return 1
	else:
		return -1

def editStaff(sid,fName,lName,sEmployeeSince,sAge):
	sql = "SELECT * FROM Staffs where first_name='" + fName + "' and last_name='" + lName + "';"
	cursor.execute(sql)
	row = cursor.fetchall()
	if cursor.rowcount == 0:
		cursor.execute("update Staffs set first_name= %s, last_name= %s, employee_since= %s, age= %s, updated_at=%s where id=%s", (fName,lName,sEmployeeSince,sAge,datenow,sid))
		connection.commit()
		return 1
	else:
		return -1

def editOrder(oid,productid,customerid,staffid,ocount):
  cursor.execute("update Orders set product_id= %s, customer_id= %s, staff_id= %s, count= %s, updated_at=%s where id=%s", (productid,customerid,staffid,ocount,datenow,oid))
  connection.commit()
  return 1
