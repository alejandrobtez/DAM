import sys
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtGui import QPalette, QColor

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QHBoxLayout()
        layout4 = QHBoxLayout()
        layout5 = QVBoxLayout()

        layout1.setContentsMargins(0,0,0,0)
        layout1.setSpacing(20)
        layout1.addLayout(layout2)
        
        layout2.addWidget(Color("Purple"))
        layout2.addLayout(layout3)

        layout3.addWidget(Color("red"))
        layout3.addWidget(Color("white"))
        layout3.addWidget(Color("red"))

        layout1.addLayout(layout4)

        layout4.addWidget(Color("green"))

        layout4.addLayout(layout5)

        layout5.addWidget(Color("blue"))
        layout5.addWidget(Color("yellow"))
        layout5.addWidget(Color("blue"))

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()