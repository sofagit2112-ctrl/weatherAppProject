from PyQt6.QtWidgets import QFrame, QScrollArea, QHBoxLayout, QVBoxLayout, QLabel
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt
from ..utils import get_forecast, get_weather
from datetime import datetime, timezone, timedelta
from PyQt6.QtSvgWidgets import QSvgWidget

class ForecastInfo(QFrame):
    def __init__(self):
        QFrame.__init__(self)
        self.vertical_layout = QVBoxLayout()
        self.setLayout(self.vertical_layout)
        self.setFixedSize(790, 157)
        self.setStyleSheet("""
                    background-color: rgba(0, 0, 0, 0.2);
                    border-radius: 20px;
                           """)
        self.horizontal_layout = QHBoxLayout()
        self.vertical_layout.addLayout(self.horizontal_layout)
        
        self.forecast_layout = QHBoxLayout()

        self.text = QLabel("Хмарна погода до кінця дня")
        self.text.setFont(QFont("Arial", 12))
        self.text.setStyleSheet("background-color: transparent")
        self.text.setFixedSize(225, 20)
        self.vertical_layout.addWidget(self.text)

        self.scroll_frame = QFrame()
        self.scroll_element = QScrollArea(self)
        self.scroll_element.setWidgetResizable(True)
        self.vertical_layout.addWidget(self.scroll_element)
        self.scroll_element.setFixedSize(790, 110)
        self.scroll_element.setStyleSheet("""
                                    background-color: transparent;
                                    border: none;
                                    """)
        self.scroll_element.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_frame.setLayout(self.forecast_layout)

        forecast_data = get_forecast(48.45, 34.9833)

        for i in forecast_data['list'][:20]:
            weather_data = get_weather("Dnipro")

            frame = QFrame()
            frame.setFixedSize(80, 90)
            frame.setStyleSheet("""
                        background-color: transparent;
                        border-radius: 0px;
                        """)
            self.layout1 = QVBoxLayout()
            frame.setLayout(self.layout1)
            self.forecast_layout.addWidget(frame)
            self.forecast_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

            tz = timezone(timedelta(seconds=weather_data['timezone']))
            forecast_time = datetime.fromtimestamp(i['dt'], tz)
            display_time = forecast_time.strftime("%H")
        
            self.hour = QLabel(display_time)
            self.hour.setFont(QFont("Arial", 11))
            self.hour = QLabel("17")
            self.hour.setFont(QFont("Arial", 12))
            self.hour.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.hour.setStyleSheet("background-color: transparent")
            self.hour.setFixedSize(60, 20)
            self.layout1.addWidget(self.hour)

            icon_code = i["weather"][0]["icon"]
            svg_path = f"weatherapp/images/dark/{icon_code}.svg"
            
            icon_svg = QSvgWidget()
            icon_svg.load(svg_path)
            icon_svg.setFixedSize(30, 30)
            icon_svg.setContentsMargins(0, 0, 0, 30)
            self.layout1.addWidget(icon_svg, alignment=Qt.AlignmentFlag.AlignCenter)

            self.temp_value = round(i['main']['temp'])
            self.temp = QLabel(f"{self.temp_value}°")
            self.temp.setFont(QFont("Arial", 12))
            self.temp.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.temp.setStyleSheet("background-color: transparent")
            self.temp.setFixedSize(60, 30)
            self.layout1.addWidget(self.temp)

        self.scroll_element.setWidget(self.scroll_frame)