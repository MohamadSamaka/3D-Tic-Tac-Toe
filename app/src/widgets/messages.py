from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from ..defaults import WARNING_FONT

class Warning(QDialog):
    def __init__(self, title, message):
        super().__init__()
        self.configure(title, message)

    def configure(self, title, message):
        self.setWindowTitle(title)
        self.setFixedSize(300, 100)  # Set the fixed size of the dialog
        layout = QHBoxLayout()
        
        label = QLabel(message)
        layout.addWidget(label)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet(WARNING_FONT)
        label.font()

        self.setLayout(layout)
        
        
class GameDialog(QDialog):
    def __init__(self, title, state):
        super().__init__()
        self.configure(title, state)

    def configure(self, title, state):
        self.setWindowTitle(title)
        # self.setGeometry(300, 300, 200, 100)
        self.setFixedSize(300, 100)  # Set the fixed size of the dialog
        layout = QVBoxLayout()

        # Winner Label
        winner_label = QLabel(state, self)
        layout.addWidget(winner_label)

        # New Game Button
        self.new_game_button = QPushButton("New Game", self)
        self.new_game_button.clicked.connect(self.on_new_game)
        layout.addWidget(self.new_game_button)

        # Exit Button
        self.exit_button = QPushButton("Exit", self)
        self.exit_button.clicked.connect(self.on_exit)
        layout.addWidget(self.exit_button)

        self.setLayout(layout)

    def on_new_game(self):
        self.accept()  # Close the dialog with accept status

    def on_exit(self):
        self.reject()  # Close the dialog with reject status