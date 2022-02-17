from flask import Flask, redirect, url_for, render_template, request, flash, request
import dbOperation as dbo

app=Flask(__name__)

@app.route("/")
@app.route("/Main.html")
def mainPage():
	return render_template('Main.html')

@app.route("/AddProduct.html", methods=["POST", "GET"])
def addProduct():
	if request.method == "POST":
		pName = request.form["pname"]
		pPrice = float(request.form["pprice"])
		pAmount = int(request.form["pamount"])
		add_new = dbo.addProduct(pName,pPrice,pAmount)
		return redirect(url_for('addProduct'))
	else:
		return render_template('AddProduct.html')

@app.route("/AddCustomer.html", methods=["POST", "GET"])
def addCustomer():
	if request.method == "POST":
		cfName = request.form["fname"]
		clName = request.form["lname"]
		cStreet = request.form["cstreet"]
		cPostCode = int(request.form["cpostcode"])
		cAge = int(request.form["cage"])
		add_new = dbo.addCustomer(cfName,clName,cStreet,cPostCode,cAge)
		return redirect(url_for('addCustomer'))
	else:
		return render_template('AddCustomer.html')
	
@app.route("/AddStaff.html", methods=["POST", "GET"])
def addStuffs():
	if request.method == "POST":
		sfName = request.form["fname"]
		slName = request.form["lname"]
		sEmployeeSince = request.form["semployeesince"]
		sAge = int(request.form["sage"])
		add_new = dbo.addStuffs(sfName,slName,sEmployeeSince,sAge)
		return redirect(url_for('addStuffs'))
	else:
		return render_template('AddStaff.html')

@app.route("/AddOrder.html")
def fillCombo():
	product_list=dbo.showProduct()
	customer_list=dbo.showCustomer()
	staff_list=dbo.showStaff()
	return render_template('AddOrder.html', product_list=product_list,customer_list=customer_list,staff_list=staff_list)

@app.route("/AddOrder.html", methods=["POST", "GET"])
def addOrders():
	if request.method == "POST":
		opid = int(request.form["ProductSelect"])
		ocid = int(request.form["CustomerSelect"])
		osid = int(request.form["StaffSelect"])
		ocount = int(request.form["pamount"])
		add_new = dbo.addOrders(opid, ocid, osid, ocount)
		return redirect(url_for('addOrders'))
	else:
		return render_template('AddOrder.html')

@app.route("/ShowProduct.html")
def showProducts():
	product_list=dbo.showProduct()
	return render_template('ShowProduct.html', product_list=product_list)

@app.route("/ShowCustomer.html")
def showCustomer():
	customer_list=dbo.showCustomer()
	return render_template("ShowCustomer.html", customer_list=customer_list)

@app.route("/ShowStaff.html")
def showStaff():
	staff_list=dbo.showStaff()
	return render_template("ShowStaff.html", staff_list=staff_list)

@app.route("/ShowOrder.html")
def showOrder():
	order_list=dbo.showOrder()
	return render_template("ShowOrder.html", order_list=order_list)

@app.route("/DelProduct.html")
def delProductMain():
	product_list=dbo.showProduct()
	return render_template('DelProduct.html', product_list=product_list)

@app.route("/DelProduct.html/<int:pid>")
def delProductID(pid):
	if (request.args.get("submit") == "Submit"):
		dbo.delExacProduct(int(pid))
		return redirect(url_for('delProductMain'))
	else:
		exac_product=dbo.showExacProduct(int(pid))
		return render_template('DelProduct.html', exac_product=exac_product)

@app.route("/DelCustomer.html")
def delCustomerMain():
  customer_list=dbo.showCustomer()
  return render_template('DelCustomer.html', customer_list=customer_list)

@app.route("/DelCustomer.html/<int:cid>")
def delCustomerID(cid):
  if (request.args.get("submit") == "Submit"):
    dbo.delExacCustomer(int(cid))
    return redirect(url_for('delCustomerMain'))
  else:
    exac_customer=dbo.showExacCustomer(int(cid))
    return render_template('DelCustomer.html', exac_customer=exac_customer)

@app.route("/DelStaff.html")
def DelStaffMain():
  staff_list=dbo.showStaff()
  return render_template('DelStaff.html', staff_list=staff_list)

@app.route("/DelStaff.html/<int:sid>")
def DelStaffID(sid):
  if (request.args.get("submit") == "Submit"):
    dbo.delExacStaff(int(sid))
    return redirect(url_for('DelStaffMain'))
  else:
    exac_staff=dbo.showExacStaff(int(sid))
    return render_template('DelStaff.html', exac_staff=exac_staff)

@app.route("/DelOrder.html")
def DelOrderMain():
  order_list=dbo.showOrder()
  return render_template('DelOrder.html', order_list=order_list)

@app.route("/DelOrder.html/<int:oid>")
def DelOrderID(oid):
  if (request.args.get("submit") == "Submit"):
    dbo.delExacOredr(int(oid))
    return redirect(url_for('DelOrderMain'))
  else:
    exac_order=dbo.showExacOrder(int(oid))
    return render_template('DelOrder.html', exac_order=exac_order)

@app.route("/EditProduct.html")
def editProductMain():
	product_list=dbo.showProduct()
	return render_template('EditProduct.html', product_list=product_list)

@app.route("/EditProduct.html/<int:pid>", methods=["POST", "GET"])
def editProductID(pid):
	if request.method == "POST":
		pID = request.form["pid"]
		pName = request.form["pname"]
		pPrice = float(request.form["pprice"])
		pAmount = int(request.form["pamount"])
		edit_row = dbo.editProduct(pID,pName,pPrice,pAmount)
		return redirect(url_for('editProductID'))
	else:
		exac_product=dbo.showExacProduct(int(pid))
		product_list=exac_product
		return render_template('EditProduct.html', exac_product=exac_product, product_list=product_list)

if __name__=='__main__':
	app.run(debug=True)
