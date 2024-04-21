from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from ..widgets.timer import TimerLabel
from ..helpers.shared import Shared


class MenuBar(QWidget):
    def __init__(self):
        super().__init__()
        self.configure()
    
    def configure(self):
        self.setFixedHeight(50)
        
        self.create_menubar_holder()
        self.create_current_turn_label()
        self.create_score_label()
        self.create_timer()
        
        self.timer.set_timer()
    
        
    def create_timer(self):
        self.timer = TimerLabel(self, self.pass_turn)
        self.menubar_holder.addWidget(self.timer)
        
    def create_menubar_holder(self):
        self.menubar_holder = QVBoxLayout()
        self.menubar_holder.setSpacing(0)
        self.menubar_holder.setContentsMargins(0,0,0,0)
        self.setLayout(self.menubar_holder)
        
    def create_current_turn_label(self):
        self.current_player_label = QLabel(f"current player: {Shared.CURRENT_PLAYERS[Shared.CURRENT_TURN]}")
        self.menubar_holder.addWidget(self.current_player_label)
        self.current_player_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
    def create_score_label(self):
        self.score_label = QLabel(f"{Shared.CURRENT_PLAYERS[0]}\t\t0:0\t\t{Shared.CURRENT_PLAYERS[1]}")
        self.menubar_holder.addWidget(self.score_label)
        self.score_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
    def pass_turn(self):
        self.timer.reset()
        current_player = f"current player: {Shared.CURRENT_PLAYERS[Shared.CURRENT_TURN]}"
        self.current_player_label.setText(current_player)
        
    def update_score(self):
        self.score_label.setText(f"{Shared.CURRENT_PLAYERS[0]}\t{Shared.PLAYERS_SCORE[0]}:{Shared.PLAYERS_SCORE[1]}\t{Shared.CURRENT_PLAYERS[1]}")
        
    def stop_timer(self):
        self.timer.timer.stop()
        
    def new_timer(self):
        self.timer.reset_timer()
    