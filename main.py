import clientes
from MainWindow import *
from windowaux import *
import var
import drivers
import sys
import eventos
import locale
import conexion
import informes
# Establecer la configuración regional en español
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)
        var.calendar = Calendar()
        var.dlgacerca = DlgAcerca()
        var.dlgabrir = FileDialogAbrir()
        #self.driver = Drivers()
        conexion.Conexion.conexion()
        conexion.Conexion.cargaprov()
        conexion.Conexion.cargaprovcli()
        estado = 1
        estadocli = 0
        conexion.Conexion.selectDrivers(estado)
        conexion.Conexion.mostrarclientes(estadocli)
        eventos.Eventos.cargastatusbar(self)

        '''
       
        zona de eventos de botones
        '''
        var.ui.btnCalendar.clicked.connect(eventos.Eventos.abrirCalendar)
        var.ui.btnCalendardri.clicked.connect(eventos.Eventos.abrirCalendar)
        var.ui.btnAltaDriver.clicked.connect(drivers.Drivers.altadriver)
        var.ui.btnBuscadri.clicked.connect(drivers.Drivers.buscaDri)
        var.ui.btnModifDriver.clicked.connect(drivers.Drivers.modifDri)
        var.ui.btnBajaDriver.clicked.connect(drivers.Drivers.borraDriv)
        var.ui.btnAltacli.clicked.connect(clientes.Clientes.altacliente)
        var.ui.btnBajacli.clicked.connect(clientes.Clientes.bajacliente)
        var.ui.btnbuscacli.clicked.connect(clientes.Clientes.buscacli)
        var.ui.btnModifcli.clicked.connect(clientes.Clientes.modifcli)
        """
        
        zona de eventos del menubar
        """
        var.ui.actionSalir.triggered.connect(eventos.Eventos.mostrarsalir)
        var.ui.actionAcerca_de.triggered.connect(eventos.Eventos.acercade)
        var.ui.actionCrear_Copia_Seguridad.triggered.connect(eventos.Eventos.crearbackup)
        var.ui.actionRestaurar_Copia_Seguridad.triggered.connect(eventos.Eventos.restaurarbackup)
        var.ui.actionExportar_Datos_Excel.triggered.connect(eventos.Eventos.exportardatosxls)
        var.ui.actionImportar_Datos_XLS.triggered.connect(eventos.Eventos.importardatosxls)
        var.ui.actionListado_Clientes.triggered.connect(informes.Informes.reportclientes)
        '''
        
        zona eventos cajas de texto
        '''
        var.ui.txtDni.editingFinished.connect(lambda: drivers.Drivers.validarDNI(var.ui.txtDni.text()))
        var.ui.txtdnicli.editingFinished.connect(lambda: clientes.Clientes.validarDNIcli(var.ui.txtdnicli.text()))
        #var.ui.txtDni.editingFinished.connect(lambda: drivers.Drivers.validarDNI(var.ui.txtDni.displayText()))

        var.ui.txtNome.editingFinished.connect(eventos.Eventos.formatCajatexto)
        var.ui.txtApel.editingFinished.connect(eventos.Eventos.formatCajatexto)
        var.ui.txtSalario.editingFinished.connect(eventos.Eventos.formatCajatexto)
        var.ui.txtMovil.editingFinished.connect(eventos.Eventos.formatCajamovil)

        '''
         eventos del toolbar
        '''
        var.ui.actionbarSalir.triggered.connect(eventos.Eventos.mostrarsalir)
        var.ui.actionlimpiaPaneldriver.triggered.connect(drivers.Drivers.limpiapanel)
        var.ui.actioncrearbackup.triggered.connect(eventos.Eventos.crearbackup)
        var.ui.actionrestaurarbackup.triggered.connect(eventos.Eventos.restaurarbackup)


        '''
        
        eventos de tablas        
        '''
        eventos.Eventos.resizeTabdrivers(self)
        eventos.Eventos.resizeTabclientes(self)
        var.ui.tabDrivers.clicked.connect(drivers.Drivers.cargadriver)
        var.ui.tablaClientes.clicked.connect(clientes.Clientes.cargacliente)


        '''
        
        eventos combobox    
    
        '''
        var.ui.cmbProv.currentIndexChanged.connect(conexion.Conexion.selMuni)
        var.ui.cmbprocli.currentIndexChanged.connect(conexion.Conexion.selmunicli)
        var.ui.rtbGroup.buttonClicked.connect(drivers.Drivers.selEstado)
        var.ui.chkclientes.stateChanged.connect(clientes.Clientes.selectclientes)

    def closeEvent(self, event):
        mbox = QtWidgets.QMessageBox(self)
        mbox.setWindowTitle('Salir')
        mbox.setText('¿Estás seguro de que quieres salir?')
        mbox.setIcon(QtWidgets.QMessageBox.Icon.Question)

        # Cambiar texto de los botones a español
        boton_si = mbox.addButton('Sí', QtWidgets.QMessageBox.ButtonRole.YesRole)
        boton_no = mbox.addButton('No', QtWidgets.QMessageBox.ButtonRole.NoRole)

        # Mostrar el cuadro de diálogo
        mbox.exec()
        if mbox.clickedButton() == boton_si:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    try:
        app = QtWidgets.QApplication([])
        window = Main()
        window.showMaximized()
        sys.exit(app.exec())
    except Exception as error:
        print(error)
