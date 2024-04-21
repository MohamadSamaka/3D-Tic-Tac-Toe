from PyQt6.QtCore import QPoint
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QVBoxLayout, QHBoxLayout
from ..layouts.boards_container import BoardsContainer
from ..layouts.active_board import ActiveBoard
from ..layouts.menu_bar import MenuBar
from ..helpers.shared import Shared
from math import floor

class GameCore(QWidget):
    def __init__(self, parent):
        super().__init__(parent)  # Initialize the QMainWindow base class
        self.resize_main_app_window()
        self.configure()
        
    def configure(self):
        self.setObjectName('game-core')
        self.game_wrapper = QVBoxLayout()
        
        self.set_menu_game_window()
        self.set_main_game_window()
        
        self.setLayout(self.game_wrapper)
        self.hide()
        
    def set_menu_game_window(self):
        self.top_menu_layout = QHBoxLayout()
        self.top_menu = MenuBar()
        self.top_menu_layout.addWidget(self.top_menu)
        self.game_wrapper.addLayout(self.top_menu_layout)
        
    def set_main_game_window(self):
        self.game_layout = QHBoxLayout()
        self.boards_container = BoardsContainer()
        self.active_board = ActiveBoard(self)
        
        self.game_layout.addWidget(self.boards_container)
        self.game_layout.addWidget( self.active_board)

        self.game_wrapper.addLayout(self.game_layout)
        
        self.setLayout(self.game_layout)

        
    def get_button_center(self, btn):
        pos = btn.pos()
        size = btn.size()
        center_x = floor(pos.x() + size.width() / 2)
        center_y = floor(pos.y() + size.height() / 2)
        return QPoint(center_x, center_y)
    
    def start_new_game(self):
        Shared.reset_variables()
        
    def resize_main_app_window(self):
        Shared.MAIN_APP_WINDOW.resize_to_default()