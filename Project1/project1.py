# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eid_proj_1.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Adafruit_DHT as ada
import sys
import time

class Ui_Dialog(QtWidgets.QWidget):
    count = 0
    error_sig = QtCore.pyqtSignal()
    humidity,temp=(0,0)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Dialog):
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.timer_handle)
        self.error_sig.connect(self.pop_up)

        Dialog.setObjectName("Dialog")
        Dialog.resize(543, 474)
        self.Temp_LE = QtWidgets.QLineEdit(Dialog)
        self.Temp_LE.setGeometry(QtCore.QRect(30, 50, 351, 25))
        self.Temp_LE.setReadOnly(True)
        self.Temp_LE.setObjectName("Temp_LE")
        self.Hum_LE = QtWidgets.QLineEdit(Dialog)
        self.Hum_LE.setGeometry(QtCore.QRect(30, 160, 351, 25))
        self.Hum_LE.setReadOnly(True)
        self.Hum_LE.setObjectName("Hum_LE")
        self.Temp = QtWidgets.QPushButton(Dialog)
        self.Temp.setGeometry(QtCore.QRect(30, 90, 112, 34))
        self.Temp.setObjectName("Temp")
        self.Humidity = QtWidgets.QPushButton(Dialog)
        self.Humidity.setGeometry(QtCore.QRect(30, 200, 131, 34))
        self.Humidity.setObjectName("Humidity")
        self.Temp_Label = QtWidgets.QLabel(Dialog)
        self.Temp_Label.setGeometry(QtCore.QRect(30, 20, 111, 19))
        self.Temp_Label.setObjectName("Temp_Label")
        self.Humidity_Label = QtWidgets.QLabel(Dialog)
        self.Humidity_Label.setGeometry(QtCore.QRect(30, 130, 81, 19))
        self.Humidity_Label.setObjectName("Humidity_Label")
        self.Avg_Temp_LE = QtWidgets.QLineEdit(Dialog)
        self.Avg_Temp_LE.setGeometry(QtCore.QRect(30, 290, 113, 25))
        self.Avg_Temp_LE.setObjectName("Avg_Temp_LE")
        self.Avg_Hum_LE = QtWidgets.QLineEdit(Dialog)
        self.Avg_Hum_LE.setGeometry(QtCore.QRect(280, 290, 113, 25))
        self.Avg_Hum_LE.setReadOnly(True)
        self.Avg_Hum_LE.setObjectName("Avg_Hum_LE")
        self.Avg_Temp = QtWidgets.QLabel(Dialog)
        self.Avg_Temp.setGeometry(QtCore.QRect(30, 250, 121, 19))
        self.Avg_Temp.setObjectName("Avg_Temp")
        self.Avg_Hum = QtWidgets.QLabel(Dialog)
        self.Avg_Hum.setGeometry(QtCore.QRect(280, 250, 151, 19))
        self.Avg_Hum.setObjectName("Avg_Hum")
        self.Hour_disp = QtWidgets.QLCDNumber(Dialog)
        self.Hour_disp.setGeometry(QtCore.QRect(120, 380, 81, 71))
        self.Hour_disp.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Hour_disp.setSmallDecimalPoint(False)
        self.Hour_disp.setDigitCount(2)
        self.Hour_disp.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.Hour_disp.setProperty("value", 16.0)
        self.Hour_disp.setObjectName("Hour_disp")
        self.colon_label = QtWidgets.QLabel(Dialog)
        self.colon_label.setGeometry(QtCore.QRect(210, 370, 21, 91))
        self.colon_label.setLineWidth(2)
        self.colon_label.setObjectName("colon_label")
        self.Min_lcd = QtWidgets.QLCDNumber(Dialog)
        self.Min_lcd.setGeometry(QtCore.QRect(220, 380, 71, 71))
        self.Min_lcd.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Min_lcd.setDigitCount(2)
        self.Min_lcd.setProperty("value", 2.0)
        self.Min_lcd.setObjectName("Min_lcd")
        self.Date_line = QtWidgets.QLineEdit(Dialog)
        self.Date_line.setGeometry(QtCore.QRect(322, 404, 161, 31))
        self.Date_line.setReadOnly(True)
        self.Date_line.setObjectName("Date_line")
        self.timer.start(1000)

        self.retranslateUi(Dialog)
        self.Temp.clicked.connect(self.temp_query)
        self.Humidity.clicked.connect(self.hum_query)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        self._translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(self._translate("Dialog", "Dialog"))
        self.Temp.setText(self._translate("Dialog", "Query Temp"))
        self.Humidity.setText(self._translate("Dialog", "Query Humidity"))
        self.Temp_Label.setText(self._translate("Dialog", "Temperature:"))
        self.Humidity_Label.setText(self._translate("Dialog", "Humidity:"))
        self.Avg_Temp.setText(self._translate("Dialog", "Average Temp:"))
        self.Avg_Hum.setText(self._translate("Dialog", "Average Humidity:"))
        self.colon_label.setText(self._translate("Dialog", ":"))
    
    
    def temp_query(self):
        self.humidity,self.temp = ada.read_retry(22,4)
        if(self.humidity == None):
            self.error_sig.emit()
            return
        temp_string = '{0:.2f}'.format(self.temp)
        self.Temp_LE.setText(self._translate("Dialog",temp_string))
        self.humidity ,self.temp = (0,0)

    def hum_query(self):
        self.humidity,self.temp = ada.read_retry(22,4)
        hum_string = '{0:.2f}'.format(self.humidity)
        self.Hum_LE.setText(self._translate("Dialog",hum_string))
        self.humidity ,self.temp = (0,0)

    def timer_handle(self):
        print("tick")
        self.count = self.count + 1

    def pop_up(self):
        print("error")
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_Dialog()
    ex.show()
    sys.exit(app.exec_())
