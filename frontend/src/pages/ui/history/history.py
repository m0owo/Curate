import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from .history_ui import *

class HistoryUI(QMainWindow):
    def __init__(self, stacked_widget):
        QMainWindow.__init__(self, None)
        self.stacked_widget = stacked_widget
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.home_button.clicked.connect(self.to_home_page)
        self.ui.wishlist_button.clicked.connect(self.to_wishlist_page)
        self.ui.profile_button.clicked.connect(self.to_profile_page)

    def to_home_page(self):
        self.stacked_widget.setCurrentIndex(1)
    def to_profile_page(self):
        self.stacked_widget.setCurrentIndex(3)
    def to_wishlist_page(self):
        self.stacked_widget.setCurrentIndex(6)

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    history_ui = HistoryUI()
    history_ui.show()
    sys.exit(app.exec())