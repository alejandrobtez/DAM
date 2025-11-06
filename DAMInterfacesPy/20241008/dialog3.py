
import sys

from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QVBoxLayout, QLabel

class CustomDialog(QDialog):
    def __init__(self,isColor):
        super().__init__()

        self.setWindowTitle("HELLO!")

        layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        message.setObjectName('hola')
        if (isColor):
            message.setStyleSheet('QLabel#hola {color: red}')
        else:   
            message.setStyleSheet('QLabel#hola {color: blue}')
        layout.addWidget(message)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.setCheckable (True)
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):

        dlg = CustomDialog(s)
        dlg.exec()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()