import eventos, var, sys
from drivers import *
from MainWindow import *
from CalendarWindow import *
from dlgAcerca import *
from dlgSalir import *
from datetime import datetime

class DlgSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DlgSalir, self).__init__()
        var.dlgsalir = Ui_dlgSalir()
        var.dlgsalir.setupUi(self)
        var.dlgsalir.btnSalir.clicked.connect(eventos.Eventos.salir)
        var.dlgsalir.btnCancelar.clicked.connect(eventos.Eventos.cerrarsalir)

class DlgAcerca(QtWidgets.QDialog):
    def __init__(self):
        super(DlgAcerca, self).__init__()
        var.dlgacerca = Ui_dlgAbout()
        var.dlgacerca.setupUi(self)
        var.dlgacerca.btnCerrar.clicked.connect(eventos.Eventos.cerraracercade)

class Calendar(QtWidgets.QDialog):
    def __init__(self):
        super(Calendar, self).__init__()
        var.calendar = Ui_dlgCalendar()
        var.calendar.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        ano = datetime.now().year

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
        
        zona de eventes del menubar
        """
        var.ui.actionSalir.triggered.connect(eventos.Eventos.mostrarsalir)
        var.ui.actionAcerca_de.triggered.connect(eventos.Eventos.acercade)

        '''
        
        zona eventos cajas de texto
        '''
        var.ui.txtDni.editingFinished.connect(Drivers.validarDNI)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())
