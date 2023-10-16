import var, sys
from PyQt6 import QtWidgets

class Eventos():
    @staticmethod
    def salir(self):
        try:
            sys.exit(0)
        except Exception as error:
            print("Error en abrir módulo eventos: ", error)

    @staticmethod
    def abrirCalendar(self):
        try:
            var.calendar.show()
        except Exception as error:
            print('error en abrir calendar: ', error)

    @staticmethod
    def acercade():
        try:
            var.dlgacerca.show()
        except Exception as error:
            print('error abrir ventana acerca: ', error)
    @staticmethod
    def cerraracercade():
        try:
            var.dlgacerca.hide()
        except Exception as error:
            print('error abrir ventana acerca: ', error)

    @staticmethod
    def cerrarsalir():
        try:
            var.dlgsalir.hide()
        except Exception as error:
            print('error abrir ventana acerca : ', error)


    def mostrarsalir(self):
        try:
            var.dlgsalir.show()
        except Exception as error:
            print('error en mostrar ventana salir: ', error)