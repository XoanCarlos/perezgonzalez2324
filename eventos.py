import var, sys


class Eventos():
    @staticmethod
    def salir(self):
        try:
            sys.exit(0)
        except Exception as error:
            print(error, "en módulo eventos ")

    @staticmethod
    def abrirCalendar(self):

        try:
            var.calendar.show()
        except Exception as error:
            print('error en abrir calendar ', error)

    @staticmethod
    def acercade():
        try:
            pass
        except Exception as error:
            print('error abrir ventana acerca de', error)

