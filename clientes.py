from PyQt6 import QtWidgets, QtCore, QtGui

import conexion
import var
class Clientes():

    def cargaFecha2(qDate):
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtaltacli.setText(data)
            return data
            var.calendar.hide()
        except Exception as error:
            print("error en cargar fecha: ", error)

    def validarDNIcli(dni):
        try:
            dni = str(dni).upper()
            var.ui.txtDni.setText(str(dni))
            tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
            dig_ext = "XYZ"
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = "1234567890"
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    var.ui.lbldnicli.setStyleSheet('color:green;')  # si es válido se pone una V en color verde
                    var.ui.lbldnicli.setText('V')
                    return True
                else:
                    var.ui.lbldnicli.setStyleSheet('color:red;')  # y si no un aspa en color rojo
                    var.ui.lbldnicli.setText('X')
                    var.ui.txtdnicli.setText(None)
                    var.ui.txtdnicli.setFocus()
            else:
                var.ui.lbldnicli.setStyleSheet('color:red;')
                var.ui.lbldnicli.setText('X')
                var.ui.txtdnicli.setText(None)
                var.ui.txtdnicli.setFocus()

        except Exception as error:
            print("error en validar dni ", error)
    def altacliente(self):
        try:
            cliente = [var.ui.txtdnicli, var.ui.txtaltacli, var.ui.txtrazonsocial,
                         var.ui.txtdircli, var.ui.txtmovilcli]
            newcli = []

            for i in cliente:
                newcli.append(i.text().title())
            prov = var.ui.cmbprocli.currentText()
            print(newcli)
            newcli.insert(5, prov)
            muni = var.ui.cmbmunicli.currentText()
            newcli.insert(6, muni)
            valor = conexion.Conexion.guardarcli(newcli)
            if valor == True:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setWindowIcon(QtGui.QIcon('./img/logo.ico'))
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("Cliente dado de alta")
                mbox.exec()
            elif valor == False:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setWindowIcon(QtGui.QIcon('./img/logo.ico'))
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Asegúrese de que el cliente no existe")
                mbox.exec()
        except Exception as error:
            print("error alta cliente", error)