from random import randint
from pathlib import Path

class Shared:
    APP_ROOT_PATH = Path(__file__).resolve().parent.parent.parent
    SRC_ROOT_PATH = APP_ROOT_PATH / "src"
    STYLES_PATH = SRC_ROOT_PATH / "styles"
    MAIN_MENU = None
    GAME_CORE = None
    CURRENT_PLAYERS = []
    PLAYERS_SCORE = [0, 0]
    CURRENT_TURN = bool(randint(0, 1))
    CURRENT_ACTIVE_BOARD = None
    BOARD_REFLECTION = None
    SIMPLIFIED_BOARDS = {}
    CURRENT_MOVES = 0
    
    def reset_variables():
        Shared.CURRENT_TURN = bool(randint(0, 1))
        Shared.CURRENT_ACTIVE_BOARD = None
        Shared.CURRENT_MOVES = 0
