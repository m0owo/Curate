import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from .home_ui import Ui_MainWindow

sys.path.append(r'/Users/musicauyeung/Documents/KMITL/Year 2/Curate')
from backend import *

# from .icons_rc import *
# from .logo_rc import *
# from .post_images_rc import *

class TagButton():
    def __init__(self, text, container, tag = None):
        if tag:
            self.tag_text = tag.get_tag_text()
            self.get_link = tag.get_link()
        self.temp_text = text #i cant pass Tag object yet so this is just the text
        self.container = container
    
        self.tag_button = QPushButton(self.container)
        self.tag_button.setText(self.temp_text)
        self.tag_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    def get_drawing(self):
        return self.tag_button

class CollectionPost():
    pass

class ItemPost():
    pass

class HomeUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
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
        self.ui.tags_frame.setLayout(self.tags_layout)
        while self.ui.tags_frame.layout().count():
            widget = self.ui.tags_frame.layout().takeAt(0).widget()
            if widget:
                widget.deleteLater()

        #in reality, use Tag objects from database
        pop_tags = {"Coquette Fashion", "Crochet", "Y2K", "Summer Outfit", "Jewelry"}
        for pop_tag in pop_tags:
            tag_button = TagButton(pop_tag, self.ui.tags_frame)
            self.tags_layout.addWidget(tag_button.get_drawing())
        # Post
        # pop_posts = {}
if __name__ == "__main__":
    app = QApplication(sys.argv)
    home_ui = HomeUI()
    home_ui.show()
    sys.exit(app.exec())
