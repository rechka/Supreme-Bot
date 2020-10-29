from PyQt5 import QtCore, QtGui, QtWidgets
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from config import product

import time
import xml.etree.ElementTree as ET
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(660, 575)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.itemFrame = QtWidgets.QFrame(self.centralwidget)
        self.itemFrame.setGeometry(QtCore.QRect(0, 20, 651, 291))
        self.itemFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.itemFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.itemFrame.setObjectName("itemFrame")
        self.formLayoutWidget = QtWidgets.QWidget(self.itemFrame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 221, 261))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.catLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.catLabel.setFont(font)
        self.catLabel.setObjectName("catLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.catLabel)
        self.catCbox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.catCbox.setAcceptDrops(True)
        self.catCbox.setObjectName("catCbox")
        self.catCbox.addItem("")
        self.catCbox.addItem("")
        self.catCbox.addItem("")
        self.catCbox.addItem("")
        self.catCbox.addItem("")
        self.catCbox.addItem("")
        self.catCbox.addItem("")
        self.catCbox.addItem("")
        self.catCbox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.catCbox)
        self.sizeLab = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sizeLab.setFont(font)
        self.sizeLab.setObjectName("sizeLab")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.sizeLab)
        self.sizeCbox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.sizeCbox.setAcceptDrops(True)
        self.sizeCbox.setObjectName("sizeCbox")
        self.sizeCbox.addItem("")
        self.sizeCbox.addItem("")
        self.sizeCbox.addItem("")
        self.sizeCbox.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sizeCbox)
        self.colorLab = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.colorLab.setFont(font)
        self.colorLab.setObjectName("colorLab")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.colorLab)
        self.ocolorLine = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.ocolorLine.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ocolorLine.setFont(font)
        self.ocolorLine.setText("")
        self.ocolorLine.setObjectName("ocolorLine")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.ocolorLine)
        self.keyLab = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.keyLab.setFont(font)
        self.keyLab.setObjectName("keyLab")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.keyLab)
        self.keyLine = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.keyLine.setEnabled(True)
        self.keyLine.setObjectName("keyLine")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.keyLine)
        self.addBut = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.addBut.setFont(font)
        self.addBut.setObjectName("addBut")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.addBut)
        self.deleteBut = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.deleteBut.setFont(font)
        self.deleteBut.setObjectName("deleteBut")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.deleteBut)
        self.colorCombo = QtWidgets.QComboBox(self.formLayoutWidget)
        self.colorCombo.setAcceptDrops(True)
        self.colorCombo.setObjectName("colorCombo")
        self.colorCombo.addItem("")
        self.colorCombo.addItem("")
        self.colorCombo.addItem("")
        self.colorCombo.addItem("")
        self.colorCombo.addItem("")
        self.colorCombo.addItem("")
        self.colorCombo.addItem("")
        self.colorCombo.addItem("")
        self.colorCombo.addItem("")
        self.colorCombo.addItem("")
        self.colorCombo.addItem("")
        self.colorCombo.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.colorCombo)
        self.tableWidget = QtWidgets.QTableWidget(self.itemFrame)
        self.tableWidget.setGeometry(QtCore.QRect(240, 10, 401, 275))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.bilFrame = QtWidgets.QFrame(self.centralwidget)
        self.bilFrame.setGeometry(QtCore.QRect(0, 310, 341, 171))
        self.bilFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bilFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bilFrame.setObjectName("bilFrame")
        self.gridLayoutWidget = QtWidgets.QWidget(self.bilFrame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 321, 91))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.nameLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nameLine.setFont(font)
        self.nameLine.setInputMask("")
        self.nameLine.setText("")
        self.nameLine.setObjectName("nameLine")
        self.gridLayout.addWidget(self.nameLine, 0, 0, 1, 1)
        self.numberLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.numberLine.setFont(font)
        self.numberLine.setText("")
        self.numberLine.setObjectName("numberLine")
        self.gridLayout.addWidget(self.numberLine, 3, 0, 1, 1)
        self.emailLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.emailLine.setFont(font)
        self.emailLine.setText("")
        self.emailLine.setObjectName("emailLine")
        self.gridLayout.addWidget(self.emailLine, 2, 0, 1, 1)
        self.addressLine = QtWidgets.QLineEdit(self.bilFrame)
        self.addressLine.setGeometry(QtCore.QRect(10, 100, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.addressLine.setFont(font)
        self.addressLine.setText("")
        self.addressLine.setObjectName("addressLine")
        self.aptLine = QtWidgets.QLineEdit(self.bilFrame)
        self.aptLine.setGeometry(QtCore.QRect(230, 100, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.aptLine.setFont(font)
        self.aptLine.setText("")
        self.aptLine.setObjectName("aptLine")
        self.zipLine = QtWidgets.QLineEdit(self.bilFrame)
        self.zipLine.setGeometry(QtCore.QRect(10, 130, 75, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.zipLine.setFont(font)
        self.zipLine.setText("")
        self.zipLine.setObjectName("zipLine")
        self.stateCbox = QtWidgets.QComboBox(self.bilFrame)
        self.stateCbox.setGeometry(QtCore.QRect(180, 130, 69, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.stateCbox.setFont(font)
        self.stateCbox.setObjectName("stateCbox")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.stateCbox.addItem("")
        self.countryCbox = QtWidgets.QComboBox(self.bilFrame)
        self.countryCbox.setGeometry(QtCore.QRect(260, 130, 69, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.countryCbox.setFont(font)
        self.countryCbox.setObjectName("countryCbox")
        self.countryCbox.addItem("")
        self.countryCbox.addItem("")
        self.countryCbox.addItem("")
        self.cityLine = QtWidgets.QLineEdit(self.bilFrame)
        self.cityLine.setGeometry(QtCore.QRect(90, 130, 75, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cityLine.setFont(font)
        self.cityLine.setText("")
        self.cityLine.setObjectName("cityLine")
        self.ccFrame = QtWidgets.QFrame(self.centralwidget)
        self.ccFrame.setGeometry(QtCore.QRect(0, 480, 341, 71))
        self.ccFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ccFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ccFrame.setObjectName("ccFrame")
        self.ccnLine = QtWidgets.QLineEdit(self.ccFrame)
        self.ccnLine.setGeometry(QtCore.QRect(10, 10, 321, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ccnLine.setFont(font)
        self.ccnLine.setText("")
        self.ccnLine.setObjectName("ccnLine")
        self.expmCbox = QtWidgets.QComboBox(self.ccFrame)
        self.expmCbox.setGeometry(QtCore.QRect(10, 40, 69, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.expmCbox.setFont(font)
        self.expmCbox.setObjectName("expmCbox")
        self.expmCbox.addItem("")
        self.expmCbox.addItem("")
        self.expmCbox.addItem("")
        self.expmCbox.addItem("")
        self.expmCbox.addItem("")
        self.expmCbox.addItem("")
        self.expmCbox.addItem("")
        self.expmCbox.addItem("")
        self.expmCbox.addItem("")
        self.expmCbox.addItem("")
        self.expmCbox.addItem("")
        self.expmCbox.addItem("")
        self.expyCbox = QtWidgets.QComboBox(self.ccFrame)
        self.expyCbox.setGeometry(QtCore.QRect(90, 40, 69, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.expyCbox.setFont(font)
        self.expyCbox.setObjectName("expyCbox")
        self.expyCbox.addItem("")
        self.expyCbox.addItem("")
        self.expyCbox.addItem("")
        self.expyCbox.addItem("")
        self.expyCbox.addItem("")
        self.expyCbox.addItem("")
        self.expyCbox.addItem("")
        self.expyCbox.addItem("")
        self.expyCbox.addItem("")
        self.expyCbox.addItem("")
        self.expyCbox.addItem("")
        self.cvvLine = QtWidgets.QLineEdit(self.ccFrame)
        self.cvvLine.setGeometry(QtCore.QRect(170, 40, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cvvLine.setFont(font)
        self.cvvLine.setText("")
        self.cvvLine.setObjectName("cvvLine")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(340, 420, 311, 131))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.startBut = QtWidgets.QPushButton(self.frame)
        self.startBut.setGeometry(QtCore.QRect(10, 10, 291, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.startBut.setFont(font)
        self.startBut.setObjectName("startBut")
        self.pauseBut = QtWidgets.QPushButton(self.frame)
        self.pauseBut.setEnabled(False)
        self.pauseBut.setGeometry(QtCore.QRect(10, 70, 131, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pauseBut.setFont(font)
        self.pauseBut.setObjectName("pauseBut")
        self.exitBut = QtWidgets.QPushButton(self.frame)
        self.exitBut.setGeometry(QtCore.QRect(150, 70, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exitBut.setFont(font)
        self.exitBut.setObjectName("exitBut")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        
        self.retranslateUi(MainWindow)
        
        self.addBut.clicked.connect(self.addTolist)
        self.deleteBut.clicked.connect(self.removeFromlist)
        
        self.exitBut.clicked.connect(MainWindow.close)
        self.startBut.clicked.connect(self.initial)
        self.startBut.clicked.connect(self.fillout)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Supreme Bot"))
        self.label.setText(_translate("MainWindow", "Supreme Bot by Yeram Hwang"))
        self.catLabel.setText(_translate("MainWindow", "Category"))
        self.catCbox.setItemText(0, _translate("MainWindow", "Jackets"))
        self.catCbox.setItemText(1, _translate("MainWindow", "Shirts"))
        self.catCbox.setItemText(2, _translate("MainWindow", "Top/Sweater"))
        self.catCbox.setItemText(3, _translate("MainWindow", "Pants"))
        self.catCbox.setItemText(4, _translate("MainWindow", "Shorts"))
        self.catCbox.setItemText(5, _translate("MainWindow", "Hats"))
        self.catCbox.setItemText(6, _translate("MainWindow", "Bags"))
        self.catCbox.setItemText(7, _translate("MainWindow", "Acc"))
        self.catCbox.setItemText(8, _translate("MainWindow", "Skate"))
        self.sizeLab.setText(_translate("MainWindow", "Size"))
        self.sizeCbox.setItemText(0, _translate("MainWindow", "S"))
        self.sizeCbox.setItemText(1, _translate("MainWindow", "M"))
        self.sizeCbox.setItemText(2, _translate("MainWindow", "L"))
        self.sizeCbox.setItemText(3, _translate("MainWindow", "XL"))
        self.colorLab.setText(_translate("MainWindow", "Color"))
        self.ocolorLine.setPlaceholderText(_translate("MainWindow", "Enter Color if not listed."))
        self.keyLab.setText(_translate("MainWindow", "Key Word"))
        self.addBut.setText(_translate("MainWindow", "Add"))
        self.deleteBut.setText(_translate("MainWindow", "Remove"))
        self.colorCombo.setItemText(0, _translate("MainWindow", "Red"))
        self.colorCombo.setItemText(1, _translate("MainWindow", "Orange"))
        self.colorCombo.setItemText(2, _translate("MainWindow", "Yellow"))
        self.colorCombo.setItemText(3, _translate("MainWindow", "Green"))
        self.colorCombo.setItemText(4, _translate("MainWindow", "Blue"))
        self.colorCombo.setItemText(5, _translate("MainWindow", "Navy"))
        self.colorCombo.setItemText(6, _translate("MainWindow", "Purple"))
        self.colorCombo.setItemText(7, _translate("MainWindow", "Black"))
        self.colorCombo.setItemText(8, _translate("MainWindow", "White"))
        self.colorCombo.setItemText(9, _translate("MainWindow", "Tan"))
        self.colorCombo.setItemText(10, _translate("MainWindow", "Olive"))
        self.colorCombo.setItemText(11, _translate("MainWindow", "Others"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Category"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Size"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Color"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Key Word"))
        self.nameLine.setPlaceholderText(_translate("MainWindow", "Full Name (F+L)"))
        self.numberLine.setPlaceholderText(_translate("MainWindow", "Phone Number"))
        self.emailLine.setPlaceholderText(_translate("MainWindow", "Email"))
        self.addressLine.setPlaceholderText(_translate("MainWindow", "Address"))
        self.aptLine.setPlaceholderText(_translate("MainWindow", "APT#"))
        self.zipLine.setPlaceholderText(_translate("MainWindow", "ZIP"))
        self.stateCbox.setItemText(0, _translate("MainWindow", "AK"))
        self.stateCbox.setItemText(1, _translate("MainWindow", "AL"))
        self.stateCbox.setItemText(2, _translate("MainWindow", "AR"))
        self.stateCbox.setItemText(3, _translate("MainWindow", "AZ"))
        self.stateCbox.setItemText(4, _translate("MainWindow", "CA"))
        self.stateCbox.setItemText(5, _translate("MainWindow", "CO"))
        self.stateCbox.setItemText(6, _translate("MainWindow", "CT"))
        self.stateCbox.setItemText(7, _translate("MainWindow", "DE"))
        self.stateCbox.setItemText(8, _translate("MainWindow", "FL"))
        self.stateCbox.setItemText(9, _translate("MainWindow", "GA"))
        self.stateCbox.setItemText(10, _translate("MainWindow", "HI"))
        self.stateCbox.setItemText(11, _translate("MainWindow", "IA"))
        self.stateCbox.setItemText(12, _translate("MainWindow", "ID"))
        self.stateCbox.setItemText(13, _translate("MainWindow", "IL"))
        self.stateCbox.setItemText(14, _translate("MainWindow", "IN"))
        self.stateCbox.setItemText(15, _translate("MainWindow", "KS"))
        self.stateCbox.setItemText(16, _translate("MainWindow", "KY"))
        self.stateCbox.setItemText(17, _translate("MainWindow", "LA"))
        self.stateCbox.setItemText(18, _translate("MainWindow", "MA"))
        self.stateCbox.setItemText(19, _translate("MainWindow", "MD"))
        self.stateCbox.setItemText(20, _translate("MainWindow", "ME"))
        self.stateCbox.setItemText(21, _translate("MainWindow", "MI"))
        self.stateCbox.setItemText(22, _translate("MainWindow", "MN"))
        self.stateCbox.setItemText(23, _translate("MainWindow", "MO"))
        self.stateCbox.setItemText(24, _translate("MainWindow", "MS"))
        self.stateCbox.setItemText(25, _translate("MainWindow", "MT"))
        self.stateCbox.setItemText(26, _translate("MainWindow", "NC"))
        self.stateCbox.setItemText(27, _translate("MainWindow", "ND"))
        self.stateCbox.setItemText(28, _translate("MainWindow", "NE"))
        self.stateCbox.setItemText(29, _translate("MainWindow", "NH"))
        self.stateCbox.setItemText(30, _translate("MainWindow", "NJ"))
        self.stateCbox.setItemText(31, _translate("MainWindow", "NM"))
        self.stateCbox.setItemText(32, _translate("MainWindow", "NV"))
        self.stateCbox.setItemText(33, _translate("MainWindow", "NY"))
        self.stateCbox.setItemText(34, _translate("MainWindow", "OH"))
        self.stateCbox.setItemText(35, _translate("MainWindow", "OK"))
        self.stateCbox.setItemText(36, _translate("MainWindow", "OR"))
        self.stateCbox.setItemText(37, _translate("MainWindow", "PA"))
        self.stateCbox.setItemText(38, _translate("MainWindow", "RI"))
        self.stateCbox.setItemText(39, _translate("MainWindow", "SC"))
        self.stateCbox.setItemText(40, _translate("MainWindow", "SD"))
        self.stateCbox.setItemText(41, _translate("MainWindow", "TN"))
        self.stateCbox.setItemText(42, _translate("MainWindow", "TX"))
        self.stateCbox.setItemText(43, _translate("MainWindow", "UT"))
        self.stateCbox.setItemText(44, _translate("MainWindow", "VA"))
        self.stateCbox.setItemText(45, _translate("MainWindow", "VT"))
        self.stateCbox.setItemText(46, _translate("MainWindow", "WA"))
        self.stateCbox.setItemText(47, _translate("MainWindow", "WI"))
        self.stateCbox.setItemText(48, _translate("MainWindow", "WV"))
        self.stateCbox.setItemText(49, _translate("MainWindow", "WY"))
        self.countryCbox.setItemText(0, _translate("MainWindow", "USA"))
        self.countryCbox.setItemText(1, _translate("MainWindow", "Mexico"))
        self.countryCbox.setItemText(2, _translate("MainWindow", "Canada"))
        self.cityLine.setPlaceholderText(_translate("MainWindow", "City"))
        self.ccnLine.setPlaceholderText(_translate("MainWindow", "Credit Card Number"))
        self.expmCbox.setItemText(0, _translate("MainWindow", "Jan"))
        self.expmCbox.setItemText(1, _translate("MainWindow", "Feb"))
        self.expmCbox.setItemText(2, _translate("MainWindow", "Mar"))
        self.expmCbox.setItemText(3, _translate("MainWindow", "Apr"))
        self.expmCbox.setItemText(4, _translate("MainWindow", "May"))
        self.expmCbox.setItemText(5, _translate("MainWindow", "Jun"))
        self.expmCbox.setItemText(6, _translate("MainWindow", "Jul"))
        self.expmCbox.setItemText(7, _translate("MainWindow", "Aug"))
        self.expmCbox.setItemText(8, _translate("MainWindow", "Sept"))
        self.expmCbox.setItemText(9, _translate("MainWindow", "Oct"))
        self.expmCbox.setItemText(10, _translate("MainWindow", "Nov"))
        self.expmCbox.setItemText(11, _translate("MainWindow", "Dec"))
        self.expyCbox.setItemText(0, _translate("MainWindow", "2020"))
        self.expyCbox.setItemText(1, _translate("MainWindow", "2021"))
        self.expyCbox.setItemText(2, _translate("MainWindow", "2022"))
        self.expyCbox.setItemText(3, _translate("MainWindow", "2023"))
        self.expyCbox.setItemText(4, _translate("MainWindow", "2024"))
        self.expyCbox.setItemText(5, _translate("MainWindow", "2025"))
        self.expyCbox.setItemText(6, _translate("MainWindow", "2026"))
        self.expyCbox.setItemText(7, _translate("MainWindow", "2027"))
        self.expyCbox.setItemText(8, _translate("MainWindow", "2028"))
        self.expyCbox.setItemText(9, _translate("MainWindow", "2029"))
        self.expyCbox.setItemText(10, _translate("MainWindow", "2030"))
        self.cvvLine.setPlaceholderText(_translate("MainWindow", "CVV"))
        self.startBut.setText(_translate("MainWindow", "START!!!"))
        self.pauseBut.setText(_translate("MainWindow", "PAUSE"))
        self.exitBut.setText(_translate("MainWindow", "EXIT"))
        
    def initial(self, MainWindow):
        # load chrome
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())

        # Goto Surpeme url
        driver.get('https://www.supremenewyork.com/shop/all')

        # Find items
        
        # Category selector
        category = driver.find_element_by_link_text(product['category'])
        category.click()
        time.sleep(1)

        # Item selector
        item = driver.find_element_by_partial_link_text(product['keyword'])
        item.click()
        time.sleep(1)

        # Color selector
        w = "//button[@data-style-name='" + product['color']+ "']"
        color = driver.find_element_by_xpath(w)
        color.click()
        time.sleep(.5)

        # Size selector option 3 is for large
        size = driver.find_element_by_xpath("//*[@id='s']/option[3]")
        size.click()

        # Add to cart
        add = driver.find_element_by_xpath("//input[@name='commit']")
        add.click()
        time.sleep(.5)

        # To cart
        checkout = driver.find_element_by_xpath("//a[@class='button checkout']")
        checkout.click()
        
    def fillout(self, MainWindow):
        # wait for checkout button element to load
        time.sleep(.3)
        tree = ET.parse('savedbinfo.xml')
        root = tree.getroot()


        # fill out checkout screen fields
        driver.find_element_by_id('order_billing_name').send_keys(root[0].text)
        driver.find_element_by_id('order_email').send_keys(root[1].text)
        driver.find_element_by_id('order_tel').send_keys(root[2].text)
        driver.find_element_by_id('bo').send_keys(root[3].text)
        driver.find_element_by_id('oba3').send_keys(root[4].text)
        driver.find_element_by_id('order_billing_zip').send_keys(root[5].text)
        driver.find_element_by_id('order_billing_city').send_keys(root[6].text)
        
        driver.find_element_by_id('order_billing_state').send_keys(root[7].text)
        driver.find_element_by_id('order_billing_country').send_keys(root[8].text)

        # Credit Card info section
        tree = ET.parse('savedcinfo.xml')
        root = tree.getroot()
        
        driver.find_element_by_id('rnsnckrn').send_keys(root[0].text)
        driver.find_element_by_name('credit_card[month]').send_keys(root[1].text)
        driver.find_element_by_name('credit_card[year]').send_keys(root[2].text)
        driver.find_element_by_id('orcer').send_keys(root[3].text)

        # Process save address and term&condition check box click
        for combo in driver.find_elements_by_css_selector('.iCheck-helper'):
            combo.click()
        
        # Click process payment 
        driver.find_element_by_name('commit').click()

    def addTolist(self, MainWindow): 
        print(self.catCbox.currentText())
        print(self.sizeCbox.currentText())
        print(self.colorCombo.currentText())
        print(self.keyLine.text())
        
        
        self.tableWidget.insertRow(0)
        #self.tableWidget.set
    
    def removeFromlist():
        pass
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())