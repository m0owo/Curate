import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from .collection_ui import *

class CollectionUI(QMainWindow):
    def __init__(self, stacked_widget):
        QMainWindow.__init__(self, None)
        self.stacked_widget = stacked_widget
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    collection_ui = CollectionUI()
    collection_ui.show()
    sys.exit(app.exec())