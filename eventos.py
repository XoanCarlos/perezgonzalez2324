import var
class Eventos():
    def saludar(self):
        try:
            var.ui.lblTitulo.setText("hola has pulsado el botón")

        except Exception as error:
            print(error, "en módulo eventos ")