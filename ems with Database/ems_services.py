from employee import *
import mysql.connector
import pandas
from dbconnection import DBconnection

class Ems_services:
	@staticmethod
	def addEmployee(emp):
		result=False
		cnx=DBconnection.connect()
		cur=cnx.cursor()
		query="insert into empDetails_2 values(%s,%s,%s,%s)"
		data=[]
		data.append(emp.getId())
		data.append(emp.getName())
		data.append(emp.getSalary())
		data.append(emp.getAddress())
		try:
			cur.execute(query,data)
		except:
			return False
		if (cur.rowcount==1):
			result=True
		cnx.commit()
		cur.close()
		cnx.close()
		return result
		
	@staticmethod
	def getAllEmployees():
		emplist=[]
		cnx=DBconnection.connect()
		cur=cnx.cursor()
		query="select * from empDetails_2"
		cur.execute(query)
		tb=cur.fetchall()
		for row in tb:
			emp=Employee()
			emp.setId(int(row[0]))
			emp.setName(row[1])
			emp.setSalary(float(row[2]))
			emp.setAddress(row[3])
			emplist.append(emp)
		cur.close()
		cnx.close()
		return emplist
		
		
	@staticmethod
	def searchById(id):
		cnx=DBconnection.connect()
		cur=cnx.cursor()
		query="select * from empDetails_2 where empId=%s"
		data=[]
		data.append(id)
		cur.execute(query,data)
		tb=cur.fetchall()
		if cur.rowcount==0:
			cur.close()
			cnx.close()
			return None
		for row in tb:
			emp=Employee()
			emp.setId(int(row[0]))
			emp.setName(row[1])
			emp.setSalary(float(row[2]))
			emp.setAddress(row[3])
		cur.close()
		cnx.close()
		return emp
		

		
	@staticmethod
	def deleteById(id):
		emp=Ems_services.searchById(id)
		if emp==None:
			return False
		else:
			cnx=DBconnection.connect()
			cur=cnx.cursor()
			query="delete from empDetails_2 where empId=%s"
			data=[]
			data.append(id)
			cur.execute(query,data)
			cnx.commit()
			cur.close()
			cnx.close()
			return True
			
	@staticmethod
	def searchByName(name):
		emplist=[]
		cnx=DBconnection.connect()
		cur=cnx.cursor()
		query="select * from empDetails_2 where empName=%s"
		data=[]
		data.append(name)
		cur.execute(query,data)
		tb=cur.fetchall()
		if cur.rowcount==0:
			cur.close()
			cnx.close()
			return None
		for row in tb:
			emp=Employee()
			emp.setId(int(row[0]))
			emp.setName(row[1])
			emp.setSalary(float(row[2]))
			emp.setAddress(row[3])
			emplist.append(emp)
		cur.close()
		cnx.close()
		return emplist
		
	@staticmethod
	def searchBySalRange(min,max):
		emplist=[]
		cnx=DBconnection.connect()
		cur=cnx.cursor()
		query="select * from empDetails_2 where empSalary>%s and empSalary<%s"
		data=[]
		data.append(min)
		data.append(max)
		cur.execute(query,data)
		tb=cur.fetchall()
		for row in tb:
			emp=Employee()
			emp.setId(int(row[0]))
			emp.setName(row[1])
			emp.setSalary(float(row[2]))
			emp.setAddress(row[3])
			emplist.append(emp)
		cur.close()
		cnx.close()
		return emplist
	@staticmethod
	def descSalary():
		emplist=[]
		cnx=DBconnection.connect()
		cur=cnx.cursor()
		query="select * from empDetails_2 order empSalary"
		cur.execute(query)
		tb=cur.fetchall()
		for row in tb:
			emp=Employee()
			emp.setId(int(row[0]))
			emp.setName(row[1])
			emp.setSalary(float(row[2]))
			emp.setAddress(row[3])
			emplist.append(emp)
		cur.close()
		cnx.close()
		return emplist
	
	@staticmethod
	def alphaName():
		emplist=[]
		cnx=DBconnection.connect()
		cur=cnx.cursor()
		query="select * from empDetails_2 order empName"
		cur.execute(query)
		tb=cur.fetchall()
		for row in tb:
			emp=Employee()
			emp.setId(int(row[0]))
			emp.setName(row[1])
			emp.setSalary(float(row[2]))
			emp.setAddress(row[3])
			emplist.append(emp)
		cur.close()
		cnx.close()
		return emplist
					

		
		