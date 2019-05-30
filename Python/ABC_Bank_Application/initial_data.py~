user1 = {
         'name':'nidhi',
         'bal': 4000,
         'password': 'joshi'
        }
user2 = {
         'name': 'ram',
         'bal': 60000,
         'password': 'heyram'
        }
user3 = {
         'name':'shyam',
         'bal':30000,
         'password': 'sunder'
        }

import shelve
db = shelve.open("database/bank.db",writeback = True) 
db['1001'] = user1
db['1002'] = user2
db['1003'] = user3

db['last_acc']=1003
db.close()


print("Exported Successfully")

