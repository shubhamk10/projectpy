import mysql.connector
mydb=mysql.connector.connect(host='localhost',username='root',passwd='AEROPLANEROCKS123',database='sk')
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE HOSPITALji(P_no INT AUTO_INCREMENT PRIMARY KEY, Phone_no BIGINT NOT NULL, Patient_first_name varchar(30) NOT NULL, Patient_last_name varchar(30) NOT NULL)")  
mycursor.execute("CREATE TABLE doctori(P_no INT PRIMARY KEY, Disease_or_Injury varchar(30) NOT NULL)")
print("Tables created!")
