import ZODB, ZODB.FileStorage
import BTrees._OOBTree
import persistent
import transaction
from datetime import datetime, date
from PySide6.QtWidgets import (
    QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QWidget
)

#topic tags, link is the placeholder for what the button would do
class Tag(persistent.Persistent):
    def __init__(self, tag_text, link = None):
        self.tag_text = tag_text
        self.link = link #what does the tag do
    def get_tag_text(self):
        return self.tag_text
    def get_link(self):
        return self.link

#product in the post
class Product(persistent.Persistent):
    def __init__(self, pr_name, pr_id, seller, status, start, tags, end = None):
    def __init__(self, pr_name, pr_id, seller, status, start, end = None):
        self.pr_name = pr_name
        self.pr_id = pr_id
        self.seller = seller
        self.status = status #upcoming, live, sold
        self.start_date = start #time to go live
        self.end_date = end #Date object for time sold
    def get_name(self):
        return self.pr_name
    def get_title(self):
        return self.pr_title
    def get_seller(self):
        return self.seller
    def get_status(self):
        return self.status
    def get_start_date(self):
        return self.start_date
    def get_end_date(self):
        if self.end_date:
            return self.end_date
        else:
            raise ValueError("Product hasn't ended")
    
#collection of items in a post, items would be persistent list in real??
class Collection(Product):
    def __init__(self, c_name, c_id, seller, status, start, items, end = None,):
        super.__init__(c_name, c_id, seller, status, start, end)
        self.items = persistent.PersistentList() #Item objects in the collection
        self.tags = persistent.PersistentList()
        for i in items:
            self.items.append(i)
            for t in items.get_tags():
                self.tags.append(t)
    def get_items(self):
        return self.items

#individual items in a post
class Item(Product):
    def __init__(self, i_name, i_id, seller, status, start, tags, price, image, end = None):
        super.__init__(i_name, i_id, seller, status, start, end)
        self.price = price
        self.image = image
        self.tags = persistent.PersistentList()
        for t in tags:
            self.tags.append(t)
    def get_price(self):
        return self.price
    def get_image(self):
        return self.image #how to store images in a class
    def get_tags(self):
        return self.tags

#info to display in post
class PostDetails(persistent.Persistent):
    def __init__(self, p_id, p_author, p_info, p_title,
                 product, type = "CF no CC"):
        self.id = p_id
        self.author = p_author
        self.product = persistent.PersistentList() #a single item is a collection size 1
        self.tags = persistent.PersistentList()
        for i in product:
            self.product.append(i)
            for t in i.get_tags:
                if t not in self.tags:
                    self.tag.append(t)
        self.info = p_info
        self.title = p_title
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
        return self.tags
    def get_sales_type(self):
        return self.sales_type
        
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

root.tags = BTrees.OOBTree.BTree()
root.tags[1000] = Tag("secondhand")
root.tags[1001] = Tag("fashion")

root.products = BTrees.OOBTree.BTree()
root.product[1000] = Collection("Mona Tops Collection",
                                1000, "Mona", "Upcoming",
                                date(2024, 5, 16), ,
                                []
)

transaction.commit()

if  __name__ == "__main__":
    admins = root.admins
    for a in admins:
        admin = admins[a]
        print(admin.get_email())
    import sys
    print(sys.path)

        
    