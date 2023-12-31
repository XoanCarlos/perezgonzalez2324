import time

from PyQt6 import QtWidgets, QtCore, QtGui

import conexion
import var
class Clientes():

    def cargaFecha2(qDate):
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtaltacli.setText(data)
            time.sleep(0.8)
            var.calendar.hide()
            return data
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

            newcli.insert(4, prov)
            muni = var.ui.cmbmunicli.currentText()
            newcli.insert(5, muni)
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
            conexion.Conexion.mostrarclientes(0)
        except Exception as error:
            print("error alta cliente", error)

    def cargartablacli(registros):
        try:
            var.ui.tablaClientes.clearContents()
            index = 0
            for registro in registros:
                var.ui.tablaClientes.setRowCount(index + 1)  # crea una fila
                var.ui.tablaClientes.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tablaClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                var.ui.tablaClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[2])))
                var.ui.tablaClientes.setItem(index, 3, QtWidgets.QTableWidgetItem(str(registro[3])))
                var.ui.tablaClientes.setItem(index, 4, QtWidgets.QTableWidgetItem(str(registro[4])))

                var.ui.tablaClientes.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaClientes.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaClientes.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaClientes.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

                index += 1
        except Exception as error:
            print("error cargar dato en tabla", error)

    def bajacliente(self):
        try:
            dni = var.ui.txtdnicli.text()
            conexion.Conexion.borraCli(dni)
            #conexion.Conexion.selectDrivers(1)
        except Exception as error:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText('El conductor no existe o no se puede borrar')
            mbox.exec()


    def cargacliente(self = None):
        try:
            fila = var.ui.tablaClientes.selectedItems()
            row = [dato.text() for dato in fila]
            registro = conexion.Conexion.onecliente(row[0])

            Clientes.cargardatos(registro)

        except Exception as error:
            print('error cargar datos de 1 cliente marcando en la tabla: ', error)

    def cargardatos(registro):
        try:
            datos = [var.ui.lblcodcliente, var.ui.txtdnicli, var.ui.txtaltacli,
                     var.ui.txtrazonsocial, var.ui.txtdircli, var.ui.cmbprocli,
                     var.ui.cmbmunicli, var.ui.txtmovilcli]
            for i, dato in enumerate(datos):
                if i == 5 or i == 6:
                    dato.setCurrentText(str(registro[i]))
                else:
                    dato.setText(str(registro[i]))

        except Exception as error:
            print("cargar datos en panel gestión", error)

    def selectclientes(self):
        try:
            if var.ui.chkclientes.isChecked():
                conexion.Conexion.mostrarclientes(0)
            else:
                conexion.Conexion.mostrarclientes(1)

        except Exception as error:
            print("en select clientes", error)

    def buscacli(self):
        try:
            dni = var.ui.txtdnicli.text()
            registro = conexion.Conexion.codcli(dni)
            if var.ui.chkclientes.isChecked():
                conexion.Conexion.mostrarclientes(0)
            else:
                conexion.Conexion.mostrarclientes(1)
            codigo = var.ui.lblcodcliente.text()
            for fila in range(var.ui.tablaClientes.rowCount()):
                if var.ui.tablaClientes.item(fila, 0).text() == str(codigo):
                    for columna in range(var.ui.tablaClientes.columnCount()):
                        item = var.ui.tablaClientes.item(fila, columna)
                        if item is not None:
                            item.setBackground(QtGui.QColor(255, 241, 150))
        except Exception as error:
            print(error, "en busca de datos de un cliente")

    def modifcli(self):
        try:
            cliente = [var.ui.lblcodcliente, var.ui.txtdnicli, var.ui.txtaltacli,
                     var.ui.txtrazonsocial, var.ui.txtdircli, var.ui.txtmovilcli]
            modifcli = []
            for i in cliente:
                modifcli.append(i.text().title())
            prov = var.ui.cmbprocli.currentText()
            modifcli.insert(5, prov)
            muni = var.ui.cmbmunicli.currentText()
            modifcli.insert(6, muni)
            conexion.Conexion.modifcliente(modifcli)
        except Exception as error:
            print('error en modif cliente en Cientes', error)