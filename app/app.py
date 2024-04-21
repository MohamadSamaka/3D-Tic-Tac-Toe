from PyQt6.QtWidgets import QApplication
from .src.windows.gui import GUI
from sys import argv

class App:
    def __init__(self):
        app = QApplication(argv)
        window = GUI()
        window.show()    
        app.exec()
        