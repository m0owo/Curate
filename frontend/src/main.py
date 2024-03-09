import sys
from PySide6.QtWidgets import *

# Import your custom UI classes
from pages.ui.home.home import HomeUI
from pages.ui.login.login import LoginUI
from pages.ui.register.register import RegisterUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QStackedWidget()

    login_ui = LoginUI(widget)
    home_ui = HomeUI()
    register_ui = RegisterUI()

    widget.addWidget(login_ui)
    widget.addWidget(home_ui)
    widget.addWidget(register_ui)

    widget.show()
    sys.exit(app.exec())

