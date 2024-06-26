# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'collection.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget, QScrollArea)
from .icons_rc import *
from .logo_rc import *
from .posts_images_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1200, 800))
        MainWindow.setMaximumSize(QSize(1200, 800))
        MainWindow.setStyleSheet(u"#centralwidget {\n"
"    background-color: #FFFFFF;\n"
"}\n"
"\n"
"QFrame {\n"
"    border:  none;\n"
"}\n"
"\n"
"* {\n"
"	color: black;\n"
"}")
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setGeometry(QRect(60, 20, 1080, 91))
        self.header.setMaximumSize(QSize(1080, 720))
        font = QFont()
        font.setFamilies([u".AppleSystemUIFont"])
        self.header.setFont(font)
        self.header.setAutoFillBackground(False)
        self.header.setStyleSheet(u"")
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(120, 10, 921, 71))
        self.frame.setStyleSheet(u"QFrame#search_frame{\n"
"    background-color: #FFFBF3;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#filter_button{\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QPushButton :hover{\n"
"    background-color: #E8F3F2;\n"
"}\n"
"\n"
"QTextEdit#search_edit{\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QLabel#page_label{\n"
"    background-color: #E8F3F2;\n"
"    border-radius: 10px;\n"
"    border: solid;\n"
"    border-width: 1px;\n"
"    border-color:rgb(154, 152, 148)\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.search_frame = QFrame()
        self.search_frame.setObjectName(u"search_frame")
        self.search_frame.setEnabled(True)
        self.search_frame.setGeometry(QRect(130, 20, 581, 30))
        font1 = QFont()
        font1.setFamilies([u"Manrope"])
        self.search_frame.setFont(font1)
        self.search_frame.setStyleSheet(u"QLineEdit{\n"
"    color: rgb(190, 123, 193);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"#search_frame{\n"
"    border: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(154, 152, 148);\n"
"}")
        self.search_frame.setFrameShape(QFrame.StyledPanel)
        self.search_frame.setFrameShadow(QFrame.Raised)
        self.search_icon = QLabel(self.search_frame)
        self.search_icon.setObjectName(u"search_icon")
        self.search_icon.setGeometry(QRect(10, 5, 18, 18))
        self.search_icon.setPixmap(QPixmap(u":/icon_images/search_icon.png"))
        self.search_icon.setScaledContents(True)
        self.filter_button = QPushButton(self.search_frame)
        self.filter_button.setObjectName(u"filter_button")
        self.filter_button.setGeometry(QRect(540, 0, 41, 30))
        icon = QIcon()
        icon.addFile(u":/icon_images/filter_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.filter_button.setIcon(icon)
        self.filter_button.setIconSize(QSize(20, 20))
        self.search_edit = QLineEdit(self.search_frame)
        self.search_edit.setObjectName(u"search_edit")
        self.search_edit.setGeometry(QRect(40, 5, 491, 16))
        self.search_edit.setFont(font1)
        self.home_button = QPushButton(self.frame)
        self.home_button.setObjectName(u"home_button")
        self.home_button.setGeometry(QRect(740, 20, 41, 30))
        font2 = QFont()
        font2.setFamilies([u"Manrope"])
        font2.setBold(True)
        self.home_button.setFont(font2)
        icon1 = QIcon()
        icon1.addFile(u":/icon_images/home_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_button.setIcon(icon1)
        self.home_button.setIconSize(QSize(20, 20))
        self.history_button = QPushButton(self.frame)
        self.history_button.setObjectName(u"history_button")
        self.history_button.setGeometry(QRect(780, 20, 41, 30))
        icon2 = QIcon()
        icon2.addFile(u":/icon_images/history_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.history_button.setIcon(icon2)
        self.history_button.setIconSize(QSize(20, 20))
        self.wishlist_button = QPushButton(self.frame)
        self.wishlist_button.setObjectName(u"wishlist_button")
        self.wishlist_button.setGeometry(QRect(820, 20, 41, 30))
        icon3 = QIcon()
        icon3.addFile(u":/icon_images/wishlist_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.wishlist_button.setIcon(icon3)
        self.wishlist_button.setIconSize(QSize(20, 20))
        self.profile_button = QPushButton(self.frame)
        self.profile_button.setObjectName(u"profile_button")
        self.profile_button.setGeometry(QRect(860, 20, 41, 30))
        icon4 = QIcon()
        icon4.addFile(u":/icon_images/profile_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.profile_button.setIcon(icon4)
        self.profile_button.setIconSize(QSize(20, 20))
        self.page_label = QLabel(self.frame)
        self.page_label.setObjectName(u"page_label")
        self.page_label.setGeometry(QRect(30, 20, 71, 30))
        self.page_label.setFont(font2)
        self.page_label.setAlignment(Qt.AlignCenter)
        self.page_widget = QWidget(self.centralwidget)
        self.page_widget_layout = QHBoxLayout()
        self.page_widget.setLayout(self.page_widget_layout)
        self.frame_2 = QFrame(self.header)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 10, 120, 71))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.curate_label = QLabel(self.frame_2)
        self.curate_label.setObjectName(u"curate_label")
        self.curate_label.setGeometry(QRect(-10, -10, 161, 91))
        font3 = QFont()
        font3.setFamilies([u"Mogena"])
        font3.setPointSize(18)
        self.curate_label.setFont(font3)
        self.curate_label.setPixmap(QPixmap(u":/logos/curatelogo.png"))
        self.curate_label.setScaledContents(True)
        self.curate_label.setAlignment(Qt.AlignCenter)

        font4 = QFont()
        font4.setFamilies([u"Manrope"])
        font4.setPointSize(20)
        font4.setBold(True)
        self.path_widget = QWidget(self.centralwidget)
        self.path_widget.setGeometry(QRect(60, 110, 591, 61))
        self.path_widget.setFont(font4)
        # self.path_widget.setStyleSheet("color: #8C237C;\n border: 1px solid black;")
        self.path_widget_layout = QHBoxLayout(self.path_widget)
        self.product_frame = QFrame(self.centralwidget)
        self.product_frame.setObjectName(u"product_frame")
        self.product_frame.setGeometry(QRect(60, 170, 1080, 420))
        self.product_frame.setMinimumSize(QSize(1080, 420))
        self.product_frame.setMaximumSize(QSize(16777215, 0))
        self.product_frame.setStyleSheet(u"Line {\n"
"	background-color: #CCCCCC;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.product_frame)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, -1, 0)
        self.image_label = QLabel(self.product_frame)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setFixedSize(QSize(400, 400))
        self.image_label.setPixmap(QPixmap(u":/post_images/IMG_7107.jpg"))
        self.image_label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.image_label)

        self.frame_3 = QFrame(self.product_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setStyleSheet("QScrollArea{background-color: transparent;}") #add border here
        self.frame_3.setMaximumHeight(400)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, 0, 0)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMaximumSize(QSize(16777215, 16777215))
        font5 = QFont()
        font5.setFamilies([u"Manrope"])
        font5.setPointSize(14)
        font5.setBold(True)
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"QLabel {\n"
"	color: #8C237C\n"
"}")

        self.verticalLayout.addWidget(self.label_2)

        self.name_label = QLabel(self.frame_3)
        self.name_label.setObjectName(u"name_label")
        sizePolicy1.setHeightForWidth(self.name_label.sizePolicy().hasHeightForWidth())
        self.name_label.setSizePolicy(sizePolicy1)
        self.name_label.setFont(font4)

        self.verticalLayout.addWidget(self.name_label)

        self.line = QFrame(self.frame_3)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(16777215, 2))
        self.line.setAutoFillBackground(False)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        # self.line.setStyleSheet("QFrame#line { color: black; border: 0.1em solid black; }")

        self.verticalLayout.addWidget(self.line)

        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setMaximumSize(QSize(16777215, 16777215))
        self.label_4.setFont(font5)
        self.label_4.setStyleSheet(u"QLabel {\n"
"	color: #8C237C\n"
"}")

        self.verticalLayout.addWidget(self.label_4)

        self.tags_frame = QScrollArea(self.frame_3)
        self.tags_frame.setObjectName(u"tags_frame")
        sizePolicy1.setHeightForWidth(self.tags_frame.sizePolicy().hasHeightForWidth())
        self.tags_frame.setSizePolicy(sizePolicy1)
        self.tags_frame.setMaximumSize(QSize(16777215, 40))
        self.tags_frame.setStyleSheet("background-color: transparent;")
                                #       "border: 1px solid black;") # add border here
        self.tags_frame_widget = QWidget(self.tags_frame)
        self.tags_frame_layout = QGridLayout(self.tags_frame_widget)
        self.tags_frame_widget.setLayout(self.tags_frame_layout)
        self.tags_frame.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tags_frame.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # self.pushButton = QPushButton(self.tags_frame)
        # self.pushButton.setObjectName(u"pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        # sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        # self.pushButton.setSizePolicy(sizePolicy2)
        # self.pushButton.setMinimumSize(QSize(0, 0))
        # font6 = QFont()
        # font6.setFamilies([u"Manrope"])
        # font6.setPointSize(12)
        # self.pushButton.setFont(font6)

        # self.pushButton_2 = QPushButton(self.tags_frame)
        # self.pushButton_2.setObjectName(u"pushButton_2")
        # sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        # self.pushButton_2.setSizePolicy(sizePolicy2)
        # self.pushButton_2.setMinimumSize(QSize(0, 0))
        # self.pushButton_2.setFont(font6)

        # self.pushButton_3 = QPushButton(self.tags_frame)
        # self.pushButton_3.setObjectName(u"pushButton_3")
        # sizePolicy2.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        # self.pushButton_3.setSizePolicy(sizePolicy2)
        # self.pushButton_3.setMinimumSize(QSize(0, 0))
        # self.pushButton_3.setFont(font6)

        self.verticalLayout.addWidget(self.tags_frame)

        self.line_2 = QFrame(self.frame_3)
        self.line_2.setObjectName(u"line_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy3)
        self.line_2.setMaximumSize(QSize(16777215, 2))
        self.line_2.setAutoFillBackground(False)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        # self.line_2.setStyleSheet("QFrame#line_2 { color: black; border: 0.1em solid black; }")
        self.verticalLayout.addWidget(self.line_2)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setMaximumSize(QSize(16777215, 16777215))
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet(u"QLabel {\n"
"	color: #8C237C\n"
"}")

        self.verticalLayout.addWidget(self.label_5)

        font7 = QFont()
        font7.setFamilies([u"Manrope"])
        font7.setPointSize(14)
        font7.setBold(True)

        self.product_type_widget = QWidget(self.frame_3)

        self.product_type_layout = QHBoxLayout(self.product_type_widget)
        self.product_type_layout.setContentsMargins(1, 1, 1, 1)
        self.product_type_layout.setSpacing(2)
        self.product_type_layout.setAlignment(Qt.AlignLeft|Qt.AlignTop)
        self.product_type_widget.setLayout(self.product_type_layout)
        self.product_type_widget.setFont(font7)

        self.product_type_label_label = QLabel(self.product_type_widget)
        self.product_type_label = QLabel(self.product_type_widget)

        self.product_type_layout.addWidget(self.product_type_label_label)
        self.product_type_layout.addWidget(self.product_type_label)

        self.status_widget = QWidget(self.frame_3)

        self.status_layout = QHBoxLayout(self.status_widget)
        self.status_layout.setContentsMargins(1, 1, 1, 1)
        self.status_layout.setSpacing(2)
        self.status_layout.setAlignment(Qt.AlignLeft|Qt.AlignTop)
        self.status_widget.setLayout(self.status_layout)
        self.status_widget.setFont(font7)

        self.status_label_label = QLabel(self.status_widget)
        self.status_label = QLabel(self.status_widget)

        self.status_layout.addWidget(self.status_label_label)
        self.status_layout.addWidget(self.status_label)

        self.verticalLayout.addWidget(self.status_widget)

        self.stock_widget = QWidget(self.frame_3)

        self.stock_layout = QHBoxLayout(self.stock_widget)
        self.stock_layout.setContentsMargins(1, 1, 1, 1)
        self.stock_layout.setSpacing(2)
        self.stock_layout.setAlignment(Qt.AlignLeft|Qt.AlignTop)
        self.stock_widget.setLayout(self.stock_layout)
        self.stock_widget.setFont(font7)

        self.stock_label_label = QLabel(self.stock_widget)
        self.stock_label = QLabel(self.stock_widget)

        self.stock_layout.addWidget(self.stock_label_label)
        self.stock_layout.addWidget(self.stock_label)

        self.verticalLayout.addWidget(self.stock_widget)

        self.mode_widget = QWidget(self.frame_3)

        self.mode_layout = QHBoxLayout(self.mode_widget)
        self.mode_layout.setAlignment(Qt.AlignLeft|Qt.AlignTop)
        self.mode_layout.setContentsMargins(1, 1, 1, 1)
        self.mode_layout.setSpacing(2)
        self.mode_widget.setLayout(self.mode_layout)

        self.mode_label = QLabel(self.mode_widget)
        self.mode_label_label = QLabel(self.mode_widget)
        sizePolicy1.setHeightForWidth(self.mode_label.sizePolicy().hasHeightForWidth())
        self.mode_label.setSizePolicy(sizePolicy1)
        self.mode_label.setMaximumSize(QSize(16777215, 16777215))
        self.mode_layout.addWidget(self.mode_label_label)
        self.mode_layout.addWidget(self.mode_label)
        self.verticalLayout.addWidget(self.mode_widget)

        self.live_date_widget = QWidget(self.frame_3)
        self.live_date_layout = QHBoxLayout(self.live_date_widget)
        self.live_date_layout.setContentsMargins(1, 1, 1, 1)
        self.live_date_layout.setSpacing(2)
        self.live_date_layout.setAlignment(Qt.AlignLeft|Qt.AlignTop)
        self.live_date_widget.setLayout(self.live_date_layout)

        self.live_date_widget.setFont(font7)
        self.date_label = QLabel(self.live_date_widget)
        self.date_label_label = QLabel(self.live_date_widget)
        self.date_label.setObjectName(u"date_label")
        sizePolicy1.setHeightForWidth(self.date_label.sizePolicy().hasHeightForWidth())
        self.date_label.setSizePolicy(sizePolicy1)
        self.date_label.setMaximumSize(QSize(16777215, 16777215))
        self.live_date_layout.addWidget(self.date_label_label)
        self.live_date_layout.addWidget(self.date_label)
        self.live_date_layout.setSpacing(2)
        self.verticalLayout.addWidget(self.live_date_widget)

        self.description_area = QScrollArea(self.frame_3)
        self.description_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.description_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.description_area.setFixedSize(QSize(630, 50))
        self.description_area.setStyleSheet('background-color: transparent;')

        self.description_widget = QWidget(self.description_area)
        self.description_widget.setMinimumSize(QSize(630, 50))
        self.description_widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.description_layout = QHBoxLayout(self.description_widget)
        self.description_layout.setContentsMargins(1, 1, 1, 1)
        self.description_layout.setSpacing(0)
        self.description_layout.setAlignment(Qt.AlignLeft|Qt.AlignTop)
        self.description_widget.setLayout(self.description_layout)
        self.description_area.setWidget(self.description_widget)

        self.description_label = QLabel(self.description_widget)
        self.description_label.setObjectName(u"description_label")
        self.description_label_label = QLabel(self.description_widget)
        sizePolicy2.setHeightForWidth(self.description_label.sizePolicy().hasHeightForWidth())
        self.description_label.setSizePolicy(sizePolicy2)
        self.description_label.setMaximumSize(QSize(16777215, 16777215))
        self.description_layout.addWidget(self.description_label_label)
        self.description_layout.addWidget(self.description_label)
        self.verticalLayout.addWidget(self.description_area)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setMaximumSize(QSize(16777215, 40))
        self.frame_5.setStyleSheet(u"QPushButton {\n"
"	background-color: #FFFFFF;\n"
"    border-radius: 10px;\n"
"    border: solid;\n"
"    border-width: 1px;\n"
"    border-color:rgb(154, 152, 148);\n"
"}\n"
"\n"
"\n"
"QPushButton::hover {\n"
"	background-color: #CCCCCC;\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.add_to_wishlist_bt = QPushButton()
        self.add_to_wishlist_bt.setObjectName(u"add_to_wishlist_bt")
        sizePolicy2.setHeightForWidth(self.add_to_wishlist_bt.sizePolicy().hasHeightForWidth())
        self.add_to_wishlist_bt.setSizePolicy(sizePolicy2)
        self.add_to_wishlist_bt.setMinimumSize(QSize(0, 0))
        font8 = QFont()
        font8.setFamilies([u"Manrope"])
        font8.setPointSize(14)
        self.add_to_wishlist_bt.setFont(font8)

        self.buy_bt = QPushButton()
        sizePolicy2.setHeightForWidth(self.buy_bt.sizePolicy().hasHeightForWidth())
        self.buy_bt.setSizePolicy(sizePolicy2)
        self.buy_bt.setMinimumSize(QSize(0, 0))
        self.buy_bt.setFont(font8)
        self.buy_bt.setText('Buy')
        
        # self.horizontalLayout_3.addWidget(self.add_to_wishlist_bt)

        self.view_products_bt = QPushButton()
        self.view_products_bt.setObjectName(u"view_products_bt")
        sizePolicy2.setHeightForWidth(self.view_products_bt.sizePolicy().hasHeightForWidth())
        self.view_products_bt.setSizePolicy(sizePolicy2)
        self.view_products_bt.setMinimumSize(QSize(0, 0))
        self.view_products_bt.setFont(font8)
        # self.horizontalLayout_3.addWidget(self.view_products_bt)

        self.next_item_bt = QPushButton()
        sizePolicy2.setHeightForWidth(self.view_products_bt.sizePolicy().hasHeightForWidth())
        self.next_item_bt.setSizePolicy(sizePolicy2)
        self.next_item_bt.setMinimumSize(QSize(0, 0))
        self.next_item_bt.setFont(font8)
        self.next_item_bt.setText('Next Item')

        self.prev_item_bt = QPushButton()
        sizePolicy2.setHeightForWidth(self.view_products_bt.sizePolicy().hasHeightForWidth())
        self.prev_item_bt.setSizePolicy(sizePolicy2)
        self.prev_item_bt.setMinimumSize(QSize(0, 0))
        self.prev_item_bt.setFont(font8)
        self.prev_item_bt.setText('Prev Item')

        self.go_to_item = QPushButton()
        sizePolicy2.setHeightForWidth(self.view_products_bt.sizePolicy().hasHeightForWidth())
        self.go_to_item.setSizePolicy(sizePolicy2)
        self.go_to_item.setMinimumSize(QSize(0, 0))
        self.go_to_item.setFont(font8)
        self.go_to_item.setText('Go to Items')

        self.back_to_col = QPushButton()
        sizePolicy2.setHeightForWidth(self.view_products_bt.sizePolicy().hasHeightForWidth())
        self.back_to_col.setSizePolicy(sizePolicy2)
        self.back_to_col.setMinimumSize(QSize(0, 0))
        self.back_to_col.setFont(font8)
        self.back_to_col.setText('Go Back to Collection')

        # self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        # self.horizontalLayout_3.addItem(self.horizontalSpacer_2)
        self.verticalLayout.addWidget(self.frame_5)

        self.horizontalLayout.addWidget(self.frame_3)

        self.shop_frame = QFrame(self.centralwidget)
        self.shop_frame.setObjectName(u"shop_frame")
        self.shop_frame.setGeometry(QRect(60, 600, 1080, 140))
        self.shop_frame.setMinimumSize(QSize(1080, 140))
        self.shop_frame.setMaximumSize(QSize(16777215, 140))
        font9 = QFont()
        font9.setBold(False)
        self.shop_frame.setFont(font9)
        self.shop_frame.setStyleSheet(u"#shop_frame {\n"
"	border-radius: 10px;\n"
"    border: solid;\n"
"    border-width: 1px;\n"
"    border-color:rgb(154, 152, 148)\n"
"}\n"
"\n"
"Line {\n"
"	background-color: #CCCCCC;\n"
"}")
        self.shop_frame.setFrameShape(QFrame.StyledPanel)
        self.shop_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.shop_frame)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.frame_6 = QFrame(self.shop_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(100, 100))
        self.label_9.setMaximumSize(QSize(100, 100))
        self.label_9.setPixmap(QPixmap(u":/post_images/IMG_7102.jpg"))
        self.label_9.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_9)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.store_name_label = QLabel(self.frame_8)
        self.store_name_label.setObjectName(u"store_name_label")
        sizePolicy1.setHeightForWidth(self.store_name_label.sizePolicy().hasHeightForWidth())
        self.store_name_label.setSizePolicy(sizePolicy1)
        self.store_name_label.setMaximumSize(QSize(16777215, 16777215))
        font10 = QFont()
        font10.setFamilies([u"Manrope"])
        font10.setPointSize(18)
        font10.setBold(True)
        self.store_name_label.setFont(font10)
        self.store_name_label.setStyleSheet(u"QLabel {\n"
"	color: #8C237C\n"
"}")
        self.store_name_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.store_name_label)

        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy1.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy1)
        self.frame_9.setMaximumSize(QSize(16777215, 40))
#         self.frame_9.setStyleSheet(u"QPushButton {\n"
# "	background-color: #FFFFFF;\n"
# "    border-radius: 10px;\n"
# "    border: solid;\n"
# "    border-width: 1px;\n"
# "    border-color:rgb(154, 152, 148);\n"
# "}\n"
# "\n"
# "\n"
# "QPushButton::hover {\n"
# "	background-color: #CCCCCC;\n"
# "}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.contact_button = QPushButton()
        self.contact_button.setObjectName(u"contact_button")
        sizePolicy2.setHeightForWidth(self.contact_button.sizePolicy().hasHeightForWidth())
        self.contact_button.setSizePolicy(sizePolicy2)
        self.contact_button.setMinimumSize(QSize(0, 0))
        self.contact_button.setFont(font8)

        # self.horizontalLayout_6.addWidget(self.contact_button)

        self.visit_shop_button = QPushButton()
        self.visit_shop_button.setObjectName(u"visit_shop_button")
        sizePolicy2.setHeightForWidth(self.visit_shop_button.sizePolicy().hasHeightForWidth())
        self.visit_shop_button.setSizePolicy(sizePolicy2)
        self.visit_shop_button.setMinimumSize(QSize(0, 0))
        self.visit_shop_button.setFont(font8)

        # self.horizontalLayout_6.addWidget(self.visit_shop_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addWidget(self.frame_9)


        self.horizontalLayout_5.addWidget(self.frame_8)


        self.horizontalLayout_4.addWidget(self.frame_6)

        self.line_3 = QFrame(self.shop_frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(2, 0))
        self.line_3.setAutoFillBackground(False)
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        # self.line_3.setStyleSheet("QFrame#line_3 { color: black; border: 0.1em solid black; }")

        self.horizontalLayout_4.addWidget(self.line_3)

        self.frame_7 = QFrame(self.shop_frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.join_date_label = QLabel()
        self.join_date_label.setObjectName(u"join_date_label")
        sizePolicy1.setHeightForWidth(self.join_date_label.sizePolicy().hasHeightForWidth())
        self.join_date_label.setSizePolicy(sizePolicy1)
        self.join_date_label.setMaximumSize(QSize(16777215, 16777215))
        font11 = QFont()
        font11.setFamilies([u"Manrope"])
        font11.setPointSize(14)
        font11.setBold(False)
        self.join_date_label.setFont(font11)

        # self.gridLayout_2.addWidget(self.join_date_label, 2, 0, 1, 1

        self.follower_label = QLabel(self.frame_7)
        self.follower_label.setObjectName(u"follower_label")
        sizePolicy1.setHeightForWidth(self.follower_label.sizePolicy().hasHeightForWidth())
        self.follower_label.setSizePolicy(sizePolicy1)
        self.follower_label.setMaximumSize(QSize(16777215, 16777215))
        self.follower_label.setFont(font11)

        self.store_description_label = QLabel(self.frame)
        self.store_description_label.setFont(font11)
        self.store_description_label.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.store_description_label)
        self.verticalLayout_3.addWidget(self.follower_label)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setAlignment(Qt.AlignTop)
        
        self.col_count_label = QLabel()
        self.col_count_label.setObjectName(u"col_count_label")
        sizePolicy1.setHeightForWidth(self.col_count_label.sizePolicy().hasHeightForWidth())
        self.col_count_label.setSizePolicy(sizePolicy1)
        self.col_count_label.setMaximumSize(QSize(16777215, 16777215))
        self.col_count_label.setFont(font11)

        # self.gridLayout_2.addWidget(self.col_count_label, 1, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.frame_7)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.search_icon.setText("")
        self.filter_button.setText("")
        self.search_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"tell us what you're looking for...", None))
        self.home_button.setText("")
        self.history_button.setText("")
        self.wishlist_button.setText("")
        self.profile_button.setText("")
        self.page_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">Product</span></p></body></html>", None))
        self.curate_label.setText("")
        # self.path_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">Home &gt; Collection_name</span></p></body></html>", None))
        self.image_label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Collection", None))
        self.name_label.setText(QCoreApplication.translate("MainWindow", u"Collection_name", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Tags", None))
        # self.pushButton.setText(QCoreApplication.translate("MainWindow", u"tag_1", None))
        # self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"tag_2", None))
        # self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"tag_3", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.date_label.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.mode_label.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.description_label.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.add_to_wishlist_bt.setText(QCoreApplication.translate("MainWindow", u"Add to Wishlist", None))
        self.view_products_bt.setText(QCoreApplication.translate("MainWindow", u"View All Items", None))
        self.label_9.setText("")
        self.store_name_label.setText(QCoreApplication.translate("MainWindow", u"store_name", None))
        self.contact_button.setText(QCoreApplication.translate("MainWindow", u"Contact", None))
        self.visit_shop_button.setText(QCoreApplication.translate("MainWindow", u"Visit Shop", None))
        self.join_date_label.setText(QCoreApplication.translate("MainWindow", u"Joined:  20/03/24", None))
        self.follower_label.setText(QCoreApplication.translate("MainWindow", u"Followers:  2", None))
        self.col_count_label.setText(QCoreApplication.translate("MainWindow", u"Collections:  71", None))
    # retranslateUi
