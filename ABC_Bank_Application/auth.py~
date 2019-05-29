import time
import shelve
import os
import getpass

def login(acc_no):
    db = shelve.open('database/bank.db')
    if acc_no in db.keys():
        password = getpass.getpass ("\n\t\tEnter your password: ")
        if (password) == db[str(acc_no)]['password']:
            print("\n\n\t\t\tFetching your details...")
            time.sleep(3)
            os.system('cls')
            print(f"\n\n\t\t\t\t\tWelcome {db[acc_no]['name']}")
            name = db[acc_no]['name']
            bal = db[acc_no]['bal']
            print(f"\n\n\t\t\t\tName: {name}\n\n\t\t\t\tCurrent Balance: {bal}")
            db.close()
            return True
        else:
            print("\n\t\t\tError: Invalid password. Try Aagin")
            time.sleep(5)
            #entry()
    else:
        print("\n\t\t\tError: No such Account Exist. \n\t\t\tSign-Up, if you are a new user.")
        time.sleep(5)
        #entry()

def signup (name,password,bal):
    db = shelve.open ('database/bank.db')
    acc_no = db.get('last_acc') + 1
    db [str(acc_no)] = {'name': name,'bal':bal,'password':password}
    db['last_acc'] = acc_no
    print("Uploading your profile...")
    time.sleep(4)
    print("Your account number is ",db['last_acc'])
    db.close()


if __name__=='__main__':
    login('1001')
    signup('john','cena',20000)

