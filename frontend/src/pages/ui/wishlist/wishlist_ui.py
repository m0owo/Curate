# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wishlist.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
from .icons_rc import *
from .logo_rc import *
from .posts_images_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(QSize(1200, 800))
        MainWindow.setMaximumSize(QSize(1200, 800))
        MainWindow.setStyleSheet(u"#centralwidget {\n"
"    background-color: #FFFFFF;\n"
"}\n"
"QFrame {\n"
"    border:  none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"* {\n"
"	color: black;\n"
"}")
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
        self.search_frame = QFrame(self.frame)
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
        self.page_label_2 = QLabel(self.centralwidget)
        self.page_label_2.setObjectName(u"page_label_2")
        self.page_label_2.setGeometry(QRect(60, 110, 251, 61))
        font4 = QFont()
        font4.setFamilies([u"Manrope"])
        font4.setPointSize(20)
        font4.setBold(True)
        self.page_label_2.setFont(font4)
        self.page_label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(60, 180, 1080, 621))
        self.scrollArea.setMinimumSize(QSize(1070, 0))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1070, 830))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(16777215, 16777215))
        self.scrollAreaWidgetContents.setAutoFillBackground(False)
        self.scrollAreaWidgetContents.setStyleSheet(u"QWidget {\n"
"	background-color: white;\n"
"}\n"
"\n"
"QFrame {\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color:#58827E;\n"
"	color: white;\n"
"	border-radius: 8px;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: #4D7672;\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_10.setSpacing(20)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 20)
        self.wishlist_box = QFrame(self.scrollAreaWidgetContents)
        self.wishlist_box.setObjectName(u"wishlist_box")
        sizePolicy.setHeightForWidth(self.wishlist_box.sizePolicy().hasHeightForWidth())
        self.wishlist_box.setSizePolicy(sizePolicy)
        self.wishlist_box.setMinimumSize(QSize(0, 250))
        self.wishlist_box.setMaximumSize(QSize(16777215, 250))
        self.wishlist_box.setAutoFillBackground(False)
        self.wishlist_box.setFrameShape(QFrame.StyledPanel)
        self.wishlist_box.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.wishlist_box)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.product_frame = QFrame(self.wishlist_box)
        self.product_frame.setObjectName(u"product_frame")
        self.product_frame.setMinimumSize(QSize(500, 0))
        self.product_frame.setMaximumSize(QSize(500, 16777215))
        self.product_frame.setStyleSheet(u"QFrame {\n"
"    background-color:#DFF1EE;\n"
"	border: none;\n"
"}")
        self.product_frame.setFrameShape(QFrame.StyledPanel)
        self.product_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.product_frame)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(20, 20, 20, 20)
        self.product_image_label = QLabel(self.product_frame)
        self.product_image_label.setObjectName(u"product_image_label")
        self.product_image_label.setMaximumSize(QSize(200, 200))
        self.product_image_label.setStyleSheet(u"")
        self.product_image_label.setPixmap(QPixmap(u":/post_images/IMG_7102.jpg"))
        self.product_image_label.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.product_image_label)

        self.frame_5 = QFrame(self.product_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.product_name_label = QLabel(self.frame_5)
        self.product_name_label.setObjectName(u"product_name_label")
        font5 = QFont()
        font5.setFamilies([u"Manrope"])
        font5.setPointSize(16)
        font5.setBold(True)
        self.product_name_label.setFont(font5)

        self.verticalLayout.addWidget(self.product_name_label)

        self.shop_name_label = QLabel(self.frame_5)
        self.shop_name_label.setObjectName(u"shop_name_label")
        font6 = QFont()
        font6.setFamilies([u"Manrope"])
        font6.setPointSize(12)
        self.shop_name_label.setFont(font6)

        self.verticalLayout.addWidget(self.shop_name_label)

        self.verticalSpacer_3 = QSpacerItem(20, 92, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.wish_status_label = QLabel(self.frame_5)
        self.wish_status_label.setObjectName(u"wish_status_label")
        font7 = QFont()
        font7.setFamilies([u"Manrope"])
        font7.setPointSize(24)
        font7.setBold(True)
        self.wish_status_label.setFont(font7)
        self.wish_status_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.wish_status_label)


        self.horizontalLayout_7.addWidget(self.frame_5)


        self.horizontalLayout_4.addWidget(self.product_frame)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.info_frame = QFrame(self.wishlist_box)
        self.info_frame.setObjectName(u"info_frame")
        self.info_frame.setMinimumSize(QSize(0, 120))
        self.info_frame.setMaximumSize(QSize(16777215, 120))
        self.info_frame.setStyleSheet(u"QFrame {\n"
"    background-color:#E8F3F2;\n"
"	border: none;\n"
"}")
        self.info_frame.setFrameShape(QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.info_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 12, 20, 12)
        self.information_label = QLabel(self.info_frame)
        self.information_label.setObjectName(u"information_label")
        self.information_label.setFont(font5)

        self.verticalLayout_3.addWidget(self.information_label)

        self.sale_date_label = QLabel(self.info_frame)
        self.sale_date_label.setObjectName(u"sale_date_label")
        font8 = QFont()
        font8.setFamilies([u"Manrope"])
        font8.setPointSize(13)
        font8.setBold(True)
        self.sale_date_label.setFont(font8)

        self.verticalLayout_3.addWidget(self.sale_date_label)

        self.mode_label = QLabel(self.info_frame)
        self.mode_label.setObjectName(u"mode_label")
        self.mode_label.setFont(font8)

        self.verticalLayout_3.addWidget(self.mode_label)


        self.verticalLayout_2.addWidget(self.info_frame)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(14)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.view_product_button = QPushButton(self.wishlist_box)
        self.view_product_button.setObjectName(u"view_product_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.view_product_button.sizePolicy().hasHeightForWidth())
        self.view_product_button.setSizePolicy(sizePolicy1)
        self.view_product_button.setMinimumSize(QSize(0, 40))
        self.view_product_button.setFont(font8)

        self.horizontalLayout_6.addWidget(self.view_product_button)

        self.view_col_button = QPushButton(self.wishlist_box)
        self.view_col_button.setObjectName(u"view_col_button")
        sizePolicy1.setHeightForWidth(self.view_col_button.sizePolicy().hasHeightForWidth())
        self.view_col_button.setSizePolicy(sizePolicy1)
        self.view_col_button.setMinimumSize(QSize(0, 40))
        self.view_col_button.setFont(font8)

        self.horizontalLayout_6.addWidget(self.view_col_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout_10.addWidget(self.wishlist_box)

        self.wishlist_box_2 = QFrame(self.scrollAreaWidgetContents)
        self.wishlist_box_2.setObjectName(u"wishlist_box_2")
        sizePolicy.setHeightForWidth(self.wishlist_box_2.sizePolicy().hasHeightForWidth())
        self.wishlist_box_2.setSizePolicy(sizePolicy)
        self.wishlist_box_2.setMinimumSize(QSize(0, 250))
        self.wishlist_box_2.setMaximumSize(QSize(16777215, 250))
        self.wishlist_box_2.setAutoFillBackground(False)
        self.wishlist_box_2.setFrameShape(QFrame.StyledPanel)
        self.wishlist_box_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.wishlist_box_2)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(20)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.product_frame_2 = QFrame(self.wishlist_box_2)
        self.product_frame_2.setObjectName(u"product_frame_2")
        self.product_frame_2.setMinimumSize(QSize(500, 0))
        self.product_frame_2.setMaximumSize(QSize(500, 16777215))
        self.product_frame_2.setStyleSheet(u"QFrame {\n"
"    background-color:#DFF1EE;\n"
"	border: none;\n"
"}")
        self.product_frame_2.setFrameShape(QFrame.StyledPanel)
        self.product_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.product_frame_2)
        self.horizontalLayout_10.setSpacing(20)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(20, 20, 20, 20)
        self.product_image_label_2 = QLabel(self.product_frame_2)
        self.product_image_label_2.setObjectName(u"product_image_label_2")
        self.product_image_label_2.setMaximumSize(QSize(200, 200))
        self.product_image_label_2.setStyleSheet(u"")
        self.product_image_label_2.setPixmap(QPixmap(u":/post_images/IMG_7102.jpg"))
        self.product_image_label_2.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.product_image_label_2)

        self.frame_7 = QFrame(self.product_frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.product_name_label_2 = QLabel(self.frame_7)
        self.product_name_label_2.setObjectName(u"product_name_label_2")
        self.product_name_label_2.setFont(font5)

        self.verticalLayout_4.addWidget(self.product_name_label_2)

        self.shop_name_label_2 = QLabel(self.frame_7)
        self.shop_name_label_2.setObjectName(u"shop_name_label_2")
        self.shop_name_label_2.setFont(font6)

        self.verticalLayout_4.addWidget(self.shop_name_label_2)

        self.verticalSpacer_4 = QSpacerItem(20, 92, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.wish_status_label_2 = QLabel(self.frame_7)
        self.wish_status_label_2.setObjectName(u"wish_status_label_2")
        self.wish_status_label_2.setFont(font7)
        self.wish_status_label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.wish_status_label_2)


        self.horizontalLayout_10.addWidget(self.frame_7)


        self.horizontalLayout_9.addWidget(self.product_frame_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.info_frame_2 = QFrame(self.wishlist_box_2)
        self.info_frame_2.setObjectName(u"info_frame_2")
        self.info_frame_2.setMinimumSize(QSize(0, 120))
        self.info_frame_2.setMaximumSize(QSize(16777215, 120))
        self.info_frame_2.setStyleSheet(u"QFrame {\n"
"    background-color:#E8F3F2;\n"
"	border: none;\n"
"}")
        self.info_frame_2.setFrameShape(QFrame.StyledPanel)
        self.info_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.info_frame_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(20, 12, 20, 12)
        self.information_label_2 = QLabel(self.info_frame_2)
        self.information_label_2.setObjectName(u"information_label_2")
        self.information_label_2.setFont(font5)

        self.verticalLayout_6.addWidget(self.information_label_2)

        self.sale_date_label_2 = QLabel(self.info_frame_2)
        self.sale_date_label_2.setObjectName(u"sale_date_label_2")
        self.sale_date_label_2.setFont(font8)

        self.verticalLayout_6.addWidget(self.sale_date_label_2)

        self.mode_label_2 = QLabel(self.info_frame_2)
        self.mode_label_2.setObjectName(u"mode_label_2")
        self.mode_label_2.setFont(font8)

        self.verticalLayout_6.addWidget(self.mode_label_2)


        self.verticalLayout_5.addWidget(self.info_frame_2)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(14)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_2)

        self.view_product_button_2 = QPushButton(self.wishlist_box_2)
        self.view_product_button_2.setObjectName(u"view_product_button_2")
        sizePolicy1.setHeightForWidth(self.view_product_button_2.sizePolicy().hasHeightForWidth())
        self.view_product_button_2.setSizePolicy(sizePolicy1)
        self.view_product_button_2.setMinimumSize(QSize(0, 40))
        self.view_product_button_2.setFont(font8)

        self.horizontalLayout_11.addWidget(self.view_product_button_2)

        self.view_col_button_2 = QPushButton(self.wishlist_box_2)
        self.view_col_button_2.setObjectName(u"view_col_button_2")
        sizePolicy1.setHeightForWidth(self.view_col_button_2.sizePolicy().hasHeightForWidth())
        self.view_col_button_2.setSizePolicy(sizePolicy1)
        self.view_col_button_2.setMinimumSize(QSize(0, 40))
        self.view_col_button_2.setFont(font8)

        self.horizontalLayout_11.addWidget(self.view_col_button_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)


        self.horizontalLayout_9.addLayout(self.verticalLayout_5)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_9)


        self.verticalLayout_10.addWidget(self.wishlist_box_2)

        self.wishlist_box_3 = QFrame(self.scrollAreaWidgetContents)
        self.wishlist_box_3.setObjectName(u"wishlist_box_3")
        sizePolicy.setHeightForWidth(self.wishlist_box_3.sizePolicy().hasHeightForWidth())
        self.wishlist_box_3.setSizePolicy(sizePolicy)
        self.wishlist_box_3.setMinimumSize(QSize(0, 250))
        self.wishlist_box_3.setMaximumSize(QSize(16777215, 250))
        self.wishlist_box_3.setAutoFillBackground(False)
        self.wishlist_box_3.setFrameShape(QFrame.StyledPanel)
        self.wishlist_box_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.wishlist_box_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(20)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.product_frame_3 = QFrame(self.wishlist_box_3)
        self.product_frame_3.setObjectName(u"product_frame_3")
        self.product_frame_3.setMinimumSize(QSize(500, 0))
        self.product_frame_3.setMaximumSize(QSize(500, 16777215))
        self.product_frame_3.setStyleSheet(u"QFrame {\n"
"    background-color:#DFF1EE;\n"
"	border: none;\n"
"}")
        self.product_frame_3.setFrameShape(QFrame.StyledPanel)
        self.product_frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.product_frame_3)
        self.horizontalLayout_14.setSpacing(20)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(20, 20, 20, 20)
        self.product_image_label_3 = QLabel(self.product_frame_3)
        self.product_image_label_3.setObjectName(u"product_image_label_3")
        self.product_image_label_3.setMaximumSize(QSize(200, 200))
        self.product_image_label_3.setStyleSheet(u"")
        self.product_image_label_3.setPixmap(QPixmap(u":/post_images/IMG_7102.jpg"))
        self.product_image_label_3.setScaledContents(True)

        self.horizontalLayout_14.addWidget(self.product_image_label_3)

        self.frame_8 = QFrame(self.product_frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.product_name_label_3 = QLabel(self.frame_8)
        self.product_name_label_3.setObjectName(u"product_name_label_3")
        self.product_name_label_3.setFont(font5)

        self.verticalLayout_7.addWidget(self.product_name_label_3)

        self.shop_name_label_3 = QLabel(self.frame_8)
        self.shop_name_label_3.setObjectName(u"shop_name_label_3")
        self.shop_name_label_3.setFont(font6)

        self.verticalLayout_7.addWidget(self.shop_name_label_3)

        self.verticalSpacer_6 = QSpacerItem(20, 92, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_6)

        self.wish_status_label_3 = QLabel(self.frame_8)
        self.wish_status_label_3.setObjectName(u"wish_status_label_3")
        self.wish_status_label_3.setFont(font7)
        self.wish_status_label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_7.addWidget(self.wish_status_label_3)


        self.horizontalLayout_14.addWidget(self.frame_8)


        self.horizontalLayout_13.addWidget(self.product_frame_3)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(20)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.info_frame_3 = QFrame(self.wishlist_box_3)
        self.info_frame_3.setObjectName(u"info_frame_3")
        self.info_frame_3.setMinimumSize(QSize(0, 120))
        self.info_frame_3.setMaximumSize(QSize(16777215, 120))
        self.info_frame_3.setStyleSheet(u"QFrame {\n"
"    background-color:#E8F3F2;\n"
"	border: none;\n"
"}")
        self.info_frame_3.setFrameShape(QFrame.StyledPanel)
        self.info_frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.info_frame_3)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(20, 12, 20, 12)
        self.information_label_3 = QLabel(self.info_frame_3)
        self.information_label_3.setObjectName(u"information_label_3")
        self.information_label_3.setFont(font5)

        self.verticalLayout_9.addWidget(self.information_label_3)

        self.sale_date_label_3 = QLabel(self.info_frame_3)
        self.sale_date_label_3.setObjectName(u"sale_date_label_3")
        self.sale_date_label_3.setFont(font8)

        self.verticalLayout_9.addWidget(self.sale_date_label_3)

        self.mode_label_3 = QLabel(self.info_frame_3)
        self.mode_label_3.setObjectName(u"mode_label_3")
        self.mode_label_3.setFont(font8)

        self.verticalLayout_9.addWidget(self.mode_label_3)


        self.verticalLayout_8.addWidget(self.info_frame_3)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(14)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_3)

        self.view_product_button_3 = QPushButton(self.wishlist_box_3)
        self.view_product_button_3.setObjectName(u"view_product_button_3")
        sizePolicy1.setHeightForWidth(self.view_product_button_3.sizePolicy().hasHeightForWidth())
        self.view_product_button_3.setSizePolicy(sizePolicy1)
        self.view_product_button_3.setMinimumSize(QSize(0, 40))
        self.view_product_button_3.setFont(font8)

        self.horizontalLayout_15.addWidget(self.view_product_button_3)

        self.view_col_button_3 = QPushButton(self.wishlist_box_3)
        self.view_col_button_3.setObjectName(u"view_col_button_3")
        sizePolicy1.setHeightForWidth(self.view_col_button_3.sizePolicy().hasHeightForWidth())
        self.view_col_button_3.setSizePolicy(sizePolicy1)
        self.view_col_button_3.setMinimumSize(QSize(0, 40))
        self.view_col_button_3.setFont(font8)

        self.horizontalLayout_15.addWidget(self.view_col_button_3)


        self.verticalLayout_8.addLayout(self.horizontalLayout_15)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_7)


        self.horizontalLayout_13.addLayout(self.verticalLayout_8)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_13)


        self.verticalLayout_10.addWidget(self.wishlist_box_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(50, 750, 1091, 51))
        self.frame_6.setAutoFillBackground(False)
        self.frame_6.setStyleSheet(u"* {\n"
"	background: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0.8));\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
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
        self.page_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">Wishlist</span></p></body></html>", None))
        self.curate_label.setText("")
        self.page_label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Wishlist</p></body></html>", None))
        self.product_image_label.setText("")
        self.product_name_label.setText(QCoreApplication.translate("MainWindow", u"Product Name", None))
        self.shop_name_label.setText(QCoreApplication.translate("MainWindow", u"Shop Name", None))
        self.wish_status_label.setText(QCoreApplication.translate("MainWindow", u"Starting", None))
        self.information_label.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.sale_date_label.setText(QCoreApplication.translate("MainWindow", u"Sale Date: Mon 26 Jan 19:00", None))
        self.mode_label.setText(QCoreApplication.translate("MainWindow", u"Mode:  CF no CC", None))
        self.view_product_button.setText(QCoreApplication.translate("MainWindow", u"View Product", None))
        self.view_col_button.setText(QCoreApplication.translate("MainWindow", u"View Collection", None))
        self.product_image_label_2.setText("")
        self.product_name_label_2.setText(QCoreApplication.translate("MainWindow", u"Product Name", None))
        self.shop_name_label_2.setText(QCoreApplication.translate("MainWindow", u"Shop Name", None))
        self.wish_status_label_2.setText(QCoreApplication.translate("MainWindow", u"Ended", None))
        self.information_label_2.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.sale_date_label_2.setText(QCoreApplication.translate("MainWindow", u"Sale Date: Mon 26 Jan 19:00", None))
        self.mode_label_2.setText(QCoreApplication.translate("MainWindow", u"Mode:  CF no CC", None))
        self.view_product_button_2.setText(QCoreApplication.translate("MainWindow", u"View Product", None))
        self.view_col_button_2.setText(QCoreApplication.translate("MainWindow", u"View Collection", None))
        self.product_image_label_3.setText("")
        self.product_name_label_3.setText(QCoreApplication.translate("MainWindow", u"Product Name", None))
        self.shop_name_label_3.setText(QCoreApplication.translate("MainWindow", u"Shop Name", None))
        self.wish_status_label_3.setText(QCoreApplication.translate("MainWindow", u"Starting", None))
        self.information_label_3.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.sale_date_label_3.setText(QCoreApplication.translate("MainWindow", u"Sale Date: Mon 26 Jan 19:00", None))
        self.mode_label_3.setText(QCoreApplication.translate("MainWindow", u"Mode:  CF no CC", None))
        self.view_product_button_3.setText(QCoreApplication.translate("MainWindow", u"View Product", None))
        self.view_col_button_3.setText(QCoreApplication.translate("MainWindow", u"View Collection", None))
    # retranslateUi

