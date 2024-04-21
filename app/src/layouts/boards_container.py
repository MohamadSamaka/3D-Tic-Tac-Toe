from PyQt6.QtWidgets import QWidget, QVBoxLayout
from ..defaults import GAME_TYPE
from ..helpers.shared import Shared
from ..widgets.board import Board


class BoardsContainer(QWidget):
    def __init__(self):
        super().__init__()
        self.configure()
        self.assign_layouts()
        
        
    def configure(self):
        self.boards_layout = QVBoxLayout()
        self.view_boards = [Board(self, disable_squares = True) for _ in range(GAME_TYPE)]
        self.setLayout(self.boards_layout)
        
    def assign_layouts(self):
        for board in self.view_boards:
            self.boards_layout.addWidget(board)
            
    def reset_boards(self):
        for board_id in list(Shared.SIMPLIFIED_BOARDS.keys()):
            Shared.SIMPLIFIED_BOARDS[board_id] = [[-1] * GAME_TYPE for _ in range(GAME_TYPE)]
        for board in self.view_boards:
            board.re_draw()
            
    def check_winner():
        board = list(Shared.SIMPLIFIED_BOARDS.values())[:-1]
        player = Shared.CURRENT_TURN
        n = len(board)
        
        # Check layers (2D wins)
        for layer in range(n):
            # Check rows and columns in each layer
            for i in range(n):
                if all(board[layer][i][j] == player for j in range(n)):  # Check row
                    return True
                if all(board[layer][j][i] == player for j in range(n)):  # Check column
                    return True
            
            # Check diagonals in each layer
            if all(board[layer][i][i] == player for i in range(n)):
                return True
            if all(board[layer][i][n-1-i] == player for i in range(n)):
                return True
        
        # Check verticals across layers
        for i in range(n):
            for j in range(n):
                if all(board[layer][i][j] == player for layer in range(n)):
                    return True

        # Check cross-layer diagonals
        if all(board[i][i][i] == player for i in range(n)):
            return True
        if all(board[i][i][n-1-i] == player for i in range(n)):
            return True
        if all(board[i][n-1-i][i] == player for i in range(n)):
            return True
        if all(board[n-1-i][i][i] == player for i in range(n)):
            return True

        return False
    
    def check_draw():
        maxmimum_moves = GAME_TYPE ** 3
        return maxmimum_moves == Shared.CURRENT_MOVES

        