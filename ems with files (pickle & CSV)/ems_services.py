from employee import *
import os
import pandas as pd
import pickle
class Ems_services:
	emplist=[]
	filename="empDetails.pickle"
	filename2="empdetails.csv"
	@classmethod
	def getAllEmployees(cls):
		return cls.emplist
	@classmethod
	def searchById(cls,id):
		for e in cls.emplist:
			if e.getId()==id:
				return e
		return None
	@classmethod
	def addEmployee(cls,emp):
		if cls.searchById(emp.getId())!=None:
			return False
		cls.emplist.append(emp)
		return True
	@classmethod
	def deleteById(cls,id):
		emp=cls.searchById(id)
		if emp==None:
			return False
		else:
			cls.emplist.remove(emp)
			return True
	@classmethod
	def searchByName(cls,name):
		lst=[]
		for e in cls.emplist:
			if e.getName()==name:
				lst.append(e)
		return lst
	@classmethod
	def searchBySalRange(cls,min,max):
		lst=[]
		for e in cls.emplist:
			if e.getSalary()>=min and e.getSalary()<=max:
				lst.append(e)
		return lst
	@classmethod
	def descSalary(cls):
		lst=cls.emplist.copy()
		for i in range(len(lst)):
			for j in range(len(lst)-1):
				if lst[j].getSalary()<lst[j+1].getSalary():
					lst[j],lst[j+1]=lst[j+1],lst[j]
		return lst
	
	@classmethod
	def alphaName(cls):
		l=[]
		m=[]
		for e in cls.emplist:
			lst.append(e.getName())
		l.sort(key=str.lower())
		for i in l:
			for j in cls.emplist:
				if j.getName()==i:
					m.append(j)
		return m
		
	@classmethod
	def loadData(cls):
		if(os.path.exists(cls.filename)):
			f=open(cls.filename,"rb")
			cls.emplist=pickle.load(f)
			f.close()
	@classmethod
	def saveData(cls):
		f=open(cls.filename,"wb")
		pickle.dump(cls.emplist,f)
		f.close()
			
	@classmethod
	def saveCSV(cls):
		data=[]
		for e in cls.emplist:
			data.append(e.getList())
		df=pd.DataFrame(data=data,columns=['EmpId','EmpName','EmpSalary','EmpAddress'])
		df.to_csv(cls.filename2,index=False)
					
		
		
					
			
		