from PyQt6.QtWidgets import QWidget, QVBoxLayout
from ..defaults import WINDOW_HEIGHT, WINDOW_WIDTH, WIDTH_PARTITIONING_PRECENT, HEIGHT_PARTITIONING_PRECENT, SKY_BLUE_BACKGROUND
from ..widgets.board import Board
from ..helpers.shared import Shared

class ActiveBoard(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure()
        
    def configure(self):
        self.boards_layout = QVBoxLayout()
        self.board = Board(self, WINDOW_WIDTH - WIDTH_PARTITIONING_PRECENT- self.width() , WINDOW_HEIGHT - HEIGHT_PARTITIONING_PRECENT)
        self.setLayout(self.boards_layout)
        self.boards_layout.addWidget(self.board)
        Shared.BOARD_REFLECTION = self.board.board_container
        self.setStyleSheet(SKY_BLUE_BACKGROUND)
        
    
        