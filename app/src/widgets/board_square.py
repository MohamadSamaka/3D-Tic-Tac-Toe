from PyQt6.QtCore import Qt, QSize, QRect
from PyQt6.QtWidgets import QPushButton, QDialog
from PyQt6.QtGui import QPainter, QPen
from .messages import GameDialog, Warning
from ..helpers.shared import Shared
from math import floor 

class BoardSquare(QPushButton):
    def __init__(self, w, h, disable=False):
        super().__init__()
        self._width = w
        self._height = h
        if disable:
            self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.configure()
       
        
    def configure(self):
        self.FIXED_BUTTON_SPACE = 20
        self.drawing_margin = 20
        self.draw = False
        self.occupied_by = None
        button_width = floor(self._width / 3) - self.FIXED_BUTTON_SPACE
        button_height = floor(self._height / 3) - self.FIXED_BUTTON_SPACE
        self.setFixedSize(QSize(button_width, button_height))
        
        
    def paintEvent(self, event):
        super().paintEvent(event)
        if self.occupied_by is not None:
            if self.occupied_by:
                self.draw_x()
            else:
                self.draw_o()
    
    def mouseReleaseEvent(self, event):
        from ..layouts.boards_container import BoardsContainer
        
        super().mouseReleaseEvent(event)
        
        current_player = Shared.CURRENT_TURN
        active_board =  Shared.CURRENT_ACTIVE_BOARD
        
        if event.button() == Qt.MouseButton.LeftButton: #if left button is clicked
            if self.occupied_by is None and active_board: #check if square is occupied by a player and a board is already selected
                self.occupied_by = current_player
                parent_board_container = self.parent().board_container
                row, col = self.find_widget_position_in_grid(parent_board_container, self)[:2]
                btn = active_board.board_container.itemAtPosition(row, col).widget()
                btn.occupied_by = current_player
                Shared.SIMPLIFIED_BOARDS[active_board.id][row][col] = self.occupied_by
                Shared.CURRENT_MOVES += 1
                if BoardsContainer.check_draw():
                    self.new_game_or_exit("Game Over", "It's A Tie!")
                elif BoardsContainer.check_winner(): #if there is a winner reset board
                    Shared.PLAYERS_SCORE[current_player] += 1
                    Shared.GAME_CORE.top_menu.stop_timer()
                    Shared.GAME_CORE.top_menu.update_score()
                    winner_name = Shared.CURRENT_PLAYERS[current_player]
                    self.new_game_or_exit("Game Over", f"Winner is: {winner_name}")
                else: 
                    Shared.CURRENT_TURN = not Shared.CURRENT_TURN
                    Shared.GAME_CORE.top_menu.pass_turn()
                self.setDisabled(True)
                btn.update()
                
            else:
                Warning("Warning", "Please Select A Board First!").exec()
            self.update()
            
    def find_widget_position_in_grid(self, grid_layout, widget): #Find the position of a widget in the given grid layout.
        for i in range(grid_layout.count()):
            item = grid_layout.itemAt(i)
            if item.widget() == widget:
                position = grid_layout.getItemPosition(i)
                return position 
        return None 
        
    def draw_o(self):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.black, 10, Qt.PenStyle.SolidLine))
        rect = QRect(10, 10, self.width() - self.drawing_margin, self.height() - self.drawing_margin)
        painter.drawEllipse(rect)
        
    def draw_x(self):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.red, 10, Qt.PenStyle.SolidLine))
        painter.drawLine(self.drawing_margin, self.drawing_margin, self.width() - self.drawing_margin, self.height() - self.drawing_margin)
        painter.drawLine(self.width() - self.drawing_margin, self.drawing_margin, self.drawing_margin, self.height() - self.drawing_margin)
        
    def new_game_or_exit(self, title, message):
        if GameDialog(title, message).exec() == QDialog.DialogCode.Accepted: #new game
            Shared.reset_variables()
            Shared.BOARD_REFLECTION.parent().re_draw()
            Shared.GAME_CORE.boards_container.reset_boards()
            Shared.GAME_CORE.top_menu.new_timer()
            Shared.MAIN_APP_WINDOW.update()
        else: #exit
            Shared.MAIN_APP_WINDOW.exit_app()
            
    def clean_up(self):
        self.draw = False
        self.occupied_by = None
        self.setDisabled(False)