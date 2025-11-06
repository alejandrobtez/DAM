import sys
import time
from PyQt6 import QtWidgets, uic

class Ventana(QtWidgets.QMainWindow):
    def __init__(self,padre = None):
        QtWidgets.QMainWindow.__init__(self,padre)
        uic.loadUi("ejercicio.ui", self)

        self.setWindowTitle("Ejercicio")

        self.pushButton1.clicked.connect(self.barra)
        self.pushButton.clicked.connect(self.resp)
        self.pushButton_2.clicked.connect(self.color)
        self.current_value = 0

    def barra(self):
        for i in range (4):
            time.sleep(0.5)
            self.current_value += 25 
            self.progressBar.setValue(self.current_value)
            if self.current_value == 100 :
                self.label.setText("BARRA COMPLETADA, ENHORABUENA")
                self.label.setStyleSheet("color: green;")
    
    def resp(self):
        if self.label_3.text() == "":
            self.label_3.setText("Forza atleti.")
        else:
            self.label_3.setText("")
            self.label_3.setStyleSheet("color:black;")

    def color(self):
        if self.label_3.styleSheet() == "color: grey;":
            self.label_3.setStyleSheet("color: red;")
        else:
                self.label_3.setStyleSheet("color: grey;")



    
# se crea la instancia de la aplicación
app = QtWidgets.QApplication(sys.argv)
# se crea la instancia de la ventana
miVentana = Ventana()
# se muestra la ventana 
miVentana.show()
# se entrega el control al sistema operativo
sys.exit(app.exec())