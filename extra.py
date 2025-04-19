from certificate_gui import generate_certificate as g_certificate
from random_date import GenerateDate as g_date
from random_date import ZeroAdder
import datetime as dt
import mysql.connector as conn

while True:
    sql_password = input("Enter your sql password: ")
    mydb = conn.connect(host = "localhost",user = "root",password = sql_password)
    mycursor = mydb.cursor()
    mycursor.execute("show databases")
    data = mycursor.fetchall()
    databases = []
    for i in data:
        databases.append(i[0])

    if 'management_of_vaccination' in databases:
        mycursor.execute("use management_of_vaccination")
    elif 'management_of_vaccination' not in databases:
        mycursor.execute("create database management_of_vaccination")
        mycursor.execute("use management_of_vaccination")

    mycursor.execute("show tables")
    data_tables = mycursor.fetchall()
    tables = []
    for i in data_tables:
        tables.append(i[0])
    if 'recipient_vaccine_data' not in tables:
        mycursor.execute("create table recipient_vaccine_data (id int(8) auto_increment primary key, name varchar(50), father_name varchar(50), mother_name varchar(50), age int(3), gender varchar(10), date_of_birth date, address varchar(150), pincode varchar(6), disease varchar(50), date_of_vaccination varchar(50), vaccine varchar(50), dose_injected int(1), total_dose int(1), vaccine_status varchar(20))")
    mydb.commit()
    if 'recipient_data' not in tables:
        mycursor.execute("create table recipient_data (id int(8) auto_increment primary key, login_name varchar(50), login_age int(3), login_password varchar(8))")
    print("1.Create new user id\n2.Have an account? Enter user id")
    option = int(input("Enter your choice: "))
    if option == 1:
        user_name = input("Enter user name: ")
        user_age = int(input("Enter your Age: "))
        user_password = input("Set your Password(upto 8 digits only): ")
        mycursor.execute(f"insert into recipient_data (login_name, login_age, login_password) values ('{user_name}', {user_age}, '{user_password}')")
        mydb.commit()
        mycursor.execute("select id from recipient_data")
        logged_ids = mycursor.fetchall()
        generated_user_id = logged_ids[-1][0]
        print(f"User ID created successfully, your id is {generated_user_id}")
        print("Remember your id and password to login in future!")
        break
    elif option == 2:
        user_login_id = int(input("Enter User ID: "))
        user_login_password = input("Enter Password(upto 8 digits only): ")
        mycursor.execute(f"select id from recipient_data where login_password = '{user_login_password}'")
        user_set_id = mycursor.fetchone()[0]
        if user_login_id in user_set_id:
            print("Logged in successfully!")
            break
        else:
            print("Your user id and password does'nt match please try again")
        


# while True:
#     print("1.Create user id\n2.Enter user id")
#     choice2 = int(input("Enter your choice: "))
#     if choice2 == 1:
#         user_name = input("Enter new User ID: ")
#         user_age = int(input("Enter your Age: "))
#         user_password = input("Set your Password: ")
#         user_data_dict[user_name] = [user_age,user_password]
#         print("User ID created successfully")
#     elif choice2 == 2:
#         user_login_name = input("Enter User ID: ")
#         if user_login_name in user_data_dict:
#             user_login_password = input("Enter Password: ")
#             if user_login_password == user_data_dict[user_login_name][1]:
#                 print("Logged in successfully")
#                 user_login_age = user_data_dict[user_login_name][0]
#                 mycursor.execute(f"insert into recipient_data values ('{user_login_name}',{user_login_age})")
#                 mydb.commit()
#             else:
#                 print("Wrong password")
#         else:
#             print("User ID does not exist.\nSelect 1 to create a new user Id")
#     else:
#         print("Wrong Choice")
    
#     print("Press S to stay")
#     ch = input("Enter your choice: ")
#     if ch.upper() != "S":
#         break
        