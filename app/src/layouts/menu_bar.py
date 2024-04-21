from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from ..widgets.timer import TimerLabel
from ..helpers.shared import Shared


class MenuBar(QWidget):
    def __init__(self):
        super().__init__()
        self.configure()
    
    def configure(self):
        self.menubar_holder = QVBoxLayout()
        self.menubar_holder.setSpacing(0)
        self.menubar_holder.setContentsMargins(0,0,0,0)
        self.current_player_label = QLabel(f"current player: {Shared.CURRENT_PLAYERS[Shared.CURRENT_TURN]}")
        self.timer = TimerLabel(self, self.pass_turn)
 
        self.setFixedHeight(50)
        self.menubar_holder.addWidget(self.current_player_label)
        self.menubar_holder.addWidget(self.timer)
        self.setLayout(self.menubar_holder)
        self.current_player_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    
        self.timer.set_timer()
        
    def pass_turn(self):
        self.timer.reset()
        current_player = f"current player: {Shared.CURRENT_PLAYERS[Shared.CURRENT_TURN]}"
        self.current_player_label.setText(current_player)
        
    def stop_timer(self):
        self.timer.timer.stop()
        
    def new_timer(self):
        self.timer.reset_timer()
    