"""
    Documentation -->

    This application is for ABC Bank. It performs all the necessary functions
    which an ideal Bank application can perform.

"""

import os 
import time
import getpass
import auth
import trans

def entry():
    os.system('cls')
    print(time.ctime())
    print("\n\n\n\t\t\t\t\tWELCOME TO ABC BANK APPLICATION")
    print("\n\n\t\t\tPress the desired number:")
    print("\n\t\t\t1. Login\n\n\t\t\t2. SignUp\n\n\t\t\t3. Credit\n\n\t\t\t4. Debit\n\n\t\t\t5. Exit\n\n")

    choice = input("\t\tEnter your choice: ")
    if(choice == '1'):
        acc_no = input("\n\t\tEnter your Account Number: ")
        auth.login(acc_no)
        input("\n\t\t\tPress any key to exit")
        entry()
    if(choice == '2'):
        os.system('cls')
        time.ctime()
        print("\n\t\t\t\t\t\t\t SIGN-UP FORM")
        name = input("\n\n\t\tEnter your name: ")
        try:
            bal = float(input("\n\t\tEnter your balance: "))
        except Exception:
            print("\n\t\t\tERROR: Please enter a valid amount")
        print("\n\t\t\tMoving to Dashboard...")
        time.sleep(5)
        entry()
        passwd = getpass.getpass("\n\t\tEnter your password:")
        auth.signup(name,passwd,bal)
        input("\t\t\tPress Any key to exit")
        entry()
    if(choice == '3'):
        name = input("\n\t\tEnter your name: ")
        acc_no = (input("\n\t\tEnter Account number: "))
        trans.credit(acc_no)
        print("\n\t\t\tRedirecting to Log in Menu...")
        time.sleep(4)
        entry()
    if(choice == '4'):

        acc_no = input("\n\t\tEnter your account number:")
        trans.debit(acc_no)
        entry()
    if(choice == '5'):

        print("\n\t\t\t\t\t\t\t\tExiting...")
        print("\n\n\t\t\t\tThank You for using our services. Have a good day :)")
        time.sleep(3)
        exit()
    else:
        print("\t\t\t\tERROR:Invalid choice. \n\n\t\t\t\tPlease Enter a valid choice")
        time.sleep(5)
        entry()

try:
    entry()
except Exception:
    print("\n\t\t\tRedirecting to Main Menu...")
    time.sleep(3)
    entry()
