# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QWidget)
import icons_rc
import logo_rc
import post_images_rc

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
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setGeometry(QRect(10, 30, 1181, 71))
        self.header.setMaximumSize(QSize(1200, 800))
        font = QFont()
        font.setFamilies([u".AppleSystemUIFont"])
        self.header.setFont(font)
        self.header.setStyleSheet(u"")
        self.nav_frame = QFrame(self.header)
        self.nav_frame.setObjectName(u"nav_frame")
        self.nav_frame.setGeometry(QRect(190, 0, 931, 71))
        self.nav_frame.setStyleSheet(u"QFrame#search_frame{\n"
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
        self.nav_frame.setFrameShape(QFrame.StyledPanel)
        self.nav_frame.setFrameShadow(QFrame.Raised)
        self.search_frame = QFrame(self.nav_frame)
        self.search_frame.setObjectName(u"search_frame")
        self.search_frame.setEnabled(True)
        self.search_frame.setGeometry(QRect(140, 20, 581, 30))
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
        self.search_edit.setGeometry(QRect(40, 5, 491, 21))
        self.search_edit.setFont(font1)
        self.home_button = QPushButton(self.nav_frame)
        self.home_button.setObjectName(u"home_button")
        self.home_button.setGeometry(QRect(750, 20, 41, 30))
        font2 = QFont()
        font2.setFamilies([u"Manrope"])
        font2.setBold(True)
        self.home_button.setFont(font2)
        self.home_button.setStyleSheet(u"QPushButton:hover {\n"
"box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.5);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"box-shadow: 0px 0px 0px rgba(0, 0, 0, 0.5);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon_images/home_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_button.setIcon(icon1)
        self.home_button.setIconSize(QSize(20, 20))
        self.history_button = QPushButton(self.nav_frame)
        self.history_button.setObjectName(u"history_button")
        self.history_button.setGeometry(QRect(790, 20, 41, 30))
        icon2 = QIcon()
        icon2.addFile(u":/icon_images/history_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.history_button.setIcon(icon2)
        self.history_button.setIconSize(QSize(20, 20))
        self.wishlist_button = QPushButton(self.nav_frame)
        self.wishlist_button.setObjectName(u"wishlist_button")
        self.wishlist_button.setGeometry(QRect(830, 20, 41, 30))
        icon3 = QIcon()
        icon3.addFile(u":/icon_images/wishlist_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.wishlist_button.setIcon(icon3)
        self.wishlist_button.setIconSize(QSize(20, 20))
        self.profile_button = QPushButton(self.nav_frame)
        self.profile_button.setObjectName(u"profile_button")
        self.profile_button.setGeometry(QRect(870, 20, 41, 30))
        icon4 = QIcon()
        icon4.addFile(u":/icon_images/profile_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.profile_button.setIcon(icon4)
        self.profile_button.setIconSize(QSize(20, 20))
        self.page_label = QLabel(self.nav_frame)
        self.page_label.setObjectName(u"page_label")
        self.page_label.setGeometry(QRect(30, 20, 71, 30))
        self.page_label.setFont(font2)
        self.page_label.setAlignment(Qt.AlignCenter)
        self.logo_frame = QFrame(self.header)
        self.logo_frame.setObjectName(u"logo_frame")
        self.logo_frame.setGeometry(QRect(29, 0, 161, 71))
        self.logo_frame.setFrameShape(QFrame.StyledPanel)
        self.logo_frame.setFrameShadow(QFrame.Raised)
        self.curate_label = QLabel(self.logo_frame)
        self.curate_label.setObjectName(u"curate_label")
        self.curate_label.setGeometry(QRect(10, -16, 191, 101))
        font3 = QFont()
        font3.setFamilies([u"Mogena"])
        font3.setPointSize(18)
        self.curate_label.setFont(font3)
        self.curate_label.setPixmap(QPixmap(u":/logos/curatelogo.png"))
        self.curate_label.setScaledContents(True)
        self.curate_label.setAlignment(Qt.AlignCenter)
        self.body = QWidget(self.centralwidget)
        self.body.setObjectName(u"body")
        self.body.setGeometry(QRect(10, 110, 1181, 671))
        self.body.setStyleSheet(u"QScrollArea {\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.tags_frame = QFrame(self.body)
        self.tags_frame.setObjectName(u"tags_frame")
        self.tags_frame.setGeometry(QRect(70, 10, 1041, 80))
        self.tags_frame.setStyleSheet(u"QPushButton {\n"
"    background-color:rgb(234, 243, 242);\n"
"    color: rgb(137, 153, 211);\n"
"    border-radius: 20%;\n"
"	font: 600 14pt \"Manrope\";\n"
"    width: fit-content;\n"
"    padding: 10px\n"
"}")
        self.tags_frame.setFrameShape(QFrame.StyledPanel)
        self.tags_frame.setFrameShadow(QFrame.Raised)
        self.tagbutton = QPushButton(self.tags_frame)
        self.tagbutton.setObjectName(u"tagbutton")
        self.tagbutton.setGeometry(QRect(30, 20, 121, 41))
        self.tagbutton.setStyleSheet(u"")
        self.posts_frame = QScrollArea(self.body)
        self.posts_frame.setObjectName(u"posts_frame")
        self.posts_frame.setGeometry(QRect(0, 99, 1181, 571))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.posts_frame.sizePolicy().hasHeightForWidth())
        self.posts_frame.setSizePolicy(sizePolicy)
        self.posts_frame.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(255, 255, 255)\n"
"\n"
"}\n"
"QLabel {\n"
"    color: rgb(0, 0, 0)\n"
"}\n"
"")
        self.posts_frame.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.posts_frame.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.posts_frame.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.posts_frame.setWidgetResizable(False)
        self.posts_frame.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(95, 0, 991, 636))
        self.scrollAreaWidgetContents.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.post_sample_10 = QFrame(self.scrollAreaWidgetContents)
        self.post_sample_10.setObjectName(u"post_sample_10")
        self.post_sample_10.setMinimumSize(QSize(230, 300))
        self.post_sample_10.setMaximumSize(QSize(230, 300))
        self.post_sample_10.setStyleSheet(u"#post_image {\n"
"  weight: 2; \n"
"}\n"
"\n"
"#post_info {\n"
"  weight: 1;\n"
"}")
        self.post_sample_10.setFrameShape(QFrame.StyledPanel)
        self.post_sample_10.setFrameShadow(QFrame.Raised)
        self.post_image_16 = QLabel(self.post_sample_10)
        self.post_image_16.setObjectName(u"post_image_16")
        self.post_image_16.setGeometry(QRect(0, 0, 230, 170))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(10)
        sizePolicy1.setHeightForWidth(self.post_image_16.sizePolicy().hasHeightForWidth())
        self.post_image_16.setSizePolicy(sizePolicy1)
        self.post_image_16.setPixmap(QPixmap(u":/post_images/IMG_7109.jpg"))
        self.post_image_16.setScaledContents(True)
        self.post_info_16 = QWidget(self.post_sample_10)
        self.post_info_16.setObjectName(u"post_info_16")
        self.post_info_16.setGeometry(QRect(10, 180, 211, 111))
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.post_info_16.sizePolicy().hasHeightForWidth())
        self.post_info_16.setSizePolicy(sizePolicy2)
        self.post_info_16.setStyleSheet(u"")
        self.post_title_16 = QLabel(self.post_info_16)
        self.post_title_16.setObjectName(u"post_title_16")
        self.post_title_16.setGeometry(QRect(10, 10, 187, 16))
        self.post_title_16.setStyleSheet(u"QLabel {\n"
"    \n"
"	font: 700 13pt \"Manrope\";\n"
"}")
        self.post_title_16.setAlignment(Qt.AlignCenter)
        self.post_title_16.setWordWrap(True)
        self.post_details_10 = QWidget(self.post_info_16)
        self.post_details_10.setObjectName(u"post_details_10")
        self.post_details_10.setGeometry(QRect(0, 60, 211, 31))
        self.post_details_10.setStyleSheet(u"QLabel {font: 400 12pt \"Manrope\";}")
        self.sales_type_11 = QLabel(self.post_details_10)
        self.sales_type_11.setObjectName(u"sales_type_11")
        self.sales_type_11.setGeometry(QRect(10, 10, 72, 16))
        self.live_date_11 = QLabel(self.post_details_10)
        self.live_date_11.setObjectName(u"live_date_11")
        self.live_date_11.setGeometry(QRect(130, 10, 55, 16))
        self.post_tags_16 = QWidget(self.post_info_16)
        self.post_tags_16.setObjectName(u"post_tags_16")
        self.post_tags_16.setGeometry(QRect(0, 30, 211, 31))
        self.post_tags_16.setStyleSheet(u"QLabel {\n"
"    font: 600 11pt \"Manrope\";\n"
"    color: rgb(137, 153, 211);\n"
"    text-align: center;\n"
"    background-color: #E8F3F2;\n"
"    border-radius: 5px;\n"
"}")
        self.tag_46 = QLabel(self.post_tags_16)
        self.tag_46.setObjectName(u"tag_46")
        self.tag_46.setGeometry(QRect(10, 10, 61, 16))
        self.tag_46.setStyleSheet(u"")
        self.tag_46.setAlignment(Qt.AlignCenter)
        self.tag_46.setMargin(1)
        self.tag_47 = QLabel(self.post_tags_16)
        self.tag_47.setObjectName(u"tag_47")
        self.tag_47.setGeometry(QRect(80, 10, 31, 16))
        self.tag_47.setStyleSheet(u"")
        self.tag_47.setAlignment(Qt.AlignCenter)
        self.tag_47.setMargin(1)
        self.tag_48 = QLabel(self.post_tags_16)
        self.tag_48.setObjectName(u"tag_48")
        self.tag_48.setGeometry(QRect(120, 10, 51, 16))
        self.tag_48.setStyleSheet(u"")
        self.tag_48.setAlignment(Qt.AlignCenter)
        self.tag_48.setMargin(1)
        self.post_type_11 = QLabel(self.post_sample_10)
        self.post_type_11.setObjectName(u"post_type_11")
        self.post_type_11.setGeometry(QRect(10, 10, 41, 16))
        font4 = QFont()
        font4.setFamilies([u"Manrope"])
        font4.setPointSize(11)
        font4.setBold(True)
        self.post_type_11.setFont(font4)
        self.post_type_11.setStyleSheet(u"border-radius: 5px; padding:3px;\n"
"background-color: rgb(255, 245, 225);\n"
"color:rgb(206, 141, 80);")
        self.post_type_11.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.post_sample_10, 0, 3, 1, 1)

        self.post_sample_9 = QFrame(self.scrollAreaWidgetContents)
        self.post_sample_9.setObjectName(u"post_sample_9")
        self.post_sample_9.setMinimumSize(QSize(230, 300))
        self.post_sample_9.setMaximumSize(QSize(230, 300))
        self.post_sample_9.setStyleSheet(u"")
        self.post_sample_9.setFrameShape(QFrame.StyledPanel)
        self.post_sample_9.setFrameShadow(QFrame.Raised)
        self.post_image_14 = QLabel(self.post_sample_9)
        self.post_image_14.setObjectName(u"post_image_14")
        self.post_image_14.setGeometry(QRect(0, 0, 230, 170))
        sizePolicy1.setHeightForWidth(self.post_image_14.sizePolicy().hasHeightForWidth())
        self.post_image_14.setSizePolicy(sizePolicy1)
        self.post_image_14.setStyleSheet(u"")
        self.post_image_14.setPixmap(QPixmap(u":/post_images/IMG_7107.jpg"))
        self.post_image_14.setScaledContents(True)
        self.post_info_14 = QWidget(self.post_sample_9)
        self.post_info_14.setObjectName(u"post_info_14")
        self.post_info_14.setGeometry(QRect(10, 180, 211, 111))
        sizePolicy2.setHeightForWidth(self.post_info_14.sizePolicy().hasHeightForWidth())
        self.post_info_14.setSizePolicy(sizePolicy2)
        self.post_info_14.setStyleSheet(u"")
        self.post_title_14 = QLabel(self.post_info_14)
        self.post_title_14.setObjectName(u"post_title_14")
        self.post_title_14.setGeometry(QRect(10, 10, 187, 16))
        self.post_title_14.setStyleSheet(u"QLabel {\n"
"    \n"
"	font: 700 13pt \"Manrope\";\n"
"}")
        self.post_title_14.setAlignment(Qt.AlignCenter)
        self.post_title_14.setWordWrap(True)
        self.post_details_8 = QWidget(self.post_info_14)
        self.post_details_8.setObjectName(u"post_details_8")
        self.post_details_8.setGeometry(QRect(0, 60, 211, 31))
        self.post_details_8.setStyleSheet(u"QLabel {font: 400 12pt \"Manrope\";}")
        self.sales_type_9 = QLabel(self.post_details_8)
        self.sales_type_9.setObjectName(u"sales_type_9")
        self.sales_type_9.setGeometry(QRect(10, 10, 72, 16))
        self.live_date_9 = QLabel(self.post_details_8)
        self.live_date_9.setObjectName(u"live_date_9")
        self.live_date_9.setGeometry(QRect(130, 10, 55, 16))
        self.post_tags_14 = QWidget(self.post_info_14)
        self.post_tags_14.setObjectName(u"post_tags_14")
        self.post_tags_14.setGeometry(QRect(0, 30, 211, 31))
        self.post_tags_14.setStyleSheet(u"QLabel {\n"
"    font: 600 11pt \"Manrope\";\n"
"    color: rgb(137, 153, 211);\n"
"    text-align: center;\n"
"    background-color: #E8F3F2;\n"
"    border-radius: 5px;\n"
"}")
        self.tag_40 = QLabel(self.post_tags_14)
        self.tag_40.setObjectName(u"tag_40")
        self.tag_40.setGeometry(QRect(10, 10, 61, 16))
        self.tag_40.setStyleSheet(u"")
        self.tag_40.setAlignment(Qt.AlignCenter)
        self.tag_40.setMargin(1)
        self.tag_41 = QLabel(self.post_tags_14)
        self.tag_41.setObjectName(u"tag_41")
        self.tag_41.setGeometry(QRect(80, 10, 31, 16))
        self.tag_41.setStyleSheet(u"")
        self.tag_41.setAlignment(Qt.AlignCenter)
        self.tag_41.setMargin(1)
        self.tag_42 = QLabel(self.post_tags_14)
        self.tag_42.setObjectName(u"tag_42")
        self.tag_42.setGeometry(QRect(120, 10, 51, 16))
        self.tag_42.setStyleSheet(u"")
        self.tag_42.setAlignment(Qt.AlignCenter)
        self.tag_42.setMargin(1)
        self.post_type_9 = QLabel(self.post_sample_9)
        self.post_type_9.setObjectName(u"post_type_9")
        self.post_type_9.setGeometry(QRect(10, 10, 71, 16))
        self.post_type_9.setFont(font4)
        self.post_type_9.setStyleSheet(u"border-radius: 5px; padding:3px;\n"
"background-color: rgb(255, 245, 225);\n"
"color:rgb(206, 141, 80);")
        self.post_type_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.post_sample_9, 0, 1, 1, 1)

        self.post_sample_11 = QFrame(self.scrollAreaWidgetContents)
        self.post_sample_11.setObjectName(u"post_sample_11")
        self.post_sample_11.setMinimumSize(QSize(230, 300))
        self.post_sample_11.setMaximumSize(QSize(230, 300))
        self.post_sample_11.setStyleSheet(u"#post_image {\n"
"  weight: 2; \n"
"}\n"
"\n"
"#post_info {\n"
"  weight: 1;\n"
"}")
        self.post_sample_11.setFrameShape(QFrame.StyledPanel)
        self.post_sample_11.setFrameShadow(QFrame.Raised)
        self.post_image_17 = QLabel(self.post_sample_11)
        self.post_image_17.setObjectName(u"post_image_17")
        self.post_image_17.setGeometry(QRect(0, 0, 230, 170))
        sizePolicy1.setHeightForWidth(self.post_image_17.sizePolicy().hasHeightForWidth())
        self.post_image_17.setSizePolicy(sizePolicy1)
        self.post_image_17.setPixmap(QPixmap(u":/post_images/IMG_7106.jpg"))
        self.post_image_17.setScaledContents(True)
        self.post_info_17 = QWidget(self.post_sample_11)
        self.post_info_17.setObjectName(u"post_info_17")
        self.post_info_17.setGeometry(QRect(10, 180, 211, 111))
        sizePolicy2.setHeightForWidth(self.post_info_17.sizePolicy().hasHeightForWidth())
        self.post_info_17.setSizePolicy(sizePolicy2)
        self.post_info_17.setStyleSheet(u"")
        self.post_title_17 = QLabel(self.post_info_17)
        self.post_title_17.setObjectName(u"post_title_17")
        self.post_title_17.setGeometry(QRect(10, 10, 187, 16))
        self.post_title_17.setStyleSheet(u"QLabel {\n"
"    \n"
"	font: 700 13pt \"Manrope\";\n"
"}")
        self.post_title_17.setAlignment(Qt.AlignCenter)
        self.post_title_17.setWordWrap(True)
        self.post_details_11 = QWidget(self.post_info_17)
        self.post_details_11.setObjectName(u"post_details_11")
        self.post_details_11.setGeometry(QRect(0, 60, 211, 31))
        self.post_details_11.setStyleSheet(u"QLabel {font: 400 12pt \"Manrope\";}")
        self.sales_type_12 = QLabel(self.post_details_11)
        self.sales_type_12.setObjectName(u"sales_type_12")
        self.sales_type_12.setGeometry(QRect(10, 10, 72, 16))
        self.live_date_12 = QLabel(self.post_details_11)
        self.live_date_12.setObjectName(u"live_date_12")
        self.live_date_12.setGeometry(QRect(130, 10, 55, 16))
        self.post_tags_17 = QWidget(self.post_info_17)
        self.post_tags_17.setObjectName(u"post_tags_17")
        self.post_tags_17.setGeometry(QRect(0, 30, 211, 31))
        self.post_tags_17.setStyleSheet(u"QLabel {\n"
"    font: 600 11pt \"Manrope\";\n"
"    color: rgb(137, 153, 211);\n"
"    text-align: center;\n"
"    background-color: #E8F3F2;\n"
"    border-radius: 5px;\n"
"}")
        self.tag_49 = QLabel(self.post_tags_17)
        self.tag_49.setObjectName(u"tag_49")
        self.tag_49.setGeometry(QRect(10, 10, 61, 16))
        self.tag_49.setStyleSheet(u"")
        self.tag_49.setAlignment(Qt.AlignCenter)
        self.tag_49.setMargin(1)
        self.tag_50 = QLabel(self.post_tags_17)
        self.tag_50.setObjectName(u"tag_50")
        self.tag_50.setGeometry(QRect(80, 10, 31, 16))
        self.tag_50.setStyleSheet(u"")
        self.tag_50.setAlignment(Qt.AlignCenter)
        self.tag_50.setMargin(1)
        self.tag_51 = QLabel(self.post_tags_17)
        self.tag_51.setObjectName(u"tag_51")
        self.tag_51.setGeometry(QRect(120, 10, 51, 16))
        self.tag_51.setStyleSheet(u"")
        self.tag_51.setAlignment(Qt.AlignCenter)
        self.tag_51.setMargin(1)
        self.post_type_12 = QLabel(self.post_sample_11)
        self.post_type_12.setObjectName(u"post_type_12")
        self.post_type_12.setGeometry(QRect(10, 10, 71, 16))
        self.post_type_12.setFont(font4)
        self.post_type_12.setStyleSheet(u"border-radius: 5px; padding:3px;\n"
"background-color: rgb(255, 245, 225);\n"
"color:rgb(206, 141, 80);")
        self.post_type_12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.post_sample_11, 0, 2, 1, 1)

        self.post_sample_2 = QFrame(self.scrollAreaWidgetContents)
        self.post_sample_2.setObjectName(u"post_sample_2")
        self.post_sample_2.setMinimumSize(QSize(230, 300))
        self.post_sample_2.setMaximumSize(QSize(230, 300))
        self.post_sample_2.setStyleSheet(u"#post_image {\n"
"  weight: 2; \n"
"}\n"
"\n"
"#post_info {\n"
"  weight: 1;\n"
"}")
        self.post_sample_2.setFrameShape(QFrame.StyledPanel)
        self.post_sample_2.setFrameShadow(QFrame.Raised)
        self.post_image_15 = QLabel(self.post_sample_2)
        self.post_image_15.setObjectName(u"post_image_15")
        self.post_image_15.setGeometry(QRect(0, 0, 230, 170))
        sizePolicy1.setHeightForWidth(self.post_image_15.sizePolicy().hasHeightForWidth())
        self.post_image_15.setSizePolicy(sizePolicy1)
        self.post_image_15.setPixmap(QPixmap(u":/post_images/IMG_7102.jpg"))
        self.post_image_15.setScaledContents(True)
        self.post_info_15 = QWidget(self.post_sample_2)
        self.post_info_15.setObjectName(u"post_info_15")
        self.post_info_15.setGeometry(QRect(10, 180, 211, 111))
        sizePolicy2.setHeightForWidth(self.post_info_15.sizePolicy().hasHeightForWidth())
        self.post_info_15.setSizePolicy(sizePolicy2)
        self.post_info_15.setStyleSheet(u"")
        self.post_title_15 = QLabel(self.post_info_15)
        self.post_title_15.setObjectName(u"post_title_15")
        self.post_title_15.setGeometry(QRect(10, 10, 187, 16))
        self.post_title_15.setStyleSheet(u"QLabel {\n"
"    \n"
"	font: 700 13pt \"Manrope\";\n"
"}")
        self.post_title_15.setAlignment(Qt.AlignCenter)
        self.post_title_15.setWordWrap(True)
        self.post_details_9 = QWidget(self.post_info_15)
        self.post_details_9.setObjectName(u"post_details_9")
        self.post_details_9.setGeometry(QRect(0, 60, 211, 31))
        self.post_details_9.setStyleSheet(u"QLabel {font: 400 12pt \"Manrope\";}")
        self.sales_type_10 = QLabel(self.post_details_9)
        self.sales_type_10.setObjectName(u"sales_type_10")
        self.sales_type_10.setGeometry(QRect(10, 10, 72, 16))
        self.live_date_10 = QLabel(self.post_details_9)
        self.live_date_10.setObjectName(u"live_date_10")
        self.live_date_10.setGeometry(QRect(130, 10, 55, 16))
        self.post_tags_15 = QWidget(self.post_info_15)
        self.post_tags_15.setObjectName(u"post_tags_15")
        self.post_tags_15.setGeometry(QRect(0, 30, 211, 31))
        self.post_tags_15.setStyleSheet(u"QLabel {\n"
"    font: 600 11pt \"Manrope\";\n"
"    color: rgb(137, 153, 211);\n"
"    text-align: center;\n"
"    background-color: #E8F3F2;\n"
"    border-radius: 5px;\n"
"}")
        self.tag_43 = QLabel(self.post_tags_15)
        self.tag_43.setObjectName(u"tag_43")
        self.tag_43.setGeometry(QRect(10, 10, 61, 16))
        self.tag_43.setStyleSheet(u"")
        self.tag_43.setAlignment(Qt.AlignCenter)
        self.tag_43.setMargin(1)
        self.tag_44 = QLabel(self.post_tags_15)
        self.tag_44.setObjectName(u"tag_44")
        self.tag_44.setGeometry(QRect(80, 10, 31, 16))
        self.tag_44.setStyleSheet(u"")
        self.tag_44.setAlignment(Qt.AlignCenter)
        self.tag_44.setMargin(1)
        self.tag_45 = QLabel(self.post_tags_15)
        self.tag_45.setObjectName(u"tag_45")
        self.tag_45.setGeometry(QRect(120, 10, 51, 16))
        self.tag_45.setStyleSheet(u"")
        self.tag_45.setAlignment(Qt.AlignCenter)
        self.tag_45.setMargin(1)
        self.post_type_10 = QLabel(self.post_sample_2)
        self.post_type_10.setObjectName(u"post_type_10")
        self.post_type_10.setGeometry(QRect(10, 10, 71, 16))
        self.post_type_10.setFont(font4)
        self.post_type_10.setStyleSheet(u"border-radius: 5px; padding:3px;\n"
"background-color: rgb(255, 245, 225);\n"
"color:rgb(206, 141, 80);")
        self.post_type_10.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.post_sample_2, 0, 0, 1, 1)

        self.post_sample_12 = QFrame(self.scrollAreaWidgetContents)
        self.post_sample_12.setObjectName(u"post_sample_12")
        self.post_sample_12.setMinimumSize(QSize(230, 300))
        self.post_sample_12.setMaximumSize(QSize(230, 300))
        self.post_sample_12.setStyleSheet(u"#post_image {\n"
"  weight: 2; \n"
"}\n"
"\n"
"#post_info {\n"
"  weight: 1;\n"
"}")
        self.post_sample_12.setFrameShape(QFrame.StyledPanel)
        self.post_sample_12.setFrameShadow(QFrame.Raised)
        self.post_image_18 = QLabel(self.post_sample_12)
        self.post_image_18.setObjectName(u"post_image_18")
        self.post_image_18.setGeometry(QRect(0, 0, 230, 170))
        sizePolicy1.setHeightForWidth(self.post_image_18.sizePolicy().hasHeightForWidth())
        self.post_image_18.setSizePolicy(sizePolicy1)
        self.post_image_18.setPixmap(QPixmap(u":/post_images/IMG_7108.jpg"))
        self.post_image_18.setScaledContents(True)
        self.post_info_18 = QWidget(self.post_sample_12)
        self.post_info_18.setObjectName(u"post_info_18")
        self.post_info_18.setGeometry(QRect(10, 180, 211, 111))
        sizePolicy2.setHeightForWidth(self.post_info_18.sizePolicy().hasHeightForWidth())
        self.post_info_18.setSizePolicy(sizePolicy2)
        self.post_info_18.setStyleSheet(u"")
        self.post_title_18 = QLabel(self.post_info_18)
        self.post_title_18.setObjectName(u"post_title_18")
        self.post_title_18.setGeometry(QRect(10, 10, 187, 16))
        self.post_title_18.setStyleSheet(u"QLabel {\n"
"    \n"
"	font: 700 13pt \"Manrope\";\n"
"}")
        self.post_title_18.setAlignment(Qt.AlignCenter)
        self.post_title_18.setWordWrap(True)
        self.user_info_12 = QWidget(self.post_info_18)
        self.user_info_12.setObjectName(u"user_info_12")
        self.user_info_12.setGeometry(QRect(0, 60, 211, 31))
        self.user_info_12.setStyleSheet(u"QLabel {font: 400 12pt \"Manrope\";}")
        self.sales_type_13 = QLabel(self.user_info_12)
        self.sales_type_13.setObjectName(u"sales_type_13")
        self.sales_type_13.setGeometry(QRect(10, 10, 72, 16))
        self.live_date_13 = QLabel(self.user_info_12)
        self.live_date_13.setObjectName(u"live_date_13")
        self.live_date_13.setGeometry(QRect(130, 10, 55, 16))
        self.post_tags_18 = QWidget(self.post_info_18)
        self.post_tags_18.setObjectName(u"post_tags_18")
        self.post_tags_18.setGeometry(QRect(0, 30, 211, 31))
        self.post_tags_18.setStyleSheet(u"QLabel {\n"
"    font: 600 11pt \"Manrope\";\n"
"    color: rgb(137, 153, 211);\n"
"    text-align: center;\n"
"    background-color: #E8F3F2;\n"
"    border-radius: 5px;\n"
"}")
        self.tag_52 = QLabel(self.post_tags_18)
        self.tag_52.setObjectName(u"tag_52")
        self.tag_52.setGeometry(QRect(10, 10, 61, 16))
        self.tag_52.setStyleSheet(u"")
        self.tag_52.setAlignment(Qt.AlignCenter)
        self.tag_52.setMargin(1)
        self.tag_53 = QLabel(self.post_tags_18)
        self.tag_53.setObjectName(u"tag_53")
        self.tag_53.setGeometry(QRect(80, 10, 31, 16))
        self.tag_53.setStyleSheet(u"")
        self.tag_53.setAlignment(Qt.AlignCenter)
        self.tag_53.setMargin(1)
        self.tag_54 = QLabel(self.post_tags_18)
        self.tag_54.setObjectName(u"tag_54")
        self.tag_54.setGeometry(QRect(120, 10, 51, 16))
        self.tag_54.setStyleSheet(u"")
        self.tag_54.setAlignment(Qt.AlignCenter)
        self.tag_54.setMargin(1)
        self.post_type_13 = QLabel(self.post_sample_12)
        self.post_type_13.setObjectName(u"post_type_13")
        self.post_type_13.setGeometry(QRect(10, 10, 71, 16))
        self.post_type_13.setFont(font4)
        self.post_type_13.setStyleSheet(u"border-radius: 5px; padding:3px;\n"
"background-color: rgb(255, 245, 225);\n"
"color:rgb(206, 141, 80);")
        self.post_type_13.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.post_sample_12, 1, 0, 1, 1)

        self.post_sample_6 = QFrame(self.scrollAreaWidgetContents)
        self.post_sample_6.setObjectName(u"post_sample_6")
        self.post_sample_6.setMinimumSize(QSize(230, 300))
        self.post_sample_6.setMaximumSize(QSize(230, 300))
        self.post_sample_6.setStyleSheet(u"#post_image {\n"
"  weight: 2; \n"
"}\n"
"\n"
"#post_info {\n"
"  weight: 1;\n"
"}")
        self.post_sample_6.setFrameShape(QFrame.StyledPanel)
        self.post_sample_6.setFrameShadow(QFrame.Raised)
        self.post_image_19 = QLabel(self.post_sample_6)
        self.post_image_19.setObjectName(u"post_image_19")
        self.post_image_19.setGeometry(QRect(0, 0, 230, 170))
        sizePolicy1.setHeightForWidth(self.post_image_19.sizePolicy().hasHeightForWidth())
        self.post_image_19.setSizePolicy(sizePolicy1)
        self.post_image_19.setPixmap(QPixmap(u":/post_images/IMG_7105.jpg"))
        self.post_image_19.setScaledContents(True)
        self.post_info_19 = QWidget(self.post_sample_6)
        self.post_info_19.setObjectName(u"post_info_19")
        self.post_info_19.setGeometry(QRect(10, 180, 211, 111))
        sizePolicy2.setHeightForWidth(self.post_info_19.sizePolicy().hasHeightForWidth())
        self.post_info_19.setSizePolicy(sizePolicy2)
        self.post_info_19.setStyleSheet(u"")
        self.post_title_19 = QLabel(self.post_info_19)
        self.post_title_19.setObjectName(u"post_title_19")
        self.post_title_19.setGeometry(QRect(10, 10, 187, 16))
        self.post_title_19.setStyleSheet(u"QLabel {\n"
"    \n"
"	font: 700 13pt \"Manrope\";\n"
"}")
        self.post_title_19.setAlignment(Qt.AlignCenter)
        self.post_title_19.setWordWrap(True)
        self.post_details_12 = QWidget(self.post_info_19)
        self.post_details_12.setObjectName(u"post_details_12")
        self.post_details_12.setGeometry(QRect(0, 60, 211, 31))
        self.post_details_12.setStyleSheet(u"QLabel {font: 400 12pt \"Manrope\";}")
        self.sales_type_14 = QLabel(self.post_details_12)
        self.sales_type_14.setObjectName(u"sales_type_14")
        self.sales_type_14.setGeometry(QRect(10, 10, 72, 16))
        self.live_date_14 = QLabel(self.post_details_12)
        self.live_date_14.setObjectName(u"live_date_14")
        self.live_date_14.setGeometry(QRect(130, 10, 55, 16))
        self.post_tags_19 = QWidget(self.post_info_19)
        self.post_tags_19.setObjectName(u"post_tags_19")
        self.post_tags_19.setGeometry(QRect(0, 30, 211, 31))
        self.post_tags_19.setStyleSheet(u"QLabel {\n"
"    font: 600 11pt \"Manrope\";\n"
"    color: rgb(137, 153, 211);\n"
"    text-align: center;\n"
"    background-color: #E8F3F2;\n"
"    border-radius: 5px;\n"
"}")
        self.tag_55 = QLabel(self.post_tags_19)
        self.tag_55.setObjectName(u"tag_55")
        self.tag_55.setGeometry(QRect(10, 10, 61, 16))
        self.tag_55.setStyleSheet(u"")
        self.tag_55.setAlignment(Qt.AlignCenter)
        self.tag_55.setMargin(1)
        self.tag_56 = QLabel(self.post_tags_19)
        self.tag_56.setObjectName(u"tag_56")
        self.tag_56.setGeometry(QRect(80, 10, 31, 16))
        self.tag_56.setStyleSheet(u"")
        self.tag_56.setAlignment(Qt.AlignCenter)
        self.tag_56.setMargin(1)
        self.tag_57 = QLabel(self.post_tags_19)
        self.tag_57.setObjectName(u"tag_57")
        self.tag_57.setGeometry(QRect(120, 10, 51, 16))
        self.tag_57.setStyleSheet(u"")
        self.tag_57.setAlignment(Qt.AlignCenter)
        self.tag_57.setMargin(1)
        self.post_type_14 = QLabel(self.post_sample_6)
        self.post_type_14.setObjectName(u"post_type_14")
        self.post_type_14.setGeometry(QRect(10, 10, 71, 16))
        self.post_type_14.setFont(font4)
        self.post_type_14.setStyleSheet(u"border-radius: 5px; padding:3px;\n"
"background-color: rgb(255, 245, 225);\n"
"color:rgb(206, 141, 80);")
        self.post_type_14.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.post_sample_6, 1, 1, 1, 1)

        self.posts_frame.setWidget(self.scrollAreaWidgetContents)
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
        self.page_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700; color:#000000\">Home</span></p></body></html>", None))
        self.curate_label.setText("")
        self.tagbutton.setText(QCoreApplication.translate("MainWindow", u"Coquette Fashion", None))
        self.post_image_16.setText("")
        self.post_title_16.setText(QCoreApplication.translate("MainWindow", u"Tagi Butter Apple Fan", None))
        self.sales_type_11.setText(QCoreApplication.translate("MainWindow", u"date posted", None))
        self.live_date_11.setText(QCoreApplication.translate("MainWindow", u"live date", None))
        self.tag_46.setText(QCoreApplication.translate("MainWindow", u"fan", None))
        self.tag_47.setText(QCoreApplication.translate("MainWindow", u"cute", None))
        self.tag_48.setText(QCoreApplication.translate("MainWindow", u"preorder", None))
        self.post_type_11.setText(QCoreApplication.translate("MainWindow", u"item", None))
        self.post_image_14.setText("")
        self.post_title_14.setText(QCoreApplication.translate("MainWindow", u"Odd Club School Keychains", None))
        self.sales_type_9.setText(QCoreApplication.translate("MainWindow", u"date posted", None))
        self.live_date_9.setText(QCoreApplication.translate("MainWindow", u"live date", None))
        self.tag_40.setText(QCoreApplication.translate("MainWindow", u"keychains", None))
        self.tag_41.setText(QCoreApplication.translate("MainWindow", u"cute", None))
        self.tag_42.setText(QCoreApplication.translate("MainWindow", u"doll", None))
        self.post_type_9.setText(QCoreApplication.translate("MainWindow", u"collection", None))
        self.post_image_17.setText("")
        self.post_title_17.setText(QCoreApplication.translate("MainWindow", u"Jellyfish Keychain", None))
        self.sales_type_12.setText(QCoreApplication.translate("MainWindow", u"date posted", None))
        self.live_date_12.setText(QCoreApplication.translate("MainWindow", u"live date", None))
        self.tag_49.setText(QCoreApplication.translate("MainWindow", u"jellyfish", None))
        self.tag_50.setText(QCoreApplication.translate("MainWindow", u"cute", None))
        self.tag_51.setText(QCoreApplication.translate("MainWindow", u"handmade", None))
        self.post_type_12.setText(QCoreApplication.translate("MainWindow", u"collection", None))
        self.post_image_15.setText("")
        self.post_title_15.setText(QCoreApplication.translate("MainWindow", u"Mona Tops Collection", None))
        self.sales_type_10.setText(QCoreApplication.translate("MainWindow", u"date posted", None))
        self.live_date_10.setText(QCoreApplication.translate("MainWindow", u"live date", None))
        self.tag_43.setText(QCoreApplication.translate("MainWindow", u"secondhand", None))
        self.tag_44.setText(QCoreApplication.translate("MainWindow", u"fashion", None))
        self.tag_45.setText(QCoreApplication.translate("MainWindow", u"preorder", None))
        self.post_type_10.setText(QCoreApplication.translate("MainWindow", u"collection", None))
        self.post_image_18.setText("")
        self.post_title_18.setText(QCoreApplication.translate("MainWindow", u"Vintage Blankets", None))
        self.sales_type_13.setText(QCoreApplication.translate("MainWindow", u"date posted", None))
        self.live_date_13.setText(QCoreApplication.translate("MainWindow", u"live date", None))
        self.tag_52.setText(QCoreApplication.translate("MainWindow", u"coquette", None))
        self.tag_53.setText(QCoreApplication.translate("MainWindow", u"cute", None))
        self.tag_54.setText(QCoreApplication.translate("MainWindow", u"jewelry", None))
        self.post_type_13.setText(QCoreApplication.translate("MainWindow", u"collection", None))
        self.post_image_19.setText("")
        self.post_title_19.setText(QCoreApplication.translate("MainWindow", u"Crocheted Hats", None))
        self.sales_type_14.setText(QCoreApplication.translate("MainWindow", u"date posted", None))
        self.live_date_14.setText(QCoreApplication.translate("MainWindow", u"live date", None))
        self.tag_55.setText(QCoreApplication.translate("MainWindow", u"handmade", None))
        self.tag_56.setText(QCoreApplication.translate("MainWindow", u"preorder", None))
        self.tag_57.setText(QCoreApplication.translate("MainWindow", u"custom", None))
        self.post_type_14.setText(QCoreApplication.translate("MainWindow", u"collection", None))
    # retranslateUi

