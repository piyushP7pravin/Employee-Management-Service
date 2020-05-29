from ems_services import Ems_services
from employee import *

if __name__=="__main__":
	while True:
		print()
		print("1. Add record")
		print("2. View all")
		print("3. Search by ID")
		print("4. Delete by ID")
		print("5. Search by Name")
		print("6. Search by Salary Range")
		print("7. View in descending order of salary")
		print("8. View in alphabetic order of Name")
		print("9. Exit")
		choice=int(input("Enter your choice : "))
		if choice==1:
			emp=Employee()
			emp.setId(int(input("Enter ID : ")))
			emp.setName(input("Enter Name : "))
			emp.setSalary(float(input("Enter Salary : ")))
			emp.setAddress(input("Enter Address : "))	
			if Ems_services.addEmployee(emp):
				print("Record Inserted")
			else:
				print("Id already exists")
		elif choice==2:
			lst=Ems_services.getAllEmployees()
			if len(lst)==0:
				print("No record found")
			else:
				for i in lst:
					print(i)
		elif choice==3:
			emp=Ems_services.searchById(int(input("Enter ID : ")))
			if emp==None:
				print("No such ID exists")
			else:
				print(emp)
		elif choice==4:
			emp=Ems_services.deleteById(int(input("Enter ID: ")))
			if emp==False:
				print("No such record exists")
			else:
				print("Record deleted")
		elif choice==5:
			emp=Ems_services.searchByName(input("Enter Name : "))
			if len(emp)==0:
				print("No such name exists")
			else:
				for e in emp:
					print(e)
		elif choice==6:
			emp=Ems_services.searchBySalRange(float(input("Enter min salary : ")),float(input("Enter max salary : ")))
			if len(emp)==0:
				print("No record in given salary range")
			else:
				for e in emp:
					print(e)
		elif choice==7:
			emp=Ems_services.descSalary()
			if len(emp)==0:
				print("No record exists")
			else:
				for e in emp:
					print(e)
		elif choice==8:
			emp=Ems_services.alphaName()
			if len(emp)==0:
				print("No record exists")
			else:
				for e in emp:
					print(e)
		elif choice==9:
			print("Thank You")
			break
		else:
			print("wrong entry.")
		
				