import sys
from PySide6.QtWidgets import QApplication, QStackedWidget

# Import your custom UI classes
from pages.ui.home.home import HomeUI
from pages.ui.login.login import LoginUI
from pages.ui.register.register import RegisterUI
from pages.ui.profile.profile import ProfileUI, ProfileAddressUI
from pages.ui.history.history import HistoryUI
from pages.ui.wishlist.wishlist import WishlistUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    
    server_host = 'localhost'
    server_port = 8888

    login_ui = LoginUI(widget,server_host, server_port)
    home_ui = HomeUI(widget)
    register_ui = RegisterUI(server_host, server_port)
    profile_ui = ProfileUI(widget,server_host, server_port, user_id = None)
    profileaddress_ui = ProfileAddressUI(widget)
    history_ui = HistoryUI(widget)
    wishlist_ui = WishlistUI(widget)
    
    login_ui.login_successful.connect(home_ui.load_user_data)
    # login_ui.login_successful.connect(profile_ui.load_user_data)

    # widget.addWidget(login_ui)
    widget.addWidget(home_ui)
    widget.addWidget(register_ui)
    widget.addWidget(profile_ui)
    widget.addWidget(profileaddress_ui)
    widget.addWidget(history_ui)
    widget.addWidget(wishlist_ui)

    widget.show()

    sys.exit(app.exec())
