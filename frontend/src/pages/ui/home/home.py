import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from .home_ui import Ui_MainWindow


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
        self.ui.profile_button.clicked.connect(self.to_profile)

    def to_profile(self):
        self.stacked_widget.setCurrentIndex(3)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    home_ui = HomeUI()
    home_ui.show()
    sys.exit(app.exec())
