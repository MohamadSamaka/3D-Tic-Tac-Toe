from PyQt6.QtWidgets import  QWidget, QVBoxLayout
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtCore import Qt
from ..widgets.start_game_btn import StartGameButton
from ..widgets.player_name_input import Player_Input
from ..defaults import WINDOW_HEIGHT, WINDOW_WIDTH

class MainMenu(QWidget):
    def __init__(self, parent, create_game_func):
        super().__init__(parent)
        self.setObjectName('game-menu')
        self.setFixedHeight(WINDOW_HEIGHT)
        self.setFixedWidth(WINDOW_WIDTH)
        self.create_menu(create_game_func)
    
    def create_menu(self, create_game_func):
        self.menu = QVBoxLayout(self)
        self.menu.addWidget(Player_Input("Player 1 Name"))
        self.menu.addWidget(Player_Input("Player 2 Name"))
        self.start_game_button = StartGameButton(create_game_func)
        self.menu.addWidget(self.start_game_button)
        self.menu.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.menu)
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor('red'))  # Set the background color
        self.setPalette(palette)
        self.setAutoFillBackground(True)
        
