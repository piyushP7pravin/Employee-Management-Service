import mysql.connector
class DBconnection:
	ht="127.0.0.1"
	pt="3306"
	un="root"
	pd=""
	db="ems_services_gui"
	@staticmethod
	def connect():
		return mysql.connector.connect(host=DBconnection.ht,port=DBconnection.pt,username=DBconnection.un,passwd=DBconnection.pd,database=DBconnection.db)