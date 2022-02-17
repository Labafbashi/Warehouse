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
		return render_template('AddProduct.html', text="No Value.")

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

if __name__=='__main__':
	app.run(debug=True)
