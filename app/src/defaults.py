import os
from dotenv import load_dotenv
from .helpers.helpers import get_style
from .helpers.shared import Shared

load_dotenv(r"D:\MyCodes\AWS projects\Tic-Tac-Toe\.env")  # Specify the exact path if not in the same directory

try:
    WINDOW_WIDTH = int(os.getenv('WINDOW_WIDTH', '1200'))
    WINDOW_HEIGHT = int(os.getenv('WINDOW_HEIGHT', '900'))
    # WINDOW_WIDTH = 1200
    # WINDOW_HEIGHT = 1200
    WIDTH_PARTITIONING_PRECENT= WINDOW_WIDTH * int(os.getenv('WIDTH_PARTITIONING_PRECENT', 20)) // 100
    HEIGHT_PARTITIONING_PRECENT = WINDOW_HEIGHT * int(os.getenv('HEIGHT_PARTITIONING_PRECENT', 20)) // 100
    TIMER = int(os.getenv('TIMER', 30))
    GAME_TYPE = int(os.getenv('GAME_TYPE', 3))
    BUTTON_STYLING =  get_style("BUTTON_STYLE_FILE")
    WARNING_FONT = get_style("WARNING_FONT")
    
except:
    print(Shared.APP_ROOT_PATH)
    print("[-] problem loading the env variables.")
    exit(1)