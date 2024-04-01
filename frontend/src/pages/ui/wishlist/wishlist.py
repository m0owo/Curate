import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from .wishlist_ui import *

class WishlistUI(QMainWindow):
    def __init__(self, stacked_widget):
        QMainWindow.__init__(self, None)
        self.stacked_widget = stacked_widget
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wishlist_ui = WishlistUI()
    wishlist_ui.show()
    sys.exit(app.exec())