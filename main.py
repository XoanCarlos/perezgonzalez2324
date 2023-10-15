from drivers import *
from MainWindow import *
from windowaux import *
from dlgSalir import *
import var, drivers, sys, eventos

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
           
        ejecución de diferentes funciones al lanzar la aplicación
        '''


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())
