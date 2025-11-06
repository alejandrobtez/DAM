import sys
import requests 
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import *

# Clase del formulario
class Form(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("proyecto2.ui", self) # Implementamos el archivo de QtDesigner
        self.setWindowTitle("Recogida de datos")
        self.pushButton.clicked.connect(self.datos) #Conectamos el botón con la función
    def datos(self):

        # Atribuimos los valores a las variables
        nombre = self.lineedit.text()
        apellido = self.lineedit2.text()
        apellido2 = self.lineedit3.text()
        telefono = self.lineedit4.text()
        correo = self.lineedit5.text()

        # Comprobamos que el usuario ha rellenado todos los apartados
        if not nombre or not apellido or not apellido2 or not telefono or not correo:
            QMessageBox.critical(self, "Campos vacíos", "Por favor, rellena todos los campos.")
            return
        
        # Comprobamos que el apartado de telefono esta compuesto por números
        if not telefono.isdigit():
            QMessageBox.critical(self,"Número de teléfono no válido","Carácter no permitido, introduzca su número de teléfono.")
            return
        
        #Recogemos la información en un único mensaje
        mensaje = (
            f"Nombre: {nombre}\n"
            f"Primer Apellido: {apellido}\n"
            f"Segundo Apellido: {apellido2}\n"
            f"Teléfono: {telefono}\n"
            f"Correo: {correo}"
        )

        # Confrimamos que los datos sean correctos y los mostramos
        confirmacion = QMessageBox.question(self,"Confirmar datos",f"¿Son estos tus datos?\n{mensaje}",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        # Damos opciones a los botones del QMessageBox.question
        if confirmacion == QMessageBox.StandardButton.Yes:
            QMessageBox.information(self, "Datos confirmados", "¡Gracias por rellenar el formulario!")
            self.close()  # Cierra el formulario si los datos son correctos
        else:
            QMessageBox.warning(self, "Datos incorrectos", "Corrige tus datos.")
            return

        print(mensaje) # Imprimimos los datos por pantalla
        self.close() # Cerramos el formulario

        # Declaramos los datos del bot de telegram
        token = 'tu_token'
        chat_id = 'tu_chat_id' 
        url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={mensaje}'
        # Activamos la url para enviar el mensaje
        r = requests.get(url)


# Clase del diálogo personalizado
class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
 
        # Configuracion del dialogo
        self.setWindowTitle("Recogida de datos")
 
        QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
 
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.form)  # Conectar botones a sus funciones
        self.buttonBox.rejected.connect(self.alerta)

        #Creo un Layout para meter el dialogo dentro
        layout = QVBoxLayout()
        message = QLabel("¿Seguro que deseas rellenar el formulario?")
        layout.addWidget(message)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)
    
    # Funcion de Cancel del dialogo
    def alerta(self):
        QMessageBox.warning(self, "Formulario cancelado.", "¡Hasta la próxima!")
        self.close()
 
    # Funcion de Ok del dialogo
    def form(self):
        
        # Confirmamos que el usuario es mayor de edad
        edad = QMessageBox.question(self,"Edad","¿Eres mayor de edad?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        # Damos opciones a los botones del QMessageBox.question
        # Funcion del yes, abre el formulario
        if edad == QMessageBox.StandardButton.Yes:
            QMessageBox.information(self, "Importante", "Los datos no se usarán para ninguna actividad ilegal.")
            self.close()  # Cierra el QMessage
            self.parent().setEnabled(False)  # Deshabilitar la ventana principal
            self.formulario = Form() 
            self.formulario.show() # Muestra la clase Form
            self.formulario.destroyed.connect(lambda: self.parent().setEnabled(True))  # Rehabilitar al cerrar

        # Función del No
        else:
            QMessageBox.critical(self, "Prohibido", "Acceso permitido para mayores de edad.")
            self.close() #Cierra el QMessage

#Clase de la ventana principal
class Ventana(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Recogida de datos")
 
        button = QPushButton("Formulario.") #Botón para entrar al dialogo
        button.setCheckable(True)
        button.clicked.connect(self.click) #Conecta el botón con su función
        self.setCentralWidget(button)
 
    #Funcion del QPushButton "Formulario" 
    def click(self):
        dlg = CustomDialog(self)
        dlg.exec() # Ejecuta QDialog
        self.close() # Cierra la ventana principal
 
app = QtWidgets.QApplication(sys.argv)
miVentana = Ventana()
miVentana.show()
sys.exit(app.exec())
