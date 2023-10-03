import var
from MainWindow import *
from CalendarWindow import *


class Eventos():

    def salir(self):
        try:
            pass

        except Exception as error:
            print(error, "en módulo eventos ")

    def abrirCalendar(self):

        try:
            var.calendar.show()
        except Exception as error:
            print('error en abrir calendar ', error)

