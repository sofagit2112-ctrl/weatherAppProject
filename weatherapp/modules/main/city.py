from PyQt6.QtWidgets import QFrame, QVBoxLayout, QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from modules.side_panel import SidePanel

class City(QFrame):
    def __init__(self, city_name, temp, description, temp_max, temp_min, time):
        self.layout = QVBoxLayout()
        
        self.city_name = city_name
        self.temp = temp
        self.description = description
        self.temp_max = temp_max
        self.temp_min = temp_min
        self.time = time

        self.setStyleSheet("background-color: transparent")

        self.name_label = QLabel(self.city_name)
        self.name_label.setFont(QFont("Arial", 20))

        self.temp_label = QLabel(f"{self.temp}°C")
        self.temp_label.setFont(QFont("Arial", 40))

        self.description_label = QLabel(self.description)
        self.description_label.setFont(QFont("Arial", 14))
        
        self.temp_max_label = QLabel(f"Max: {self.temp_max}°C")
        self.temp_max_label.setFont(QFont("Arial", 12))

        self.temp_min_label = QLabel(f"Min: {self.temp_min}°C")
        self.temp_min_label.setFont(QFont("Arial", 12))

        self.time_label = QLabel(self.time)
        self.time_label.setFont(QFont("Arial", 12))

        self.city_name.setAlignment(Qt.AlignmentFlag.AlignLeft)

