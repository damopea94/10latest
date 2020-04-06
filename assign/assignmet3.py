import mysql.connector
def getCountries():
	connection=mysql.connector.connect("localhost","root","python3020","world")#established connection between your database
	cursor=connection.cursor()#cursor() method create a cursor object
	try:
		cursor.execute("select * from country")#Execute SQL Query to select all record
		result=cursor.fetchall() #fetches all the rows in a result set
		for i in result:
			print(i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4])
	except:
		print('Error:Unable to fetch data.')
	connection.close()#Connection Close

def getCountry(choice):
	connection=mysql.connector.connect(host="localhost",user="root",password="",database="world")#established connection between your database
	cursor=connection.cursor()#cursor() method create a cursor object
	try:
		cursor.execute("select * from country where name=%s",(choice,))#Execute SQL Query to select all record
		result=cursor.fetchall() #fetches all the rows in a result set
		for i in result:
			print(i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4])
	except:
		print('Error:Unable to fetch data.')
	connection.close()#Connection Close
print("1:all countries")
print("2: country by name")
choice=int(input("Enter your chance"))
if choice==1:
	getCountries()
elif choice==2:
	choice=input("enter country name to search:")
	getCountry(choice)
else:
	print("invalid choice")
