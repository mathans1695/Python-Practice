import sqlite3
from emp import Employee

def add_data(emp):
	conn = sqlite3.connect('employee.db')
	c = conn.cursor()
	c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})
	conn.commit()
	conn.close()
	
def get_emp_by_name(first_name):
	conn = sqlite3.connect('employee.db')
	c = conn.cursor()
	c.execute("SELECT * FROM employees WHERE first_name = :first", {'first': first_name})
	data = c.fetchall()
	conn.close()
	return data
	
def update_data(emp, pay):
	conn = sqlite3.connect('employee.db')
	c = conn.cursor()
	c.execute("""UPDATE employees SET pay = :pay 
				 WHERE first_name = :first AND last_name = :last""",
				 {'first': emp.first, 'last': emp.last, 'pay': pay})
	conn.commit()
	conn.close()
	
def delete(emp):
	conn = sqlite3.connect('employee.db')
	c = conn.cursor()
	c.execute("DELETE FROM employees WHERE first_name = :first AND last_name = :last OR pay = :pay", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})
	conn.commit()
	conn.close()
	
def get_all():
	conn = sqlite3.connect('employee.db')
	c = conn.cursor()
	c.execute("SELECT * FROM employees")
	data = c.fetchall()
	conn.close()
	return data
	
emp1 = Employee('Mahalingam', 'Sundararaj', 50000)
emp2 = Employee('Suresh', 'Sundararaj', 50000)

conn = sqlite3.connect('employee.db')
c = conn.cursor()

c.execute("""CREATE TABLE employees (first_name, last_name, pay)""")
conn.commit()

add_data(emp1)
add_data(emp2)

print(get_all())

conn.close()