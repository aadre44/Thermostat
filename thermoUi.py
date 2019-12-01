# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'thermoUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from thermostat import thermo
from weatherAPI import weatherInfo
import time
import multiprocessing
import sys


class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        `tuple` (exctype, value, traceback.format_exc() )

    result
        `object` data returned from processing, anything

    '''
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)

class WorkThread(QRunnable):

    def __init__(self, thermostat, **kwargs):#):
        super(WorkThread, self).__init__()
        self.thermostat = thermostat
        #self.kwargs = kwargs
        self.signals = WorkerSignals()


    print("Signal set")

    @pyqtSlot()
    def run(self):
        print("run Function entered")
        self.thermostat.cycle



class Ui_Form(object):
    thermostat = thermo()
    desiredTemp = thermostat.desiredTemp
    weather = weatherInfo()
    #weather.getTemp("18064")


    def __init__(self):
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

    '''
    #THIS IS A TEST TO TRY AND ORGANIZE CODE WITH INIT FUNCTION
    def __init__(self):
        self.thermostat = thermo()
        self.setTemp = 0
        Form = QtWidgets.QWidget()
        self.setupUi(self, Form)

        self.btnUp.clicked.connect(self.increaseTemp)
        self.btnDown.clicked.connect(self.downBtnClicked())
        self.btnAC.clicked.connect(self.thermostat.acOn)
        self.btnHeat.clicked.connect(self.thermostat.heatOn)
        self.btnAuto.clicked.connect(self.thermostat.AutoOn)
        self.btnOff.clicked.connect(self.thermostat.turnOff)
        self.btnSchedule.clicked.connect(self.thermostat.printCurTemp)

        self.workThread = WorkThread(self.thermostat)  # creates thread object
        print("step 1")
        self.workThread.signal.connect(self.updateCurTemp)  # Connect the signal from the thread to the finished method
    '''
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(849, 671)
        Form.setStyleSheet("*{\n"
        "    font-family:centry gothic;\n"
        "    font-size:24px;\n"
        "}\n"
        "\n"
        "QFrame\n"
        "{\n"
        "    background:rgba(0,0,0,0.8);\n"
        "    border-radius:15px;\n"
        "}\n"
        "\n"
        "QPushButton\n"
        "{\n"
        "    color:white;\n"
        "    background:red;\n"
        "    border-radius:15px;\n"
        "}\n"
        "\n"
        "QPushButton:hover\n"
        "{\n"
        "    color:red;\n"
        "    background:#333;\n"
        "    border-radius:15px;\n"
        "}\n"
        "\n"
        "QLabel\n"
        "{\n"
        "    color:white;\n"
        "    background:transparent;\n"
        "}\n"
        "\n"
        "QCommandLinkButton\n"
        "{\n"
        "    color:white;\n"
        "    background:#333;\n"
        "}\n"
        "\n"
        "QCommandLinkButton:hover\n"
        "{\n"
        "    color:#333;\n"
        "    background:#333;\n"
        "}\n"
        "\n"
        "QLineEdit\n"
        "{\n"
        "\n"
        "    background:transparent;\n"
        "    border:none;\n"
        "    color:#717072;\n"
        "    border-bottom:1px solid #717072\n"
        "}")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 821, 641))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btnUp = QtWidgets.QPushButton(self.frame)
        self.btnUp.setGeometry(QtCore.QRect(60, 40, 141, 51))
        self.btnUp.setObjectName("btnUp")

        self.btnAC = QtWidgets.QPushButton(self.frame)
        self.btnAC.setGeometry(QtCore.QRect(20, 570, 131, 41))
        self.btnAC.setObjectName("btnAC")
        self.btnHeat = QtWidgets.QPushButton(self.frame)
        self.btnHeat.setGeometry(QtCore.QRect(190, 570, 131, 41))
        self.btnHeat.setObjectName("btnHeat")
        self.btnAuto = QtWidgets.QPushButton(self.frame)
        self.btnAuto.setGeometry(QtCore.QRect(360, 570, 131, 41))
        self.btnAuto.setObjectName("btnAuto")
        self.btnOff = QtWidgets.QPushButton(self.frame)
        self.btnOff.setGeometry(QtCore.QRect(530, 570, 131, 41))
        self.btnOff.setObjectName("btnOff")
        self.btnSchedule = QtWidgets.QPushButton(self.frame)
        self.btnSchedule.setGeometry(QtCore.QRect(680, 570, 131, 41))
        self.btnSchedule.setObjectName("btnSchedule")
        self.btnDown = QtWidgets.QPushButton(self.frame)
        self.btnDown.setGeometry(QtCore.QRect(70, 390, 141, 51))
        self.btnDown.setObjectName("btnDown")

        self.labelWeatherF = QtWidgets.QLabel(self.frame)
        self.labelWeatherF.setGeometry(QtCore.QRect(710, 330, 31, 61))
        self.labelWeatherF.setObjectName("labelWeatherF")
        self.labelCurTemp_2 = QtWidgets.QLabel(self.frame)
        self.labelCurTemp_2.setGeometry(QtCore.QRect(490, 160, 61, 41))
        self.labelCurTemp_2.setStyleSheet("*{\n"
        "    font-family:centry gothic;\n"
        "    font-size:48px;\n"
        "}")
        self.labelCurTemp_2.setObjectName("labelCurTemp_2")
        self.labelCurF = QtWidgets.QLabel(self.frame)
        self.labelCurF.setGeometry(QtCore.QRect(550, 140, 31, 61))
        self.labelCurF.setObjectName("labelCurF")
        self.iconWeather = QtWidgets.QLabel(self.frame)
        self.iconWeather.setGeometry(QtCore.QRect(420, 310, 241, 191))
        self.iconWeather.setText("")
        self.iconWeather.setPixmap(QtGui.QPixmap("weather Images/sunShowers.png"))
        self.iconWeather.setObjectName("iconWeather")
        self.labelWeather = QtWidgets.QLabel(self.frame)
        self.labelWeather.setGeometry(QtCore.QRect(480, 260, 91, 29))
        self.labelWeather.setObjectName("labelWeather")
        self.labelCurTemp = QtWidgets.QLabel(self.frame)
        self.labelCurTemp.setGeometry(QtCore.QRect(450, 30, 181, 81))
        self.labelCurTemp.setObjectName("labelCurTemp")
        self.labelTemp = QtWidgets.QLabel(self.frame)
        self.labelTemp.setGeometry(QtCore.QRect(70, 180, 131, 191))
        self.labelTemp.setStyleSheet("*{\n"
        "    font-family:centry gothic;\n"
        "    font-size:118px;\n"
        "}")
        self.labelTemp.setObjectName("labelTemp")
        self.labelTempF = QtWidgets.QLabel(self.frame)
        self.labelTempF.setGeometry(QtCore.QRect(210, 200, 31, 61))
        self.labelTempF.setObjectName("labelTempF")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 120, 211, 71))
        self.label.setStyleSheet("*{\n"
        "    font-family:centry gothic;\n"
        "    font-size:48px;\n"
        "}")
        self.label.setObjectName("label")
        self.labelWeatherTemp = QtWidgets.QLabel(self.frame)
        self.labelWeatherTemp.setGeometry(QtCore.QRect(650, 350, 61, 51))
        self.labelWeatherTemp.setStyleSheet("*{\n"
        "    font-family:centry gothic;\n"
        "    font-size:48px;\n"
        "}")
        self.labelWeatherTemp.setObjectName("labelWeatherTemp")
        self.btnUp.raise_()
        self.btnAC.raise_()
        self.btnHeat.raise_()
        self.btnAuto.raise_()
        self.btnOff.raise_()
        self.btnSchedule.raise_()
        self.btnDown.raise_()
        self.labelWeatherF.raise_()
        self.iconWeather.raise_()
        self.labelWeather.raise_()
        self.labelCurTemp.raise_()
        self.labelCurTemp_2.raise_()
        self.labelCurF.raise_()
        self.labelTemp.raise_()
        self.labelTempF.raise_()
        self.label.raise_()
        self.labelWeatherTemp.raise_()

        self.btnUp.clicked.connect(self.increaseTemp)
        #self.btnUp.clicked.connect(self.thermostat.tempUp)
        self.btnDown.clicked.connect(self.decreaseTemp)
        #self.btnDown.clicked.connect(self.thermostat.tempDown)
        self.btnAC.clicked.connect(self.thermostat.acOn)
        self.btnHeat.clicked.connect(self.thermostat.heatOn)
        self.btnAuto.clicked.connect(self.thermostat.autoOn)
        self.btnAuto.clicked.connect(self.runCycle)
        self.btnOff.clicked.connect(self.thermostat.turnOff)
        self.btnSchedule.clicked.connect(self.thermostat.getCurTemp)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.runCycle()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnUp.setText(_translate("Form", "Up"))
        self.btnAC.setText(_translate("Form", "A/C"))
        self.btnHeat.setText(_translate("Form", "HEAT"))
        self.btnAuto.setText(_translate("Form", "AUTO"))
        self.btnOff.setText(_translate("Form", "OFF"))
        self.btnSchedule.setText(_translate("Form", "Schedule"))
        self.btnDown.setText(_translate("Form", "Down"))
        self.labelWeatherF.setText(_translate("Form", "*F"))
        self.labelCurTemp_2.setText(_translate("Form", "67"))
        self.labelCurF.setText(_translate("Form", "*F"))
        self.labelWeather.setText(_translate("Form", "Weather"))
        self.labelCurTemp.setText(_translate("Form", "Current Temp"))
        self.labelTemp.setText(_translate("Form", "75"))
        self.labelTempF.setText(_translate("Form", "*F"))
        self.label.setText(_translate("Form", "Set Temp"))
        self.labelWeatherTemp.setText(_translate("Form", "67"))

    def increaseTemp(self):
        if (self.thermostat.desiredTemp == 99):
            self.thermostat.desiredTemp = 0
        self.thermostat.desiredTemp += 1
        print("thermostat "+str(self.thermostat.desiredTemp))
        self.updateDesiredTemp()
        """
        if(self.desiredTemp== 99):
            self.desiredTemp = 0
        self.desiredTemp+=1
        self.labelTemp.setText(str(self.desiredTemp))
        print(self.desiredTemp)"""

    def decreaseTemp(self):
        if (self.thermostat.desiredTemp == 99):
            self.thermostat.desiredTemp = 0
        self.thermostat.desiredTemp -= 1
        print("thermostat "+str(self.thermostat.desiredTemp))
        self.updateDesiredTemp()
        """
        if(self.desiredTemp== 0):
            self.desiredTemp = 99
        self.desiredTemp-=1
        self.labelTemp.setText(str(self.desiredTemp))
        print(self.desiredTemp)"""

    def updateCurTemp(self, temp):
        print(temp)
        self.labelCurTemp2.setText(str(temp))

    def runCycle(self):
        worker = WorkThread(self.thermostat) # creates thread object
        self.threadpool.start(worker)

    def updateWeather(self):
        info = self.weather.getWeather()
        temp = info[0]
        self.labelWeatherTemp.setText(str(temp))
        if(info[3] == "overcast clouds"):
            print("ITS OVERCASTING")
            self.iconWeather.setPixmap(QtGui.QPixmap("weather Images/overcast.png"))
        if (info[3] == "drizzle"):
            self.iconWeather.setPixmap(QtGui.QPixmap("weather Images/rain.png"))
        """
        Implement change in icon depending on the weather
        add humidity 
        add pressure
        """
    def updateDesiredTemp(self):
        print("setting "+str(self.thermostat.desiredTemp))
        self.labelTemp.setText(str(self.thermostat.desiredTemp))


def main():
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    ui.updateWeather()

    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")

    #sys.exit(app.exec_())

if __name__ == "__main__":
    main()

