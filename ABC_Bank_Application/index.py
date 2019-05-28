"""
    Documentation -->

    This application is for ABC Bank. It performs all the necessary functions
    which an ideal Bank application can perform.

"""

import os 
import time
import getpass
from auth import login
import trans

def entry():
    os.system('cls')
    print(time.ctime())
    print("\n\n\n\t\t\t\t\tWELCOME TO ABC BANK APPLICATION")
    print("\n\n\t\t\tPress the desired number:")
    print("\n\t\t\t1. Login\n\n\t\t\t2. SignUp\n\n\t\t\t3. Credit\n\n\t\t\t4. Debit\n\n\t\t\t5. Exit\n\n")

    choice = int(input("\t\tEnter your choice: "))
    if(choice == 1):
        acc_no = input("\n\t\tEnter your Account Number: ")
        login(acc_no)
        input("Press any key to exit")
        entry()
    if(choice == 2):
        os.system('cls')
        name = input("\n\t\tEnter your name: ")
        bal = int(input("\n\t\tEnter your balance: "))
        passwd = getpass.getpass("\n\t\tEnter your password:")
        auth.signup(name,passwd,bal)
        input("\t\t\tPress Any key to exit")
        entry()
    if(choice == 3):
        name = input("\n\t\tEnter your name: ")
        acc_no = (input("\n\t\tEnter Account number: "))
        amt = int(input ("\n\t\tEnter Amount you want to transfer: "))
        trans.credit(acc_no,amt)
        print("Redirecting to Log in Menu...")
        time.sleep(4)
        entry()
    if(choice == 4):
        acc_no = input("\n\t\tEnter your account number:")
        trans.debit(acc_no)
    if(choice == 5):

        print("\n\t\t\t\t\t\t\t\tExiting...")
        time.sleep(3)
        exit()
    else:
        print("\t\t\t\tERROR:Invalid choice. \n\n\t\t\t\tPlease Enter a valid choice")
        time.sleep(5)
        entry()



entry()
