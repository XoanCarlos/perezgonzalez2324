from PyQt6 import QtWidgets,QtCore
from datetime import datetime
import var, sys, locale
# Establecer la configuración regional en español
locale.setlocale(locale.LC_TIME, 'es_ES')
locale.setlocale(locale.LC_MONETARY, 'es_ES')

class Eventos():
    @staticmethod
    def abrirCalendar(self):
        try:
            var.calendar.show()
        except Exception as error:
            print('error en abrir calendar: ', error)

    @staticmethod
    def acercade():
        try:
            var.dlgacerca.show()
        except Exception as error:
            print('error abrir ventana acerca: ', error)
    @staticmethod
    def cerraracercade():
        try:
            var.dlgacerca.hide()
        except Exception as error:
            print('error abrir ventana acerca: ', error)


    def mostrarsalir(self):

        #mbox = QtWidgets.QMessageBox.question(None, 'Salir', '¿Estás seguro que quieres salir?',
                                             # QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)

        mbox = QtWidgets.QMessageBox.question(None, 'Salir', '¿Estás seguro que quieres salir?')
        yes_button = mbox.addButton("Sí", QtWidgets.QMessageBox.YesRole)
        if mbox == QtWidgets.QMessageBox.StandardButton.Yes:
            sys.exit()
        else:
            return False


    def cargastatusbar(self):
        '''

        Formatear la fecha según el formato deseadofecha_actual.strftime()
        statusbar
        '''
        try:
            fecha = datetime.now().strftime("%A  -  " + "%d/%m/%Y")
            self.labelstatus = QtWidgets.QLabel(fecha, self)
            self.labelstatus.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
            var.ui.statusbar.addPermanentWidget(self.labelstatus, 1)
            self.labelstatusversion = QtWidgets.QLabel("Version: " + var.version, self)
            self.labelstatusversion.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
            var.ui.statusbar.addPermanentWidget(self.labelstatusversion, 0)
        except Exception as error:
            print('Error cargar el statusbar: ', error)

    def selEstado(self):
        if var.ui.rbtTodos.isChecked():
            print('pulsaste todos')
        elif var.ui.rbtAlta.isChecked():
            print('pulsaste alta')
        elif var.ui.rbtBaja.isChecked():
            print('pulsaste baja')

    def resizeTabdrivers(self):
        try:
            header = var.ui.tabDrivers.horizontalHeader()
            for i in range(5):
                if i == 0 or i == 4 or i == 3:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                elif i == 1 or i == 2:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)

        except Exception as error:
            print('error resize en tab drivers', error)
    @staticmethod
    def formatCajatexto(self = None):
        try:
            var.ui.txtApel.setText(var.ui.txtApel.text().title())
            var.ui.txtNome.setText(var.ui.txtNome.text().title())
            salario = var.ui.txtSalario.text()
            valores = "1234567890."
            for n in salario:
                if n in valores:
                    pass
                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Aviso')
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    msg.setText('Valor de Salario incorrect (00000000.00')
                    msg.exec()
                    var.ui.txtSalario.setText("")
                    break
            var.ui.txtSalario.setText(str(locale.currency(float(var.ui.txtSalario.text()),grouping=True)))
        except Exception as error:
            print('error poner letra capital cajas text', error)

    def formatCajamovil(self=None):
        try:
            var.ui.txtApel.setText(var.ui.txtApel.text().title())
            var.ui.txtNome.setText(var.ui.txtNome.text().title())
            movil = var.ui.txtMovil.text()
            valorm = "1234567890"
            for n in movil:
                if n in valorm and len(movil) == 9:
                    pass
                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Aviso')
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    msg.setText('Escriba un número de móvil correcto')
                    msg.exec()
                    var.ui.txtMovil.setText("")
                    break
        except Exception as error:
            print('error poner movil', error)













