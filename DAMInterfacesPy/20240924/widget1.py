import sys 
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QVBoxLayout
from PyQt6.QtGui import QPixmap

class Mainwindow (QMainWindow):
    def __init__(self):
        super().__init__()

        label = QLabel(self)
        pixmap = QPixmap("hola.jpg")
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())
        self.setWindowTitle("ea ea ea Getafe es una aldea")
        self.setCentralWidget(label)

app = QApplication(sys.argv)
window = Mainwindow()
window.show()
app.exec()


