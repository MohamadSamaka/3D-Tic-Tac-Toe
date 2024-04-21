from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QGridLayout, QGridLayout
from PyQt6.QtGui import  QPainter, QPainter, QColor
from ..defaults import WIDTH_PARTITIONING_PRECENT, HEIGHT_PARTITIONING_PRECENT
from ..defaults import GAME_TYPE
from ..helpers.shared import Shared
from .board_square import BoardSquare

            
class Board(QWidget):
    ID = 1
    FIXED_BUTTON_SPACE = 0
    
    def __init__(self, parent, w=WIDTH_PARTITIONING_PRECENT, h=HEIGHT_PARTITIONING_PRECENT, disable_squares=False):
        super().__init__(parent)
        self.disable_squares = disable_squares
        self.configure(w, h)
        self.generate_board()
        
        
    def configure(self, w, h):
        self.id = Board.ID
        self.setObjectName(f"{self.id}")
        Board.ID += 1
        self._width = w
        self._height = h
        self.board_container = QGridLayout(self)
        self.setFixedWidth(self._width)
        self.setFixedHeight(self._height)
        self.board_container.setSpacing(0)
        self.board_container.setContentsMargins(0,0,0,0)
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor('black'))  # Fill the widget rect with red
        
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton and self.id != Board.ID - 1:
            Shared.CURRENT_ACTIVE_BOARD = self
            self.reflect_simplified_board()
        
    def generate_board(self):
        for row in range(3):
            for col in range(3):
                btn = BoardSquare(self._width ,self._height, self.disable_squares)
                self.board_container.addWidget(btn, row, col)
                Shared.SIMPLIFIED_BOARDS[self.id] = [[-1, -1, -1] for _ in range(GAME_TYPE)]
                
    def reflect_simplified_board(self):
        simplified_clicked_board = Shared.SIMPLIFIED_BOARDS[self.id]
        for row in range(3):
            for col in range(3):
                square_state = simplified_clicked_board[row][col]
                square_to_redraw =  Shared.BOARD_REFLECTION.itemAtPosition(row, col).widget()
                if square_state == -1:
                    square_to_redraw.occupied_by = None
                    square_to_redraw.setDisabled(False)
                else:
                    square_to_redraw.occupied_by = square_state
                    square_to_redraw.setDisabled(True)
                square_to_redraw.update()
                
    def re_draw(self):
        for i in range(self.board_container.count()):
            item = self.board_container.itemAt(i)
            if item.widget():
                item.widget().clean_up()
                item.widget().update()
                
                
    def disable_board(self):
        for i in range(self.board_container.count()):
            item = self.board_container.itemAt(i)
            if item.widget():
                item.widget().setDisabled(True)
                