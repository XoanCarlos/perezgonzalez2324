from PyQt6 import QtWidgets, QtSql, QtGui, QtCore
from windowaux import *
from datetime import date, datetime
import drivers
import var
import clientes


class Conexion():
    def conexion(self = None):
        var.bbdd = 'bbdd.sqlite'
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(var.bbdd)
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

    def cargaprovcli(self=None):
        try:
            var.ui.cmbProv.clear()
            query = QtSql.QSqlQuery()
            query.prepare('select provincia from provincias')
            if query.exec():
                var.ui.cmbprocli.addItem('')
                while query.next():
                    var.ui.cmbprocli.addItem(query.value(0))
        except Exception as error:
            print('error en la carga del combo prov', error)

    def selmunicli(self=None):
        try:
            id = 0
            var.ui.cmbmunicli.clear()
            prov = var.ui.cmbprocli.currentText()
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
                var.ui.cmbmunicli.addItem('')
                while query1.next():
                    var.ui.cmbmunicli.addItem(query1.value(0))
        except Exception as error:
            print('error seleccion municipios: ', error)

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
                    return True
                else:
                   return False
                Conexion.mostrardrivers(self=None)
        except Exception as e:
                print("otro error", e)
    @staticmethod
    def mostrardrivers(self):
        try:
            registros = []
            if var.ui.rbtAlta.isChecked():
                estado = 1
                Conexion.selectDrivers(estado)
            else:
                query1 = QtSql.QSqlQuery()
                query1.prepare("select codigo, apeldri, nombredri, movildri, "
                               " carnet, bajadri from drivers")
                if query1.exec():
                    while query1.next():
                        row = [query1.value(i) for i in range(query1.record().count())]  # función lambda
                        registros.append(row)
            if registros:
                drivers.Drivers.cargartabladri(registros)
                return registros
            else:
                var.ui.tabDrivers.setRowCount(0)

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

    def modifDriver(modifdriver):
        try:
            registro = Conexion.onedriver(int(modifdriver[0]))
            if modifdriver == registro[:-1]:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('No hay datos que modificar. Desea cambiar la fecha o eliminar fecha de baja?')
                msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No |
                                          QtWidgets.QMessageBox.StandardButton.Cancel)
                msg.button(QtWidgets.QMessageBox.StandardButton.Yes).setText("Alta")
                msg.button(QtWidgets.QMessageBox.StandardButton.No).setText("Modificar")
                msg.button(QtWidgets.QMessageBox.StandardButton.Cancel).setText('Cancelar')
                opcion = msg.exec()
                if opcion == QtWidgets.QMessageBox.StandardButton.Yes:
                    if registro[11] != '':
                        query1 = QtSql.QSqlQuery()
                        query1.prepare('update drivers set bajadri = NULL where '
                                       ' dnidri = :dni')
                        query1.bindValue(':dni', str(modifdriver[1]))
                        if query1.exec():
                            msg = QtWidgets.QMessageBox()
                            msg.setWindowTitle('Aviso')
                            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                            msg.setText('Datos Conductor Modificados')
                            msg.exec()
                            Conexion.selectDrivers(0)
                    else:
                        msg = QtWidgets.QMessageBox()
                        msg.setWindowTitle('Aviso')
                        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                        msg.setText('El conductor está en alta. Nada que modificar')
                        msg.exec()
                        Conexion.selectDrivers(1)
                elif opcion == QtWidgets.QMessageBox.StandardButton.No:
                    var.calendar2 = QtWidgets.QCalendarWidget()
                    dia = datetime.now().day
                    mes = datetime.now().month
                    ano = datetime.now().year
                    var.calendar2.setSelectedDate((QtCore.QDate(ano, mes, dia)))
                    var.calendar2.clicked.connect(Conexion.handleDateClick)
                    #var.calendar2.selectionChanged.connect(Conexion.showSelectedDate)
                    data = var.calendar2.getSelectedDate()
                    data = data.toString("dd/MM/yyyy")
                    var.calendar2.show()
                    print(data)
                    if registro[11] != '':
                        query1 = QtSql.QSqlQuery()
                        query1.prepare('update drivers set bajadri = :data where '
                                       ' dnidri = :dni')
                        query1.bindValue(':data', str(data))
                        query1.bindValue(':dni', str(modifdriver[1]))
                        if query1.exec():
                            msg = QtWidgets.QMessageBox()
                            msg.setWindowTitle('Aviso')
                            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                            msg.setText('Baja Modificada. Nueva Fecha Baja')
                            msg.exec()
                        Conexion.selectDrivers(0)
                    else:
                        msg = QtWidgets.QMessageBox()
                        msg.setWindowTitle('Aviso')
                        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                        msg.setText('El conductor está en alta. Nada que modificar')
                        msg.exec()
                        Conexion.selectDrivers(1)
                elif opcion == QtWidgets.QMessageBox.StandardButton.Cancel:
                    pass
            else:
                query = QtSql.QSqlQuery()
                query.prepare('update drivers set dnidri = :dni, altadri= :alta, apeldri = :apel, nombredri = :nombre, '
                              ' direcciondri = :direccion, provdri = :provincia, munidri = :municipio, '
                              ' movildri = :movil, salario = :salario, carnet = :carnet where codigo = :codigo')

                query.bindValue(':codigo', int(modifdriver[0]))
                query.bindValue(':dni', str(modifdriver[1]))
                query.bindValue(':alta', str(modifdriver[2]))
                query.bindValue(':apel', str(modifdriver[3]))
                query.bindValue(':nombre', str(modifdriver[4]))
                query.bindValue(':direccion', str(modifdriver[5]))
                query.bindValue(':provincia', str(modifdriver[6]))
                query.bindValue(':municipio', str(modifdriver[7]))
                query.bindValue(':movil', str(modifdriver[8]))
                query.bindValue(':salario', str(modifdriver[9]))
                query.bindValue(':carnet', str(modifdriver[10]))
                if query.exec():
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Aviso')
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    msg.setText('Datos Conductor Modificados')
                    msg.exec()
                    Conexion.selectDrivers(1)
                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Aviso')
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    msg.setText(query.lastError().text())
                    msg.exec()
        except Exception as error:
            print('error en modificar driver en conexion ', error)


    def handleDateClick(self, date):
        Conexion.showSelectedDate(date)
    def borraDriv(dni):
        try:
            query1 = QtSql.QSqlQuery()
            query1.prepare('select bajadri from drivers where '
                          ' dnidri = :dni')
            query1.bindValue(':dni', str(dni))
            if query1.exec():
                while query1.next():
                    valor = query1.value(0)
            if str(valor) == '':
                fecha = datetime.today()
                fecha = fecha.strftime('%d/%m/%Y')
                query = QtSql.QSqlQuery()
                query.prepare('update drivers set bajadri = :fechabaja where '
                              ' dnidri = :dni')
                query.bindValue(':fechabaja', str(fecha))
                query.bindValue(':dni', str(dni))
                if query.exec():
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Aviso')
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    msg.setText('Conductor con dado de Baja')
                    msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText('No existe conductor o conductor dado de baja anteriormente')
                msg.exec()
        except Exception as error:
            print('error en baja driver en conexion ', error)

    def selectDrivers(estado):
        try:
            registros = []
            if int(estado) == 0:
                query = QtSql.QSqlQuery()
                query.prepare("select codigo, apeldri, nombredri, movildri, "
                               " carnet, bajadri from drivers")
                if query.exec():
                    while query.next():
                        row = [query.value(i) for i in range(query.record().count())]   # función lambda
                        registros.append(row)
                if registros:
                    drivers.Drivers.cargartabladri(registros)
                else:
                    var.ui.tabDrivers.setRowCount(0)
            elif int(estado) == 1:
                query = QtSql.QSqlQuery()
                query.prepare("select codigo, apeldri, nombredri, movildri, "
                              " carnet, bajadri from drivers where bajadri is null")
                if query.exec():
                    while query.next():
                        row = [query.value(i) for i in range(query.record().count())]  # función lambda
                        registros.append(row)
                if registros:
                    drivers.Drivers.cargartabladri(registros)
                else:
                    var.ui.tabDrivers.setRowCount(0)
            elif int(estado) == 2:
                query = QtSql.QSqlQuery()
                query.prepare("select codigo, apeldri, nombredri, movildri, "
                              " carnet, bajadri from drivers where bajadri is not null")
                if query.exec():
                    while query.next():
                        row = [query.value(i) for i in range(query.record().count())]  # función lambda
                        registros.append(row)
                if registros:
                    drivers.Drivers.cargartabladri(registros)
                else:
                    var.ui.tabDrivers.setRowCount(0)

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error en cargar tabla o selección de datos')
            msg.exec()

    @staticmethod
    def selectDriverstodos():
        try:
            registros = []
            query = QtSql.QSqlQuery()
            query.prepare("select * from drivers order by apeldri")
            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]  # función lambda
                    registros.append(row)
            return registros
        except Exception as error:
            print('error devolver todos los drivers ', error)

    def guardarcli(newcli):
        try:
            estado = Conexion.controlbajacli(newcli[0])
            print(estado)

            if (newcli[0].strip() == "" or newcli[1].strip() == ""):
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setWindowIcon(QtGui.QIcon('./img/logo.ico'))
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mensaje = 'Faltan Datos. Debe introducir al menos:\n\nDNI, Apellidos, Nombre, Fecha de alta y Móvil'
                mbox.setText(mensaje)
                mbox.exec()
            else:
                if estado == False:
                    query = QtSql.QSqlQuery()
                    query.prepare('insert into clientes (dni, altacli, razonsocial, direccion, provincia, '
                                  ' municipio, telefono) VALUES (:dni, :alta, :razon, :direccion, '
                                  ' :provincia, :municipio, :movil)')
                    query.bindValue(':dni', str(newcli[0]))
                    query.bindValue(':alta', str(newcli[1]))
                    query.bindValue(':razon', str(newcli[2]))
                    query.bindValue(':direccion', str(newcli[3]))
                    query.bindValue(':provincia', str(newcli[4]))
                    query.bindValue(':municipio', str(newcli[5]))
                    query.bindValue(':movil', str(newcli[6]))
                    if query.exec():
                        return True
                elif estado == True:
                    dni = str(var.ui.txtdnicli.text())
                    query = QtSql.QSqlQuery()
                    query.prepare('update clientes set baja = NULL where '
                                  ' dni = :dni')
                    query.bindValue(':dni', str(dni))
                    if query.exec():
                        msg = QtWidgets.QMessageBox()
                        msg.setWindowTitle('Aviso')
                        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                        msg.setText('Cliente dado de Altas')
                        msg.exec()
                else:
                    pass
                Conexion.mostrarclientes(1)
        except Exception as e:
                print("otro error", e)

    @staticmethod
    def mostrarclientes(estado):
        try:
            registros = []
            if estado == 1:
                query1 = QtSql.QSqlQuery()
                query1.prepare("select codcli, razonsocial, telefono, "
                               " provincia, baja from clientes where baja"
                               " is null ")
                if query1.exec():
                    while query1.next():
                        row = [query1.value(i) for i in range(query1.record().count())]  # función lambda
                        registros.append(row)
            else:
                query1 = QtSql.QSqlQuery()
                query1.prepare("select codcli, razonsocial, telefono, "
                               " provincia, baja from clientes")
                if query1.exec():
                    while query1.next():
                        row = [query1.value(i) for i in range(query1.record().count())]  # función lambda
                        registros.append(row)
            if registros:
                clientes.Clientes.cargartablacli(registros)
                return registros
            else:
                var.ui.tabDrivers.setRowCount(0)

        except Exception as error:
            print('error mostrar resultados', error)

    def borraCli(dni):
        try:
            query1 = QtSql.QSqlQuery()
            query1.prepare('select baja from clientes where '
                          ' dni = :dni')
            query1.bindValue(':dni', str(dni))
            if query1.exec():
                while query1.next():
                    valor = query1.value(0)
            if str(valor) == '':
                fecha = datetime.today()
                fecha = fecha.strftime('%d/%m/%Y')
                query = QtSql.QSqlQuery()
                query.prepare('update clientes set baja = :fechabaja where '
                              ' dni = :dni')
                query.bindValue(':fechabaja', str(fecha))
                query.bindValue(':dni', str(dni))
                if query.exec():
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Aviso')
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    msg.setText('Cliente dado de Baja')
                    msg.exec()
                Conexion.mostrarclientes(0)
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText('No existe cliente o cliente dado de baja anteriormente')
                msg.exec()
        except Exception as error:
            print('error en baja cliente en conexion ', error)

    def onecliente(codigo):
        try:
            registro = []

            query = QtSql.QSqlQuery()
            query.prepare('select * from clientes where codcli = :codigo')
            query.bindValue(':codigo', int(codigo))
            if query.exec():
                while query.next():
                    for i in range(9):
                        registro.append(str(query.value(i)))
            return registro
        except Exception as error:
            print('error en fichero conexion datos de 1 driver: ', error)
    def codcli(dni):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('select codcli from clientes where dni = :dnicli')
            query.bindValue(':dnicli', str(dni))
            if query.exec():
                while query.next():
                    codigo = query.value(0)
                if codigo is not None:
                    registro = Conexion.onecliente(codigo)
                    return registro
        except Exception as error:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText('El conductor no existe o error de búsqueda')
            mbox.exec()

    def modifcliente(registro):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('update clientes set dni = :dni, altacli= :alta, razonsocial= :razon, '
                          ' direccion = :direccion, provincia = :provincia, municipio = :municipio, '
                          ' telefono = :telefono where codcli = :codigo')

            query.bindValue(':codigo', int(registro[0]))
            query.bindValue(':dni', str(registro[1]))
            query.bindValue(':alta', str(registro[2]))
            query.bindValue(':razon', str(registro[3]))
            query.bindValue(':direccion', str(registro[4]))
            query.bindValue(':provincia', str(registro[5]))
            query.bindValue(':municipio', str(registro[6]))
            query.bindValue(':telefono', str(registro[7]))
            if query.exec():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Datos Cliente Modificados')
                msg.exec()
                Conexion.selectDrivers(1)
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText(query.lastError().text())
                msg.exec()

        except Exception as error:
            print('error modifica cliente en conexion', error)

    def controlbajacli(dni):
        try:
            baja = ''
            codigo = ''
            query = QtSql.QSqlQuery()
            query.prepare('select codcli, baja from clientes where dni = :dni')
            query.bindValue(':dni', str(dni))
            if query.exec():
                while query.next():
                    codigo = str(query.value(0))
                    baja = str(query.value(1))

            if baja  != '' and codigo != '':
                #modifico la baja
                return True
            elif baja == '' and codigo != '':
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                mbox.setWindowIcon(QtGui.QIcon('./img/logo.ico'))
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('El Cliente esta dado de Alta')
                msg.exec()
            elif baja == '' and codigo == '':
                return False
        except Exception as error:
            print('error control baja cli', error)