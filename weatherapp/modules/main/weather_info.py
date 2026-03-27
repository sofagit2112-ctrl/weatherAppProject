from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from PyQt6.QtSvgWidgets import QSvgWidget
from ..utils import get_weather

class WeatherInfo(QFrame):
    def __init__(self, city_name="Dnipro"):
        super().__init__()
        self.setFixedSize(390, 303)
        

        self.layout1 = QVBoxLayout() 
        self.layout2 = QHBoxLayout()
        self.layout3 = QHBoxLayout() 
            
        data = get_weather(city_name)
        
        self.city_name_label = QLabel(city_name)
        self.city_name_label.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        self.city_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.city_name_label.setStyleSheet("background-color: transparent")
        self.city_name_label.setContentsMargins(0, 30, 0, 0)
        self.layout1.addWidget(self.city_name_label)

        self.icon = data.get("icon")
        self.svg_path = f"weatherapp/images/dark/{self.icon}.svg"
        
        self.weather_image = QSvgWidget()
        self.weather_image.load(self.svg_path)
        self.weather_image.setStyleSheet("background-color: transparent")
        self.weather_image.setFixedSize(120, 120)
        
        self.temp = QLabel(f"{data['temp']}°")
        self.temp.setFont(QFont("Arial", 60))  
        self.temp.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.temp.setStyleSheet("background-color: transparent")
        self.temp.setContentsMargins(0, 20, 40, 0)

        self.layout3.addWidget(self.weather_image)
        self.layout3.addWidget(self.temp)
        self.layout1.addLayout(self.layout3)

        self.description = QLabel(data['desc'])
        self.description.setFont(QFont("Arial", 14))
        self.description.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.description.setStyleSheet("background-color: transparent")
        self.description.setContentsMargins(0, 0, 0, 0)
        self.layout1.addWidget(self.description)

        self.temp_max = QLabel(f"Макс: {data['temp_max']}°")
        self.temp_max.setFont(QFont("Arial", 12))
        self.temp_max.setStyleSheet("background-color: transparent")
        self.temp_max.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.temp_min = QLabel(f"Мін: {data['temp_min']}°")
        self.temp_min.setFont(QFont("Arial", 12))
        self.temp_min.setStyleSheet("background-color: transparent")
        self.temp_min.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.layout2.addWidget(self.temp_max)
        self.layout2.addWidget(self.temp_min)
        self.layout1.addLayout(self.layout2)

        self.setLayout(self.layout1)
        self.setStyleSheet("""
            background-color: rgba(0, 0, 0, 0.2);
            border-radius: 20px;
        """)

        self.layout3.setAlignment(Qt.AlignmentFlag.AlignCenter)