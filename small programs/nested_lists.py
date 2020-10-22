num_of_emp = int(input("Enter number of employees details you want to enter: "))
print ("Enter employees details: ")

i = 0
employee_details = []

while i < num_of_emp:
	employee_details[i][0], employee_details[i][1], employee_details[i][2] = input("Name: "), int(input("Age: ")), input("Department: ")
	
	i += 1

for j in range(len(employee_details[0])):
	if employee_details[0][j]  == "Lisa Crawford":
		print ("Name: {0}\nAge: {1}\nDepartment: {2} " .format(employee_details[j][0], employee_details[j][1], employee_details[j][2]))