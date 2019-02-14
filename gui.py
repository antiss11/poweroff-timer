# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(454, 387)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.timeEdit.setFont(font)
        self.timeEdit.setObjectName("timeEdit")
        self.verticalLayout.addWidget(self.timeEdit)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.radioButton_in = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_in.setFont(font)
        self.radioButton_in.setObjectName("radioButton_in")
        self.buttonGroup_timer = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_timer.setObjectName("buttonGroup_timer")
        self.buttonGroup_timer.addButton(self.radioButton_in)
        self.verticalLayout.addWidget(self.radioButton_in)
        self.radioButton_after = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_after.setFont(font)
        self.radioButton_after.setObjectName("radioButton_after")
        self.buttonGroup_timer.addButton(self.radioButton_after)
        self.verticalLayout.addWidget(self.radioButton_after)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.radioButton_off = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_off.setFont(font)
        self.radioButton_off.setObjectName("radioButton_off")
        self.buttonGroup_action = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_action.setObjectName("buttonGroup_action")
        self.buttonGroup_action.addButton(self.radioButton_off)
        self.verticalLayout.addWidget(self.radioButton_off)
        self.radioButton_restart = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_restart.setFont(font)
        self.radioButton_restart.setObjectName("radioButton_restart")
        self.buttonGroup_action.addButton(self.radioButton_restart)
        self.verticalLayout.addWidget(self.radioButton_restart)
        self.radioButton_sleep = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_sleep.setFont(font)
        self.radioButton_sleep.setObjectName("radioButton_sleep")
        self.buttonGroup_action.addButton(self.radioButton_sleep)
        self.verticalLayout.addWidget(self.radioButton_sleep)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("pushButton_start")
        self.verticalLayout.addWidget(self.pushButton_start)
        self.pushButton_stop = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_stop.setFont(font)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.verticalLayout.addWidget(self.pushButton_stop)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.timeEdit.setDisplayFormat(_translate("MainWindow", "HH:mm:ss"))
        self.radioButton_in.setText(_translate("MainWindow", "In"))
        self.radioButton_after.setText(_translate("MainWindow", "After"))
        self.radioButton_off.setText(_translate("MainWindow", "Off"))
        self.radioButton_restart.setText(_translate("MainWindow", "Restart"))
        self.radioButton_sleep.setText(_translate("MainWindow", "Sleep"))
        self.pushButton_start.setText(_translate("MainWindow", "START"))
        self.pushButton_stop.setText(_translate("MainWindow", "STOP"))

