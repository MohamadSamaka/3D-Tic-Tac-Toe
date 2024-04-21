from PyQt6.QtWidgets import QPushButton
from ..widgets.player_name_input import Player_Input
from ..helpers.shared import Shared


class StartGameButton(QPushButton):
    def __init__(self, create_game_func):
        super().__init__()
        self.configure()
        self.create_game_func = create_game_func
    
    def configure(self):
        self.setText("Start")
        self.setFixedWidth(200)  # Set a fixed height for each line edit
        self.clicked.connect(self.start_game)
        
    def start_game(self):
        self.set_player_name()
        game_core = self.create_game_func()
        game_core.show()
        main_game_window = self.parentWidget()
        main_game_window.hide()
        main_game_window.parentWidget().setCentralWidget(game_core)
        
        Shared.GAME_CORE = game_core
        
    def set_player_name(self):
        current_parent_children = self.parent()
        input_names = current_parent_children.findChildren(Player_Input)
        for name in input_names:
            Shared.CURRENT_PLAYERS.append(name.text())
                