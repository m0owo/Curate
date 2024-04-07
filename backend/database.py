import ZODB, ZODB.FileStorage
import sys
import os
import io
from pathlib import Path
root_dir = Path('/Users/Miki Ajiki/desktop/Curate')
sys.path.append(r'/Users/musicauyeung/Documents/KMITL/Year 2/Curate')
sys.path.append('C:\school\Curate')
sys.path.append(os.getcwd())
sys.path.append(str(root_dir))
import BTrees._OOBTree
import persistent
import transaction
import uuid
from PIL import Image
from io import BytesIO
from datetime import datetime, date
from frontend.public.images.post_images.db_test_pics import *

#for getting image data
images_path = str(root_dir / 'frontend' / 'public' / 'images' / 'post_images' / 'db_test_pics') + '/'
images_path_ms = 'frontend/public/images/post_images/db_test_pics/'
images_path_putter = 'C:\school\Curate\\frontend\public\images\post_images\db_test_pics\\'
images_path_k = r'C:\Users\Miki Ajiki\Desktop\Curate\frontend\public\images\post_images\db_test_pics\\'


# # getting webP image data
# def get_webp_data(image_name):
#     full_image_path = images_path_k + image_name
#     try:
#         with Image.open(full_image_path) as img:
#             webp_data = io.BytesIO()
#             img.save(webp_data, format='WEBP')
#             return webp_data.getvalue()
#     except IOError:
#         print(f'Unable to convert {full_image_path} to WebP format')

# def get_webp_datas(images_arr):
#     return [get_webp_data(x) for x in images_arr]

# # getting original image data
# def get_image_data(images_name):
#     full_image_path = images_path_ms + images_name
#     original_data = open(full_image_path, 'rb').read()
#     return original_data

# def get_image_datas(images_arr):
#     return [get_image_data(x) for x in images_arr]

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
root.posts = BTrees.OOBTree.BTree()
root.tags = BTrees.OOBTree.BTree()
root.addresses = BTrees.OOBTree.BTree()
root.orders = BTrees.OOBTree.BTree()
root.stores =  BTrees.OOBTree.BTree()

#topic tags, prolly gonna keep information like statistics??
class Tag(persistent.Persistent):
    def __init__(self, tag_text, link = None):
        if tag_text in root.tags:
            raise ValueError("Tag Already Exists")
        else:
            self.tag_text = tag_text
        self.link = link #what does the tag do
        self.times_used = 0
    def get_tag_text(self):
        return self.tag_text
    def add_times_used(self):
        self.times_used += 1
    def minus_times_used(self):
        self.times_used -= 1
    def get_link(self):
        return self.link
    def get_times_used(self):
        return self.times_used
    def serialize(self):
        return {
            'tag_text': self.tag_text
        }
    def print_info(self):
        print(f'tag_text: {self.tag_text}\n'
              f'times_used: {self.times_used}\n')

#product in the post
class Product(persistent.Persistent):
    def __init__(self, pr_id, seller, start, description = "", pr_name = "", images = "", tags = [], end = None, mode = ""):
        self.pr_id = pr_id
        self.pr_name = pr_name
        self.seller = seller
        if datetime.now() >= start: #upcoming, live, sold out = when stock is zero
            self.status = "available"
        else:
            self.status = "upcoming"
        self.mode = mode
        self.description = description
        self.created = datetime.now() #date post created
        self.modified = self.created #default modified date is date created
        self.start_date = start #time to go live
        self.end_date = end #Date object for time sold
        self.images = images
        # for image in images:
        #     self.images.append(image)
        self.tags = persistent.list.PersistentList()
        self.description = description
        for tag in tags:
            self.tags.append(tag)
        self.wishlist = persistent.list.PersistentList()
        self.queue = persistent.list.PersistentList()
    def get_id(self):
        return self.pr_id
    def get_pr_description(self):
        return self.description
    def get_pr_name(self):
        return self.pr_name
    def get_seller(self):
        return self.seller
    def get_status(self):
        return self.status
    def get_start_date(self):
        return self.start_date
    def get_end_date(self): #ends sale when sold out
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
        print(f'Description {self.description}')
        print(f'Images: {self.images}')
    def serialize(self):
        return {
            'product_id': self.pr_id,
            'product_name': self.pr_name,
            'seller': self.seller,
            "mode": self.mode,
            "description": self.description,
            'status': self.status,
            'created': self.created,
            'modified': self.modified,
            'start': self.start_date,
            'end': self.end_date,
            'images' : self.images,
            'tags': [tag.serialize() for tag in self.tags],
            'description': self.description,
            'wishlist' : [w for w in self.wishlist],
            'queue' : [q for q in self.queue]
             
        }
        
#collection of items in a post, items would be persistent list in real??
class Collection(Product):
    def __init__(self, c_id, seller, start, items, description ="", c_name = "", images = [], tags = [], end = None):
        super().__init__(c_id, seller, start, description, c_name, images, tags, end)
        self.items = persistent.list.PersistentList() #Item objects in the collection
        for i in items:
            self.items.append(i)
            for t in i.get_tags():
                self.tags.append(t)
        not_sold_out = any(item.get_status() != 'sold out' for item in self.items)
        if not not_sold_out:
            self.status = 'sold out'
        print(items[0].get_price())
        max_price = max(item.get_price() for item in self.items)
        min_price = min(item.get_price() for item in self.items)
        self.price_range = (min_price, max_price)
    def get_items(self):
        return self.items
    def add_item(self, item):
        if item not in self.items:
            self.items.append(item)
    def get_price_range(self):
        return self.price_range
    def print_info(self):
        super().print_info()
        print("Items: ")
        for item in self.items:
            print(item.get_id())
        print(f'Collection Name: {self.pr_name}\n'
              f'Price Range: {self.price_range}\n')
    def serialize(self):
        serialized_data = super().serialize()
        serialized_data.update({
            'items': [x.serialize() for x in self.items],
            'price_range': self.price_range
        })
        return serialized_data

#individual items in a post
class Item(Product):
    def __init__(self, i_id, seller, start, price, stock, description="", i_name = "", images = [], tags = [], end = None):
        super().__init__(i_id, seller, start, description, i_name, images, tags, end)
        self.price = price
        self.stock = stock
        self.update_stock(stock)
    def get_price(self):
        return self.price
    def get_image(self):
        return self.images
    def get_tags(self):
        return self.tags
    def get_stock(self):
        return self.stock
    def update_stock(self, num): #change the stock value with purchases
        self.stock = num
        if num == 0:
            self.status = 'sold out'
    def print_info(self):
        super().print_info()
        print("Price: " + str(self.price))
        print(f'Item Name: {self.pr_name}\n'
              f'Remaining Stock: {self.stock}\n'
              f'Status: {self.status}\n')
    def serialize(self):
        serialized_data = super().serialize()
        serialized_data.update({
            'price': self.price,
            'stock': self.stock,
            'status': self.status,
        })
        return serialized_data

#info to display in post
class PostDetails(persistent.Persistent):
    def __init__(self, p_id, p_author, product, p_info = "", p_title = "",
                 type = "cf no cc"): #types can be cf no cc, preorder, or bidding
        self.id = p_id
        self.author_id = p_author.get_id()
        self.author_name = p_author.get_store_name()
        self.author_pic = p_author.get_store_picture()
        self.product = product
        self.tags = persistent.list.PersistentList()
        for tag in product.get_tags(): # make sure the tags are not repeated
            if tag not in self.tags:
                self.tags.append(tag)
                tag.add_times_used()
        self.info = p_info
        self.title = p_title
        self.created = datetime.now()
        self.modified = self.created
        self.sales_type = type
        if isinstance(product, Collection):
            self.product_type = 'Collection'
        elif isinstance(product, Item):
            self.product_type = 'Item'
        self.status = self.product.get_status()
    def get_id(self):
        return self.id
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
        return self.product_type
    def get_tags(self):
        return self.tags
    def get_sales_type(self):
        return self.sales_type
    def print_info(self):
        print(
            f'----Post Info----\n'
            f'post id: {self.id}\n'
            f'post author: {self.author_name}\n',
            f'product: {self.product.get_id()}\n'
            f'tags: {[x.get_tag_text() for x in self.tags]}\n'
            f'info: {self.info}\n'
            f'title: {self.title}\n'
            f'created: {self.created.strftime("%Y-%m-%d %H:%M:%S")}\n'
            f'sales type: {self.sales_type}\n'
            f'post status: {self.status}\n'
        )
    def serialize(self):
        return {
            'post_id': self.id, #id of the post
            'author_id': self.author_id, #username of the author 
            'author_name': self.author_name, #username of the author 
            'author_pic': self.author_pic,
            'product': self.product.serialize(), #one product, either a collection or an item
            'info': self.info, #post info or description
            'title': self.title, #post title, display will be bold
            'created': self.created, #date created
            'modified': self.modified, #date last modified
            'product_type': self.product_type, #tells whether the product is item/col
            'tags': [x.serialize() for x in self.tags], #list of tags
            'sales_type': self.sales_type, #cf no cc, bidding
            'status': self.status,
        }

class Order(persistent.Persistent):
    def __init__(self, order_id, product, buyer, seller, status="unpaid"):
        self.order_id = order_id
        self.product = product
        self.buyer = buyer
        self.seller = seller
        self.order_date = datetime.now() #date order created
        self.status = status
        self.slip_picture = ''

    def get_order_id(self):
        return self.order_id
    def get_product(self):
        return self.product
    def get_buyer(self):
        return self.buyer
    def get_seller(self):
        return self.seller
    def get_status(self):
        return self.status
    def get_order_date(self):
        return self.order_date
    
    def pay_product(self):
        self.status = "shipping"

    def confirm_shipment(self):
        self.status = "completed"

    def cancel_shipment(self):
        self.status = "cancelled"
    
    def print_info(self):
        print(
            f'----Post Info----\n'
            f'Order id: {self.order_id}\n'
            f'Order Date: {self.order_date.strftime("%Y-%m-%d %H:%M:%S")}\n'
            f'Order status: {self.status}\n'
            f'Buyer: {self.buyer}\n'
            f'Seller: {self.seller}\n'
        )

    def serialize(self):
        serialized_data = {
            'order_id': self.order_id,
            'order_buyer': self.buyer,
            'order_seller': self.seller,
            'order_status': self.status,
            'order_date': self.order_date,
            'slip_picture' : self.slip_picture
        }
        serialized_data.update(self.product.serialize())

        return serialized_data
    


class Account(persistent.Persistent):
    def __init__(self, id, email, password, username = "", sex = "", pic = "", store = None):
        self.id = id
        self.email = email
        self.password = password
        self.phone_number = ""
        self.username = username
        self.birthdate = None
        self.addresses = persistent.list.PersistentList()
        self.follower = 0
        self.following = 0
        self.sex = sex
        self.products = persistent.list.PersistentList()
        self.orders = persistent.list.PersistentList()
        self.wishlist = persistent.list.PersistentList()
        self.pic = pic
        self.store = store

    def get_pic(self):
        return self.pic
    
    def set_store(self, store):
        self.store = store

    def get_email(self):
        return self.email
    
    def get_id(self):
        return self.id
    
    def get_password(self):
        return self.password

    def get_username(self):
        return self.username

    def set_username(self, username):
        if username in root.accounts:
            raise ValueError("Username is Already in Use")
        else:
            self.username = username

    def add_product(self, product):
        self.products.add(product.get_id()) #id of the product

    def add_wishlist(self, product):
        self.wishlist.append(product)

    def get_phone_num(self):
        return self.phone_number

    def print_info(self):
        serialized_addresses = [address.serialize() for address in self.addresses]
        print(f'----User Info---\nEmail: {self.email}\n'
              f'Password: {self.password}\n'
              f'Username: {self.username}\n'
              f'Adderres: {serialized_addresses}\n'
              f'store: {self.store}\n')

    def serialize(self):
        serialized_addresses = [address.serialize() for address in self.addresses]
        serialized_products = [products.serialize() for products in self.wishlist]
        return {
            'id': self.id,
            'email': self.email,
            'username': self.username,
            'addresses': serialized_addresses,  # Correct attribute name
            'sex': self.sex,
            'birthdate': self.birthdate,
            'phone_number': self.phone_number,
            'follower': self.follower,
            'following': self.following,
            'wishlist': serialized_products,
            'store': self.store
        }

class Address:
    def __init__(self, name, phone_number, province, district, sub_district, postal, details):
        self.name = name
        self.phone_number = phone_number
        self.province = province
        self.district = district
        self.sub_district = sub_district
        self.postal = postal
        self.details = details
    def set_details(self, new_details):
        self.details = new_details
    def serialize(self):
        return {
            'name': self.name,
            'phone_number' : self.phone_number,
            'province': self.province,
            'district': self.district,
            'sub_district': self.sub_district,
            'postal' : self.postal,
            'details': self.details
        }
    
class Admin(Account):
    def __init__(self, id, email, password, username = ""):
        super().__init__(id, email, password, username)
        
class Customer(Account):
    def __init__(self, id, email, password, username = ""):
        super().__init__(id, email, password, username)
        self.wishlists = persistent.list.PersistentList()
        
class Seller(Account):
    def __init__(self, id, email, password, username = ""):
        super().__init__(id, email, password, username)
        

class Store:
    def __init__(self, store_id, user_name, store_name, email, phone_num, description, picture):
        self.store_id = store_id
        self.store_user_name = user_name
        root.accounts[self.store_user_name].set_store(self.store_id)
        self.store_name = store_name
        self.email = email
        self.phone_num = phone_num
        self.description = description
        self.picture = picture
        self.items = persistent.list.PersistentList()
        self.collections = persistent.list.PersistentList()
        self.orders = persistent.list.PersistentList()
        self.reviews = persistent.list.PersistentList()

    def get_id(self):
        return self.store_id
    
    def add_item(self, item):
        self.items.append(item)
    
    def get_store_name(self):
        return self.store_name
    
    def get_store_picture(self):
        return self.picture
    
    def add_collection(self, collection):
        self.collections.append(collection)

    def add_order(self, order):
        self.orders.append(order)

    def add_review(self, review):
        self.reviews.append(review)

    def change_picture(self, picture):
        self.picture = picture

    def serialize(self):
        collections = [c.serialize() for c in self.collections]
        items = [i.serialize() for i in self.items]
        orders = [o.serialize() for o in self.orders]

        return{
            "store_id" : self.store_id,
            "store_user_name": self.store_user_name,
            "store_name" : self.store_name,
            "email" : self.email,
            "phone_number" : self.phone_num,
            "description" : self.description,
            "picture" : self.picture,
            "items" : items,
            "collections" : collections,
            "orders" : orders 
            
        }
    def print_info(self):
        serialized_collection = [collection.serialize() for collection in self.collections]
        serialized_items =  [item.serialize() for item in self.items]
        serialized_orders = [order.serialize() for order in self.orders]
        print(f'----Store Info---\n'
            f'username: {self.store_user_name}\n'
            f'store name: {self.store_name}\n'
            f'store_id: {self.store_id}')
            # f'collections: {serialized_collection}\n'
            # f'items: {serialized_items}\n'
            # f'order: {serialized_orders}\n')

# accounts
# key value = username
admin_1 = Admin(generate_id('accounts'), "admin1@gmail.com", "1234")
admin_1.set_username("adminnajaa~~")
admin_1.phone_number = "000-000-0000"
admin_1.sex = "Others"
admin_1.birthdate = date(2000, 10, 30)
root.accounts[admin_1.get_username()] = admin_1

# users
user_1 = Account(generate_id('accounts'), "user1@gmail.com", "1234", "iammuser1")
root.accounts[user_1.get_username()] = user_1

# STORE PARAMETER store_id, user_name, store_name, email, phone_num, description, picture
store_1_pic = 'user1.jpeg'
store_1 = Store(user_1.get_id() + generate_id('stores'),
                user_1.get_username(), "Gumie Preorder",
                user_1.get_email(), user_1.get_phone_num(),
                "preorder goods and toys", store_1_pic)
root.stores[store_1.get_id()] = store_1

user_2 = Account(generate_id('accounts'), "user2@gmail.com", "1234")
user_2.set_username("user2day")
root.accounts[user_2.get_username()] = user_2

store_2_pic = 'user2.jpeg'
store_2 = Store(user_2.get_id() + generate_id('stores'),
                user_2.get_username(), "User 2's Store",
                user_2.get_email(), user_2.get_phone_num(),
                "Secondhand Coquette Fits", store_2_pic)
root.stores[store_2.get_id()] = store_2

user_3 = Account(generate_id('accounts'), "user3@gmail.com", "1234")
user_3.set_username("me3")
root.accounts[user_3.get_username()] = user_3

store_3_pic = 'user3.JPG'
store_3 = Store(user_3.get_id() + generate_id('stores'),
                user_3.get_username(), "Secondhand Coquette Fits",
                user_3.get_email(), user_3.get_phone_num(),
                "Coquette outfits and clothes", store_3_pic)
root.stores[store_3.get_id()] = store_3

user_4 = Account(generate_id('accounts'), "user4@gmail.com", "1234")
user_4.set_username("4youtoo")
root.accounts[user_4.get_username()] = user_4

store_4_pic = 'user4.JPG'
store_4 = Store(user_4.get_id() + generate_id('stores'),
                user_4.get_username(), "Home Decoo",
                user_4.get_email(), user_4.get_phone_num(),
                "Secondhand home deco from Japan", store_4_pic)
root.stores[store_4.get_id()] = store_4

user_5 = Account(generate_id('accounts'), "user5@gmail.com", "1234")
user_5.set_username("5h.aha")
root.accounts[user_5.get_username()] = user_5

store_5_pic = 'user5.JPG'
store_5 = Store(user_5.get_id() + generate_id('stores'),
                user_5.get_username(), "Q_rochet",
                user_5.get_email(), user_5.get_phone_num(),
                "handmade crocheted goods", store_5_pic)
root.stores[store_5.get_id()] = store_5

user_6 = Account(generate_id('accounts'), "user6@gmail.com", "1234")
user_6.set_username("Plen6")
root.accounts[user_6.get_username()] = user_6

store_6_pic = 'user6.JPG'
store_6 = Store(user_6.get_id() + generate_id('stores'),
                user_6.get_username(), "Ceram6",
                user_6.get_email(), user_6.get_phone_num(),
                "Ceramics and Paint", store_6_pic)
root.stores[store_6.get_id()] = store_6

user_7 = Account(generate_id('accounts'), "user7@gmail.com", "1234")
user_7.set_username("say_ven")
root.accounts[user_7.get_username()] = user_7

store_7_pic = 'user7.JPG'
store_7 = Store(user_7.get_id() + generate_id('stores'),
                user_7.get_username(), "VenShop",
                user_7.get_email(), user_7.get_phone_num(),
                "premium vintage secondhand gadgets", store_7_pic)
root.stores[store_7.get_id()] = store_7

# tags
# key value = tag text
second_hand = Tag("secondhand")
root.tags[second_hand.get_tag_text()] = second_hand

fashion = Tag("fashion")
root.tags[fashion.get_tag_text()] = fashion

cute = Tag("cute")
root.tags[cute.get_tag_text()] = cute

jellyfish = Tag("jellyfish")
root.tags[jellyfish.get_tag_text()] = jellyfish

keychain = Tag("keychain")
root.tags[keychain.get_tag_text()] = keychain

handmade = Tag("handmade")
root.tags[handmade.get_tag_text()] = handmade

custom = Tag("custom")
root.tags[custom.get_tag_text()] = custom

cottagecore = Tag("cottagecore")
root.tags[cottagecore.get_tag_text()] = cottagecore

coquette = Tag("coquette")
root.tags[coquette.get_tag_text()] = coquette

toy = Tag("toy")
root.tags[toy.get_tag_text()] = toy

crochet = Tag("crochet")
root.tags[crochet.get_tag_text()] = crochet

gadget = Tag("gadget")
root.tags[gadget.get_tag_text()] = gadget

aesthetic = Tag("aesthetic")
root.tags[aesthetic.get_tag_text()] = aesthetic

flower = Tag("flower")
root.tags[flower.get_tag_text()] = flower

home = Tag("home")
root.tags[home.get_tag_text()] = home

minimal = Tag("minimal")
root.tags[minimal.get_tag_text()] = minimal

# products
# index = {product_id}
# value = Collection() or Item()
item1_pics_data = 'item2.jpg'
item1_tags = [fashion, cute, handmade, crochet]
item1 = Item(generate_id("products"), store_1.store_user_name, datetime(2024, 5, 20, 10, 15),
             350, 5, "", "Pastel Fluffy Hats", item1_pics_data, item1_tags)
root.products[item1.get_id()] = item1

item2_pics_data = 'item3.jpg'
item2_tags = [jellyfish, handmade, custom, keychain]
item2 = Item(generate_id("products"), store_1.store_user_name, datetime(2024, 5, 20, 10, 15),
             75, 3, "", "Jellyfish Keychains", item2_pics_data, item2_tags)
root.products[item2.get_id()] = item2

item3_pics_data = 'item4.jpg'
item3_tags = [toy, cute]
item3 = Item(generate_id('products'), store_1.store_user_name,
             datetime(2024, 5, 21, 15, 20), 150, 10, "", 'ODD Club School',
             item3_pics_data, item3_tags)
root.products[item3.get_id()] = item3

item4_pics_data = 'item5.jpg'
item4_tags = [second_hand, cottagecore]
item4 = Item(generate_id('products'), store_1.store_user_name,
             datetime(2024, 5, 22, 19, 30), 350, 5, "", "Secondhand Knitted Blanket",
             item4_pics_data, item4_tags)
root.products[item4.get_id()] = item4

item5_pics_data = 'item6.jpg'
item5_tags = [toy, gadget, cute]
item5 = Item(generate_id('products'), store_1.store_user_name,
             datetime(2024, 4, 4, 19, 30), 75, 4, "", "Tomato Handheld Fan",
             item5_pics_data, item5_tags)
root.products[item5.get_id()] = item5

item6_pics_data = 'item8.jpg'
item6_tags = [cute, fashion, coquette]
item6 = Item(generate_id('products'), store_2.store_user_name,
             datetime(2024, 4, 4, 19, 30), 75, 4, "", "Flower Set 1",
             item6_pics_data, item6_tags)
root.products[item6.get_id()] = item6

item7_pics_data = 'item9.jpg'
item7_tags = [cute, fashion, coquette]
item7 = Item(generate_id('products'), store_2.store_user_name,
             datetime(2024, 4, 4, 19, 30), 75, 4, "", "Dolly Set 1",
             item7_pics_data, item7_tags)
root.products[item7.get_id()] = item7

item8_pics_data = 'item10.jpg'
item8_tags = [cute, fashion, coquette]
item8 = Item(generate_id('products'), store_2.store_user_name,
             datetime(2024, 4, 4, 19, 30), 75, 4, "", "Spaghetti Set 1",
             item8_pics_data, item8_tags)
root.products[item8.get_id()] = item8

item9_pics_data = 'item11.jpg'
item9_tags = [cute, fashion, coquette]
item9 = Item(generate_id('products'), store_2.store_user_name,
             datetime(2024, 4, 4, 19, 30), 75, 4, "", "Dolly Set 2",
             item9_pics_data, item9_tags)
root.products[item9.get_id()] = item9

item10_pics_data = 'item12.jpg'
item10_tags = [cute, fashion, coquette]
item10 = Item(generate_id('products'), store_2.store_user_name,
             datetime(2024, 4, 4, 19, 30), 75, 4, "", "Spaghetti Set 1",
             item10_pics_data, item10_tags)
root.products[item10.get_id()] = item8

item11_pics_data = 'item13.jpg'
item11_tags = [toy, gadget, cute]
item11 = Item(generate_id('products'), store_2.store_user_name,
             datetime(2024, 4, 4, 19, 30), 75, 4, "", "Caramel Set 1",
             item11_pics_data, item11_tags)
root.products[item11.get_id()] = item11

item12_pics_data = 'item14.jpg'
item12_tags = [home, minimal]
item12 = Item(generate_id('products'), store_3.store_user_name,
             datetime(2024, 4, 4, 19, 30), 75, 4, "", "Goldfish Baht Curtains",
             item12_pics_data, item12_tags)
root.products[item12.get_id()] = item12

item13_pics_data = 'item15.jpg'
item13_tags = [cute, flower, home, cottagecore]
item13 = Item(generate_id('products'), store_3.store_user_name,
             datetime(2024, 4, 4, 19, 30), 75, 4, "", "Touch Grass Rug",
             item13_pics_data, item13_tags)
root.products[item13.get_id()] = item13

item14_pics_data = 'item16.jpg'
item14_tags = [toy, gadget, cute]
item14 = Item(generate_id('products'), store_3.store_user_name,
             datetime(2024, 4, 4, 19, 30), 75, 4, "", "Teakub Pom",
             item14_pics_data, item14_tags)
root.products[item14.get_id()] = item14

item15_pics_data = 'item17.jpg'
item15_tags = [toy, gadget, cute, home, minimal]
item15 = Item(generate_id('products'), store_3.store_user_name,
             datetime(2024, 4, 4, 19, 30), 75, 4, "", "Desk Organizer",
             item15_pics_data, item15_tags)
root.products[item15.get_id()] = item15

item16_pics_data = 'item18.jpg'
item16_tags = [cute, fashion, crochet, handmade]
item16 = Item(generate_id('products'), store_4.store_user_name,
             datetime(2024, 4, 4, 19, 30), 75, 4, "", "Lavendar",
             item16_pics_data, item16_tags)
root.products[item16.get_id()] = item16

item17_pics_data = 'item19.jpg'
item17_tags = [cute, fashion, crochet, handmade]
item17 = Item(generate_id('products'), store_4.store_user_name,
             datetime(2024, 4, 4, 19, 30), 75, 4, "", "Matcha Strawberry",
             item17_pics_data, item17_tags)
root.products[item17.get_id()] = item17

item18_pics_data = 'item20.jpg'
item18_tags = [cute, fashion, crochet, handmade]
item18 = Item(generate_id('products'), store_4.store_user_name,
             datetime(2024, 4, 4, 19, 30), 75, 4, "", "Cherry Bunny",
             item18_pics_data, item18_tags)
root.products[item18.get_id()] = item18

item19_pics_data = 'item21.jpg'
item19_tags = [cottagecore, crochet, fashion]
item19 = Item(generate_id('products'), store_4.store_user_name,
             datetime(2024, 4, 4, 19, 30), 75, 4, "", "Star Girl",
             item19_pics_data, item19_tags)
root.products[item19.get_id()] = item19

item20_pics_data = 'item22.jpg'
item20_tags = [home, cute, aesthetic]
item20 = Item(generate_id('products'), store_4.store_user_name,
             datetime(2024, 4, 4, 19, 30), 75, 4, "", "Smiley Cereal",
             item20_pics_data, item20_tags)
root.products[item20.get_id()] = item20

item21_pics_data = 'item23.jpg'
item21_tags = [toy, cute, aesthetic]
item21 = Item(generate_id('products'), store_5.store_user_name,
             datetime(2024, 4, 4, 19, 30), 75, 4, "", "Star Rings",
             item21_pics_data, item21_tags)
root.products[item21.get_id()] = item21

item22_pics_data = 'item24.jpg'
item22_tags = [toy, gadget, cute]
item22 = Item(generate_id('products'), store_5.store_user_name,
             datetime(2024, 4, 4, 19, 30), 75, 4, "", "Orca Ceramug",
             item22_pics_data, item22_tags)
root.products[item22.get_id()] = item22

item23_pics_data = 'item25.jpg'
item23_tags = [toy, gadget, cute]
item23 = Item(generate_id('products'), store_5.store_user_name,
             datetime(2024, 4, 4, 19, 30), 75, 4, "", "Bed Cat Mug",
             item23_pics_data, item23_tags)
root.products[item23.get_id()] = item23

# item8_pics = ['item10.jpg']
# item8_pics_data = get_webp_datas(item8_pics)
# item8_tags = [toy, gadget, cute]
# item8 = Item(generate_id('products'), store_1.store_user_name,
#              datetime(2024, 4, 4, 19, 30), 75, 4, "", "Spaghetti Set 1",
#              item8_pics_data, item8_tags)
# root.products[item8.get_seller() + item8.get_id()] = item8

# item8_pics = ['item10.jpg']
# item8_pics_data = get_webp_datas(item8_pics)
# item8_tags = [toy, gadget, cute]
# item8 = Item(generate_id('products'), store_1.store_user_name,
#              datetime(2024, 4, 4, 19, 30), 75, 4, "", "Spaghetti Set 1",
#              item8_pics_data, item8_tags)
# root.products[item8.get_seller() + item8.get_id()] = item8

# item8_pics = ['item10.jpg']
# item8_pics_data = get_webp_datas(item8_pics)
# item8_tags = [toy, gadget, cute]
# item8 = Item(generate_id('products'), store_1.store_user_name,
#              datetime(2024, 4, 4, 19, 30), 75, 4, "", "Spaghetti Set 1",
#              item8_pics_data, item8_tags)
# root.products[item8.get_seller() + item8.get_id()] = item8

#-----------------

# col1_pics = ['IMG_7368.jpg']
# col1_pics_data = [get_webp_data(x) for x in col1_pics]
# col1_tags = [root.tags['secondhand'], root.tags['coquette'], root.tags['cute']]
# col1 = Collection(generate_id("products"), user_1.get_username(), datetime(2024, 5, 20, 10, 15),
#                   [item1, item2], "This is Collection 1", "~New Drop OOEE~", col1_pics_data, col1_tags)
# root.products[col1.get_seller() + col1.get_id()] = col1

# post1 = PostDetails(generate_id('posts'), user_1.get_username(), col1, "TEST INFO", "TEST TITLE")
# root.posts[post1.get_id()] = post1

post1 = PostDetails(generate_id('posts'), store_1, item1, item1.get_pr_description(), item2.get_pr_name())
root.posts[post1.get_id()] = post1

post2 = PostDetails(generate_id('posts'), store_1, item2, item2.get_pr_description(), item2.get_pr_name())
root.posts[post2.get_id()] = post2

post3 = PostDetails(generate_id('posts'), store_1, item3, item3.get_pr_description(), item3.get_pr_name())
root.posts[post3.get_id()] = post3

post4 = PostDetails(generate_id('posts'), store_1, item4, item4.get_pr_description(), item4.get_pr_name())
root.posts[post4.get_id()] = post4

post5 = PostDetails(generate_id('posts'), store_1, item5, item5.get_pr_description(), item5.get_pr_name())
root.posts[post5.get_id()] = post5

post6 = PostDetails(generate_id('posts'), store_2, item6, item6.get_pr_description(), item6.get_pr_name())
root.posts[post6.get_id()] = post6

post7 = PostDetails(generate_id('posts'), store_2, item7, item7.get_pr_description(), item7.get_pr_name())
root.posts[post7.get_id()] = post7

post8 = PostDetails(generate_id('posts'), store_2, item8, item8.get_pr_description(), item8.get_pr_name())
root.posts[post8.get_id()] = post8

post9 = PostDetails(generate_id('posts'), store_2, item9, item9.get_pr_description(), item9.get_pr_name())
root.posts[post9.get_id()] = post9

post10 = PostDetails(generate_id('posts'), store_2, item10, item10.get_pr_description(), item10.get_pr_name())
root.posts[post10.get_id()] = post10

post11 = PostDetails(generate_id('posts'), store_3, item11, item11.get_pr_description(), item11.get_pr_name())
root.posts[post11.get_id()] = post11

post12 = PostDetails(generate_id('posts'), store_3, item12, item12.get_pr_description(), item12.get_pr_name())
root.posts[post12.get_id()] = post3

post13 = PostDetails(generate_id('posts'), store_3, item13, item13.get_pr_description(), item13.get_pr_name())
root.posts[post13.get_id()] = post13

post14 = PostDetails(generate_id('posts'), store_3, item14, item14.get_pr_description(), item14.get_pr_name())
root.posts[post14.get_id()] = post14

post15 = PostDetails(generate_id('posts'), store_3, item15, item15.get_pr_description(), item15.get_pr_name())
root.posts[post15.get_id()] = post15

post16 = PostDetails(generate_id('posts'), store_4, item16, item16.get_pr_description(), item16.get_pr_name())
root.posts[post16.get_id()] = post16

post17 = PostDetails(generate_id('posts'), store_4, item17, item17.get_pr_description(), item17.get_pr_name())
root.posts[post17.get_id()] = post17

post18 = PostDetails(generate_id('posts'), store_4, item18, item18.get_pr_description(), item18.get_pr_name())
root.posts[post18.get_id()] = post18

post19 = PostDetails(generate_id('posts'), store_4, item19, item19.get_pr_description(), item19.get_pr_name())
root.posts[post19.get_id()] = post19

post20 = PostDetails(generate_id('posts'), store_4, item20, item20.get_pr_description(), item20.get_pr_name())
root.posts[post14.get_id()] = post14

post21 = PostDetails(generate_id('posts'), store_5, item21, item21.get_pr_description(), item21.get_pr_name())
root.posts[post21.get_id()] = post21

post22 = PostDetails(generate_id('posts'), store_5, item22, item22.get_pr_description(), item22.get_pr_name())
root.posts[post22.get_id()] = post22

post23 = PostDetails(generate_id('posts'), store_5, item23, item23.get_pr_description(), item23.get_pr_name())
root.posts[post23.get_id()] = post23

# order history appear only in admin_1 interface (admin_1 is the buyer)

order1 = Order(generate_id('orders'), item1, admin_1.get_username(), user_1.get_username())
root.orders[order1.get_order_id()] = order1

order2 = Order(generate_id('orders'), item2, admin_1.get_username(), user_1.get_username(), status="shipping")
root.orders[order2.get_order_id()] = order2

order3 = Order(generate_id('orders'), item1, user_1.get_username(), user_1.get_username())
root.orders[order3.get_order_id()] = order3

# order1 = Order(generate_id('orders'), item1, user_2.get_username(), user_1.get_username())
# root.orders[order1.get_order_id()] = order1

# order2 = Order(generate_id('orders'), item2, user_2.get_username(), user_1.get_username(), status="shipping")
# root.orders[order2.get_order_id()] = order2

# order3 = Order(generate_id('orders'), item3, user_3.get_username(), user_1.get_username())
# root.orders[order3.get_order_id()] = order3

order4 = Order(generate_id('orders'), item4, user_3.get_username(), user_1.get_username())
root.orders[order4.get_order_id()] = order4

order5 = Order(generate_id('orders'), item5, user_4.get_username(), user_1.get_username())
root.orders[order5.get_order_id()] = order5

order6 = Order(generate_id('orders'), item6, user_4.get_username(), user_2.get_username())
root.orders[order6.get_order_id()] = order6

order7 = Order(generate_id('orders'), item6, user_5.get_username(), user_2.get_username())
root.orders[order7.get_order_id()] = order7

order8 = Order(generate_id('orders'), item6, user_5.get_username(), user_2.get_username())
root.orders[order8.get_order_id()] = order8

order9 = Order(generate_id('orders'), item7, user_5.get_username(), user_2.get_username())
root.orders[order9.get_order_id()] = order9

order10 = Order(generate_id('orders'), item10, user_5.get_username(), user_2.get_username())
root.orders[order10.get_order_id()] = order10

order11 = Order(generate_id('orders'), item9, user_5.get_username(), user_2.get_username())
root.orders[order11.get_order_id()] = order11

#wishlist testing admin_1 only
admin_1.add_wishlist(item1)
admin_1.add_wishlist(item2)
admin_1.add_wishlist(item3)

user_1.add_wishlist(item6)
user_1.add_wishlist(item7)
user_1.add_wishlist(item8)

user_2.add_wishlist(item4)
user_2.add_wishlist(item5)

user_3.add_wishlist(item16)
user_3.add_wishlist(item17)

user_4.add_wishlist(item1)
user_4.add_wishlist(item2)

user_5.add_wishlist(item3)
user_5.add_wishlist(item4)

user_6.add_wishlist(item6)
user_6.add_wishlist(item7)

user_7.add_wishlist(item8)
user_7.add_wishlist(item9)

# #self, store_id, user_name, store_name, email, phone_num, description, picture)
# store_admin = Store(generate_id("stores"), "adminnajaa~~", "Admin Kai kong", "kaikongaddmin1@gmail.com", "000000000", "Admin yark kai kong ka", item1_pics_data)
# # store_admin.collections.append(col1)
# store_admin.items.append(item1)
# root.stores[store_admin.get_id()] = store_admin

transaction.commit()
if  __name__ == "__main__":
    accounts = root.accounts
    for key in accounts:
        accounts[key].print_info()

    products = root.products
    for key in products:
        products[key].print_info()
    
    posts = root.posts
    for key in posts:
        posts[key].print_info()

    tags = root.tags
    for key in tags:
        print(key)
        tags[key].print_info()
    
    # for key in tags:
    if "cute" in tags:
        print("CUTE YES")
    else: print("CUTE NO")

    # orders = root.orders
    # for key in orders:
    #     orders[key].print_info()

    order_details = root.orders
    new_order_details = []
    for order_detail in order_details:
        if order_details[order_detail].get_buyer() == 'User1':
            new_order_details.append(order_details[order_detail])
            print(order_details[order_detail].serialize())
    orders_data = [order.serialize() for order in new_order_details] 
    print("ADMIN ORDER") 
    print(orders_data)
    
    stores = root.stores 
    for key in stores:
        stores[key].print_info()
    

    # print("Check whether create a store yet")
    # stores = root.stores
    # for key in stores:
    #     if stores[key].store_user_name == "adminnajaa~~":
    #         print({'success' : True, 'exists' : True})
    #     else: print({'success' : True, 'exists' : False})
    


        
    