from PyQt6 import QtWidgets, QtSql, QtGui

import drivers
import var
import sqlite3


class Conexion():
    def conexion(self = None):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('bbdd.sqlite')
        if not db.open():
            print('error de conexión')
            return False
        else:
            print('base datos conectada')
            return True

    def cargaprov(self = None):
        try:
            var.ui.cmbProv.clear()
            query = QtSql.QSqlQuery()
            query.prepare('select provincia from provincias')
            if query.exec():
                var.ui.cmbProv.addItem('')
                while query.next():
                    var.ui.cmbProv.addItem(query.value(0))
        except Exception as error:
            print('error en la carga del combo prov', error)

    def selMuni(self=None):
        try:
            id = 0
            var.ui.cmbMuni.clear()
            prov = var.ui.cmbProv.currentText()
            query = QtSql.QSqlQuery()
            query.prepare('select idprov from provincias where provincia = :prov')
            query.bindValue(':prov', prov)
            if query.exec():
                while query.next():
                    id = query.value(0)
            query1 = QtSql.QSqlQuery()
            query1.prepare('select municipio from municipios where idprov = :id')
            query1.bindValue(':id', int(id))
            if query1.exec():
                var.ui.cmbMuni.addItem('')
                while query1.next():
                    var.ui.cmbMuni.addItem(query1.value(0))
        except Exception as error:
            print('error seleccion municipios: ', error)

    @staticmethod
    def guardardri(newdriver):
        try:
            if (newdriver[0].strip() == "" or newdriver[1].strip() == "" or newdriver[2].strip() == ""
                    or newdriver[3].strip() == "" or newdriver[7].strip() == ""):
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setWindowIcon(QtGui.QIcon('./img/logo.ico'))
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mensaje = 'Faltan Datos. Debe introducir al menos:\n\nDNI, Apellidos, Nombre, Fecha de alta y Móvil'
                mbox.setText(mensaje)
                mbox.exec()
            else:
                query = QtSql.QSqlQuery()
                query.prepare('insert into drivers (dnidri, altadri, apeldri, nombredri, direcciondri, provdri, '
                              ' munidri, movildri, salario, carnet) VALUES (:dni, :alta, :apel, :nombre,:direccion, '
                              ' :provincia, :municipio, :movil, :salario, :carnet)')
                query.bindValue(':dni', str(newdriver[0]))
                query.bindValue(':alta', str(newdriver[1]))
                query.bindValue(':apel', str(newdriver[2]))
                query.bindValue(':nombre', str(newdriver[3]))
                query.bindValue(':direccion', str(newdriver[4]))
                query.bindValue(':provincia', str(newdriver[5]))
                query.bindValue(':municipio', str(newdriver[6]))
                query.bindValue(':movil', str(newdriver[7]))
                query.bindValue(':salario', str(newdriver[8]))
                query.bindValue(':carnet', str(newdriver[9]))
                if query.exec():
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setWindowIcon(QtGui.QIcon('./img/logo.ico'))
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    mbox.setText("Empleado dado de alta")
                    mbox.exec()
                else:
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setWindowIcon(QtGui.QIcon('./img/logo.ico'))
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox.setText("Asegúrese de que el conductor no existe")
                    mbox.exec()
                Conexion.mostrardrivers(self=None)
        except Exception as e:
                print("otro error", e)

    def mostrardrivers(self):
        try:
            registros = []
            query1 = QtSql.QSqlQuery()
            query1.prepare("select codigo, apeldri, nombredri, movildri, "
                           " carnet, bajadri from drivers")
            if query1.exec():
                while query1.next():
                    row = [query1.value(i) for i in range(query1.record().count())]   # función lambda
                    registros.append(row)
            #drivers.Drivers.cargartabladri(registros)
            return registros
        except Exception as error:
            print('error mostrar resultados', error)

    def onedriver(codigo):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('select * from drivers where codigo = :codigo')
            query.bindValue(':codigo', int(codigo))
            if query.exec():
                while query.next():
                    for i in range(12):
                        registro.append(str(query.value(i)))
            return registro

        except Exception as error:
            print('error en fichero conexion datos de 1 driver: ', error)

    def codDri(dni):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('select codigo from drivers where dnidri = :dnidri')
            query.bindValue(':dnidri', str(dni))
            if query.exec():
                while query.next():
                    codigo = query.value(0)
                if codigo is not None:
                    registro = Conexion.onedriver(codigo)
                    return registro

        except Exception as error:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText('El conductor no existe o error de búsqueda')
            mbox.exec()
