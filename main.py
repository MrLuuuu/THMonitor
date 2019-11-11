# -*- coding: utf-8 -*-

from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtWidgets import QMainWindow,QApplication,QDialog,QWidget,QButtonGroup,QGroupBox,QMessageBox,QTextEdit
from PyQt5.QtCore import QTimer
import sys
import time
import os
import serial
import mainwindow
from mainwindow import Ui_Dialog_Main

global recv_data # 全部下位机数据暂存
recv_data={"Humidity":'10',"Temperature":'27'} # 默认测试数据

class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__(parent=None)
        # 主界面实例化
        print("主界面正在实例化")

        # 读取串口
        try:
            self.serial=serial.Serial(port='COM3',baudrate=9600)
            print("串口打开成功")
        except:
            print("串口打开失败")

        self.window=QMainWindow(self)
        self.window_ui=Ui_Dialog_Main()
        self.window_ui.setupUi(self.window)
        # 完成主界面与主UI的绑定

        self.timer_refresh=QTimer(self)
        self.timer_refresh.timeout.connect(self.Refresh)
        self.timer_refresh.start(1500)
        # 绑定数据刷新函数，定时刷新数据

    def showall(self):
        self.window.show()
        pass

    # 刷新LCD数据
    def Refresh(self):
        try:
            recv=self.serial.read(9)
            recv=recv.decode(encoding='ascii')
            Humidity=recv[2:4]
            Temp=recv[7:9]
        except:
            global recv_data
            Temp, Humidity = recv_data["Temperature"], recv_data["Humidity"]
        # print(Temp,Humidity)
        self.window_ui.lcd_T.display(Temp)
        self.window_ui.lcd_H.display(Humidity)


if __name__=='__main__':
    app=QApplication(sys.argv)
    myWindow=MyMainWindow()
    myWindow.showall()
    sys.exit(app.exec_())

