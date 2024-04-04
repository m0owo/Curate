import sys
from PySide6.QtWidgets import QApplication, QStackedWidget

# Import your custom UI classes
from pages.ui.home.home import HomeUI
from pages.ui.login.login import LoginUI
from pages.ui.register.register import RegisterUI
from pages.ui.profile.profile import ProfileUI, ProfileAddressUI, AddAddressUI
from pages.ui.history.history import HistoryUI
from pages.ui.wishlist.wishlist import WishlistUI
from pages.ui.collection.collection import CollectionUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    
    server_host = 'localhost'
    server_port = 8888

    login_ui = LoginUI(widget,server_host, server_port)
    home_ui = HomeUI(widget, server_host, server_port)
    register_ui = RegisterUI(server_host, server_port)
    profile_ui = ProfileUI(widget,server_host, server_port)
    history_ui = HistoryUI(widget, server_host, server_port)
    profileaddress_ui = ProfileAddressUI(widget, server_host, server_port)
    wishlist_ui = WishlistUI(widget)
    collection_ui = CollectionUI(widget, server_host, server_port)
    
    # Connect the signal to the slot function   
    login_ui.login_successful.connect(home_ui.load_user_data)
    login_ui.login_successful.connect(profile_ui.load_user_data)
    login_ui.login_successful.connect(history_ui.load_user_data)
    login_ui.login_successful.connect(collection_ui.load_user_data)
    
    home_ui.clicked.connect(collection_ui.load_post_data)


    login_ui.login_successful.connect(profileaddress_ui.load_user_data)
    
    widget.addWidget(login_ui)
    widget.addWidget(home_ui)
    widget.addWidget(register_ui)
    widget.addWidget(profile_ui)
    widget.addWidget(profileaddress_ui)
    widget.addWidget(history_ui)
    widget.addWidget(wishlist_ui)
    widget.addWidget(collection_ui)

    widget.show()

    sys.exit(app.exec())
