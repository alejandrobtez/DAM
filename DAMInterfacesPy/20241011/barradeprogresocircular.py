import sys
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPainter, QPen, QColor, QFont
from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout
 
class CircularProgress(QWidget):
    def __init__(self):
        super().__init__()
 
        self.minimum = 0
        self.maximum = 100
        self.value = 0
 
        self.progress_color = QColor("#03A9F4")  # Color de progreso
        self.background_color = QColor("#E5E5E5")  # Color de fondo
 
        self.width = 200
        self.height = 200
 
        self.animation = QTimer()
        self.animation.timeout.connect(self.animate)
        self.animation.start(100)  # 100 ms (0.1 segundos) para actualizar
 
        self.increment_value = 0.5  # Incrementar 0.5 por cada tick para 20 segundos
 
    def animate(self):
        if self.value < self.maximum:
            self.value += self.increment_value
            self.update()
        else:
            self.animation.stop()  # Detener el temporizador cuando alcance 100
 
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
 
        # Dibujar el fondo circular
        painter.setPen(QPen(self.background_color, 10))
        painter.drawEllipse(10, 10, self.width - 20, self.height - 20)
 
        # Dibujar el progreso basado en el valor
        angle_span = int(360 * (self.value / self.maximum))  # Proporción de la barra de progreso
        painter.setPen(QPen(self.progress_color, 10))
        painter.drawArc(10, 10, self.width - 20, self.height - 20, 90 * 16, -angle_span * 16)
 
        # Dibujar el texto del porcentaje
        font = QFont("Arial", 28)
        painter.setFont(font)
 
        text = f"{int(self.value)}%"  # Mostrar el valor entero del progreso
        painter.drawText(self.rect(), Qt.AlignmentFlag.AlignCenter, text)
 
    def setValue(self, value):
        if value < self.minimum:
            value = self.minimum
        elif value > self.maximum:
            value = self.maximum
 
        self.value = value
        self.update()
 
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
 
        self.progress = CircularProgress()
        self.setMinimumHeight(250)
        self.setMinimumWidth(250)
 
        layout = QVBoxLayout()
        layout.addWidget(self.progress)
 
        self.setLayout(layout)
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
 