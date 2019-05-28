""" 
    This contains functions required for performing transcations such as debit, credit
    and updating passwords.
"""

import shelve
import time
import auth
import index

def credit (acc_no,amt):
    db = shelve.open("database/bank.db",writeback = True)
    if str(acc_no) in db.keys():
        n = db[acc_no]['bal']
        n = n+amt
        db[acc_no]['bal'] = n
        db.close()
        print("Please wait while we are transferring the Amount.")
        time.sleep(2)
        print(f"Credited with Rs. {amt}")
    else:
        print("\t\t\t\tERROR: No such user exists. \n\n\t\t\t\tPlease check the Account Number and Try again")


def debit (acc_no):
    if auth.login(acc_no):
        amt = int(input("\n\t\t\t\tEnter amount you want to debit: "))
        db = shelve.open("database/bank.db", writeback = True)
        balance = db[acc_no]['bal']
        if amt>balance:
            print("\t\t\t\tERROR: Insufficient amount")
        else:
            balance = balance -amt
            db[acc_no]['bal'] = balance
            print(f"\n\t\t\t\tAmount of Rs. {amt} is debited from your account")
            print(f"\n\t\t\t\tRemaining balance Rs. {balance}")
            db.close()
            time.sleep(10)
            print("Redirecting to main-menu")
            entry()

if __name__ == "__main__":
    #credit ('1001',5000)
    debit('1001')
