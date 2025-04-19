from certificate_gui import generate_certificate as g_certificate
from random_date import GenerateDate as g_date
from random_date import ZeroAdder
import datetime as dt
import mysql.connector as conn

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
if 'recipient_data' not in tables:
    mycursor.execute("create table recipient_data (id int(8) auto_increment primary key, login_name varchar(50), login_age int(3), login_password varchar(8))")

while True:
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
        print(f"User ID created successfully, your id is {generated_user_id} and your password is {user_password}")
        print("\n\nRemember your id and password to login in future!")
        break
    elif option == 2:
        user_login_id = int(input("Enter User ID: "))
        user_login_password = input("Enter Password(upto 8 digits only): ")
        mycursor.execute(f"select id, login_password from recipient_data")
        all_user_data = mycursor.fetchall()
        all_user_ids = []
        all_user_password = []
        for i in all_user_data:
            all_user_ids.append(i[0])
            all_user_password.append(i[1])
        if user_login_id in all_user_ids:
            value = 0
            for i in all_user_data:
                if (i[0] == user_login_id):
                    if (i[1] == user_login_password):
                        print("Logged In successfully!")
                        value = 1
                        break
                    else:
                        print("User Id and password doesn't match! Please try again")
                        break
            if (value == 1):
                break
            mycursor.execute(f"select id from recipient_data where login_password = '{user_login_password}'")
            user_set_id = mycursor.fetchone()
            if user_login_id == user_set_id:
                print("\n\nLogged in successfully!")
                break
            else:
                print("\nYour user id and password does'nt match please try again!\n")
        elif user_login_id not in all_user_ids and user_login_password in all_user_password:
            print("\nYou have entered incorrect id, please try again!\n")
        elif user_login_id in all_user_ids and user_login_password not in all_user_password:
            print("\nYou have entered incorrect password, please try again!\n")
        else:
            print("\nYou have entered incorrect id and password, please try again!\n")
        
# Functions
def Reverse(str_name, separator):
    list_name = str_name.split(separator)
    list_name = list_name[::-1]
    str_name = separator.join(list_name)
    return str_name

# format = "dd-mm-yyyy" for both date1 and date2
def DateCompare(date1, date2):
    date_list1 = str(date1).split('-')
    date_list2 = str(date2).split('-')
    if date_list1[2] > date_list2[2] or (date_list1[2] == date_list2[2] and date_list1[1] > date_list2[1]) or (date_list1[2] == date_list2[2] and date_list1[1] == date_list2[1] and date_list1[0] > date_list2[0]):
        return 1
    elif date_list1[2] < date_list2[2] or (date_list1[2] == date_list2[2] and date_list1[1] < date_list2[1]) or (date_list1[2] == date_list2[2] and date_list1[1] == date_list2[1] and date_list1[0] < date_list2[0]):
        return 2
    else:
        return 0

def RegisterVaccine(data, disease_number):
    data_definition = ['name', 'father name', 'mother name', 'age', 'gender', 'date of birth', 'address', 'pincode', 'date of vaccination', 'disease', 'vaccine status']
    vaccine_dict = {
        1: "covaxin",
        2: "covishield",
        3: "pfizer",
        4: "moderna",
        5: "sputnik v",
    }
    dose = 0
    if data[8] == 1:
        dose = int(input("Enter for which dose you are about to get vaccinated(1 to 3): "))
    elif data[8] == 2:
        dose = int(input("Enter for which dose you are about to get vaccinated(1 to 4): "))
    disease = disease_dict[data[8]].title()
    data[8] = disease
    if dose == 1 and disease_number in [1, 2]:
        if disease_number == 1:
            vaccine = int(input("Which vaccine you would like to get injected (number corresponding to the vaccine) ?\n1.Covaxin\n2.Covishield\n3.Pfizer\n4.Moderna\n5.Sputnik V\nEnter your Choice: "))
            vaccine = vaccine_dict[vaccine].title()
            total_dose = 3
        elif disease_number == 2:
            vaccine = 'OPV'
            total_dose = 4

        mycursor.execute(f"insert into recipient_vaccine_data (name, father_name, mother_name, age, gender, date_of_birth, address, pincode, disease, date_of_vaccination, vaccine, dose_injected, total_dose, vaccine_status) values ('{data[0]}', '{data[1]}', '{data[2]}', {data[3]}, '{data[4]}', '{data[5]}', '{data[6]}', {data[7]}, '{data[8]}', '{data[9]}', '{vaccine}', {dose}, {total_dose}, '{data[10]}')")
        mydb.commit()
        mycursor.execute(f"select id from recipient_vaccine_data")
        recipient_id = mycursor.fetchall()[-1][0]
        print(f"Your date of vaccination is registered on {Reverse(data[9], '-')}, your recipient id is {recipient_id} and please do update your vaccine status once you are vaccinated by choosing '4.Update your vaccination status'.")
    elif (dose == 2 or dose == 3 and disease_number in [1, 2]) or (dose == 4 and disease_number == 2):
        recipient_id = int(input("Enter your previous dose id: "))
        mycursor.execute(f"select * from recipient_vaccine_data where id = {recipient_id}")
        previous_detail = list(mycursor.fetchone())
        previous_detail[6] = str(previous_detail[6])
        vaccine = previous_detail[-4]
        total_dose = 3
        for i in range(9):
            if data[i] == previous_detail[i+1] and previous_detail[-1] == 'yes':
                return_number = 1
            elif data[i] == previous_detail[i+1] and previous_detail[-1] == 'no':
                return_number = 2
            elif data[i] != previous_detail[i+1]:
                return_number = 3

        if return_number == 1:
            mycursor.execute(f"insert into recipient_vaccine_data(name, father_name, mother_name, age, gender, date_of_birth, address, pincode, disease, date_of_vaccination, vaccine, dose_injected, total_dose, vaccine_status) values ('{data[0]}', '{data[1]}', '{data[2]}', {data[3]}, '{data[4]}', '{data[5]}', '{data[6]}', {data[7]}, '{data[8]}', '{data[9]}', '{vaccine}', {dose}, {total_dose}, '{data[10]}')")
            mydb.commit()
            mycursor.execute(f"select id from recipient_vaccine_data")
            recipient_id = mycursor.fetchall()[-1][0]
            print(f"Your date of vaccination is registered on {Reverse(data[9], '-')}, your recipient id for this dose is {recipient_id} and please do update your vaccine status once you are vaccinated by choosing '4.Update your vaccination status'.")
        elif return_number == 2:
            print(f"Please first get vaccinated and update your vaccine status for {dose - 1} dose by choosing option '4.Update your vaccination status'.")
        elif return_number == 3:
            print(f"Your {data_definition[i]} ({data[i]}) doesn't match with your previous {data_definition[i]} ({previous_detail[i+1]})")
            print("Please Try Again!!")
    elif disease_number in [3, 4, 5]:
        vaccine = '-'
        dose = 0
        total_dose = 0
        mycursor.execute(f"insert into recipient_vaccine_data (name, father_name, mother_name, age, gender, date_of_birth, address, pincode, disease, date_of_vaccination, vaccine, dose_injected, total_dose, vaccine_status) values ('{data[0]}', '{data[1]}', '{data[2]}', {data[3]}, '{data[4]}', '{data[5]}', '{data[6]}', {data[7]}, '{data[8]}', '{data[9]}', '{vaccine}', {dose}, {total_dose}, '{data[10]}')")
        mydb.commit()
        mycursor.execute(f"select id from recipient_vaccine_data")
        recipient_id = mycursor.fetchall()[-1][0]
        print(f"Your date of vaccination is registered on {Reverse(data[9], '-')}, your recipient id is {recipient_id} and please do update your vaccine status once you are vaccinated by choosing '4.Update your vaccination status'.")
    
    else:
        print("You have entered incorrect data, please try again.")

disease_dict = {
    1: "Covid",
    2: "Polio",
    3: "tetanus",
    4: 'typhoid',
    5: 'chicken pox'
}

print("\n\n\n**********YOU HAVE SUCCESSFULLY LOGGED IN**********")
print("**********GET YOURSELF VACCINATED AND BE DISEASE FREE**********\n\n\n")


#     # EXTRA CODE
mycursor.execute(f"insert into recipient_vaccine_data (name, father_name, mother_name, age, gender, date_of_birth, address, pincode, disease, date_of_vaccination, vaccine, dose_injected, total_dose, vaccine_status) values ('Ajay Sharma', 'Suresh Sharma', 'Rohini Sharma', 21, 'Male', '2001-05-14', 'C-12, Anand Vihar, New Delhi', 110001, 'Covid', '2022-10-05', 'Pfizer', 1, 3, 'yes')")
mydb.commit()
mycursor.execute(f"insert into recipient_vaccine_data (name, father_name, mother_name, age, gender, date_of_birth, address, pincode, disease, date_of_vaccination, vaccine, dose_injected, total_dose, vaccine_status) values ('Rahul Raj', 'Murli Raj', 'Meena Raj', 56, 'Male', '1966-08-05', 'A-12, Ambe Residency, New Delhi', 110005, 'Covid', '2022-06-14', 'Moderna', 1, 3, 'yes')")
mydb.commit()
mycursor.execute(f"insert into recipient_vaccine_data (name, father_name, mother_name, age, gender, date_of_birth, address, pincode, disease, date_of_vaccination, vaccine, dose_injected, total_dose, vaccine_status) values ('Ajay Sharma', 'Suresh Sharma', 'Rohini Sharma', 21, 'Male', '2001-05-14', 'C-12, Anand Vihar, New Delhi', 110001, 'Covid', '2022-03-01', 'Pfizer', 2, 3, 'yes')")
mydb.commit()
mycursor.execute(f"insert into recipient_vaccine_data (name, father_name, mother_name, age, gender, date_of_birth, address, pincode, disease, date_of_vaccination, vaccine, dose_injected, total_dose, vaccine_status) values ('Rohit Kumar', 'Vinay Kumar', 'Laxmi Kumar', 18, 'Male', '2004-03-25', 'F-302, Sharda Society, New Delhi', 110008, 'Tetanus', '2022-04-23', '-', 0, 0, 'yes')")
mydb.commit()

while True:
    choice = int(input("Select one option:\n1.Register for vaccine\n2.See your status\n3.Get vaccine certificate\n4.Update your vaccination status\n5.Exit\nEnter your choice: "))
    print("")
    if choice == 1:
        name = input("Enter recipient's full name: ").title()
        f_name = input("Enter recipient's Father's name: ").title()
        m_name = input("Enter recipient's Mother's name: ").title()
        age = int(input("Enter recipient's age: "))
        gender = input("Enter recipient's gender: ").title()
        dob = input("Enter recipient's date of birth(dd-mm-yyyy): ")
        dob = Reverse(dob, '-')
        address = input("Enter recipient's address: ").title()
        pincode = input("Enter recipient's pincode: ")
        dov = Reverse(g_date(), '-')
        disease = int(input("Enter against the disease your vaccination is(number corresponding to the disease):\n1.Covid\n2.Polio\n3.Tetanus\n4.Typhoid\n5.Chicken Pox\n"))
        vaccine_status = 'no'
        recipient_data = [name, f_name, m_name, age, gender, dob, address, pincode, disease, dov, vaccine_status]
        if disease in [1, 2, 3, 4, 5]:
            RegisterVaccine(recipient_data, disease)
        else:
            print("You entered incorrect value, please try again.")

    elif choice == 2:
        user_id = int(input("Enter your vaccination id: "))
        mycursor.execute(f'select * from recipient_vaccine_data where id = {user_id}')
        user_tup = list(mycursor.fetchone())
        current_date = ''
        user_tup[-5] = Reverse(user_tup[-5], '-')
        if current_date < user_tup[-5]:
            print(f"The recipient, {user_tup[1]} has registered against the disease {user_tup[-6]}, your date of vaccination is {user_tup[-5]}.")
        elif current_date > user_tup[-5] and user_tup[-1] == 'no':
            print(f"The recipient, {user_tup[1]} had registered against the disease {user_tup[-6]} and your date of vaccination was {user_tup[-5]} but you did'nt get vaccinated.")
        elif current_date > user_tup[-5] and user_tup[-1] == 'yes':
            print(f"The recipient, {user_tup[1]} had registered against the disease {user_tup[-6]} and you are vaccinated on {user_tup[-5]}.")

    elif choice == 3:
        user_id = int(input("Enter your recipient id: "))
        mycursor.execute(f"select id from recipient_vaccine_data")
        ids = mycursor.fetchall()
        vaccine_ids = []
        for i in ids:
            vaccine_ids.append(i[0])
        if user_id in vaccine_ids:
            mycursor.execute(f"select vaccine_status from recipient_vaccine_data where id = {user_id}")
            user_status = mycursor.fetchone()[0]
            if user_status == 'yes':
                mycursor.execute(f"select * from recipient_vaccine_data where id = {user_id}")
                user_data = list(mycursor.fetchone())
                if user_data[-3] == 0:
                    user_data[-3] = '-'
                recipient_details = [user_data[1], user_data[2], user_data[3], user_data[4], user_data[5], user_data[0]]
                vaccine_details = [user_data[-6], user_data[-4], Reverse(user_data[-5], '-'), user_data[-3]]
                g_certificate(recipient_details, vaccine_details)
            else:
                print("You have not updated your vaccine status to yes once you are vaccinated do update it and then by entering 3 you can get your vacination certificate.")
        else:
            print("You have entered incorrect id, please try again.")

    elif choice == 4:
        user_id = int(input("Enter your recipient id: "))
        mycursor.execute(f"select vaccine_status from recipient_vaccine_data where id = {user_id}")
        status = mycursor.fetchone()[0]
        current_date = dt.datetime.now()
        current_date = str(current_date.date())
        mycursor.execute(f"select date_of_vaccination from recipient_vaccine_data where id = {user_id}")
        user_dov = mycursor.fetchone()[0]
        mycursor.execute('select * from recipient_vaccine_data')
        all_data = mycursor.fetchall()
        recipient_ids = []
        for i in all_data:
            recipient_ids.append(i[0])
        if DateCompare(current_date, user_dov) == 1:
            if user_id in recipient_ids and status == 'no':
                for i in all_data:
                    if i[0] == user_id:
                        active_recipient_id = list(i)
                active_recipient_id[6] = str(active_recipient_id[6])
                active_recipient_id[9] = str(active_recipient_id[9])
                mycursor.execute(f"UPDATE recipient_vaccine_data SET vaccine_status = 'yes' WHERE id = {user_id}")
                mydb.commit()
                print("\nThank you for getting vaccinated, your data has been successfully saved. Please enter 3 for your vaccination certificate.\n")
            elif user_id in recipient_ids and status == 'yes':
                print("\nYou have already updated for your vaccination and you can get your vaccine certificate by entering 3.\n")
        elif DateCompare(current_date, user_dov) == 2:
            # print(current_date, user_dov)
            print(f"Sorry your date of vaccination is {Reverse(user_dov, '-')}, you can update your vaccine status to yes once you are vaccinated.")

    elif choice == 5:
        print("Thank you, Visit again.")
        break

    else:
        print("You entered incorrect value, please try again.\n")