import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap
from .home_ui import *

sys.path.append(r'/Users/musicauyeung/Documents/KMITL/Year 2/Curate')
from backend import *
from backend.database import PostDetails

# from .icons_rc import *
# from .logo_rc import *
# from .post_images_rc import *

# def get_button_content_width(button):
#     font_metrics = button.fontMetrics()
#     text_width = font_metrics.horizontalAdvance(button.text())
#     return text_width

class TagButton():
    def __init__(self, text, container, tag = None):
        if tag:
            self.tag_text = tag.get_tag_text()
            self.get_link = tag.get_link()
        self.temp_text = text #i cant pass Tag object yet so this is just the text
        self.container = container

        self.tag_button = QPushButton(self.container)
        self.tag_button.setText(self.temp_text)

        preferred_size = self.tag_button.sizeHint()
        self.tag_button.setFixedWidth(preferred_size.width())
        min_width = self.tag_button.fontMetrics().boundingRect(self.tag_button.text()).width() + 100
        self.tag_button.setMinimumWidth(min_width)

        cur_stylesheet = self.tag_button.styleSheet()
        self.tag_button.setStyleSheet(cur_stylesheet + 
            "QPushButton:hover{background-color:rgb(201, 212, 249); color:rgb(238, 248, 255);}")
    def get_drawing(self):
        return self.tag_button
    def get_tag_button(self):
        return self.tag_button

class PostTagButton(TagButton):
    def __init__(self, text, container, tag = None):
        super().__init__(text, container, tag)

        self.tag_button = QPushButton(self.container)
        self.tag_button.setText(self.temp_text)

        set_preferred_size(self.tag_button, 100)

        cur_stylesheet = self.tag_button.styleSheet()
        self.tag_button.setStyleSheet(cur_stylesheet + 
            "QPushButton:hover{background-color:rgb(201, 212, 249); color:rgb(238, 248, 255);}")

def clear_frame(frame):
        for widget in frame.findChildren(QPushButton):
            widget.deleteLater()
def clear_widget(widget):
    for i in reversed(range(widget.layout().count())):
        widget.layout().itemAt(i).widget().setParent(None)

def set_preferred_size(w, padding = 20, hpadding = 8):
    preferred_size = w.sizeHint()
    w.setFixedWidth(preferred_size.width())
    w.setFixedWidth(preferred_size.height())
    min_width = w.fontMetrics().boundingRect(w.text()).width() + padding
    w.setMinimumWidth(min_width)
    min_height = w.fontMetrics().boundingRect(w.text()).height() + hpadding
    w.setMinimumHeight(min_height)

class Post():
    def __init__(self, details, container):
        if details:
            self.author = details.get_author()
            self.product = details.get_product()
            self.info = details.get_info()
            self.title = details.get_title()
            self.type = details.get_type()
            self.tags = details.get_tags()
            self.created = details.get_created()
            self.modified = details.get_modified()
            self.container = container
 
            post_layout = QVBoxLayout()
            post_layout.setAlignment(Qt.AlignCenter)
            post_layout.setContentsMargins(0, 0, 0, 0)
            self.post = QFrame(self.container)
            self.post.setLayout(post_layout)
            self.post.setFixedSize(QSize(230, 300))
            self.post.setStyleSheet("border: 1px solid black;")
            self.post.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

            self.post_image = QLabel(self.post)
            self.post_image.setFixedSize(QSize(200, 200))
            self.post_image.setPixmap(QPixmap(u":/post_images/IMG_7109.jpg"))
            self.post_image.setScaledContents(True)
            post_layout.addWidget(self.post_image, alignment=Qt.AlignCenter)

            self.post_info = QWidget(self.post)
            post_layout.addWidget(self.post_info)
            post_info_layout = QVBoxLayout()
            self.post_info.setLayout(post_info_layout)
            self.post_info.setMinimumSize(QSize(200, 100))
            self.post_title = QLabel(self.post_info)
            self.post_title.setMinimumSize(QSize(200, 16))
            self.post_title.setStyleSheet(u"QLabel {font: 700 12pt \"Manrope\";}")
            self.post_title.setWordWrap(True)
            self.post_title.setAlignment(Qt.AlignCenter)
            self.post_title.setText("TESTING TITLE")
            post_info_layout.addWidget(self.post_title, alignment=Qt.AlignCenter)

            post_details_layout = QHBoxLayout()
            self.post_details = QWidget(self.post_info)
            self.post_details.setLayout(post_details_layout)
            self.post_details.setMinimumSize(QSize(200, 30))
            self.post_details.setStyleSheet(u"QLabel {font: 400 12pt \"Manrope\";}")
            post_info_layout.addWidget(self.post_details, alignment=Qt.AlignCenter)

            self.post_type = QLabel(self.post_details)
            self.post_type.setText(self.type)
            post_details_layout.addWidget(self.post_type)
            set_preferred_size(self.post_type)

            self.created_date = QLabel(self.post_details)
            self.created_date.setText("Date Created: ")
            post_details_layout.addWidget(self.created_date)

            self.live_date = QLabel(self.post_details)
            self.live_date.setText("Live Date")
            post_details_layout.addWidget(self.live_date)

            post_tags_layout = QHBoxLayout()
            self.post_tags = QWidget(self.post_info)
            self.post_tags.setLayout(post_tags_layout)
            post_info_layout.addWidget(self.post_tags)
            self.post_tags.setStyleSheet(u"QLabel {\n"
                                    "    font: 600 11pt \"Manrope\";\n"
                                    "    color: rgb(137, 153, 211);\n"
                                    "    text-align: center;\n"
                                    "    background-color: #E8F3F2;\n"
                                    "    border-radius: 5px;\n"
                                    "}")
            for tag in self.tags:
                post_tag = QLabel(self.post_tags)
                post_tag.setAlignment(Qt.AlignCenter)
                post_tag.setMargin(1)
                post_tag.setText(tag)
                set_preferred_size(post_tag)
                post_tags_layout.addWidget(post_tag)

            font = QFont()
            font.setFamilies([u"Manrope"])
            font.setPointSize(11)
            font.setBold(True)
            self.post_type.setFont(font)
            self.post_type.setStyleSheet(u"border-radius: 5px; padding:3px;"
                                        "background-color: rgb(255, 245, 225);"
                                        "color:rgb(206, 141, 80);")
            self.post_type.setAlignment(Qt.AlignCenter)
    def get_post(self):
        return self.post
        
class HomeUI(QMainWindow):
    def __init__(self, stacked_widget):
        QMainWindow.__init__(self, None)
        self.stacked_widget = stacked_widget
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(10)
        shadow.setXOffset(1)
        shadow.setYOffset(2)

        self.ui.search_frame.setGraphicsEffect(shadow)
        button_stylesheet = (
            "QPushButton {"
            "   border-radius: 5px;"
            "   padding: 10px;"
            "   background-color: #fff;"
            "   box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.5);"
            "}"
            "QPushButton:hover {"
            "   background-color: #eee;"
            "}"
        )
        filter_stylesheet = (
            "QPushButton {"
            "   border-radius: 20px;"
            "   background-color: #fff;"
            "   box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.5);"
            "}"
            "QPushButton{"
            "   background-color: transparent;"
            "}"
            "QPushButton::icon:hover { color: rgb(255, 231, 204); }"
        )
        self.ui.home_button.setStyleSheet(button_stylesheet)
        self.ui.profile_button.setStyleSheet(button_stylesheet)
        self.ui.wishlist_button.setStyleSheet(button_stylesheet)
        self.ui.history_button.setStyleSheet(button_stylesheet)
        self.ui.filter_button.setStyleSheet(filter_stylesheet)

        self.tags_layout = QHBoxLayout()
        self.tags_layout.setSpacing(1)
        self.ui.tags_frame.setLayout(self.tags_layout)
        clear_frame(self.ui.tags_frame)
        # drawing tags
        # in reality, use Tag objects from database
        pop_tags = {"Crochet", "Y2K", "Summer Outfit", "Bam Yang Gang", "Acubi"}
        for pop_tag in pop_tags:
            tag_button = TagButton(pop_tag, self.ui.tags_frame)
            self.tags_layout.addWidget(tag_button.get_tag_button())
        
        # drawing posts
        clear_widget(self.ui.scrollAreaWidgetContents)
        # Post Details
        test_post = PostDetails("1", "Music", "This is very important", "bananas?", ["Acubi", "Cottagecore"])
        # test_post_ui = Post(test_post, self.ui.scrollAreaWidgetContents)
        # self.ui.scrollAreaWidgetContents.layout().addWidget(test_post_ui.get_post(), 0, 0)
        
        post_details = [test_post] * 14
        post_widgets = []
        i = 0
        self.ui.scrollAreaWidgetContents.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.ui.gridLayout.setSpacing(20)
        for post_data in post_details:
            # Create the Post widget
            post = Post(post_data, self.ui.scrollAreaWidgetContents)
            post_widget = post.get_post()
            post_widgets.append(post_widget)

            # Calculate the row and column indices based on the position in the grid
            row = i // 4
            column = i % 4

            # Add the widget to the grid layout at the calculated row and column indices
            self.ui.gridLayout.addWidget(post_widget, row, column)
            i += 1
            self.ui.scrollAreaWidgetContents.adjustSize()

        self.ui.gridLayout.setAlignment(Qt.AlignTop)
        self.ui.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.ui.scrollAreaWidgetContents.setLayout(self.ui.gridLayout)
    


        self.ui.profile_button.clicked.connect(self.to_profile)

    def to_profile(self):
        self.stacked_widget.setCurrentIndex(3)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    home_ui = HomeUI()
    home_ui.show()
    sys.exit(app.exec())
