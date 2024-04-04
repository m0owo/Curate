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
        print(f'post_id {details.get("post_id")}\n')
        self.p_type = details.get('product_type')
        self.product = details.get('product')
        if details.get('product_type').lower() == 'collection':
            self.items = []
        elif details.get('product_type').lower() == 'collection':
            self.items = [ItemUI(item) for item in self.product.get('items')]
        self.product_name = details.get('title')
        self.s_type = details.get('sales_type')
        self.tags = details.get('tags')
        self.start = self.product.get('start')
        self.info = details.get('info')
        self.images = []
        for image_data in self.product.get('images'):
            image = QImage.fromData(image_data)
            self.images.append(image)

        self.set_image(self.images[0])

        info_font = QFont()
        info_font.setFamily("Manrope")
        info_font.setPointSize(13)
        info_font.setBold(True)

        # making the name label
        self.ui.label_2.setText(self.p_type)
        self.ui.name_label.setText(self.product_name)

        # making the path label
        path_layout = QHBoxLayout(self.ui.path_label)
        self.ui.path_label.setText('')
        path_layout.setAlignment(Qt.AlignLeft)
        path_layout.setSpacing(0)

        path_font = QFont()
        path_font.setFamily("Manrope")
        path_font.setPointSize(20)
        path_font.setBold(True)
        for x in path:
            path_source = PathSource(x[0], x[1], self).get_path_source()
            path_source.setStyleSheet('color: #8C237C;')
            path_source.setFont(path_font)
            path_layout.addWidget(path_source)
            set_preferred_size(path_source)
            divider = PathDivider().get_divider()
            set_preferred_size(divider)
            divider.setFont(path_font)

            path_layout.addWidget(divider)
            # self.ui.path_label.setStyleSheet('border: 1px solid black;') #to check box
        path_source = PathSource(self.product_name, self.stacked_widget.currentIndex(), self).get_path_source()
        path_source.setStyleSheet('color: #8C237C;')
        path_source.setFont(path_font)
        path_layout.addWidget(path_source)
        set_preferred_size(path_source)
        path_layout.addWidget(path_source)

        # tags frame
        self.ui.tags_frame_widget.setMinimumSize(QSize(610, 50))
        self.ui.tags_frame_widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.ui.tags_frame_widget.setLayout(self.ui.tags_frame_layout)
        self.ui.tags_frame_layout.setSpacing(10)
        
        self.ui.tags_frame.setMinimumSize(QSize(610, 50))
        self.ui.tags_frame.setMaximumSize(QSize(610, 100))
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
        
        # Info Section
        # self.ui.frame_3.setStyleSheet(f'border:1px solid black;')
        self.add_info_widget('Product Type:', self.ui.product_type_layout, info_font)
        info_font.setPointSize(12)
        info_font.setBold(False)
        self.add_info_widget(self.p_type, self.ui.product_type_layout, info_font)
        self.add_info_widget(self.s_type, self.ui.mode_layout, info_font)
        self.add_info_widget(self.start.strftime('%B %d, %y @ %I:%M %p'), self.ui.live_date_layout, info_font)
        self.add_info_widget(self.info, self.ui.description_layout, info_font)
        self.ui.description_label = set_preferred_size(self.ui.description_label)

    def add_info_widget(self, info, layout, font):
        w = QLabel(info)
        w.setFont(font)
        layout.addWidget(set_preferred_size(w, 20, 7))
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
        print('path clicked')
    def to_profile(self):
        self.stacked_widget.setCurrentIndex(3)
    def to_history(self):
        self.stacked_widget.setCurrentIndex(5)
    def to_wishlist(self):
        self.stacked_widget.setCurrentIndex(6)
    def to_home(self):
        self.stacked_widget.setCurrentIndex(1)

class ItemUI(CollectionUI):
    def __init__(self, item_details):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    collection_ui = CollectionUI()
    collection_ui.show()
    sys.exit(app.exec())
