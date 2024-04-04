# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wishlist_box.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
from .posts_images_rc import *


class Ui_WishlistBox(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1080, 250)
        Form.setMinimumSize(QSize(1080, 250))
        Form.setMaximumSize(QSize(1080, 250))
        Form.setStyleSheet(u"* {\n"
"	color: black;\n"
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
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(20)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.product_frame_2 = QFrame(Form)
        self.product_frame_2.setObjectName(u"product_frame_2")
        self.product_frame_2.setMinimumSize(QSize(500, 0))
        self.product_frame_2.setMaximumSize(QSize(500, 16777215))
        self.product_frame_2.setStyleSheet(u"QFrame {\n"
"    background-color:#DFF1EE;\n"
"	border: none;\n"
"}")
        self.product_frame_2.setFrameShape(QFrame.StyledPanel)
        self.product_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.product_frame_2)
        self.horizontalLayout_9.setSpacing(20)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(20, 20, 20, 20)
        self.wl_product_image_label = QLabel(self.product_frame_2)
        self.wl_product_image_label.setObjectName(u"wl_product_image_label")
        self.wl_product_image_label.setMaximumSize(QSize(200, 200))
        self.wl_product_image_label.setStyleSheet(u"")
        self.wl_product_image_label.setPixmap(QPixmap(u":/post_images/IMG_7102.jpg"))
        self.wl_product_image_label.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.wl_product_image_label)

        self.frame_6 = QFrame(self.product_frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.wl_product_name_label = QLabel(self.frame_6)
        self.wl_product_name_label.setObjectName(u"wl_product_name_label")
        font = QFont()
        font.setFamilies([u"Manrope"])
        font.setPointSize(16)
        font.setBold(True)
        self.wl_product_name_label.setFont(font)

        self.verticalLayout_4.addWidget(self.wl_product_name_label)

        self.wl_shop_name_label = QLabel(self.frame_6)
        self.wl_shop_name_label.setObjectName(u"wl_shop_name_label")
        font1 = QFont()
        font1.setFamilies([u"Manrope"])
        font1.setPointSize(12)
        self.wl_shop_name_label.setFont(font1)

        self.verticalLayout_4.addWidget(self.wl_shop_name_label)

        self.verticalSpacer_4 = QSpacerItem(20, 92, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.wl_status_label = QLabel(self.frame_6)
        self.wl_status_label.setObjectName(u"wl_status_label")
        font2 = QFont()
        font2.setFamilies([u"Manrope"])
        font2.setPointSize(24)
        font2.setBold(True)
        self.wl_status_label.setFont(font2)
        self.wl_status_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.wl_status_label)


        self.horizontalLayout_9.addWidget(self.frame_6)


        self.horizontalLayout_8.addWidget(self.product_frame_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.info_frame_2 = QFrame(Form)
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
        self.information_label_2.setFont(font)

        self.verticalLayout_6.addWidget(self.information_label_2)

        self.wl_sale_date_label = QLabel(self.info_frame_2)
        self.wl_sale_date_label.setObjectName(u"wl_sale_date_label")
        font3 = QFont()
        font3.setFamilies([u"Manrope"])
        font3.setPointSize(13)
        font3.setBold(True)
        self.wl_sale_date_label.setFont(font3)

        self.verticalLayout_6.addWidget(self.wl_sale_date_label)

        self.wl_mode_label = QLabel(self.info_frame_2)
        self.wl_mode_label.setObjectName(u"wl_mode_label")
        self.wl_mode_label.setFont(font3)

        self.verticalLayout_6.addWidget(self.wl_mode_label)


        self.verticalLayout_5.addWidget(self.info_frame_2)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(14)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_3)

        self.wl_go_to_page_bt = QPushButton(Form)
        self.wl_go_to_page_bt.setObjectName(u"wl_go_to_page_bt")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wl_go_to_page_bt.sizePolicy().hasHeightForWidth())
        self.wl_go_to_page_bt.setSizePolicy(sizePolicy)
        self.wl_go_to_page_bt.setMinimumSize(QSize(0, 40))
        self.wl_go_to_page_bt.setFont(font3)

        self.horizontalLayout_10.addWidget(self.wl_go_to_page_bt)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)


        self.horizontalLayout_8.addLayout(self.verticalLayout_5)


        self.horizontalLayout.addLayout(self.horizontalLayout_8)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.wl_product_image_label.setText("")
        self.wl_product_name_label.setText(QCoreApplication.translate("Form", u"Product Name", None))
        self.wl_shop_name_label.setText(QCoreApplication.translate("Form", u"Shop Name", None))
        self.wl_status_label.setText(QCoreApplication.translate("Form", u"Starting", None))
        self.information_label_2.setText(QCoreApplication.translate("Form", u"Information", None))
        self.wl_sale_date_label.setText(QCoreApplication.translate("Form", u"Sale Date: Mon 26 Jan 19:00", None))
        self.wl_mode_label.setText(QCoreApplication.translate("Form", u"Mode:  CF no CC", None))
        self.wl_go_to_page_bt.setText(QCoreApplication.translate("Form", u"Go To Page", None))
    # retranslateUi

