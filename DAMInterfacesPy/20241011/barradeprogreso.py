#importamos las librerías necesarias
import sys
import time
from PyQt6 import QtWidgets, uic

#Carga la interfaz gráfica y conecta los botones
class Ventana(QtWidgets.QMainWindow):
    '''Esta es la clase principal'''
    #Inicializamos la ventana y conectamos los botones
    def __init__(self, padre=None):
        #Inicializa la ventana
        QtWidgets.QMainWindow.__init__(self, padre)
        uic.loadUi("barradeprogreso.ui",self) #Lee el archivo de QtDesigner
        
        self.setWindowTitle("Ejemplo") #Título de la ventana
        
        #setear barra de progreso 
        self.progressBar 
        #Conectar botón a función
        self.pushButton.clicked.connect(self.auto)
        self.current_value = 0
        #funcion no mencionada
    def funcion(self):
        if self.progressBar.value() < self.progressBar.maximum():
            self.progressBar.setValue(self.progressBar.value() + 20) 
        else:
            self.progressBar.setValue(0)
            self.label.setText("BARRA COMPLETADA")
    
    def auto(self):
        for i in range (20):
            time.sleep(1)
            self.current_value += 20 
            self.progressBar.setValue(self.current_value)
        

# se crea la instancia de la aplicación
app = QtWidgets.QApplication(sys.argv)
# se crea la instancia de la ventana
miVentana = Ventana()
# se muestra la ventana 
miVentana.show()
# se entrega el control al sistema operativo
sys.exit(app.exec())