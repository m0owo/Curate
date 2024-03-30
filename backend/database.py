import ZODB, ZODB.FileStorage
import BTrees._OOBTree
import persistent
import transaction
from datetime import datetime
from PySide6.QtWidgets import (
    QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QWidget
)

#topic tags, link is the placeholder for what the button would do
class Tag(persistent.Persistent):
    def __init__(self, tag_text, link):
        self.tag_text = tag_text
        self.link = link #what does the tag do
    def get_tag_text(self):
        return self.tag_text
    def get_link(self):
        return self.link

#product in the post
class Product(persistent.Persistent):
    def __init__(self, pr_name, pr_id, seller, status, start, end, tags):
        self.pr_name = pr_name
        self.pr_id = pr_id
        self.seller = seller
        self.status = status
        self.start = start
        self.end = end
        self.tags = tags
    def get_name(self):
        return self.pr_name
    def get_title(self):
        return self.pr_title
    def get_seller(self):
        return self.seller
    def get_status(self):
        return self.status
    def get_tags(self):
        return self.tags
    
#collection of items in a post, items would be persistent list in real??
class Collection(Product):
    def __init__(self, c_name, c_id, seller, status, start, end, tags, items = {}):
        super.__init__(c_name, c_id, seller, status, start, end, tags)
        self.items = items #Item objects in the collection
    def get_items(self):
        return self.items

#individual items in a post
class Item(Product):
    def __init__(self, i_name, i_id, seller, status, start, end, tags, price, image):
        super.__init__(i_name, i_id, seller, status, start, end, tags)
        self.price = price
        self.image = image
    def get_price(self):
        return self.price
    def get_image(self):
        return self.image #how to store images in a class

#info to display in post
class PostDetails(persistent.Persistent):
    def __init__(self, p_id, p_author, p_info, p_title,
                 p_tags, type = "CF no CC",
                 product = []):
        self.id = p_id
        self.author = p_author
        self.product = product #a single item is a collection size 1
        self.info = p_info
        self.title = p_title
        self.tags = p_tags
        self.created = datetime.now()
        self.modified = self.created
        if len(product) > 1:
            self.p_type = "collection"
        else:
            self.p_type = "item"
        self.type = type
    def get_author(self):
        return self.author
    def get_product(self):
        return self.product
    def get_info(self):
        return self.info
    def get_title(self):
        return self.title
    def get_created(self):
        return self.created
    def get_modified(self):
        return self.modified
    def get_type(self):
        return self.p_type
    def get_tags(self):
        # for p in product:
        #     self.tags.append(p.get_tags())
        return self.tags
        
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

        
    import sys
    print(sys.path)

        
    