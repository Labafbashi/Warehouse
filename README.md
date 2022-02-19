# Warehouse
### Final Project of Database in Linux Project (Python and MySql)
### EC-Utbildning
###### MohammadHossein Labafbashi
###### Paramont@gmail.com
###### [Linkedin](https://www.linkedin.com/in/labafbashi)
###### version: 202202.001

**About Project**

This is a project about warehouses. On this project, we have many parts such as Products, Customers, Staff, and orders. End-user can add, delete, edit, and look at each part of the Warehouse. I did use an HTML template, CSS to design a web page, Rest Application with Python Flask.

**Requirments**

- Linux Operating System.
	you can install Ubuntu20.1 on the virtual michine or using other Linux distribution.
- Python version 3. (sudo apt-get install python)
- Virtual environment for python 3 (sudo apt-get install python3-virtualenv)
- Mysql (sudo apt-get install mysql)
- Github user.
- Some python packages that intruduce later.
- internet connection.

**How To Install Project**

 1. Download project from GitHub repository.
	````
	cd ~
	git clone git@github.com:Labafbashi/Warehouse.git
	````
 2. Change directory to project folder.
	````
	cd Warehouse
	````
 3. excute below file on mysql to create a database and some sample data.
	````
	cd documents
	mysql -u root -p
	mysql> source warehouse.sql
	````
 4. install virtual environment on your project folder.
	````
	python3 -m pip install virtualenv
	````
 5. Create you virtualenv on the project folder.
	````
	virtualenv -p /usr/bin/python3 venv
	````
 6. Activate your virtualenv.
	````
	source venv/bin/activate
	````
 7. install Flask on the project folder.
	````
	(venv) python3 -m pip install flask
	````
 8. install database connector on the project folder.
	````
	(venv) python3 -m pip install mysql-connector-python
	````
 9. excute main file of project with python.
	````
	(venv) python3 warehouse.py
	````
10. Open firefox and run below web page address.
	````
	http://127.0.0.1:5000
	````
