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
        self.setFixedSize(QSize(600, 600))
        
    def create_game(self): #creates the game , it's called when user inserts names and clicks start
        self.board = GameCore(self)
        self.setCentralWidget(self.board)
        return self.board
    
    def resize_to_default(self):
        self.setFixedSize(QSize(WINDOW_WIDTH, WINDOW_HEIGHT))
        self.center_window()
        
    def center_window(self):
        # Get the screen resolution from the app's primary screen
        screen = QApplication.primaryScreen().geometry()
        # Calculate the center point
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        # Move the window to the center
        self.move(x, y)
        
    def exit_app(self):
        QApplication.quit()
