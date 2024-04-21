from PyQt6.QtWidgets import  QWidget, QVBoxLayout
from PyQt6.QtCore import Qt
from ..widgets.start_game_btn import StartGameButton
from ..widgets.player_name_input import Player_Input

from app.src.defaults import BLACK_BORDER

class MainMenu(QWidget):
    def __init__(self, parent, create_game_func):
        super().__init__(parent)
        self.configure()
        self.create_menu(create_game_func)
        
    def configure(self):
        self.setObjectName('game-menu')
        self.setStyleSheet(BLACK_BORDER)  # Using CSS-like properties
                
    def create_menu(self, create_game_func):
        self.menu = QVBoxLayout(self)
        self.menu.addWidget(Player_Input("Player 1 Name"))
        self.menu.addWidget(Player_Input("Player 2 Name"))
        self.menu.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.create_start_game_btn(create_game_func)
        self.setLayout(self.menu)
        
        
    def create_start_game_btn(self, create_game_func):
        self.start_game_button = StartGameButton(create_game_func)
        self.menu.addWidget(self.start_game_button)
