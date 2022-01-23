import sys
import mysql.connector
mydb=mysql.connector.connect(host='localhost',username='root',passwd='AEROPLANEROCKS123',database='sk')
mycursor=mydb.cursor()

print("\n\n*************************************WELCOME TO THE HOSPITAL !!!************************************")

doc=str(input("\n\n\n\n\n\nAre you a staff/doctor of this hospital?(y/n) : "))

if doc=='y':
     passwd=input("\nPlease enter the pin(2 attempts) : ")
     if passwd=='82154':
          dis=input("\nDo you want to\n\n1.See the records\n\nOR\n\n2.Exit? : ")
          if dis=='1':
               sql2="SELECT HOSPITAL.P_no, HOSPITAL.Phone_no, HOSPITAL.Patient_first_name, HOSPITAL.Patient_last_name, doctor.Disease_or_injury from HOSPITAL right join doctor on HOSPITAL.P_no=doctor.P_no"
               mycursor.execute(sql2)
               myres=mycursor.fetchall()
               print("\n\n-------------------------------------------------------------------------------------------------------")
               print("P_no\t""\tPhone_no""\tPatient_first_name""\tPatient_last_name""\t\tDisease_or_Injury")
               for x in myres:
                    print("-------------------------------------------------------------------------------------------------------")
                    print(x[0],"\t\t",x[1],"   \t ",x[2],"\t\t\t",x[3],"\t\t\t",x[4])
               print("\nThere are",50-mycursor.rowcount,"beds available")
               sys.exit()
          elif dis=='2':
               sys.exit()
          else:
               print("Please input only 1 or 2!")
               sys.exit()
     else:
          passwd1=input("\nPlease enter the pin(last attempt) : ")
          if passwd1=='82154':
               dis=input("\nDo you want to\n\n1.See the records\n\nOR\n\n2.Exit? ")
               if dis=='1':
                    sql2="SELECT HOSPITAL.P_no, HOSPITAL.Phone_no, HOSPITAL.Patient_first_name, HOSPITAL.Patient_last_name, doctor.Disease_or_injury from HOSPITAL right join doctor on HOSPITAL.P_no=doctor.P_no"
                    mycursor.execute(sql2)
                    myres=mycursor.fetchall()
                    print("\n\n-------------------------------------------------------------------------------------------------------")
                    print("P_no\t""\t\Phone_no""\tPatient_first_name""\tPatient_last_name""\t\tDisease_or_Injury")
                    for x in myres:
                         print("-------------------------------------------------------------------------------------------------------")
                         print(x[0],"\t\t",x[1],"   \t ",x[2],"\t\t\t",x[3],"\t\t\t",x[4])
                    print("\nThere are",50-mycursor.rowcount,"beds available")
                    sys.exit()
               elif dis=='2':
                    sys.exit()
          else:
               print("\nSorry you have exceeded the number of tries!!")
               sys.exit()     
elif doc=='n':
     opt=input("\nTo checkout, please press o \n\n OR \n\nTo checkin, please press i : ")
     if opt=='i':
          if mycursor.rowcount>50:
               print("Sorry there are no beds available :(")
               sys.exit()
          print("\nPlease note that there must be no errors while filling in the form as you will have to fill it again if there are any errors.")
          firstname=str(input("\nEnter the patient's first name : "))
          if len(firstname)<2:
               print("\nPlease enter a valid name!")
               print("\nPlease refill the form!")
               sys.exit()
          else:
               if firstname.isalpha()==False:
                    print("\nEnter a name with only alphabets!")
                    print("\nPlease refill the form!")
                    sys.exit()  
          lastname=str(input("\nEnter the patient's last name : "))
          if len(firstname)<2:
               print("\nPlease enter a valid name!")
               print("\nPlease refill the form!")
               sys.exit()
          else:
               if lastname.isalpha()==False:
                    print("\nEnter a name with only alphabets!")
                    print("\nPlease refill the form!")
                    sys.exit()  
          phoneno=input("\nEnter your phone number : ")
          if phoneno.isnumeric()==False:
               print("\nEnter a vaid phone number!")
               sys.exit()
          else:     
               if len(phoneno)<10:
                    print("Please enter a valid phone number!")
                    sys.exit()
               else:     
                    print("\nForm successfully filled!")
                    print("\n\nProceeding to disease/injury input(To be filled only by Doctor)...")
                    pin=str(input("\nEnter pin for authorized entry : "))
                    if pin=='82154':
                         sql="insert into HOSPITAL(Phone_no,Patient_first_name,Patient_last_name) values(%s,%s,%s)"
                         val=(phoneno,firstname,lastname)
                         mycursor.execute(sql,val)
                         mydb.commit()
                         print("\nYou can refer to this data before entering the patient number : ")
                         mycursor.execute("select * from HOSPITAL")
                         myresult = mycursor.fetchall()
                         print("\n--------------------------------------------------------------------------------------------------")
                         print("P_no\t""\tPhone_no""\tPatient_first_name""\tPatient_last_name")
                         for y in myresult:
                              print("--------------------------------------------------------------------------------------------------")
                              print(y[0],"\t\t",y[1],"   \t ",y[2],"\t\t\t",y[3])
                         Patientno=int(input("\nPlease enter the patient number : "))
                         dise=input("\nPlease enter the disease/injury the patient is suffering from : ")
                         sql1="insert into doctor(P_no,Disease_or_Injury) values(%s,%s)"
                         val1=(Patientno,dise)
                         mycursor.execute(sql1,val1)
                         mydb.commit()
                         sql2="SELECT HOSPITAL.P_no, HOSPITAL.Phone_no, HOSPITAL.Patient_first_name, HOSPITAL.Patient_last_name, doctor.Disease_or_injury from HOSPITAL right join doctor on HOSPITAL.P_no=doctor.P_no"
                         mycursor.execute(sql2)
                         myres=mycursor.fetchall()
                         print("\n\n-------------------------------------------------------------------------------------------------------")
                         print("P_no\t""\tPhone_no""\tPatient_first_name""\tPatient_last_name""\t\tDisease_or_Injury")
                         for x in myres:
                              print("-------------------------------------------------------------------------------------------------------")
                              print(x[0],"\t\t",x[1],"   \t ",x[2],"\t\t\t",x[3],"\t\t\t",x[4])
                    else:
                         print("\nOnly authorized personnel are allowed ")
                         sys.exit()
     elif opt=='o':
          name=str(input("\nEnter the name of the patient you want to checkout(please enter the name correctly as this programme is case sensitive) : "))
          diseas=str(input("\nEnter the disease/injury the person was suffering with(please enter the disease/injury correctly as this programme is case sensitive) : "))
          mycursor.execute("select Patient_first_name from HOSPITAL where Patient_first_name=%s",(name,))
          myres1=mycursor.fetchall()
          if not myres1:
               print("\nNo name as ",name,"found!")
               sys.exit()
          else:
               mycursor.execute("select Disease_or_Injury from doctor where Disease_or_Injury=%s",(diseas,))
               myres2=mycursor.fetchall()
               if not myres2:
                    print("\nNo disease as ",diseas," found!")
                    sys.exit()
               else:     
                    val6=(name,)
                    sql6="delete from HOSPITAL where Patient_first_name=%s"
                    mycursor.execute(sql6,val6)
                    mydb.commit()
                    val7=(diseas,)
                    sql7="delete from doctor where Disease_or_Injury=%s"
                    mycursor.execute(sql7,val7)
                    mydb.commit()
                    print("\nCheck out successful!""\n\n\n""Stay home, Stay safe :)")
     else:
          print("Please enter only o or i!")
else:
     print("Please enter input only y or n!")







