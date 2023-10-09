import var
class Drivers():
    @staticmethod
    def validarDNI(self = None):
        try:
            dni = var.ui.txtDni.text()
            dni = dni.upper() #poner mayúscula
            var.ui.txtDni.setText(dni)
            tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
            dig_ext = "XYZ"
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = "1234567890"
            if len(dni) == 9 :          #comprueba que son nueve
                dig_control = dni[8]    #tomo la letra del dni
                dni = dni[:8]           #tomo los números del dni
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) %23] == dig_control:
                    var.ui.lblValidardni.setStyleSheet('color:green;') # si es válido se pone una V en color verde
                    var.ui.lblValidardni.setText('V')
                else:
                    var.ui.lblValidardni.setStyleSheet('color:red;') #y si no un aspa en color rojo
                    var.ui.lblValidardni.setText('X')
                    var.ui.txtDni.setText("")
                    var.ui.txtDni.setFocus()
            else:
                var.ui.lblValidardni.setStyleSheet('color:red;')
                var.ui.lblValidardni.setText('X')
                var.ui.txtDni.setText("")
                var.ui.txtDni.setFocus()

        except Exception as error:
            print("error en validar dni ", error)