from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QScrollArea, QLabel, QWidget, QPushButton
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont
from .utils import get_weather
from datetime import datetime, timezone, timedelta

class SidePanel(QFrame):
    city_changed = pyqtSignal(str)

    def __init__(self, city_name="Dnipro"):
        QFrame.__init__(self)
        self.setFixedSize(370, 800)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0.1)")
        self.active_button = None
        self.current_city = city_name

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.scroll_element = QScrollArea()
        self.scroll_element.setWidgetResizable(True)
        self.scroll_element.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.main_layout.addWidget(self.scroll_element)

        self.content = QWidget()
        self.vertical_layout = QVBoxLayout(self.content)
        self.vertical_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.vertical_layout.setContentsMargins(20, 20, 20, 20)
        self.vertical_layout.setSpacing(15)

        city_list = ["Dnipro", "Paris", "Madrid", "Rome"]
        ua_names = {"Dnipro": "Дніпро", "Paris": "Париж", "Madrid": "Мадрид", "Rome": "Рим"}

        for city in city_list:
            weather_data = get_weather(city_name=city)
            frame = QPushButton()
            frame.setFixedSize(330, 115)
            
            card_layout = QHBoxLayout(frame)
            card_layout.setContentsMargins(15, 12, 15, 12)

            left_column = QVBoxLayout()
            city_label = QLabel(ua_names.get(city, city))
            city_label.setFont(QFont("Arial", 20))
            city_label.setStyleSheet("color: white; background: transparent;")

            tz = timezone(timedelta(seconds=weather_data['timezone']))
            local_time = datetime.now(tz).strftime("%H:%M")
            time_label = QLabel(local_time)
            time_label.setStyleSheet("background-color: transparent; color: white;")

            desc_label = QLabel(weather_data['desc'])
            desc_label.setStyleSheet("background-color: transparent; color: white;")

            left_column.addWidget(city_label)
            left_column.addWidget(time_label)
            left_column.addWidget(desc_label)

            right_column = QVBoxLayout()
            temp_label = QLabel(f"{weather_data['temp']}°")
            temp_label.setFont(QFont("Arial", 38))
            temp_label.setStyleSheet("background-color: transparent; border: none")
            temp_label.setAlignment(Qt.AlignmentFlag.AlignRight)

            min_max_text = f"Макс: {weather_data['temp_max']}° Мін: {weather_data['temp_min']}°"
            min_max_label = QLabel(min_max_text)
            min_max_label.setFont(QFont("Arial", 12))
            min_max_label.setStyleSheet("background-color: transparent")
            min_max_label.setContentsMargins(30, 0, 0, 0)
            min_max_label.setAlignment(Qt.AlignmentFlag.AlignBottom)

            right_column.addWidget(temp_label)
            right_column.addWidget(min_max_label)

            card_layout.addLayout(left_column)
            card_layout.addLayout(right_column)

            if city == self.current_city:
                self.active_button = frame
                frame.setStyleSheet("background-color: rgba(0, 0, 0, 0.3); border: none")
            else:
                frame.setStyleSheet("background-color: transparent; border: none;")

            frame.clicked.connect(lambda checked, c=city, b=frame: self.change_city(b, c))
            self.vertical_layout.addWidget(frame)

        self.scroll_element.setWidget(self.content)

    def change_city(self, clicked_button, city_name):
        if self.active_button:
            self.active_button.setStyleSheet("background-color: transparent; border: none;")
        
        clicked_button.setStyleSheet("background-color: rgba(0, 0, 0, 0.3); border: none")
        self.active_button = clicked_button
        
        self.city_changed.emit(city_name)