from PyQt6 import QtWidgets, QtCore, QtGui

import conexion
import var


class Drivers():

    @staticmethod
    def limpiapanel(self):
        try:
            listawidgets = [var.ui.lblcodbd, var.ui.txtDni, var.ui.txtDatadriver, var.ui.txtApel, var.ui.txtNome,
                            var.ui.txtDirdriver, var.ui.txtMovil, var.ui.txtSalario, var.ui.lblValidardni]

            for i in listawidgets:
                i.setText(None)

            chklicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]
            for i in chklicencia:
                i.setChecked(False)
            var.ui.cmbProv.setCurrentText('')
            var.ui.cmbMuni.setCurrentText('')
            registros = conexion.Conexion.mostrardrivers(self)
            Drivers.cargartabladri(registros)
        except Exception as error:
            print('error limpia panel driver: ', error)

    def cargaFecha(qDate):
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtDatadriver.setText(str(data))
            var.calendar.hide()
        except Exception as error:
            print("error en cargar fecha: ", error)

    @staticmethod
    def validarDNI(self=None):
        try:
            dni = var.ui.txtDni.text()
            dni = dni.upper()  # poner mayúscula
            var.ui.txtDni.setText(dni)
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
                    var.ui.lblValidardni.setStyleSheet('color:green;')  # si es válido se pone una V en color verde
                    var.ui.lblValidardni.setText('V')
                else:
                    var.ui.lblValidardni.setStyleSheet('color:red;')  # y si no un aspa en color rojo
                    var.ui.lblValidardni.setText('X')
                    var.ui.txtDni.setText(None)
                    var.ui.txtDni.setFocus()
            else:
                var.ui.lblValidardni.setStyleSheet('color:red;')
                var.ui.lblValidardni.setText('X')
                var.ui.txtDni.setText(None)
                var.ui.txtDni.setFocus()

        except Exception as error:
            print("error en validar dni ", error)

    def altadriver(self):
        try:
            driver = [var.ui.txtDni, var.ui.txtDatadriver, var.ui.txtApel, var.ui.txtNome,
                      var.ui.txtDirdriver, var.ui.txtMovil, var.ui.txtSalario]
            newdriver = []
            for i in driver:
                newdriver.append(i.text().title())
            prov = var.ui.cmbProv.currentText()
            newdriver.insert(5, prov)
            muni = var.ui.cmbMuni.currentText()
            newdriver.insert(6, muni)
            licencias = []
            chklicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]
            for i in chklicencia:
                if i.isChecked():
                    licencias.append(i.text())
            newdriver.append('-'.join(licencias))
            conexion.Conexion.guardardri(newdriver)

        except Exception as error:
            print("error alta cliente", error)

    def cargartabladri(registros):
        try:
            print(registros)
            var.ui.tabDrivers.clearContents()
            index = 0
            for registro in registros:
                var.ui.tabDrivers.setRowCount(index + 1)  # crea una fila
                var.ui.tabDrivers.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tabDrivers.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                var.ui.tabDrivers.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[2])))
                var.ui.tabDrivers.setItem(index, 3, QtWidgets.QTableWidgetItem(str(registro[3])))
                var.ui.tabDrivers.setItem(index, 4, QtWidgets.QTableWidgetItem(str(registro[4])))
                var.ui.tabDrivers.setItem(index, 5, QtWidgets.QTableWidgetItem(str(registro[5])))
                var.ui.tabDrivers.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabDrivers.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabDrivers.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                index += 1
        except Exception as error:
            print("error cargar dato en tabla", error)

    def cargadriver(self = None):
        try:
            registros = conexion.Conexion.mostrardrivers(self)
            Drivers.cargartabladri(registros)
            row = var.ui.tabDrivers.selectedItems()
            fila = [dato.text() for dato in row]
            print(fila)
            registro = conexion.Conexion.onedriver(fila[0])
            Drivers.cargardatos(registro)

        except Exception as error:
            print('error cargar datos de 1 cliente marcando en la tabla: ', error)

    def buscaDri(self):
        try:
            dni = var.ui.txtDni.text()
            registro = conexion.Conexion.codDri(dni)
            Drivers.cargardatos(registro)
            registros = conexion.Conexion.mostrardrivers(self=None)
            Drivers.cargartabladri(registros)
            codigo = var.ui.lblcodbd.text()
            for fila in range(var.ui.tabDrivers.rowCount()):
                if var.ui.tabDrivers.item(fila, 0).text() == str(codigo):
                    #var.ui.tabDrivers.selectRow(fila)
                    var.ui.tabDrivers.scrollToItem(var.ui.tabDrivers.item(fila, 0))
                    var.ui.tabDrivers.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                    var.ui.tabDrivers.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(registro[3])))
                    var.ui.tabDrivers.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(registro[4])))
                    var.ui.tabDrivers.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(registro[8])))
                    var.ui.tabDrivers.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(registro[10])))
                    var.ui.tabDrivers.setItem(fila, 5, QtWidgets.QTableWidgetItem(str(registro[11])))
                    var.ui.tabDrivers.item(fila, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabDrivers.item(fila, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabDrivers.item(fila, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabDrivers.item(fila, 0).setBackground(QtGui.QColor(255, 241, 150))
                    var.ui.tabDrivers.item(fila, 1).setBackground(QtGui.QColor(255, 241, 150))
                    var.ui.tabDrivers.item(fila, 2).setBackground(QtGui.QColor(255, 241, 150))
                    var.ui.tabDrivers.item(fila, 3).setBackground(QtGui.QColor(255, 241, 150))
                    var.ui.tabDrivers.item(fila, 4).setBackground(QtGui.QColor(255, 241, 150))
                    var.ui.tabDrivers.item(fila, 5).setBackground(QtGui.QColor(255, 241, 150))
                    break
        except Exception as error:
            print(error, "en busca de datos de un conductor")


    def cargardatos(registro):
        try:
            #Drivers.limpiapanel(self = None)
            datos = [var.ui.lblcodbd, var.ui.txtDni, var.ui.txtDatadriver, var.ui.txtApel, var.ui.txtNome,
                     var.ui.txtDirdriver, var.ui.cmbProv, var.ui.cmbMuni, var.ui.txtMovil, var.ui.txtSalario]
            for i, dato in enumerate(datos):
                if i == 6 or i == 7:
                    dato.setCurrentText(str(registro[i]))
                else:
                    dato.setText(str(registro[i]))
            if 'A' in registro[10]:
                var.ui.chkA.setChecked(True)
            else:
                var.ui.chkA.setChecked(False)
            if 'B' in registro[10]:
                var.ui.chkB.setChecked(True)
            else:
                var.ui.chkB.setChecked(False)
            if 'C' in registro[10]:
                var.ui.chkC.setChecked(True)
            else:
                var.ui.chkC.setChecked(False)
            if 'D' in registro[10]:
                var.ui.chkD.setChecked(True)
            else:
                var.ui.chkD.setChecked(False)
            #registros = conexion.Conexion.mostrardrivers()
            Drivers.cargartabladri(conexion.Conexion.mostrardrivers())

        except Exception as error:
            print("cargar datos en panel gestión", error)

    def modifDri(self):
        try:
            driver = [var.ui. lblcodbd, var.ui.txtDni, var.ui.txtDatadriver, var.ui.txtApel, var.ui.txtNome,
                      var.ui.txtDirdriver, var.ui.txtMovil, var.ui.txtSalario]
            modifdriver = []
            for i in driver:
                modifdriver.append(i.text().title())
            prov = var.ui.cmbProv.currentText()
            modifdriver.insert(6, prov)
            muni = var.ui.cmbMuni.currentText()
            modifdriver.insert(7, muni)
            licencias = []
            chklicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]
            for i in chklicencia:
                if i.isChecked():
                    licencias.append(i.text())
            modifdriver.append('-'.join(licencias))
            conexion.Conexion.modifDriver(modifdriver)
        except Exception as error:
            print('error en modif drivaer en Drivers', error)





























