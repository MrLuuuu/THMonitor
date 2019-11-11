# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Main(object):
    def setupUi(self, Dialog_Main):
        Dialog_Main.setObjectName("Dialog_Main")
        Dialog_Main.resize(800, 500)
        self.label_Headline = QtWidgets.QLabel(Dialog_Main)
        self.label_Headline.setGeometry(QtCore.QRect(325, 20, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_Headline.setFont(font)
        self.label_Headline.setTextFormat(QtCore.Qt.AutoText)
        self.label_Headline.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Headline.setIndent(-1)
        self.label_Headline.setObjectName("label_Headline")
        self.label_Temp = QtWidgets.QLabel(Dialog_Main)
        self.label_Temp.setGeometry(QtCore.QRect(220, 160, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_Temp.setFont(font)
        self.label_Temp.setObjectName("label_Temp")
        self.label_Humidity = QtWidgets.QLabel(Dialog_Main)
        self.label_Humidity.setGeometry(QtCore.QRect(220, 290, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_Humidity.setFont(font)
        self.label_Humidity.setObjectName("label_Humidity")
        self.lcd_T = QtWidgets.QLCDNumber(Dialog_Main)
        self.lcd_T.setGeometry(QtCore.QRect(343, 142, 131, 61))
        self.lcd_T.setObjectName("lcd_T")
        self.lcd_H = QtWidgets.QLCDNumber(Dialog_Main)
        self.lcd_H.setGeometry(QtCore.QRect(343, 272, 131, 61))
        self.lcd_H.setObjectName("lcd_H")
        self.label_T_Company = QtWidgets.QLabel(Dialog_Main)
        self.label_T_Company.setGeometry(QtCore.QRect(500, 161, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_T_Company.setFont(font)
        self.label_T_Company.setObjectName("label_T_Company")
        self.label_H_Company = QtWidgets.QLabel(Dialog_Main)
        self.label_H_Company.setGeometry(QtCore.QRect(500, 301, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_H_Company.setFont(font)
        self.label_H_Company.setObjectName("label_H_Company")

        self.retranslateUi(Dialog_Main)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Main)

    def retranslateUi(self, Dialog_Main):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Main.setWindowTitle(_translate("Dialog_Main", "Dialog"))
        self.label_Headline.setText(_translate("Dialog_Main", "温湿度监测"))
        self.label_Temp.setText(_translate("Dialog_Main", "温度"))
        self.label_Humidity.setText(_translate("Dialog_Main", "湿度"))
        self.label_T_Company.setText(_translate("Dialog_Main", "摄氏度"))
        self.label_H_Company.setText(_translate("Dialog_Main", "%"))
