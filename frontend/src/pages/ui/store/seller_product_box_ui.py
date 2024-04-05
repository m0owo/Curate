# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'seller_product_box.ui'
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

class Ui_ProductBox(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(863, 150)
        Form.setMinimumSize(QSize(0, 150))
        Form.setMaximumSize(QSize(16777215, 150))
        Form.setStyleSheet(u"QWidget {\n"
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
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.product_frame = QFrame(Form)
        self.product_frame.setObjectName(u"product_frame")
        self.product_frame.setMinimumSize(QSize(400, 0))
        self.product_frame.setMaximumSize(QSize(500, 16777215))
        self.product_frame.setStyleSheet(u"QFrame {\n"
"    background-color:#DFF1EE;\n"
"	border: none;\n"
"}")
        self.product_frame.setFrameShape(QFrame.StyledPanel)
        self.product_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.product_frame)
        self.horizontalLayout_18.setSpacing(15)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(20, 15, 20, 15)
        self.product_image_label = QLabel(self.product_frame)
        self.product_image_label.setObjectName(u"product_image_label")
        self.product_image_label.setMaximumSize(QSize(110, 110))
        self.product_image_label.setStyleSheet(u"")
        self.product_image_label.setPixmap(QPixmap(u":/post_images/IMG_7102.jpg"))
        self.product_image_label.setScaledContents(True)

        self.horizontalLayout_18.addWidget(self.product_image_label)

        self.frame_6 = QFrame(self.product_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.product_name_label = QLabel(self.frame_6)
        self.product_name_label.setObjectName(u"product_name_label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.product_name_label.sizePolicy().hasHeightForWidth())
        self.product_name_label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Manrope"])
        font.setPointSize(16)
        font.setBold(True)
        self.product_name_label.setFont(font)

        self.verticalLayout_14.addWidget(self.product_name_label)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_9)

        self.price_label = QLabel(self.frame_6)
        self.price_label.setObjectName(u"price_label")
        font1 = QFont()
        font1.setFamilies([u"Manrope"])
        font1.setPointSize(13)
        font1.setBold(True)
        self.price_label.setFont(font1)
        self.price_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_14.addWidget(self.price_label)


        self.horizontalLayout_18.addWidget(self.frame_6)


        self.horizontalLayout.addWidget(self.product_frame)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(10)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.info_frame = QFrame(Form)
        self.info_frame.setObjectName(u"info_frame")
        self.info_frame.setMinimumSize(QSize(0, 0))
        self.info_frame.setMaximumSize(QSize(16777215, 120))
        self.info_frame.setStyleSheet(u"QFrame {\n"
"    background-color:#E8F3F2;\n"
"	border: none;\n"
"}")
        self.info_frame.setFrameShape(QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.info_frame)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(20, 12, 20, 12)
        self.sale_date_label = QLabel(self.info_frame)
        self.sale_date_label.setObjectName(u"sale_date_label")
        self.sale_date_label.setFont(font1)

        self.verticalLayout_16.addWidget(self.sale_date_label)

        self.mode_label = QLabel(self.info_frame)
        self.mode_label.setObjectName(u"mode_label")
        self.mode_label.setFont(font1)

        self.verticalLayout_16.addWidget(self.mode_label)

        self.status_label = QLabel(self.info_frame)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setFont(font1)

        self.verticalLayout_16.addWidget(self.status_label)


        self.verticalLayout_15.addWidget(self.info_frame)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(14)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer)

        self.view_product_button = QPushButton(Form)
        self.view_product_button.setObjectName(u"view_product_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.view_product_button.sizePolicy().hasHeightForWidth())
        self.view_product_button.setSizePolicy(sizePolicy1)
        self.view_product_button.setMinimumSize(QSize(0, 30))
        self.view_product_button.setFont(font1)

        self.horizontalLayout_19.addWidget(self.view_product_button)


        self.verticalLayout_15.addLayout(self.horizontalLayout_19)


        self.horizontalLayout.addLayout(self.verticalLayout_15)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.product_image_label.setText("")
        self.product_name_label.setText(QCoreApplication.translate("Form", u"Product Name", None))
        self.price_label.setText(QCoreApplication.translate("Form", u"999 B", None))
        self.sale_date_label.setText(QCoreApplication.translate("Form", u"Sale Date: Mon 26 Jan 19:00", None))
        self.mode_label.setText(QCoreApplication.translate("Form", u"Mode:  CF no CC", None))
        self.status_label.setText(QCoreApplication.translate("Form", u"Status: Live", None))
        self.view_product_button.setText(QCoreApplication.translate("Form", u"Configure Product", None))
    # retranslateUi

