# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_address.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(600, 570)
        Dialog.setStyleSheet(u"QDialog{\n"
"	background-color: rgb(232, 243, 242);\n"
"}\n"
"QLabel{\n"
"	color: black;\n"
"	font-family: Manrope;\n"
"    font-size: 9;\n"
"}\n"
"")
        self.edit_address_label = QLabel(Dialog)
        self.edit_address_label.setObjectName(u"edit_address_label")
        self.edit_address_label.setGeometry(QRect(50, 20, 211, 51))
        font = QFont()
        font.setFamilies([u"Manrope"])
        font.setPointSize(20)
        font.setBold(True)
        self.edit_address_label.setFont(font)
        self.edit_widget = QWidget(Dialog)
        self.edit_widget.setObjectName(u"edit_widget")
        self.edit_widget.setGeometry(QRect(40, 70, 501, 481))
        self.edit_widget.setStyleSheet(u"QWidget{\n"
"	background-color: white;\n"
"	border-radius: 20px;\n"
"}\n"
"QLineEdit{\n"
"	color: black;\n"
"	font-family: Manrope;\n"
"    font-size: 10;\n"
"	background-color: rgb(231, 231, 231);\n"
"	border-radius: 8px;\n"
"}\n"
"QComboBox{\n"
"	color: black;\n"
"	font-family: Manrope;\n"
"    font-size: 10;\n"
"	background-color: rgb(231, 231, 231);\n"
"	border-radius: 8px;\n"
"}\n"
"QTextEdit{\n"
"	color: black;\n"
"	font-family: Manrope;\n"
"    font-size: 10;\n"
"	background-color: rgb(231, 231, 231);\n"
"	border-radius: 8px;\n"
"}\n"
"QPushButton{\n"
"	color: black;\n"
"	font-family: Manrope;\n"
"	background-color: None;\n"
"	border: 2px solid rgb(138, 138, 138);\n"
"	border-radius: 20px\n"
"}")
        self.name_label = QLabel(self.edit_widget)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(40, 30, 51, 21))
        font1 = QFont()
        font1.setFamilies([u"Manrope"])
        font1.setPointSize(9)
        self.name_label.setFont(font1)
        self.name_edit = QLineEdit(self.edit_widget)
        self.name_edit.setObjectName(u"name_edit")
        self.name_edit.setGeometry(QRect(40, 60, 201, 31))
        self.phone_number_edit = QLineEdit(self.edit_widget)
        self.phone_number_edit.setObjectName(u"phone_number_edit")
        self.phone_number_edit.setGeometry(QRect(270, 60, 201, 31))
        self.phone_number_label = QLabel(self.edit_widget)
        self.phone_number_label.setObjectName(u"phone_number_label")
        self.phone_number_label.setGeometry(QRect(270, 30, 161, 21))
        self.phone_number_label.setFont(font1)
        self.province_label = QLabel(self.edit_widget)
        self.province_label.setObjectName(u"province_label")
        self.province_label.setGeometry(QRect(40, 120, 61, 21))
        self.province_label.setFont(font1)
        self.province_combobox = QComboBox(self.edit_widget)
        self.province_combobox.setObjectName(u"province_combobox")
        self.province_combobox.setGeometry(QRect(40, 150, 201, 31))
        self.district_label = QLabel(self.edit_widget)
        self.district_label.setObjectName(u"district_label")
        self.district_label.setGeometry(QRect(270, 120, 61, 21))
        self.district_label.setFont(font1)
        self.district_combobox = QComboBox(self.edit_widget)
        self.district_combobox.setObjectName(u"district_combobox")
        self.district_combobox.setGeometry(QRect(270, 150, 201, 31))
        self.sub_district_label = QLabel(self.edit_widget)
        self.sub_district_label.setObjectName(u"sub_district_label")
        self.sub_district_label.setGeometry(QRect(40, 200, 91, 21))
        self.sub_district_label.setFont(font1)
        self.sub_district_combobox = QComboBox(self.edit_widget)
        self.sub_district_combobox.setObjectName(u"sub_district_combobox")
        self.sub_district_combobox.setGeometry(QRect(40, 230, 201, 31))
        self.postal_code_label = QLabel(self.edit_widget)
        self.postal_code_label.setObjectName(u"postal_code_label")
        self.postal_code_label.setGeometry(QRect(270, 200, 91, 21))
        self.postal_code_label.setFont(font1)
        self.postal_code_combobox = QComboBox(self.edit_widget)
        self.postal_code_combobox.setObjectName(u"postal_code_combobox")
        self.postal_code_combobox.setGeometry(QRect(270, 230, 201, 31))
        self.details_label = QLabel(self.edit_widget)
        self.details_label.setObjectName(u"details_label")
        self.details_label.setGeometry(QRect(40, 280, 231, 21))
        self.details_label.setFont(font1)
        self.details_textedit = QTextEdit(self.edit_widget)
        self.details_textedit.setObjectName(u"details_textedit")
        self.details_textedit.setGeometry(QRect(40, 310, 421, 87))
        self.cancel_button = QPushButton(self.edit_widget)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(200, 420, 131, 41))
        self.save_button = QPushButton(self.edit_widget)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(340, 420, 131, 41))
        self.save_button.setStyleSheet(u"background-color: rgb(88, 130, 126);\n"
"color: white;\n"
"border: None;")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.edit_address_label.setText(QCoreApplication.translate("Dialog", u"Edit Address", None))
        self.name_label.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.name_edit.setText(QCoreApplication.translate("Dialog", u"Firstname Surname", None))
        self.phone_number_edit.setText(QCoreApplication.translate("Dialog", u"000-000-0000", None))
        self.phone_number_label.setText(QCoreApplication.translate("Dialog", u"Phone Number", None))
        self.province_label.setText(QCoreApplication.translate("Dialog", u"Province", None))
        self.district_label.setText(QCoreApplication.translate("Dialog", u"District", None))
        self.sub_district_label.setText(QCoreApplication.translate("Dialog", u" Sub District", None))
        self.postal_code_label.setText(QCoreApplication.translate("Dialog", u"Postal Code", None))
        self.details_label.setText(QCoreApplication.translate("Dialog", u"Street Name, Building, House No.", None))
        self.cancel_button.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.save_button.setText(QCoreApplication.translate("Dialog", u"Save", None))
    # retranslateUi

