from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QMainWindow, QApplication
from ..defaults import WINDOW_HEIGHT, WINDOW_WIDTH
from ..inner_windows.game_core import GameCore
from ..inner_windows.menu import MainMenu
from ..helpers.shared import Shared

class GUI(QMainWindow):
    TITLE = "Tic Tac Toe"
    def __init__(self):
        super().__init__()
        self.initaite_window()
        self.main_menu = MainMenu(self, self.create_game)
        self.setCentralWidget(self.main_menu)

        Shared.MAIN_APP_WINDOW = self
        

    def initaite_window(self):
        self.setWindowTitle(GUI.TITLE)
        self.setFixedSize(QSize(WINDOW_WIDTH, WINDOW_HEIGHT))
        
    def create_game(self):
        self.board = GameCore(self)
        self.setCentralWidget(self.board)
        return self.board
    
    
    def exit_app(self):
        QApplication.quit()
