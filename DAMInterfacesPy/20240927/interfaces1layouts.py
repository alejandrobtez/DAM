import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtGui import QPalette, QColor

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout = QVBoxLayout()

        button = QPushButton("Botón 1")
        button2 = QPushButton("Botón 2")
        button3 = QPushButton("Botón 3")

        layout.addWidget(button)
        layout.addWidget(button2)
        layout.addWidget(button3)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()