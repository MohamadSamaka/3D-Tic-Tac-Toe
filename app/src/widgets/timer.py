from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QColor
from ..defaults import TIMER
from ..helpers.shared import Shared


class TimerLabel(QLabel):
    def __init__(self, parent, pass_turn_func):
        super().__init__(parent)
        self.configure()
        self.pass_turn_func = pass_turn_func
        
    def configure(self):
        self.setFixedHeight(5)
        self.update_progress_bar_color()

    def set_timer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.duration = TIMER # Duration of the countdown in seconds
        self.elapsed_time = 0
        self.timer.start(1000)  # Timer updates every second
        
    def reset_timer(self):
        self.timer.stop()
        self.reset()
        self.update_progress_bar_color()
        self.timer.start(1000)
        
    def reset(self):
        self.elapsed_time = 0
        self.update_progress_bar_color()
        parent_width = self.parent().width()
        self.setFixedWidth(int(parent_width))
    
    
    def update_progress(self):
        if self.elapsed_time < self.duration:
            self.elapsed_time += 1
            percent = (self.duration - self.elapsed_time) / self.duration * 100
            self.set_progress(percent)
        else:
            Shared.CURRENT_TURN = not Shared.CURRENT_TURN
            self.pass_turn_func()
            # self.timer.stop()
            
    def update_progress_bar_color(self, percent=100):
        palette = self.palette()
        role = self.backgroundRole()
        if percent > 60:
            palette.setColor(role, QColor('green'))
        if percent <= 60:
            palette.setColor(role, QColor('yellow'))
        if percent <= 30:
            palette.setColor(role, QColor('red'))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

    def set_progress(self, percent):
        parent_width = self.parent().width()
        new_width = parent_width * (percent / 100)
        self.update_progress_bar_color(percent)
        self.setFixedWidth(int(new_width))