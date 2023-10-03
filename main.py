import eventos, var, sys
from MainWindow import *
from CalendarWindow import *
from datetime import datetime

class Calendar(QtWidgets.QDialog):
    def __init__(self):
        super(Calendar, self).__init__()
        var.calendar = Ui_DialogCalendar()
        var.calendar.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        ano = datetime.now().year


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self) #encargado construir la interfaz
        var.calendar = Calendar()

        '''
        
        zona de eventos de botones
        '''
        var.ui.btnCalendar.clicked.connect(eventos.Eventos.abrirCalendar)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())


