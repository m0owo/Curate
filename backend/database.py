import ZODB, ZODB.FileStorage
import BTrees._OOBTree
import persistent
import transaction
from datetime import datetime
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QWidget)

#product in the post
class Product():
    def __init__(self, p_name, p_title, seller, start_date, end_date, status):
        self.p_name = p_name
        self.p_title = p_title
        self.seller = seller
        self.start_date = start_date
        self.end_date = end_date
        self.status = status

#collection of items in a post
class Collection(Product):
    def __init__(self, c_name, c_title, seller, start_date, end_date, status, items = persistent.PersistentList()):
        super.__init__(c_name, c_title, seller, start_date, end_date, status)
        self.items = items

#individual items in a post
class Item(Product):
    def __init__(self, i_name, i_title, seller, start_date, end_date, status, price):
        super.__init__(i_name, i_title, seller, start_date, end_date, status)
        self.price = price

class Tag():
    def __init__(self, tag_text, container):
        self.tag_text = tag_text
        self.container = container
        self.tagbutton = QPushButton(self.container)

        self.tagbutton.setText(self.tag_text)
        self.tagbutton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

class Post():
    def __init__(self, seller, product):
        self.seller = seller
        self.created = datetime.now().date()
        self.modified = None
        self.product = product

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
