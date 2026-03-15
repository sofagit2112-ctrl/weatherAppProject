from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt
from datetime import datetime

class TimeInfo(QFrame):
    def __init__(self):
        QFrame.__init__(self)
        self.setFixedSize(390, 303)

        self.layout1 = QVBoxLayout()
        self.layout2 = QHBoxLayout()
        self.layout3 = QVBoxLayout()
        self.layout4 = QHBoxLayout()

        self.date = QLabel("Сьогодні")
        self.date.setFont(QFont("Arial", 15))
        self.date.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.date.setStyleSheet("background-color: transparent")
        self.date.setFixedSize(100, 50)
        self.date.setContentsMargins(15, 0, 0, 0)
        self.layout1.addWidget(self.date)
        
        days_ua = [
            "Понеділок", 
            "Вівторок", 
            "Середа", 
            "Четвер", 
            "П'ятниця", 
            "Субота", 
            "Неділя"
            ]
        now = datetime.now()
        today = days_ua[now.weekday()]
        
        self.day = QLabel(today)
        self.day.setFont(QFont("Arial", 20))
        self.day.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.day.setStyleSheet("background-color: transparent")
        self.day.setFixedHeight(50)
        self.day.setContentsMargins(15, 0, 0, 0)
        self.layout2.addWidget(self.day)
        
        self.date_now = datetime.now().strftime("%d.%m.%Y")
        
        self.date = QLabel(self.date_now)
        self.date.setFont(QFont("Arial", 20))
        self.date.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.date.setStyleSheet("background-color: transparent")
        self.date.setFixedHeight(50)
        self.date.setContentsMargins(0, 0, 15, 0)
        self.layout2.addWidget(self.date)
        
        self.time_image_label = QLabel()
        self.time_image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_image_label.setFixedSize(360, 190)
        self.time_image_label.setStyleSheet("background-color: transparent")
        self.time_image_label.setContentsMargins(0, 0, 0, 20)
        self.time_image_label.setLayout(self.layout4)
        self.layout3.addWidget(self.time_image_label)



        self.time_image = QPixmap("weatherapp/images/time.svg")
        self.time_image = self.time_image.scaled(170, 170)
        self.time_image_label.setPixmap(self.time_image)
        
        self.time_now = datetime.now().strftime("%H:%M")
        self.time = QLabel(self.time_now)
        self.time.setFont(QFont("Arial", 25))
        self.time.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time.setStyleSheet("background-color: transparent")
        self.time.setFixedSize(200, 150)
        self.layout4.addWidget(self.time)
        

        self.setLayout(self.layout1)
        self.layout1.addLayout(self.layout2)
        self.layout1.addLayout(self.layout3)
        self.layout1.addLayout(self.layout4)
        self.setStyleSheet("""
                    background-color: rgba(0, 0, 0, 0.2);
                    border-radius: 20px;
                    """)