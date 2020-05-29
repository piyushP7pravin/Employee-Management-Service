from ems_services import Ems_services
from employee import *
import tkinter
from tkinter import messagebox

class Login:
	def __init__(self):
		self.root=tkinter.Tk()
		self.root.title("EMS Services")
		self.root.geometry("300x150")
		self.__user="admin"
		self.__pass="admin"
		tkinter.Label(self.root,text="Username").grid(row=0,column=0,padx=40,pady=20)
		tkinter.Label(self.root,text="Password").grid(row=1,column=0)
		self.__username=tkinter.Entry(self.root)
		self.__username.grid(row=0,column=1,pady=20)
		self.__password=tkinter.Entry(self.root,show="*")
		self.__password.grid(row=1,column=1)
		tkinter.Button(self.root,text="Login",command=self.login).grid(row=3,column=1,pady=20)
		self.__password.bind("<Return>",self.login)
		tkinter.Button(self.root,text="Clear",command=self.clear).grid(row=3,columnspan=3)
		self.root.mainloop()
	def login(self,event=None):
		u=self.__username.get()
		p=self.__password.get()
		if self.__user==u and self.__pass==p:
			messagebox.showinfo("EMS Services","Login success")
			self.root.destroy()
			EMS()
		else:
			messagebox.showerror("Error","Wrong username or password")
	
	def clear(self):
		self.__username.delete(0,"end")
		self.__password.delete(0,"end")

class EMS:
	def __init__(self):
		self.root=tkinter.Tk()
		self.root.title("EMS Services")
		self.root.geometry("230x300")
		tkinter.Label(self.root,text="Select your choice",font=("consolas",14)).grid(row=0,columnspan=1,padx=20,pady=10)
		self.__choice=tkinter.StringVar()
		self.__choice.set("1")
		tkinter.Radiobutton(self.root,text="1. Add Record",font=("consolas",12),variable=self.__choice,value="1").grid(row=1,column=0)
		tkinter.Radiobutton(self.root,text="2. View all",font=("consolas",12),variable=self.__choice,value="2").grid(row=2,column=0)
		tkinter.Radiobutton(self.root,text="3. Search by ID",font=("consolas",12),variable=self.__choice,value="3").grid(row=3,column=0)
		tkinter.Radiobutton(self.root,text="4. Delete by ID",font=("consolas",12),variable=self.__choice,value="4").grid(row=4,column=0)
		tkinter.Button(self.root,text="Select",font=(10),command=self.menu).grid(row=5,column=0,pady=10)
		tkinter.Button(self.root,text="Exit",font=(10),command=self.root.destroy).grid(row=6,column=0)
		self.root.mainloop()
	def menu(self):
		if self.__choice.get()=="1":
			self.root.destroy()
			addRecord()
		elif self.__choice.get()=="2":
			self.root.destroy()
			viewAll()
		elif self.__choice.get()=="3":
			self.root.destroy()
			search()
		elif self.__choice.get()=="4":
			self.root.destroy()
			delete()
			

class addRecord():
	def __init__(self):
		self.root=tkinter.Tk()
		self.root.title("EMS Services - Add record")
		self.root.geometry("500x300")
		tkinter.Label(self.root,text="Enter employee details",font=("Consolas",14)).grid(row=0,columnspan=1,padx=40,pady=20)
		tkinter.Label(self.root,text="Employee ID :").grid(row=1,column=0)
		tkinter.Label(self.root,text="Employee Name :").grid(row=2,column=0)
		tkinter.Label(self.root,text="Employee Salary :").grid(row=3,column=0)
		tkinter.Label(self.root,text="Employee Address :").grid(row=4,column=0)
		self.__id=tkinter.Entry(self.root)
		self.__id.grid(row=1,column=1)
		self.__name=tkinter.Entry(self.root)
		self.__name.grid(row=2,column=1)
		self.__salary=tkinter.Entry(self.root)
		self.__salary.grid(row=3,column=1)
		self.__address=tkinter.Entry(self.root)
		self.__address.grid(row=4,column=1)
		tkinter.Button(self.root,text="ADD Record",command=self.add).grid(row=5,column=0,pady=10)
		tkinter.Button(self.root,text="Main Menu",command=self.main_menu).grid(row=5,column=1)
		tkinter.Button(self.root,text="Exit",command=self.exit).grid(row=5,column=2)
		self.root.mainloop()
	def main_menu(self):
		self.root.destroy()
		EMS()
	def exit(self):
		self.root.destroy()
	def add(self):
		emp=Employee()
		emp.setId(self.__id.get())
		emp.setName(self.__name.get())
		emp.setSalary(self.__salary.get())
		emp.setAddress(self.__address.get())
		if Ems_services.addEmployee(emp):
			messagebox.showinfo("EMS Services - Add record","Record added successfully")
			self.root.destroy()
			addRecord()
		else:
			messagebox.showerror("EMS Services - Add record","ID already exists")
			self.root.destroy()
			addRecord()
	
class viewAll:
	def __init__(self):
		self.root=tkinter.Tk()
		self.root.geometry("500x300")
		self.root.title("EMS Services - View all")
		lst=Ems_services.getAllEmployees()
		if len(lst)==0:
			tkinter.Label(self.root,text="No record exists",font=(8)).pack()
		else:
			for i in lst:
				tkinter.Label(self.root,text=i,font=(6),anchor="w",relief="groove",width=500).pack()
		tkinter.Button(self.root,text="Main Menu",font=(4),command=self.main_menu).pack(pady=10)
		tkinter.Button(self.root,text="Exit",font=(4),command=self.exit).pack()
	def main_menu(self):
		self.root.destroy()
		EMS()
	def exit(self):
		self.root.destroy()
		
		
if __name__=="__main__":
	Login()
	'''while True:
		print()
		print("1. Add record")
		print("2. View all")
		print("3. Search by ID")
		print("4. Delete by ID")
		print("5. Exit")
		choice=int(input("Enter your choice : "))
		if choice==1:
			emp=Employee()
			emp.setId(int(input("Enter Id : ")))
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
				print("No record available")
			else:
				for i in lst:
					print(i)
		elif choice==3:
			emp=Ems_services.searchById(int(input("Enter ID: ")))
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
			print("Thank You")
			break
		else:
			print("Wrong Choice")'''
			