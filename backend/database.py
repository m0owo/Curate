import ZODB, ZODB.FileStorage
import BTrees._OOBTree
import persistent
import transaction

class Account(persistent.Persistent):
    def __init__(self, gmail, password):
        self.gmail = gmail
        self.password = password
        self.username = ""

    def get_email(self):
        return self.gmail
    
    def get_password(self):
        return self.password

class Admin(Account):
    def __init__(self, gmail, password):
        super().__init__(gmail, password)

storage = ZODB.FileStorage.FileStorage('mydata.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root
root.admins = BTrees.OOBTree.BTree()
root.admins[1000] = Admin("admin1@gmail.com", "1234")

transaction.commit()

if  __name__ == "__main__":
    admins = root.admins
    for a in admins:
        admin = admins[a]
        print(admin.get_email())