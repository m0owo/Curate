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

# # creating a smaller version of the image
# def create_thumbnail(image_path, thumbnail_size=(230, 230)):
#     try:
#         with Image.open(image_path) as img:
#             img.thumbnail(thumbnail_size)
#             thumbnail_data = BytesIO()
#             img.save(thumbnail_data, format='JPEG')
#             thumbnail_data.seek(0)
#             return thumbnail_data.getvalue()
#     except IOError:
#         print("Unable to create thumbnail.")
# #getting thumbnail image data
# def get_image_data(images_name):
#     full_image_path = images_path_ms + images_name
#     thumbnail_data = create_thumbnail(full_image_path)
#     return thumbnail_data

# getting webP image data
def get_webp_data(image_name):
    full_image_path = images_path_k + image_name
    try:
        with Image.open(full_image_path) as img:
            webp_data = io.BytesIO()
            img.save(webp_data, format='WEBP')
            return webp_data.getvalue()
    except IOError:
        print(f'Unable to convert {full_image_path} to WebP format')

def get_webp_datas(images_arr):
    return [get_webp_data(x) for x in images_arr]

# getting original image data
def get_image_data(images_name):
    full_image_path = images_path_ms + images_name
    original_data = open(full_image_path, 'rb').read()
    return original_data

def get_image_datas(images_arr):
    return [get_image_data(x) for x in images_arr]

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
    def __init__(self, pr_id, seller, start, pr_name = "", images = [], tags = [], end = None):
        self.pr_id = pr_id
        self.pr_name = pr_name
        self.seller = seller
        if datetime.now() >= start: #upcoming, live, sold out = when stock is zero
            self.status = "live"
        else:
            self.status = "upcoming"
        self.created = datetime.now() #date post created
        self.modified = self.created #default modified date is date created
        self.start_date = start #time to go live
        self.end_date = end #Date object for time sold
        self.images = persistent.list.PersistentList()
        for image in images:
            self.images.append(image)
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
    def serialize(self):
        return {
            'product_id': self.pr_id,
            'product_name': self.pr_name,
            'seller': self.seller,
            'status': self.status,
            'created': self.created,
            'modified': self.modified,
            'start': self.start_date,
            'end': self.end_date,
            'images' : self.images,
            'tags': [tag.serialize() for tag in self.tags] 
        }
        
#collection of items in a post, items would be persistent list in real??
class Collection(Product):
    def __init__(self, c_id, seller, start, items, c_name = "", images = [], tags = [], end = None):
        super().__init__(c_id, seller, start, c_name, images, tags, end)
        self.items = persistent.list.PersistentList() #Item objects in the collection
        for i in items:
            self.items.append(i)
            for t in i.get_tags():
                self.tags.append(t)
        not_sold_out = any(item.get_status() != 'sold out' for item in self.items)
        if not not_sold_out:
            self.status = 'sold out'
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
    def __init__(self, i_id, seller, start, price, stock, i_name = "", images = [], tags = [], end = None):
        super().__init__(i_id, seller, start, i_name, images, tags, end)
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
        self.author = p_author
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
            f'post author: {self.author}\n',
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
            'post_author': self.author, #username of the author
            'product': self.product.serialize(), #one product, either a collection or an item
            'info': self.info, #post info or description
            'title': self.title, #post title, display will be bold
            'created': self.created, #date created
            'modified': self.modified, #date last modified
            'product_type': self.product_type, #tells whether the product is item/col
            'tags': [x.serialize() for x in self.tags], #list of tags
            'sales_type': self.sales_type, #cf no cc, bidding
            'status': self.status
        }

class Order(persistent.Persistent):
    def __init__(self, order_id, product, buyer, seller, status="unpaid"):
        self.order_id = order_id
        self.product = product
        self.buyer = buyer
        self.seller = seller
        self.order_date = datetime.now() #date order created
        self.status = status

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
        }
        serialized_data.update(self.product.serialize())

        return serialized_data
    


class Account(persistent.Persistent):
    def __init__(self, id, email, password, username = "", sex = ""):
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

    def print_info(self):
        serialized_addresses = [address.serialize() for address in self.addresses]
        print(f'----User Info---\nEmail: {self.email}\n'
              f'Password: {self.password}\n'
              f'Username: {self.username}\n'
              f'Adderres: {serialized_addresses}')


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
            'wishlist': serialized_products
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
    def __init__(self, user_name, store_name, email, phone_num, description, picture):
        self.user_name = user_name
        self.store_name = store_name
        self.email = email
        self.phone_num = phone_num
        self.description = description
        self.picture = self.picture
        self.items = persistent.list.PersistentList()
        self.collections = persistent.list.PersistentList()
        
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

user_2 = Account(generate_id('accounts'), "user2@gmail.com", "1234")
user_2.set_username("iammuser2")
root.accounts[user_2.get_username()] = user_2

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
item1_pics_data = get_webp_datas(item1_pics)
# print(f'pofiasjldfjsd {len(item1_pics_data[0])}')
# item1_pics_data2 = [get_image_data(x) for x in item1_pics]
# print(f'pofiasjldfjsd {len(item1_pics_data2[0])}')
item1_tags = [root.tags['coquette'], root.tags['cute']]
item1 = Item(generate_id("products"), user_1.get_username(), datetime(2024, 5, 20, 10, 15),
             50, 5, "item 1", item1_pics_data, item1_tags)
root.products[item1.get_seller() + item1.get_id()] = item1

item2_pics = ['IMG_7370.jpg']
item2_pics_data = get_webp_datas(item2_pics)
item2_tags = [root.tags['coquette'], root.tags['cute']]
item2 = Item(generate_id("products"), user_1.get_username(), datetime(2024, 5, 20, 10, 15),
             100, 3, "item 2 laa", item2_pics_data, item2_tags)
root.products[item2.get_seller() + item2.get_id()] = item2

item3_pics = ['IMG_7102.jpg']
item3_pics_data = get_webp_datas(item3_pics)
item3_tags = [root.tags['secondhand'], root.tags['fashion'], root.tags['cottagecore']]
item3 = Item(generate_id('products'), user_2.get_username(),
             datetime(2024, 5, 21, 15, 20), 150, 10, 'Mona Top',
             item3_pics_data, item3_tags)
root.products[item3.get_seller() + item3.get_id()] = item3

item4_pics = ['IMG_7105.jpg']
item4_pics_data = get_webp_datas(item4_pics)
item4_tags = [root.tags['custom'], root.tags['handmade'], root.tags['cottagecore']]
item4 = Item(generate_id('products'), user_2.get_username(),
             datetime(2024, 5, 22, 19, 30), 350, 5, "Crocheted Beanies",
             item4_pics_data, item4_tags)
root.products[item4.get_seller() + item4.get_id()] = item4

item5_pics = ['IMG_7106.jpg']
item5_pics_data = get_webp_datas(item5_pics)
item5_tags = [root.tags['keychains'], root.tags['handmade'], root.tags['jellyfish']]
item5 = Item(generate_id('products'), user_1.get_username(),
             datetime(2024, 5, 24, 19, 30), 75, 4, "Jellyfish Keychains",
             item5_pics_data, item5_tags)
root.products[item5.get_seller() + item4.get_id()] = item5

col1_pics = ['IMG_7368.jpg']
col1_pics_data = [get_webp_data(x) for x in col1_pics]
col1_tags = [root.tags['secondhand'], root.tags['coquette'], root.tags['cute']]
col1 = Collection(generate_id("products"), user_1.get_username(), datetime(2024, 5, 20, 10, 15),
                  [item1, item2], "~New Drop OOEE~", col1_pics_data, col1_tags)
root.products[col1.get_seller() + col1.get_id()] = col1

post1 = PostDetails(generate_id('posts'), user_1.get_username(), col1, "TEST INFO", "TEST TITLE")
root.posts[post1.get_id()] = post1

post2 = PostDetails(generate_id('posts'), item3.get_seller(), item3, "haleisfls", "Mona Tops Post")
root.posts[post2.get_id()] = post2
post3 = PostDetails(generate_id('posts'), item4.get_seller(), item4, "smata baby smata im smata", "Crocheted Beanies")
root.posts[post3.get_id()] = post3

post4 = PostDetails(generate_id('posts'), item5.get_seller(), item5, "boongboongboong", "Jellyfish Keychains")
root.posts[post4.get_id()] = post4


# order history appear only in admin_1 interface (admin_1 is the buyer)
order1 = Order(generate_id('orders'), item1, admin_1.get_username(), user_1.get_username())
root.orders[order1.get_order_id()] = order1

order2 = Order(generate_id('orders'), item2, admin_1.get_username(), user_1.get_username(), status="shipping")
root.orders[order2.get_order_id()] = order2

#wishlist testing admin_1 only
admin_1.add_wishlist(item1)
admin_1.add_wishlist(item2)
admin_1.add_wishlist(item3)

transaction.commit()
if  __name__ == "__main__":
    accounts = root.accounts
    for key in accounts:
        accounts[key].print_info()

    # products = root.products
    # for key in products:
    #     products[key].print_info()
    
    posts = root.posts
    for key in posts:
        posts[key].print_info()

    tags = root.tags
    for key in tags:
        tags[key].print_info()

    orders = root.orders
    for key in orders:
        orders[key].print_info()

    order_details = root.orders
    new_order_details = []
    for order_detail in order_details:
        if order_details[order_detail].buyer == "adminnajaa~~":
            new_order_details.append(order_details[order_detail])
    orders_data = [order.serialize() for order in new_order_details]   
    print(orders_data)
    
    