##ALL IMPORT STATEMENTS##
from datetime import datetime as t
import mysql.connector as sql
connect = sql.Connect(
    host='localhost',
    user='root',
    password='q1w2e3r4t5y6u7@',
    database='medical_store_record')
if connect.is_connected:
    print("successfully connected")
cursor = connect.cursor()
a = t.now()
## EXIT FUCNTION##


def exit():
    print("              THANK YOU                  ")
    print(a)
## LOGIN MENU##


def menu1():
    print(" YOUR WELLWISHER MEDICAL STORE ")
    print(a)
    print("1. Login")
    print("2. Exit")
    select = int(input("Enter your choice"))
    if select == 1:
        login()
    elif select == 2:
        exit()
    else:
        print("Invalid value")
    menu1()
## LOGIN FUNCTION##


def login():
    print(a)
    user = input('User Name(Enter in Upper Case) : ')
    user = user.upper()
    cursor.execute("select * from account_details where User_Name like '%user%' ")
    datas = cursor.fetchall()
    user_Name = {'Anmol'}
    password = ()
    if user_Name == True:
        password = input('Password : ')
        password = Password.upper()
        if password == password:
            print()
            print('Login successfull')
            print()
    mainmenu()
##MAINMENU##


def mainmenu():
    print(a)
    print("1. Customer Account")
    print("2. Medicine Management")
    print("3.Customer Bill")
    print("4.Exit")
    select = int(input("Enter your choice"))
    if select == 1:
        customer_account()
    elif select == 2:
        medicine_management()
    elif select == 3:
        customer_bill()
    elif select == 4:
        menu1()
    else:
        print("Invalid Choice. Enter 1-4")
## CUSTOMER ACCOUNT##


def customer_account():
    print(a)
    print("1.New Account")
    print("2.Existing Account")
    print("3.Exit")
    select = int(input("Enter your choice"))
    if select == 1:
        new_account()
    elif select == 2:
        existing_account()
    elif select == 3:
        mainmenu()
## CREATE CUSTOMER NEW ACCOUNT##


def new_account():
    print(a)
    account_number = int(input("enter your acct_number:"))
    patient_name = input("enter your name:")
    age = int(input("enter your age:"))
    address = input("enter your address:")
    phone_number = int(input("enter your number:"))
    balance_amount = float(input("enter your amount:"))
    x = "insert into customers_details values(" + str(
    account_number) + ",'" + patient_name + "'," + str(age) + ",'" + address + "'," + str(
    phone_number) + "," + str(balance_amount) + ")"
    print(x)
    cursor.execute(x)
    connect.commit()
    print("Account created successfully")
    customer_account()
## CHECK EXISTING ACCOUNT IF NOT CREATE NEW ACCOUNT##


def existing_account():
    print(a)
    phone_number= input("Enter your phone_number")
    cursor.execute(" select * from customers_details where phone_number like '%phone%' ")
    data1 = cursor.fetchall()
    if phone_number == True:
        print("Your Account Exists")
    else:
        print("Create New Account")
    new_account()
## MEDICINE DETAILS##


def medicine_management():
    print(a)
    print("1.Add new medicines")
    print("2.Check in stock medicines")
    print("3.exit")
    select = int(input("Enter your choice"))
    if select == 1:
        new_medicines()
    elif select == 2:
        stock_medicine()
    elif select == 3:
        mainmenu()
    else:
        print("Inavlid Input")
        medicine_management()
## ADD NEW MEDICINES IN STOCK##


def new_medicines():
    print(a)
    add_new_medicine = int(input("Enter number of new medicines to add"))
    for d in range(add_new_medicine):
        medicine_name = input("Enter name of medicine")
        medicine_code = int(input("Enter code of medicine"))
        cgst = float(input("Enter cgst of medicine"))
        sgst = float(input("Enter sgst of medicine"))
        quantity = int(input("Enter quantity of medicine"))
        cost_per_each = float(input("Enter per cost per each medicine"))
        E = "insert into medicine_details value('{}',{},{},{},{},{})".format(medicine_name,
                                                    medicine_code, cgst, sgst, quantity, cost_per_each)
        cursor.execute(E)
        connect.commit()
        print("Medicines Added in Stock")
        medicine_management()
## CHECK MEDICINES IN STOCK##
def stock_medicine():
    print(a)
    medicine_code = int(input("Enter medcine code"))
    cursor.execute(" select * from medicine_details where medicine_code like '%code%' ")
    data1 = cursor.fetchall()
    if medicine_code == True:
        print("In Stock")
    else:
        print("Out of Stock")
    medicine_management()
## BILL GENERATION##
def customer_bill():
    print(a)
    patient_name = input("enter the patient_name :")
    no = int(input('enter the number of medicine:'))
    print('customer name:', patient_name)
    for i in range(no):
        medicine_name = input('enter medicine name : ')
        cursor.execute("select medicine_code,cgst,sgst,cost_per_each from medicine_details"
                       " where medicine_name like '%medicine%' ")
        data = cursor.fetchall()
        for row in data:
            print('medicine_code of', medicine_name, ':', row[0])
            print('cgst of', medicine_name, ':', row[1])
            print('sgst of', medicine_name, ':', row[2])
            print('cost_per_item of', medicine_name, ':', row[3])
            connect.commit()
            account_number = input('enter account_number:')
            cursor.execute("select balance_amount from customers_details where account_number like '%account%' ")
            datas = cursor.fetchall()
            datas = list(datas[0])
            datas = datas[0]
            print(datas)
            connect.commit()
            print("rows affected:", cursor.rowcount)
            connect.commit()
            quantity = int(input("enter the quantity:"))
            total_amount = row[3] * quantity
            print("total_amount of", medicine_name, ':', total_amount)
            v_sql_insert = "insert into Patient_bill (medicine_name," \
                            "medicine_code,cgst," \
                            "sgst," \
                            "cost_per_each," \
                            "quantity,discount_on_balance_amount," \
                            "total_amount)values('{}',{},{},{},{},{},{},{})".format(
                        medicine_name, row[0], row[1], row[2], row[3], quantity, datas, total_amount)
            print(v_sql_insert)
            cursor.execute(v_sql_insert)
            connect.commit()
            print("Bill Generated")
            mainmenu()
## CREATING TABLES IN DATABASE##


cursor.execute('create table if not exists account_details('
                'User_Name varchar(30) primary key,'
                'password varchar(30) unique)')
print(a)
print("1.New user(signup)")
print("2.Exisiting User(signin)")
Action = int(input("Enter your Action"))
## ADDING NEW USER##
if Action == 1:
    add_user = int(input("Enter the number of new users to Add "))
    for b in range(add_user):
        User_Name = str(input("Enter your preffered User Name"))
        Password = str(input("Enter your password"))
        A = "insert into account_details values('{}','{}')".format(User_Name, Password)
        cursor.execute(A)
        connect.commit()
        print("Users Added Successfully")
else:
    print("WELCOME USER")
##CUSTOMER DETAILS TABLES##
cursor.execute('create table if not exists customers_details('
                'account_number int primary key,'
                'patient_name varchar(30),'
                'age int,address varchar(50),'
                'phone_number bigint(11),balance_amount float)')
##MEDICINE DETAILS TABLE##
cursor.execute('create table if not exists medicine_details('
               'medicine_name varchar(30),'
               'medicine_code int,'
               'cgst float,sgst float,'
               'total_quantity float,'
               'cost_per_each float)')
## PATIENT BILL TABLE##
cursor.execute('create table if not exists Patient_bill('
               'medicine_name varchar(30),'
               'medicine_code int ,cgst float,'
               'sgst float,cost_per_item float,'
               'quantity int,'
               'discount_on_balance_amount float,'
               'total_amount float)')
print('table created')
print(a)
menu1()
