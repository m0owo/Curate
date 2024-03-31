import ZODB, ZODB.FileStorage
import BTrees._OOBTree
import persistent
import transaction
from datetime import datetime
# from PySide6.QtWidgets import (
#     QAbstractScrollArea, QApplication, QFrame, QGridLayout,
#     QLabel, QLineEdit, QMainWindow, QPushButton,
#     QScrollArea, QSizePolicy, QWidget
# )

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
    def __init__(self, pr_name, pr_id, seller, status, start, tags, end = None):
        self.pr_name = pr_name
        self.pr_id = pr_id
        self.seller = seller
        self.status = status #upcoming, live, sold
        self.start_date = start #time to go live
        self.end_date = end #Date object for time sold
        self.tags = tags #list of Tag objects
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
    def get_start_date(self):
        return self.start_date
    def get_end_date(self):
        if self.end_date:
            return self.end_date
        else:
            raise ValueError("Product hasn't ended")
    
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
            self.pr_type = "collection"
        else:
            self.pr_type = "item"
        self.sales_type = type
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
    def get_product_type(self):
        return self.pr_type
    def get_tags(self):
        # for p in product:
        #     self.tags.append(p.get_tags())
        return self.tags
    def get_sales_type(self):
        return self.sales_type
        
class Account(persistent.Persistent):
    def __init__(self,id, gmail, username, password):
        self.id = id
        self.gmail = gmail
        self.password = password
        self.username = username
        self.address = "Samutprakan ja"
        self.follower = 0
        self.following = 0

    def get_email(self):
        return self.gmail
    
    def get_password(self):
        return self.password
    
    def serialize(self):
        return {
            'gmail': self.gmail,
            'username': self.username,
            'address': self.address,
            'follower': self.follower,
            'following': self.following
        }


class Admin(Account):
    def __init__(self, id, gmail, username, password):
        super().__init__(id, gmail, username, password)
        
class Customer(Account):
    def __init__(self, id, gmail, username, password):
        super().__init__(id, gmail, username, password)
        self.sex = None
        
class Seller(Account):
    def __init__(id, gmail, username, password):
        super().__init__(id, gmail, username, password)
        
storage = ZODB.FileStorage.FileStorage('mydata.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root
root.accounts = BTrees.OOBTree.BTree()
root.accounts[10000] = Admin(10000, "admin1@gmail.com", "admin1", "1234")


transaction.commit()

if  __name__ == "__main__":
    accounts = root.accounts
    for a in accounts:
        account = accounts[a]
        print(account.get_email())

        
    import sys
    print(sys.path)

        
    