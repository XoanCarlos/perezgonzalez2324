# Form implementation generated from reading ui file '.\templates\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1068, 760)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\templates\\../img/logo.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(64, 64))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(1024, 700))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        self.panelPrincipal = QtWidgets.QTabWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.panelPrincipal.sizePolicy().hasHeightForWidth())
        self.panelPrincipal.setSizePolicy(sizePolicy)
        self.panelPrincipal.setMinimumSize(QtCore.QSize(900, 650))
        self.panelPrincipal.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.panelPrincipal.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.panelPrincipal.setFont(font)
        self.panelPrincipal.setStyleSheet("")
        self.panelPrincipal.setTabShape(QtWidgets.QTabWidget.TabShape.Triangular)
        self.panelPrincipal.setObjectName("panelPrincipal")
        self.panelDrivers = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.panelDrivers.sizePolicy().hasHeightForWidth())
        self.panelDrivers.setSizePolicy(sizePolicy)
        self.panelDrivers.setAutoFillBackground(True)
        self.panelDrivers.setObjectName("panelDrivers")
        self.gridLayout = QtWidgets.QGridLayout(self.panelDrivers)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(parent=self.panelDrivers)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        self.frngestdrive = QtWidgets.QFrame(parent=self.panelDrivers)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frngestdrive.sizePolicy().hasHeightForWidth())
        self.frngestdrive.setSizePolicy(sizePolicy)
        self.frngestdrive.setMinimumSize(QtCore.QSize(400, 20))
        self.frngestdrive.setMaximumSize(QtCore.QSize(2048, 300))
        self.frngestdrive.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.frngestdrive.setStyleSheet("border-color: rgb(255, 253, 225);")
        self.frngestdrive.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frngestdrive.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frngestdrive.setObjectName("frngestdrive")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frngestdrive)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btnAltaDriver = QtWidgets.QPushButton(parent=self.frngestdrive)
        self.btnAltaDriver.setMinimumSize(QtCore.QSize(75, 20))
        self.btnAltaDriver.setMaximumSize(QtCore.QSize(80, 16777215))
        self.btnAltaDriver.setObjectName("btnAltaDriver")
        self.horizontalLayout_2.addWidget(self.btnAltaDriver)
        spacerItem2 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.btnModifDriver = QtWidgets.QPushButton(parent=self.frngestdrive)
        self.btnModifDriver.setMinimumSize(QtCore.QSize(75, 20))
        self.btnModifDriver.setMaximumSize(QtCore.QSize(80, 16777215))
        self.btnModifDriver.setObjectName("btnModifDriver")
        self.horizontalLayout_2.addWidget(self.btnModifDriver)
        spacerItem3 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.btnBajaDriver = QtWidgets.QPushButton(parent=self.frngestdrive)
        self.btnBajaDriver.setMinimumSize(QtCore.QSize(75, 20))
        self.btnBajaDriver.setMaximumSize(QtCore.QSize(80, 16777215))
        self.btnBajaDriver.setObjectName("btnBajaDriver")
        self.horizontalLayout_2.addWidget(self.btnBajaDriver)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.gridLayout_10.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.txtNome = QtWidgets.QLineEdit(parent=self.frngestdrive)
        self.txtNome.setMinimumSize(QtCore.QSize(300, 20))
        self.txtNome.setMaximumSize(QtCore.QSize(16777215, 20))
        self.txtNome.setObjectName("txtNome")
        self.gridLayout_4.addWidget(self.txtNome, 0, 4, 1, 1)
        self.lblApel = QtWidgets.QLabel(parent=self.frngestdrive)
        self.lblApel.setMinimumSize(QtCore.QSize(70, 20))
        self.lblApel.setMaximumSize(QtCore.QSize(70, 20))
        self.lblApel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblApel.setObjectName("lblApel")
        self.gridLayout_4.addWidget(self.lblApel, 0, 0, 1, 1)
        self.lblNome = QtWidgets.QLabel(parent=self.frngestdrive)
        self.lblNome.setMinimumSize(QtCore.QSize(60, 20))
        self.lblNome.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblNome.setObjectName("lblNome")
        self.gridLayout_4.addWidget(self.lblNome, 0, 3, 1, 1)
        self.txtApel = QtWidgets.QLineEdit(parent=self.frngestdrive)
        self.txtApel.setMinimumSize(QtCore.QSize(350, 20))
        self.txtApel.setCursorPosition(0)
        self.txtApel.setObjectName("txtApel")
        self.gridLayout_4.addWidget(self.txtApel, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_4.addItem(spacerItem5, 0, 2, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_4, 2, 0, 1, 4)
        spacerItem6 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_9.addItem(spacerItem6, 7, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_9.addItem(spacerItem7, 5, 0, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.gridLayout_7.setContentsMargins(0, -1, -1, -1)
        self.gridLayout_7.setHorizontalSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.chkA = QtWidgets.QCheckBox(parent=self.frngestdrive)
        self.chkA.setMaximumSize(QtCore.QSize(40, 16777215))
        self.chkA.setAutoFillBackground(False)
        self.chkA.setObjectName("chkA")
        self.gridLayout_7.addWidget(self.chkA, 0, 1, 1, 1)
        self.chkD = QtWidgets.QCheckBox(parent=self.frngestdrive)
        self.chkD.setMaximumSize(QtCore.QSize(40, 16777215))
        self.chkD.setObjectName("chkD")
        self.gridLayout_7.addWidget(self.chkD, 0, 4, 1, 1)
        self.chkC = QtWidgets.QCheckBox(parent=self.frngestdrive)
        self.chkC.setMaximumSize(QtCore.QSize(40, 16777215))
        self.chkC.setObjectName("chkC")
        self.gridLayout_7.addWidget(self.chkC, 0, 3, 1, 1)
        self.chkB = QtWidgets.QCheckBox(parent=self.frngestdrive)
        self.chkB.setMaximumSize(QtCore.QSize(40, 16777215))
        self.chkB.setObjectName("chkB")
        self.gridLayout_7.addWidget(self.chkB, 0, 2, 1, 1)
        self.lblCarnet = QtWidgets.QLabel(parent=self.frngestdrive)
        self.lblCarnet.setMinimumSize(QtCore.QSize(80, 0))
        self.lblCarnet.setMaximumSize(QtCore.QSize(100, 20))
        self.lblCarnet.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblCarnet.setObjectName("lblCarnet")
        self.gridLayout_7.addWidget(self.lblCarnet, 0, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_7, 8, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.gridLayout_6.setContentsMargins(0, -1, -1, -1)
        self.gridLayout_6.setHorizontalSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.txtMovil = QtWidgets.QLineEdit(parent=self.frngestdrive)
        self.txtMovil.setMinimumSize(QtCore.QSize(90, 20))
        self.txtMovil.setMaximumSize(QtCore.QSize(80, 20))
        self.txtMovil.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txtMovil.setObjectName("txtMovil")
        self.gridLayout_6.addWidget(self.txtMovil, 0, 2, 1, 1)
        self.lblMovil = QtWidgets.QLabel(parent=self.frngestdrive)
        self.lblMovil.setMinimumSize(QtCore.QSize(45, 0))
        self.lblMovil.setMaximumSize(QtCore.QSize(50, 20))
        self.lblMovil.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblMovil.setObjectName("lblMovil")
        self.gridLayout_6.addWidget(self.lblMovil, 0, 1, 1, 1)
        self.txtSalario = QtWidgets.QLineEdit(parent=self.frngestdrive)
        self.txtSalario.setMinimumSize(QtCore.QSize(100, 20))
        self.txtSalario.setMaximumSize(QtCore.QSize(110, 20))
        self.txtSalario.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.txtSalario.setObjectName("txtSalario")
        self.gridLayout_6.addWidget(self.txtSalario, 0, 5, 1, 1)
        self.lblSalario = QtWidgets.QLabel(parent=self.frngestdrive)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.lblSalario.sizePolicy().hasHeightForWidth())
        self.lblSalario.setSizePolicy(sizePolicy)
        self.lblSalario.setMinimumSize(QtCore.QSize(60, 20))
        self.lblSalario.setMaximumSize(QtCore.QSize(60, 20))
        self.lblSalario.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblSalario.setObjectName("lblSalario")
        self.gridLayout_6.addWidget(self.lblSalario, 0, 4, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_6.addItem(spacerItem8, 0, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_6.addItem(spacerItem9, 0, 3, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_6, 6, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lblLocalidad = QtWidgets.QLabel(parent=self.frngestdrive)
        self.lblLocalidad.setMaximumSize(QtCore.QSize(70, 20))
        self.lblLocalidad.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblLocalidad.setObjectName("lblLocalidad")
        self.gridLayout_5.addWidget(self.lblLocalidad, 0, 5, 1, 1)
        self.cmbMuni = QtWidgets.QComboBox(parent=self.frngestdrive)
        self.cmbMuni.setMinimumSize(QtCore.QSize(170, 20))
        self.cmbMuni.setMaximumSize(QtCore.QSize(240, 20))
        self.cmbMuni.setObjectName("cmbMuni")
        self.gridLayout_5.addWidget(self.cmbMuni, 0, 6, 1, 1)
        self.lblDirdriver = QtWidgets.QLabel(parent=self.frngestdrive)
        self.lblDirdriver.setMinimumSize(QtCore.QSize(70, 0))
        self.lblDirdriver.setMaximumSize(QtCore.QSize(90, 20))
        self.lblDirdriver.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblDirdriver.setObjectName("lblDirdriver")
        self.gridLayout_5.addWidget(self.lblDirdriver, 0, 0, 1, 1)
        self.txtDirdriver = QtWidgets.QLineEdit(parent=self.frngestdrive)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtDirdriver.sizePolicy().hasHeightForWidth())
        self.txtDirdriver.setSizePolicy(sizePolicy)
        self.txtDirdriver.setMinimumSize(QtCore.QSize(385, 20))
        self.txtDirdriver.setObjectName("txtDirdriver")
        self.gridLayout_5.addWidget(self.txtDirdriver, 0, 1, 1, 1)
        self.lblPRov = QtWidgets.QLabel(parent=self.frngestdrive)
        self.lblPRov.setMaximumSize(QtCore.QSize(70, 20))
        self.lblPRov.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblPRov.setObjectName("lblPRov")
        self.gridLayout_5.addWidget(self.lblPRov, 0, 3, 1, 1)
        self.cmbProv = QtWidgets.QComboBox(parent=self.frngestdrive)
        self.cmbProv.setMinimumSize(QtCore.QSize(120, 20))
        self.cmbProv.setMaximumSize(QtCore.QSize(150, 20))
        self.cmbProv.setObjectName("cmbProv")
        self.gridLayout_5.addWidget(self.cmbProv, 0, 4, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_5.addItem(spacerItem10, 0, 2, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_5, 4, 0, 1, 4)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lblDni = QtWidgets.QLabel(parent=self.frngestdrive)
        self.lblDni.setMinimumSize(QtCore.QSize(30, 20))
        self.lblDni.setMaximumSize(QtCore.QSize(30, 20))
        self.lblDni.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblDni.setObjectName("lblDni")
        self.gridLayout_3.addWidget(self.lblDni, 0, 3, 1, 1)
        self.lblDatadriver = QtWidgets.QLabel(parent=self.frngestdrive)
        self.lblDatadriver.setMinimumSize(QtCore.QSize(90, 20))
        self.lblDatadriver.setMaximumSize(QtCore.QSize(110, 20))
        self.lblDatadriver.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblDatadriver.setObjectName("lblDatadriver")
        self.gridLayout_3.addWidget(self.lblDatadriver, 0, 7, 1, 1)
        self.txtDatadriver = QtWidgets.QLineEdit(parent=self.frngestdrive)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtDatadriver.sizePolicy().hasHeightForWidth())
        self.txtDatadriver.setSizePolicy(sizePolicy)
        self.txtDatadriver.setMinimumSize(QtCore.QSize(80, 20))
        self.txtDatadriver.setMaximumSize(QtCore.QSize(60, 20))
        self.txtDatadriver.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txtDatadriver.setObjectName("txtDatadriver")
        self.gridLayout_3.addWidget(self.txtDatadriver, 0, 9, 1, 1)
        self.lblCod = QtWidgets.QLabel(parent=self.frngestdrive)
        self.lblCod.setMinimumSize(QtCore.QSize(50, 20))
        self.lblCod.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lblCod.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblCod.setObjectName("lblCod")
        self.gridLayout_3.addWidget(self.lblCod, 0, 1, 1, 1)
        self.lblcodbd = QtWidgets.QLabel(parent=self.frngestdrive)
        self.lblcodbd.setMinimumSize(QtCore.QSize(70, 20))
        self.lblcodbd.setMaximumSize(QtCore.QSize(70, 20))
        self.lblcodbd.setStyleSheet("background-color: rgb(255, 248, 192);")
        self.lblcodbd.setText("")
        self.lblcodbd.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblcodbd.setObjectName("lblcodbd")
        self.gridLayout_3.addWidget(self.lblcodbd, 0, 2, 1, 1)
        self.btnCalendar = QtWidgets.QPushButton(parent=self.frngestdrive)
        self.btnCalendar.setMinimumSize(QtCore.QSize(28, 28))
        self.btnCalendar.setMaximumSize(QtCore.QSize(28, 28))
        self.btnCalendar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\templates\\../img/calendar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnCalendar.setIcon(icon1)
        self.btnCalendar.setIconSize(QtCore.QSize(28, 28))
        self.btnCalendar.setObjectName("btnCalendar")
        self.gridLayout_3.addWidget(self.btnCalendar, 0, 10, 1, 1)
        self.lblValidardni = QtWidgets.QLabel(parent=self.frngestdrive)
        self.lblValidardni.setMinimumSize(QtCore.QSize(40, 30))
        self.lblValidardni.setMaximumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        self.lblValidardni.setFont(font)
        self.lblValidardni.setText("")
        self.lblValidardni.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblValidardni.setObjectName("lblValidardni")
        self.gridLayout_3.addWidget(self.lblValidardni, 0, 5, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem11, 0, 0, 1, 1)
        self.txtDni = QtWidgets.QLineEdit(parent=self.frngestdrive)
        self.txtDni.setMinimumSize(QtCore.QSize(120, 20))
        self.txtDni.setMaximumSize(QtCore.QSize(120, 20))
        self.txtDni.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txtDni.setObjectName("txtDni")
        self.gridLayout_3.addWidget(self.txtDni, 0, 4, 1, 1)
        self.btnBuscadri = QtWidgets.QPushButton(parent=self.frngestdrive)
        self.btnBuscadri.setMaximumSize(QtCore.QSize(30, 30))
        self.btnBuscadri.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\templates\\../img/lupa.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnBuscadri.setIcon(icon2)
        self.btnBuscadri.setIconSize(QtCore.QSize(24, 24))
        self.btnBuscadri.setObjectName("btnBuscadri")
        self.gridLayout_3.addWidget(self.btnBuscadri, 0, 6, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_3, 0, 0, 1, 3)
        spacerItem12 = QtWidgets.QSpacerItem(13, 13, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_9.addItem(spacerItem12, 3, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_9.addItem(spacerItem13, 1, 0, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.lblEstado = QtWidgets.QLabel(parent=self.frngestdrive)
        self.lblEstado.setMinimumSize(QtCore.QSize(80, 0))
        self.lblEstado.setMaximumSize(QtCore.QSize(100, 20))
        self.lblEstado.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblEstado.setObjectName("lblEstado")
        self.gridLayout_8.addWidget(self.lblEstado, 0, 0, 1, 1)
        self.rbtTodos = QtWidgets.QRadioButton(parent=self.frngestdrive)
        self.rbtTodos.setMinimumSize(QtCore.QSize(60, 0))
        self.rbtTodos.setMaximumSize(QtCore.QSize(60, 16777215))
        self.rbtTodos.setChecked(False)
        self.rbtTodos.setObjectName("rbtTodos")
        self.rtbGroup = QtWidgets.QButtonGroup(MainWindow)
        self.rtbGroup.setObjectName("rtbGroup")
        self.rtbGroup.addButton(self.rbtTodos)
        self.gridLayout_8.addWidget(self.rbtTodos, 0, 1, 1, 1)
        self.rbtAlta = QtWidgets.QRadioButton(parent=self.frngestdrive)
        self.rbtAlta.setMinimumSize(QtCore.QSize(60, 0))
        self.rbtAlta.setMaximumSize(QtCore.QSize(60, 16777215))
        self.rbtAlta.setChecked(True)
        self.rbtAlta.setObjectName("rbtAlta")
        self.rtbGroup.addButton(self.rbtAlta)
        self.gridLayout_8.addWidget(self.rbtAlta, 0, 2, 1, 1)
        self.rbtBaja = QtWidgets.QRadioButton(parent=self.frngestdrive)
        self.rbtBaja.setMinimumSize(QtCore.QSize(60, 0))
        self.rbtBaja.setMaximumSize(QtCore.QSize(60, 16777215))
        self.rbtBaja.setObjectName("rbtBaja")
        self.rtbGroup.addButton(self.rbtBaja)
        self.gridLayout_8.addWidget(self.rbtBaja, 0, 3, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_8, 6, 3, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.frngestdrive)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_9.addWidget(self.label, 6, 1, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_9.addItem(spacerItem14, 8, 1, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_9, 0, 1, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_10.addItem(spacerItem15, 0, 0, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_10.addItem(spacerItem16, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.frngestdrive, 1, 1, 1, 1)
        self.tabDrivers = QtWidgets.QTableWidget(parent=self.panelDrivers)
        self.tabDrivers.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.tabDrivers.sizePolicy().hasHeightForWidth())
        self.tabDrivers.setSizePolicy(sizePolicy)
        self.tabDrivers.setMinimumSize(QtCore.QSize(400, 350))
        self.tabDrivers.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabDrivers.setStyleSheet("QHeaderView::section:horizontal\n"
"{\n"
"border-top: 1px solid #ffffff;\n"
"color: \'white\';\n"
"font: 11pt \"Arial\";\n"
"background-color:rgb(100,100,100);\n"
"}\n"
"")
        self.tabDrivers.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tabDrivers.setAlternatingRowColors(True)
        self.tabDrivers.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
        self.tabDrivers.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tabDrivers.setObjectName("tabDrivers")
        self.tabDrivers.setColumnCount(6)
        self.tabDrivers.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabDrivers.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabDrivers.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabDrivers.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabDrivers.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabDrivers.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabDrivers.setHorizontalHeaderItem(5, item)
        self.tabDrivers.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tabDrivers, 2, 1, 1, 1)
        self.panelPrincipal.addTab(self.panelDrivers, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(120, 90, 131, 16))
        self.label_2.setObjectName("label_2")
        self.panelPrincipal.addTab(self.tab_2, "")
        self.gridLayout_2.addWidget(self.panelPrincipal, 0, 1, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem17, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1068, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(parent=self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuHerramientas = QtWidgets.QMenu(parent=self.menubar)
        self.menuHerramientas.setObjectName("menuHerramientas")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setAutoFillBackground(False)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(parent=MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionSalir = QtGui.QAction(parent=MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.actionAcerca_de = QtGui.QAction(parent=MainWindow)
        self.actionAcerca_de.setObjectName("actionAcerca_de")
        self.actionbarSalir = QtGui.QAction(parent=MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\templates\\../img/salir.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionbarSalir.setIcon(icon3)
        self.actionbarSalir.setObjectName("actionbarSalir")
        self.actionlimpiaPaneldriver = QtGui.QAction(parent=MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(".\\templates\\../img/limpiar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionlimpiaPaneldriver.setIcon(icon4)
        self.actionlimpiaPaneldriver.setObjectName("actionlimpiaPaneldriver")
        self.actionCrear_Copia_Seguridad = QtGui.QAction(parent=MainWindow)
        self.actionCrear_Copia_Seguridad.setObjectName("actionCrear_Copia_Seguridad")
        self.actionRestaurar_Copia_Seguridad = QtGui.QAction(parent=MainWindow)
        self.actionRestaurar_Copia_Seguridad.setObjectName("actionRestaurar_Copia_Seguridad")
        self.actioncrearbackup = QtGui.QAction(parent=MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(".\\templates\\../img/backup.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.actioncrearbackup.setIcon(icon5)
        self.actioncrearbackup.setObjectName("actioncrearbackup")
        self.actionExportar_Datos_Excel = QtGui.QAction(parent=MainWindow)
        self.actionExportar_Datos_Excel.setObjectName("actionExportar_Datos_Excel")
        self.actionrestaurarbackup = QtGui.QAction(parent=MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(".\\templates\\../img/backup1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionrestaurarbackup.setIcon(icon6)
        self.actionrestaurarbackup.setObjectName("actionrestaurarbackup")
        self.menuArchivo.addAction(self.actionSalir)
        self.menuHelp.addAction(self.actionAcerca_de)
        self.menuHerramientas.addAction(self.actionCrear_Copia_Seguridad)
        self.menuHerramientas.addAction(self.actionRestaurar_Copia_Seguridad)
        self.menuHerramientas.addSeparator()
        self.menuHerramientas.addAction(self.actionExportar_Datos_Excel)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuHerramientas.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionrestaurarbackup)
        self.toolBar.addAction(self.actioncrearbackup)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionlimpiaPaneldriver)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionbarSalir)

        self.retranslateUi(MainWindow)
        self.panelPrincipal.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.panelPrincipal, self.txtDni)
        MainWindow.setTabOrder(self.txtDni, self.txtDatadriver)
        MainWindow.setTabOrder(self.txtDatadriver, self.btnCalendar)
        MainWindow.setTabOrder(self.btnCalendar, self.txtApel)
        MainWindow.setTabOrder(self.txtApel, self.txtNome)
        MainWindow.setTabOrder(self.txtNome, self.txtDirdriver)
        MainWindow.setTabOrder(self.txtDirdriver, self.cmbProv)
        MainWindow.setTabOrder(self.cmbProv, self.cmbMuni)
        MainWindow.setTabOrder(self.cmbMuni, self.txtMovil)
        MainWindow.setTabOrder(self.txtMovil, self.txtSalario)
        MainWindow.setTabOrder(self.txtSalario, self.chkA)
        MainWindow.setTabOrder(self.chkA, self.chkB)
        MainWindow.setTabOrder(self.chkB, self.chkC)
        MainWindow.setTabOrder(self.chkC, self.chkD)
        MainWindow.setTabOrder(self.chkD, self.btnAltaDriver)
        MainWindow.setTabOrder(self.btnAltaDriver, self.btnModifDriver)
        MainWindow.setTabOrder(self.btnModifDriver, self.btnBajaDriver)
        MainWindow.setTabOrder(self.btnBajaDriver, self.rbtTodos)
        MainWindow.setTabOrder(self.rbtTodos, self.rbtAlta)
        MainWindow.setTabOrder(self.rbtAlta, self.rbtBaja)
        MainWindow.setTabOrder(self.rbtBaja, self.tabDrivers)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CarTeis"))
        self.btnAltaDriver.setText(_translate("MainWindow", "Alta"))
        self.btnModifDriver.setText(_translate("MainWindow", "Modificar"))
        self.btnBajaDriver.setText(_translate("MainWindow", "Baja"))
        self.lblApel.setText(_translate("MainWindow", "Apellidos:"))
        self.lblNome.setText(_translate("MainWindow", "Nombre:"))
        self.chkA.setText(_translate("MainWindow", "A"))
        self.chkD.setText(_translate("MainWindow", "D"))
        self.chkC.setText(_translate("MainWindow", "C"))
        self.chkB.setText(_translate("MainWindow", "B"))
        self.lblCarnet.setText(_translate("MainWindow", "Tipo de Carnet:"))
        self.lblMovil.setText(_translate("MainWindow", "Móvil:"))
        self.lblSalario.setText(_translate("MainWindow", "Salario: "))
        self.lblLocalidad.setText(_translate("MainWindow", "Localidad:"))
        self.lblDirdriver.setText(_translate("MainWindow", "Dirección:"))
        self.lblPRov.setText(_translate("MainWindow", "Provincia:"))
        self.lblDni.setText(_translate("MainWindow", "DNI:"))
        self.lblDatadriver.setText(_translate("MainWindow", "Fecha Alta:"))
        self.lblCod.setText(_translate("MainWindow", "Código:"))
        self.txtDni.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">Introducir DNI</span></p></body></html>"))
        self.lblEstado.setText(_translate("MainWindow", "Histórico:"))
        self.rbtTodos.setText(_translate("MainWindow", "Todos"))
        self.rbtAlta.setText(_translate("MainWindow", "Alta"))
        self.rbtBaja.setText(_translate("MainWindow", "Baja"))
        self.label.setText(_translate("MainWindow", "(000000.00)"))
        item = self.tabDrivers.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Código"))
        item = self.tabDrivers.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Apellidos"))
        item = self.tabDrivers.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tabDrivers.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Móvil"))
        item = self.tabDrivers.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Licencias"))
        item = self.tabDrivers.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Fecha Baja"))
        self.panelPrincipal.setTabText(self.panelPrincipal.indexOf(self.panelDrivers), _translate("MainWindow", "CONDUCTORES"))
        self.label_2.setText(_translate("MainWindow", "Esta es la pestaña 2"))
        self.panelPrincipal.setTabText(self.panelPrincipal.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuHelp.setTitle(_translate("MainWindow", "Ayuda"))
        self.menuHerramientas.setTitle(_translate("MainWindow", "Herramientas"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionAcerca_de.setText(_translate("MainWindow", "Acerca de..."))
        self.actionbarSalir.setText(_translate("MainWindow", "barSalir"))
        self.actionlimpiaPaneldriver.setText(_translate("MainWindow", "limpiaPaneldriver"))
        self.actionCrear_Copia_Seguridad.setText(_translate("MainWindow", "Crear Copia Seguridad"))
        self.actionCrear_Copia_Seguridad.setShortcut(_translate("MainWindow", "Alt+S"))
        self.actionRestaurar_Copia_Seguridad.setText(_translate("MainWindow", "Restaurar Copia Seguridad"))
        self.actionRestaurar_Copia_Seguridad.setShortcut(_translate("MainWindow", "Alt+R"))
        self.actioncrearbackup.setText(_translate("MainWindow", "crearbackup"))
        self.actionExportar_Datos_Excel.setText(_translate("MainWindow", "Exportar Datos XLS"))
        self.actionrestaurarbackup.setText(_translate("MainWindow", "restaurarbackup"))
