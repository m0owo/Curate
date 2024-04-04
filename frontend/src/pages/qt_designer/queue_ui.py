# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'queue.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 500)
        Form.setMinimumSize(QSize(400, 500))
        Form.setMaximumSize(QSize(400, 500))
        Form.setStyleSheet(u"* {\n"
"	color: black;\n"
"}\n"
"\n"
"#Form {\n"
"	background-color: white;\n"
"}\n"
"\n"
"#scrollArea {\n"
"	border-width: 1px;\n"
"    border-color:rgb(154, 152, 148);\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #FFFFFF;\n"
"    border-radius: 10px;\n"
"    border: solid;\n"
"    border-width: 1px;\n"
"    border-color:rgb(154, 152, 148);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: #CCCCCC;\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Manrope"])
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 380, 392))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.username_1 = QLabel(self.scrollAreaWidgetContents)
        self.username_1.setObjectName(u"username_1")
        font1 = QFont()
        font1.setFamilies([u"Manrope"])
        font1.setPointSize(14)
        self.username_1.setFont(font1)

        self.verticalLayout_2.addWidget(self.username_1)

        self.username_2 = QLabel(self.scrollAreaWidgetContents)
        self.username_2.setObjectName(u"username_2")
        self.username_2.setFont(font1)

        self.verticalLayout_2.addWidget(self.username_2)

        self.username_3 = QLabel(self.scrollAreaWidgetContents)
        self.username_3.setObjectName(u"username_3")
        self.username_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.username_3)

        self.verticalSpacer = QSpacerItem(20, 275, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.queue_button = QPushButton(Form)
        self.queue_button.setObjectName(u"queue_button")
        self.queue_button.setMinimumSize(QSize(0, 35))
        font2 = QFont()
        font2.setPointSize(16)
        self.queue_button.setFont(font2)

        self.verticalLayout.addWidget(self.queue_button)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Current Queue", None))
        self.username_1.setText(QCoreApplication.translate("Form", u"1. username_1", None))
        self.username_2.setText(QCoreApplication.translate("Form", u"2. username_2", None))
        self.username_3.setText(QCoreApplication.translate("Form", u"3.username_3", None))
        self.queue_button.setText(QCoreApplication.translate("Form", u"Enqueue", None))
    # retranslateUi

