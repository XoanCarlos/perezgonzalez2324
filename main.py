from drivers import *
from MainWindow import *
from windowaux import *
from dlgSalir import *
import var, drivers, sys, eventos
from datetime import datetime
import locale
from PyQt6.QtCore import Qt

# Establecer la configuración regional en español
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)
        var.calendar = Calendar()
        var.dlgacerca = DlgAcerca()
        var.dlgsalir = DlgSalir()
        self.driver = Drivers()

        '''
       
        zona de eventos de botones
        '''
        var.ui.btnCalendar.clicked.connect(eventos.Eventos.abrirCalendar)

        """
        
        zona de eventos del menubar
        """
        var.ui.actionSalir.triggered.connect(eventos.Eventos.mostrarsalir)
        var.ui.actionAcerca_de.triggered.connect(eventos.Eventos.acercade)

        '''
        
        zona eventos cajas de texto
        '''
        var.ui.txtDni.editingFinished.connect(Drivers.validarDNI)

        '''
         eventos del toolbar
        '''
        var.ui.actionbarSalir.triggered.connect(eventos.Eventos.mostrarsalir)
        var.ui.actionlimpiaPaneldriver.triggered.connect(drivers.Drivers.limpiapanel)

        '''
        
        statusbar
        '''
               # Formatear la fecha según el formato deseadofecha_actual.strftime()

        fecha = datetime.now().strftime("%A  -  " + "%d/%m/%Y")
        self.labelstatus = QtWidgets.QLabel(fecha, self)
        self.labelstatus.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        var.ui.statusbar.addPermanentWidget(self.labelstatus,1)

        #
        var.ui.statusbar.showMessage(fecha)
        '''
           
        ejecución de diferentes funciones al lanzar la aplicación
        '''

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
    window.show()
    sys.exit(app.exec())
