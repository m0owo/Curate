import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from .home_ui import Ui_MainWindow

class HomeUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    home_ui = HomeUI(None)
    home_ui.show()
    sys.exit(app.exec())