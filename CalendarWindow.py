# Form implementation generated from reading ui file 'CalendarWindow.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DialogCalendar(object):
    def setupUi(self, DialogCalendar):
        DialogCalendar.setObjectName("DialogCalendar")
        DialogCalendar.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/logo.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        DialogCalendar.setWindowIcon(icon)
        self.Calendar = QtWidgets.QCalendarWidget(parent=DialogCalendar)
        self.Calendar.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.Calendar.setObjectName("Calendar")

        self.retranslateUi(DialogCalendar)
        QtCore.QMetaObject.connectSlotsByName(DialogCalendar)

    def retranslateUi(self, DialogCalendar):
        _translate = QtCore.QCoreApplication.translate
        DialogCalendar.setWindowTitle(_translate("DialogCalendar", "Fecha de Alta"))
