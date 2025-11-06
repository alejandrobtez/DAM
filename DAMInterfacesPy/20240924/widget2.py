import sys
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        contenedor = QWidget()
 
        layout = QVBoxLayout()
 
        widget = QLabel("Hello")
        font = widget.font()
        font.setPointSize(10)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
 
        widget2 = QLabel("Goodbye")
        font2 = widget2.font()
        font2.setPointSize(10)
        widget2.setFont(font2)
        widget2.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight)
 
        layout.addWidget(widget)
        layout.addWidget(widget2)
 
        contenedor.setLayout(layout)
 
        self.setCentralWidget(contenedor)
 
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
 