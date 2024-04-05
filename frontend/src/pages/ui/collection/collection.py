import sys
import os
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from .collection_ui import *

current_directory = os.getcwd()
sys.path.append(current_directory)

from frontend.src.pages.ui.common import *

class CollectionUI(QMainWindow):
    def __init__(self, stacked_widget, server_host, server_port):
        QMainWindow.__init__(self, None)
        self.stacked_widget = stacked_widget
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.stacked_products = QStackedWidget()
        self.server_host = server_host
        self.server_port = server_port

        button_stylesheet = (
            "QPushButton {"
            "   border-radius: 5px;"
            "   padding: 10px;"
            "   background-color: #fff;"
            "}"
            "QPushButton:hover {"
            "   background-color: #eee;"
            "}"
        )
        self.ui.home_button.setStyleSheet(button_stylesheet)
        self.ui.profile_button.setStyleSheet(button_stylesheet)
        self.ui.wishlist_button.setStyleSheet(button_stylesheet)
        self.ui.history_button.setStyleSheet(button_stylesheet)

        filter_stylesheet = (
            "QPushButton {"
            "   border-radius: 20px;"
            "   background-color: #fff;"
            "}"
            "QPushButton{"
            "   background-color: transparent;"
            "}"
            "QPushButton::icon:hover { color: rgb(255, 231, 204); }"
        )
        self.ui.filter_button.setStyleSheet(filter_stylesheet)

        self.ui.profile_button.clicked.connect(self.to_profile)
        self.ui.history_button.clicked.connect(self.to_history)
        self.ui.wishlist_button.clicked.connect(self.to_wishlist)
        self.ui.home_button.clicked.connect(self.to_home)

    def load_post_data(self, details, path):
        # getting info from home ui's signal
        # keep items in a list so its just a list of one item for Item obj
        
        # self.stacked_products.insertWidget(0, self)
        index = 1
        self.p_type = details.get('product_type')
        self.product = details.get('product')

        if details.get('product_type').lower() == 'item':
            self.items = [self.product] # current showing page
        elif details.get('product_type').lower() == 'collection':
            self.items = self.product.get('items')
            for item in self.items:
                self.stacked_products.addWidget(ItemUI(self.stacked_widget, self.server_host,
                                                       self.server_port, item,
                                                       self.stacked_products, index, path))
                print(f'adding item {item.get("product_id")}')
                index += 1

        self.product_name = details.get('title')

        self.path = [path, [self.product_name, self.stacked_products, 0]]
        self.s_type = details.get('sales_type')
        self.tags = details.get('tags')
        self.start = self.product.get('start')
        self.info = details.get('info')

        #convert image binary data to usable image
        self.images = []
        for image_data in self.product.get('images'):
            image = QImage.fromData(image_data)
            self.images.append(image)
        #use the first image as cover
        self.set_image(self.images[0])

        #font to be used for info
        info_font = QFont()
        info_font.setFamily("Manrope")
        info_font.setPointSize(13)
        info_font.setBold(True)

        # making the name label
        self.ui.label_2.setText(self.p_type)
        self.ui.name_label.setText(self.product_name)

        # making the path label
        path_font = QFont()
        path_font.setFamily("Manrope")
        path_font.setPointSize(20)
        path_font.setBold(True)

        clear_widget(self.ui.path_widget)
        self.path_label = QLabel(self.ui.path_widget)
        self.ui.path_widget_layout.addWidget(self.path_label)
        self.ui.path_widget_layout.setContentsMargins(0, 0, 0, 0)
        # self.path_label.setText('TESt')
        self.path_label.setGeometry(QRect(60, 110, 591, 61))
        self.path_label.setFont(path_font)
        self.path_label.setStyleSheet("color: #8C237C;\n")
        path_layout = QHBoxLayout(self.path_label)
        self.path_label.setLayout(path_layout)
        path_layout.setAlignment(Qt.AlignLeft)
        path_layout.setSpacing(0)
        print(f'path {path}')

        for x in path:
            # PathSource(source name, stack, stack_index, collection_ui) returns a Clickable Label
            path_source = PathSource(x[0], x[1], x[2], self).get_path_source()
            path_source.setStyleSheet('color: #8C237C;')
            path_source.setFont(path_font)
            path_layout.addWidget(path_source)
            set_preferred_size(path_source)

            # the > between paths
            divider = PathDivider().get_divider()
            set_preferred_size(divider)
            divider.setFont(path_font)
            path_layout.addWidget(divider)
            # self.ui.path_label.setStyleSheet('border: 1px solid black;') #to check box

        # path to current page
        path_source = PathSource(self.product_name, self.stacked_products, 1, self).get_path_source()
        path_source.setFont(path_font)
        path_layout.addWidget(path_source)
        set_preferred_size(path_source)

        # tags frame for this post
        self.ui.tags_frame_widget.setFixedSize(QSize(600, 50))
        self.ui.tags_frame_widget.setLayout(self.ui.tags_frame_layout)
        self.ui.tags_frame_layout.setSpacing(10)
        self.ui.tags_frame.setMinimumSize(QSize(600, 50))
        self.ui.tags_frame.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.populate_tags()
        
        # Info Section
        self.ui.label_5.setText("Product Information")
        self.ui.frame_3.setStyleSheet(f'border:1px solid black;')
        self.ui.product_type_label_label.setText("Product Type:")
        self.ui.product_type_label_label.setFont(info_font)

        self.ui.mode_label_label.setText("Sales Type:")
        self.ui.mode_label_label.setFont(info_font)

        self.ui.date_label_label.setText("Scheduled For:")
        self.ui.date_label_label.setFont(info_font)

        self.ui.description_label_label.setText("Description:")
        self.ui.description_label_label.setFont(info_font)

        info_font.setPointSize(12)
        info_font.setBold(False)
        self.ui.product_type_label.setText(self.p_type)
        self.ui.product_type_label.setFont(info_font)

        self.ui.mode_label.setText(self.s_type)
        self.ui.mode_label.setFont(info_font)

        self.ui.date_label.setText(self.start.strftime('%B %d, %y @ %I:%M %p'))
        self.ui.date_label.setFont(info_font)

        self.ui.description_label.setText(self.info)
        self.ui.description_label.setFont(info_font)

        # Buttons
        self.ui.horizontalLayout_3.addWidget(self.ui.add_to_wishlist_bt)

        self.ui.horizontalLayout_3.addWidget(self.ui.view_products_bt)

        self.ui.horizontalLayout_3.addWidget(self.ui.go_to_item)
        self.ui.go_to_item.clicked.connect(self.to_stacked_products())
    
    def populate_tags(self):
        # calculate the total width of all tags plus padding to get how many rows needed
        i = 0
        total_width = 0
        for tag in self.tags:
            tag_button = BigPostTagButton(tag.get('tag_text'))
            total_width += set_preferred_size(tag_button.get_tag_button()).size().width()
            total_width += (5 * len(self.tags))
        clear_widget(self.ui.tags_frame_widget)
        # if total_width > self.ui.tags_frame.viewport().size().width():
        #     print("Horizontal overflow detected")
        #     print(f'total width: {total_width}\n {self.ui.tags_frame.viewport().size().width()}')
        num_columns = self.ui.tags_frame.viewport().size().width() // 100
        for tag in self.tags:
            tag_button = BigPostTagButton(tag.get('tag_text'), self.ui.tags_frame_widget)
            row = i // num_columns
            column = i % num_columns
            self.ui.tags_frame_layout.addWidget(set_preferred_size(tag_button.get_tag_button()), row, column, alignment=Qt.AlignTop)
            i += 1
        spacers_needed = num_columns - (len(self.tags) % num_columns)
        for _ in range(spacers_needed):
            row = i // num_columns
            column = i % num_columns
            self.ui.tags_frame_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum), row, column)
            i += 1
    
    def add_info_widget(self, info, layout, font):
        w = QLabel(info)
        w.setFont(font)
        layout.addWidget(set_preferred_size(w, 20, 12))
        return w
    
    def set_image(self, image):
        pic = QPixmap(image)
        scaled_pic = pic.scaled(self.ui.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.image_label.setPixmap(scaled_pic)

    def load_user_data(self, user_id, user_data):
        self.user_id = user_id
        self.user_data = user_data
        print('Received userdata and userid')
    
    def handle_path_click(self, path_source):
        print(f'\n{path_source.get_name()} clicked')
        print(f'{path_source.get_stacked_widget()}')
        print(f'{path_source.get_stacked_index()}\n')
        stacked_widget = path_source.get_stacked_widget()
        index = path_source.get_stacked_index()
        stacked_widget.setCurrentIndex(index)

    def to_profile(self):
        self.stacked_widget.setCurrentIndex(3)
    def to_history(self):
        self.stacked_widget.setCurrentIndex(5)
    def to_wishlist(self):
        self.stacked_widget.setCurrentIndex(6)
    def to_home(self):
        self.stacked_widget.setCurrentIndex(1)
    
    def to_stacked_products(self):
        print('go to items')
        self.stacked_products.show()
        self.stacked_products.setCurrentIndex(2)

class ItemUI(QMainWindow):
    # has the details of the item, has the container of the item, and the path to the item
    def __init__(self, stacked_widget, server_host, server_port, details, stacked_container, index, path):
        QMainWindow.__init__(self, None)
        # init ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.stacked_container = stacked_container # the stack im in
        self.index = index # the index im at
        self.stacked_widget = stacked_widget
        self.server_host = server_host
        self.server_port = server_port

        # nav bar
        button_stylesheet = (
            "QPushButton {"
            "   border-radius: 5px;"
            "   padding: 10px;"
            "   background-color: #fff;"
            "}"
            "QPushButton:hover {"
            "   background-color: #eee;"
            "}"
        )
        self.ui.home_button.setStyleSheet(button_stylesheet)
        self.ui.profile_button.setStyleSheet(button_stylesheet)
        self.ui.wishlist_button.setStyleSheet(button_stylesheet)
        self.ui.history_button.setStyleSheet(button_stylesheet)

        filter_stylesheet = (
            "QPushButton {"
            "   border-radius: 20px;"
            "   background-color: #fff;"
            "}"
            "QPushButton{"
            "   background-color: transparent;"
            "}"
            "QPushButton::icon:hover { color: rgb(255, 231, 204); }"
        )
        self.ui.filter_button.setStyleSheet(filter_stylesheet)
        self.ui.profile_button.clicked.connect(self.to_profile)
        self.ui.history_button.clicked.connect(self.to_history)
        self.ui.wishlist_button.clicked.connect(self.to_wishlist)
        self.ui.home_button.clicked.connect(self.to_home)

        # getting data from parameters
        self.p_type = 'item'
        self.product_name = details.get('title')
        print(self.product_name)
        self.path = [path, [self.product_name, self.stacked_container, self.index]]
        self.s_type = details.get('sales_type')
        self.tags = details.get('tags')
        self.start = details.get('start')
        self.info = details.get('info')

        self.images = []
        for image_data in details.get('images'):
            image = QImage.fromData(image_data)
            self.images.append(image)
        self.set_image(self.images[0])

        info_font = QFont()
        info_font.setFamily("Manrope")
        info_font.setPointSize(13)
        info_font.setBold(True)
        
        self.ui.label_2.setText(self.p_type)
        self.ui.name_label.setText(self.product_name)
        self.ui.verticalLayout.addWidget(self.ui.label_2)
        self.ui.verticalLayout.addWidget(self.ui.name_label)

        path_font = QFont()
        path_font.setFamily("Manrope")
        path_font.setPointSize(20)
        path_font.setBold(True)

        clear_widget(self.ui.path_widget)
        self.path_label = QLabel(self.ui.path_widget)
        self.ui.path_widget_layout.addWidget(self.path_label)
        self.ui.path_widget_layout.setContentsMargins(0, 0, 0, 0)
        # self.path_label.setText('TESt')
        self.path_label.setGeometry(QRect(60, 110, 591, 61))
        self.path_label.setFont(path_font)
        self.path_label.setStyleSheet("color: #8C237C;\n")
        path_layout = QHBoxLayout(self.path_label)
        self.path_label.setLayout(path_layout)
        path_layout.setAlignment(Qt.AlignLeft)
        path_layout.setSpacing(0)
        print(f'path {path}')

        for x in path:
            # PathSource(source name, stack, stack_index, collection_ui) returns a Clickable Label
            path_source = PathSource(x[0], x[1], x[2], self).get_path_source()
            path_source.setStyleSheet('color: #8C237C;')
            path_source.setFont(path_font)
            path_layout.addWidget(path_source)
            set_preferred_size(path_source)

            # the > between paths
            divider = PathDivider().get_divider()
            set_preferred_size(divider)
            divider.setFont(path_font)
            path_layout.addWidget(divider)
            # self.ui.path_label.setStyleSheet('border: 1px solid black;') #to check box

        # path to current page
        path_source = PathSource(self.product_name, self.stacked_widget, self.stacked_widget.currentIndex(), self).get_path_source()
        path_source.setFont(path_font)
        path_layout.addWidget(path_source)
        set_preferred_size(path_source)

        # tags frame for this post
        self.ui.tags_frame_widget.setFixedSize(QSize(600, 50))
        self.ui.tags_frame_widget.setLayout(self.ui.tags_frame_layout)
        self.ui.tags_frame_layout.setSpacing(10)
        self.ui.tags_frame.setMinimumSize(QSize(600, 50))

        self.populate_tags()

        # Info Section
        clear_widget(self.ui.product_type_layout)
        clear_widget(self.ui.mode_layout)
        clear_widget(self.ui.live_date_layout)
        clear_widget(self.ui.description_layout)

        # self.ui.frame_3.setStyleSheet(f'border:1px solid black;')
        self.add_info_widget('Product Type:', self.ui.product_type_layout, info_font)
        info_font.setPointSize(12)
        info_font.setBold(False)
        self.add_info_widget(self.p_type, self.ui.product_type_layout, info_font)
        self.add_info_widget(self.s_type, self.ui.mode_layout, info_font)
        self.add_info_widget(self.start.strftime('%B %d, %y @ %I:%M %p'), self.ui.live_date_layout, info_font)
        self.add_info_widget(self.info, self.ui.description_layout, info_font)
        self.ui.description_label = set_preferred_size(self.ui.description_label)
        self.ui.description_label.setStyleSheet(f'text-align: center;')

        #Buttons 
        self.ui.horizontalLayout_3.addWidget(self.ui.prev_item_bt)
        self.ui.horizontalLayout_3.addWidget(self.ui.next_item_bt)
        self.ui.horizontalLayout_3.addWidget(self.ui.back_to_col)

    def populate_tags(self):
        # calculate the total width of all tags plus padding to get how many rows needed
        i = 0
        total_width = 0
        for tag in self.tags:
            tag_button = BigPostTagButton(tag.get('tag_text'))
            total_width += set_preferred_size(tag_button.get_tag_button()).size().width()
            total_width += (5 * len(self.tags))
        clear_widget(self.ui.tags_frame_widget)
        if total_width > self.ui.tags_frame.viewport().size().width():
            print("Horizontal overflow detected")
            print(f'total width: {total_width}\n {self.ui.tags_frame.viewport().size().width()}')
        num_columns = self.ui.tags_frame.viewport().size().width() // 100
        for tag in self.tags:
            tag_button = BigPostTagButton(tag.get('tag_text'), self.ui.tags_frame_widget)
            row = i // num_columns
            column = i % num_columns
            self.ui.tags_frame_layout.addWidget(set_preferred_size(tag_button.get_tag_button()), row, column, alignment=Qt.AlignTop)
            i += 1
        spacers_needed = num_columns - (len(self.tags) % num_columns)
        for _ in range(spacers_needed):
            row = i // num_columns
            column = i % num_columns
            self.ui.tags_frame_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum), row, column)
            i += 1
    
    def add_info_widget(self, info, layout, font):
        w = QLabel(info)
        w.setFont(font)
        layout.addWidget(set_preferred_size(w, 20, 7))
        return w
    
    def set_image(self, image):
        pic = QPixmap(image)
        scaled_pic = pic.scaled(self.ui.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.image_label.setPixmap(scaled_pic)
    
    def handle_path_click(self, path_source):
        print(f'{path_source.get_name()} clicked')

    def to_profile(self):
        self.stacked_widget.setCurrentIndex(3)
    def to_history(self):
        self.stacked_widget.setCurrentIndex(5)
    def to_wishlist(self):
        self.stacked_widget.setCurrentIndex(6)
    def to_home(self):
        self.stacked_widget.setCurrentIndex(1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    collection_ui = CollectionUI()
    sys.exit(app.exec())
