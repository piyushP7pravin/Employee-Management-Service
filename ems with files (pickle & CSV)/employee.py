class Employee:
	def __init__(self,id=None,name=None,salary=None,address=None):
		self.__id=id
		self.__name=name
		self.__salary=salary
		self.__address=address
	def __str__(self):
		return (str(self.__id)+" "+str(self.__name)+" "+str(self.__salary)+" "+str(self.__address))
	def getId(self):
		return self.__id
	def getName(self):
		return self.__name
	def getSalary(self):
		return self.__salary
	def getAddress(self):
		return self.__address
	def setId(self,id):
		self.__id=id
	def setName(self,name):
		self.__name=name
	def setSalary(self,salary):
		self.__salary=salary
	def setAddress(self,address):
		self.__address=address
	def getList(self):
		lst=[]
		lst.append(str(self.__id))
		lst.append(self.__name)
		lst.append(str(self.__salary))
		lst.append(self.__address)	
		return lst
	@staticmethod
	def emp(str):
		lst=str.split(" ")
		return Employee(int(lst[0]),lst[1],float(lst[2]),lst[3])