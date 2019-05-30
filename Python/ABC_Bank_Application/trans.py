""" 
    This contains functions required for performing transcations such as debit, credit
    and updating passwords.
"""

import shelve
import time
import auth
#import index

def credit (acc_no):
    db = shelve.open("database/bank.db",writeback = True)
    if str(acc_no) in db.keys():
        try:
            amt = float(input("\n\t\tEnter the amount you want to Transfer: "))
        except Exception:
            print ("\n\t\t\tERROR: Enter a valid number.")
        n = db[acc_no]['bal']
        n = n+amt
        db[acc_no]['bal'] = n
        db.close()
        print("\n\t\t\tPlease wait while we are transferring the Amount.")
        time.sleep(2)
        print(f"\n\t\t\tCredited with Rs. {amt}")
    else:
        print("\t\t\t\tERROR: No such user exists. \n\n\t\t\t\tPlease check the Account Number and Try again")


def debit (acc_no):
    if auth.login(acc_no):
        try:
             amt = int(input("\n\t\t\t\tEnter amount you want to debit: "))
        except Exception:
            print ("\n\t\t\tERROR: Enter a valid Number")
        db = shelve.open("database/bank.db", writeback = True)
        balance = db[acc_no]['bal']
        if amt>balance:
            print("\t\t\t\tERROR: Insufficient amount")
            print("\n\t\t\tRedirecting to Main Menu")
            time.sleep(3)
        else:
            balance = balance -amt
            db[acc_no]['bal'] = balance
            print(f"\n\t\t\t\tAmount of Rs. {amt} is debited from your account")
            print(f"\n\t\t\t\tRemaining balance Rs. {balance}")
            db.close()
            input("Press enter to exit")
            time.sleep(4)
            print("\n\t\t\tRedirecting to main-menu..")

if __name__ == "__main__":
    #credit ('1001',5000)
    debit('1001')
