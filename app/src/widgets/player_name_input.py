from PyQt6.QtWidgets import QLineEdit


class Player_Input(QLineEdit):
    def __init__(self, place_holder):
        super().__init__()
        self.configure(place_holder)
    
    def configure(self, place_holder):
        self.setPlaceholderText(place_holder)
        self.setFixedWidth(200)  # Set a fixed height for each line edit