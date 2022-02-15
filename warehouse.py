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
	
@app.route("/AddOrder.html", methods=["POST", "GET"])
def addOrders():
	product_list=dbo.showProduct()
	if request.method == "POST":
		opid = int(request.form["ProductSelect"])
		ocid = int(request.form["CustomerSelect"])
		osid = int(request.form["StaffSelect"])
		ocount = int(request.form["pamount"])
		add_new = dbo.addOrders(opid, ocid, osid, ocount)
		return redirect(url_for('addOrders'))
	else:
		return render_template('AddOrder.html', option_list=product_list)


if __name__=='__main__':
	app.run(debug=True)
