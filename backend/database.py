import ZODB, ZODB.FileStorage
import sys
import os
from pathlib import Path
root_dir = Path('/Users/Miki Ajiki/desktop/Curate')
sys.path.append(str(root_dir))
import BTrees._OOBTree
import persistent
import transaction
import uuid
from datetime import datetime, date
from frontend.public.images.post_images.db_test_pics import *

#for getting image data
images_path = str(root_dir / 'frontend' / 'public' / 'images' / 'post_images' / 'db_test_pics') + '/'
def get_image_data(image_name):
    with open(images_path+image_name, 'rb') as f:
        return f.read()

#generates a random unique id
def generate_id(type):
    while str(uuid.uuid4()) in getattr(root, type, []):
        pass
    return str(uuid.uuid4())


# creating the database
storage = ZODB.FileStorage.FileStorage('mydata.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root

# creating the BTrees
root.accounts = BTrees.OOBTree.BTree()
root.products = BTrees.OOBTree.BTree()
root.tags = BTrees.OOBTree.BTree()

#topic tags, prolly gonna keep information like statistics??
class Tag(persistent.Persistent):
    def __init__(self, tag_text, link = None):
        if tag_text in root.tags:
            raise ValueError("Tag Already Exists")
        else:
            self.tag_text = tag_text
        self.link = link #what does the tag do
    def get_tag_text(self):
        return self.tag_text
    def get_link(self):
        return self.link

#product in the post
class Product(persistent.Persistent):
    def __init__(self, pr_id, seller, start, pr_name = "", images = [], tags = [], end = None):
        self.pr_id = pr_id
        self.pr_name = pr_name
        self.seller = seller
        if datetime.now() >= start: #upcoming, live, sold out
            self.status = "live"
        else:
            self.status = "upcoming"
        self.created = datetime.now() #date post created
        self.modified = self.created
        self.start_date = start #time to go live
        self.end_date = end #Date object for time sold
        self.image = persistent.list.PersistentList()
        for image in images:
            self.image.append(image)
        self.tags = persistent.list.PersistentList()
        for tag in tags:
            self.tags.append(tag)
    def get_id(self):
        return self.pr_id
    def get_name(self):
        return self.pr_name
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
    def get_tags(self):
        return self.tags
    def print_info(self):
        print(f'----Product Info----\nProduct ID: {self.pr_id}\n'
              f'Seller: {self.seller}\n'
              f'Status: {self.status}')
        print(f'Start Date: {self.start_date.strftime("%Y-%m-%d %H:%M:%S")}')
        
    
#collection of items in a post, items would be persistent list in real??
class Collection(Product):
    def __init__(self, c_id, seller, start, items, c_name = "", images = [], tags = [], end = None):
        super().__init__(c_id, seller, start, c_name, images, tags, end)
        self.items = persistent.list.PersistentList() #Item objects in the collection
        for i in items:
            self.items.append(i)
            for t in i.get_tags():
                self.tags.append(t)
    def get_items(self):
        return self.items
    def add_item(self, item):
        if item not in self.items:
            self.items.append(item)
    def print_info(self):
        super().print_info()
        print("Items: ")
        for item in self.items:
            print(item.get_id())
        print(f'Collection Name: {self.pr_name}')
        print()

#individual items in a post
class Item(Product):
    def __init__(self, i_id, seller, start, price, i_name = "", images = [], tags = [], end = None):
        super().__init__(i_id, seller, start, i_name, images, tags, end)
        self.price = price
    def get_price(self):
        return self.price
    def get_image(self):
        return self.images
    def get_tags(self):
        return self.tags
    def print_info(self):
        super().print_info()
        print("Price: " + str(self.price))
        print(f'Item Name: {self.pr_name}')
        print()

#info to display in post
class PostDetails(persistent.Persistent):
    def __init__(self, p_id, p_author, p_info, p_title,
                 product, type = "cf no cc"): #types can be cf no cc, preorder, or bidding
        self.id = p_id
        self.author = p_author
        self.product = persistent.list.PersistentList() #a single item is a collection size 1
        self.tags = persistent.list.PersistentList()
        # for i in product:
        #     self.product.append(i)
        #     for t in i.get_tags:
        #         if t not in self.tags:
        #             self.tag.append(t)
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
    def __init__(self, id, email, password, username = ""):
        self.id = id
        self.email = email
        self.password = password
        self.phone_number = ""
        self.sex = None
        self.username = username
        self.birthdate = None
        self.address = "Samutprakan ja"
        self.follower = 0
        self.following = 0

        self.products = persistent.list.PersistentList()
        # self.user_id = generate_user_id()
    def get_email(self):
        return self.email
    def get_password(self):
        return self.password
    def get_username(self):
        return self.username
    def set_username(self, username):
        if username in root.accounts:
            raise ValueError("Bad Dog")
        else:
            self.username = username
    def add_product(self, product):
        self.products.add(product.get_id())
    def print_info(self):
        print(f'----User Info---\nEmail: {self.email}\n'
              f'Password: {self.password}\n'
              f'Username: {self.username}\n')
    def serialize(self):
        return {
            'email': self.email,
            'username': self.username,
            'address': self.address,
            'sex' : self.sex,
            'birthdate' : self.birthdate,
            'phone_number' : self.phone_number,
            'follower': self.follower,
            'following': self.following
        }


class Admin(Account):
    def __init__(self, id, email, password, username = ""):
        super().__init__(id, email, password, username)
        
class Customer(Account):
    def __init__(self, id, email, password, username = ""):
        super().__init__(id, email, password, username)
        
class Seller(Account):
    def __init__(self, id, email, password, username = ""):
        super().__init__(id, email, password, username)
        
    def __init__(self, email, password):
        super().__init__(email, password)
        
# admins
# key value = username
admin_1 = Admin(generate_id('admins'), "admin1@gmail.com", "1234")
admin_1.set_username("adminnajaa~~")
admin_1.phone_number = "000-000-0000"
admin_1.sex = "Others"
admin_1.birthdate = date(2000, 10, 30)
root.accounts[admin_1.get_username()] = admin_1

# users
user_1 = Account(generate_id('users'), "user1@gmail.com", "1234")
user_1.set_username("iammuser1")
root.accounts[user_1.get_username()] = user_1

user_2 = Account(generate_id('users'), "user2@gmail.com", "1234")
root.accounts[user_2.get_username()] = user_2
user_2.set_username("iammuser2")

# tags
# key value = tag text
tag1 = Tag("secondhand")
root.tags[tag1.get_tag_text()] = tag1
tag2 = Tag("fashion")
root.tags[tag2.get_tag_text()] = tag2
tag3 = Tag("cute")
root.tags[tag3.get_tag_text()] = tag3
tag4 = Tag("jellyfish")
root.tags[tag4.get_tag_text()] = tag4
tag5 = Tag("keychains")
root.tags[tag5.get_tag_text()] = tag5
tag6 = Tag("handmade")
root.tags[tag6.get_tag_text()] = tag6
tag7 = Tag("custom")
root.tags[tag7.get_tag_text()] = tag7
tag8 = Tag("cottagecore")
root.tags[tag8.get_tag_text()] = tag8
tag9 = Tag("coquette")
root.tags[tag9.get_tag_text()] = tag9

# products
# index = {product_id}
# value = Collection() or Item()
# product_id = {seller's user}{1...}
item1_pics = ['IMG_7369.jpg']
item1_pics_data = [get_image_data(x) for x in item1_pics]
item1_tags = [root.tags['coquette'], root.tags['cute']]
item1 = Item(generate_id("products"), user_1.get_username(), datetime(2024, 5, 20, 10, 15),
             50, "item 1", item1_pics_data, item1_tags)
root.products[item1.get_seller() + item1.get_id()] = item1

item2_pics = ['IMG_7370.jpg']
item2_pics_data = [get_image_data(x) for x in item2_pics]
item2_tags = [root.tags['coquette'], root.tags['cute']]
item2 = Item(generate_id("products"), user_1.get_username(), datetime(2024, 5, 20, 10, 15),
             50, "item 2 laa", item1_pics_data, item1_tags)
root.products[item2.get_seller() + item1.get_id()] = item2

col1_pics = ['IMG_7368.jpg']
col1_pics_data = [get_image_data(x) for x in col1_pics]
col1_tags = [root.tags['secondhand'], root.tags['coquette'], root.tags['cute']]
col1 = Collection(generate_id("products"), user_1.get_username(), datetime(2024, 5, 20, 10, 15),
                  [item1, item2], "~New Drop OOEE~", col1_pics_data, col1_tags)
root.products[col1.get_seller() + col1.get_id()] = col1

transaction.commit()
if  __name__ == "__main__":
    admins = root.admins
    for key in admins:
        admins[key].print_info()
    
    users = root.users
    for key in users:
        users[key].print_info()

    products = root.products
    for key in products:
        products[key].print_info()
        
    