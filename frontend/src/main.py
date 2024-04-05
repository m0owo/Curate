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
from pages.ui.store.store import StoreUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    
    server_host = 'localhost'
    server_port = 8888

    login_ui = LoginUI(widget,server_host, server_port)
    home_ui = HomeUI(widget, server_host, server_port)
    register_ui = RegisterUI(widget, server_host, server_port)
    profile_ui = ProfileUI(widget,server_host, server_port)
    history_ui = HistoryUI(widget, server_host, server_port)
    profileaddress_ui = ProfileAddressUI(widget, server_host, server_port)
    wishlist_ui = WishlistUI(widget, server_host, server_port)
    collection_ui = CollectionUI(widget, server_host, server_port)
    store_ui = StoreUI(widget, server_host, server_port)
    
    
    # Connect the signal to the slot function   
    login_ui.login_successful.connect(home_ui.load_user_data)
    # login_ui.login_successful.connect(profile_ui.load_user_data)
    # login_ui.login_successful.connect(history_ui.load_user_data)
    # login_ui.login_successful.connect(wishlist_ui.load_user_data)
    login_ui.login_successful.connect(collection_ui.load_user_data)
    
    home_ui.post_clicked.connect(collection_ui.load_post_data)
    # login_ui.login_successful.connect(profileaddress_ui.load_user_data)
    # login_ui.login_successful.connect(profile_ui.load_user_data)
    # login_ui.login_successful.connect(profile_ui.fetch_check_store_exist)
    # login_ui.login_successful.connect(store_ui.fetch_check_store_exist)

    widget.insertWidget(0, login_ui)
    widget.insertWidget(1, home_ui)
    widget.insertWidget(2, register_ui)
    widget.insertWidget(3, profile_ui)
    widget.insertWidget(4, profileaddress_ui)
    widget.insertWidget(5, history_ui)
    widget.insertWidget(6, wishlist_ui)
    widget.insertWidget(7, collection_ui)
    widget.insertWidget(8, store_ui)

    widget.show()

    sys.exit(app.exec())
