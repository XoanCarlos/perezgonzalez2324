from drivers import *
from MainWindow import *
from windowaux import *
import var
import drivers
import sys
import eventos
import locale
import conexion
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
        self.driver = Drivers()
        conexion.Conexion.conexion()
        conexion.Conexion.cargaprov()
        conexion.Conexion.mostrardrivers(self)

        '''
       
        zona de eventos de botones
        '''
        var.ui.btnCalendar.clicked.connect(eventos.Eventos.abrirCalendar)
        var.ui.btnAltaDriver.clicked.connect(drivers.Drivers.altadriver)
        var.ui.btnBuscadri.clicked.connect(drivers.Drivers.buscaDri)
        var.ui.btnModifDriver.clicked.connect(drivers.Drivers.modifDri)
        var.ui.btnBajaDriver.clicked.connect(drivers.Drivers.borraDriv)

        """
        
        zona de eventos del menubar
        """
        var.ui.actionSalir.triggered.connect(eventos.Eventos.mostrarsalir)
        var.ui.actionAcerca_de.triggered.connect(eventos.Eventos.acercade)
        var.ui.actionCrear_Copia_Seguridad.triggered.connect(eventos.Eventos.crearbackup)

        '''
        
        zona eventos cajas de texto
        '''
        var.ui.txtDni.editingFinished.connect(Drivers.validarDNI)
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


        '''
        
        eventos de tablas        
        '''
        eventos.Eventos.resizeTabdrivers(self)
        var.ui.tabDrivers.clicked.connect(drivers.Drivers.cargadriver)

        '''
        
        eventos combobox    
    
        '''
        var.ui.cmbProv.currentIndexChanged.connect(conexion.Conexion.selMuni)
        var.ui.rtbGroup.buttonClicked.connect(drivers.Drivers.selEstado)

    def closeEvent(self, event):
        # event.ignore()
        # eventos.Eventos.mostrarsalir()
        mbox = QtWidgets.QMessageBox.information(self, 'Salir', '¿Estás seguro de que quieres salir?',
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)

        if mbox == QtWidgets.QMessageBox.StandardButton.Yes:
            app.quit()
        if mbox == QtWidgets.QMessageBox.StandardButton.No:
            event.ignore()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())
