import eventos
from MainWindow import *
import sys, var
class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_mainWindow()
        var.ui.setupUi(self) #encargado construir la interfaz

        '''
        
        zona de eventos de botones
        '''
        var.ui.btnSalir.clicked.connect(eventos.Eventos.saludar)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())


