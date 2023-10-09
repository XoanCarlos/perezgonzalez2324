# Form implementation generated from reading ui file 'dlgAcerca.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlgAbout(object):
    def setupUi(self, dlgAbout):
        dlgAbout.setObjectName("dlgAbout")
        dlgAbout.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        dlgAbout.resize(400, 300)
        dlgAbout.setMinimumSize(QtCore.QSize(400, 300))
        dlgAbout.setMaximumSize(QtCore.QSize(400, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/logo.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        dlgAbout.setWindowIcon(icon)
        dlgAbout.setModal(True)
        self.btnCerrar = QtWidgets.QPushButton(parent=dlgAbout)
        self.btnCerrar.setGeometry(QtCore.QRect(150, 230, 80, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCerrar.sizePolicy().hasHeightForWidth())
        self.btnCerrar.setSizePolicy(sizePolicy)
        self.btnCerrar.setMinimumSize(QtCore.QSize(80, 25))
        self.btnCerrar.setMaximumSize(QtCore.QSize(80, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnCerrar.setFont(font)
        self.btnCerrar.setAutoDefault(True)
        self.btnCerrar.setObjectName("btnCerrar")
        self.layoutWidget = QtWidgets.QWidget(parent=dlgAbout)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 20, 402, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(2)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.lblLogo = QtWidgets.QLabel(parent=self.layoutWidget)
        self.lblLogo.setText("")
        self.lblLogo.setPixmap(QtGui.QPixmap("img/logo.ico"))
        self.lblLogo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblLogo.setObjectName("lblLogo")
        self.gridLayout.addWidget(self.lblLogo, 0, 0, 1, 1)
        self.lblVersion_2 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.lblVersion_2.setMinimumSize(QtCore.QSize(140, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblVersion_2.setFont(font)
        self.lblVersion_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblVersion_2.setObjectName("lblVersion_2")
        self.gridLayout.addWidget(self.lblVersion_2, 1, 0, 1, 1)
        self.lblMotivo = QtWidgets.QLabel(parent=self.layoutWidget)
        self.lblMotivo.setMinimumSize(QtCore.QSize(400, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblMotivo.setFont(font)
        self.lblMotivo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblMotivo.setObjectName("lblMotivo")
        self.gridLayout.addWidget(self.lblMotivo, 2, 0, 1, 1)
        self.lblVersion = QtWidgets.QLabel(parent=self.layoutWidget)
        self.lblVersion.setMinimumSize(QtCore.QSize(140, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblVersion.setFont(font)
        self.lblVersion.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblVersion.setObjectName("lblVersion")
        self.gridLayout.addWidget(self.lblVersion, 3, 0, 1, 1)
        self.lblAutor = QtWidgets.QLabel(parent=self.layoutWidget)
        self.lblAutor.setMinimumSize(QtCore.QSize(140, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblAutor.setFont(font)
        self.lblAutor.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblAutor.setObjectName("lblAutor")
        self.gridLayout.addWidget(self.lblAutor, 4, 0, 1, 1)

        self.retranslateUi(dlgAbout)
        QtCore.QMetaObject.connectSlotsByName(dlgAbout)

    def retranslateUi(self, dlgAbout):
        _translate = QtCore.QCoreApplication.translate
        dlgAbout.setWindowTitle(_translate("dlgAbout", "Acerca de..."))
        self.btnCerrar.setText(_translate("dlgAbout", "Cerrar"))
        self.lblVersion_2.setText(_translate("dlgAbout", "Car Teis"))
        self.lblMotivo.setText(_translate("dlgAbout", "Alquiler de coches con o sin conductor"))
        self.lblVersion.setText(_translate("dlgAbout", "Version 0.0.1rc"))
        self.lblAutor.setText(_translate("dlgAbout", "Autor: El Profe"))