from PyQt6.QtWidgets import QMainWindow, QFrame, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt 
from .main import MainInfo
from .side_panel import SidePanel
from .title_bar import TitleBar

class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setFixedSize(1200, 850)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        
        self.current_city = "Dnipro"

        self.central_widget = QFrame()
        self.central_widget.setStyleSheet("""
            background-color: qlineargradient(
                x1: 0, y1: 1, x2: 1, y2: 0,
                stop: 0 #8A2BE2, stop: 1 #191970
            )
        """)
        self.setCentralWidget(self.central_widget)
        
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.title_bar = TitleBar(self)
        self.main_layout.addWidget(self.title_bar)

        self.content_area = QFrame()
        self.content_layout = QHBoxLayout(self.content_area)
        self.content_layout.setContentsMargins(0, 0, 20, 0)
        self.content_layout.setSpacing(20)
        self.main_layout.addWidget(self.content_area)

        self.side_panel = SidePanel(city_name=self.current_city)
        self.side_panel.city_changed.connect(self.update_info)
        self.content_layout.addWidget(self.side_panel)

        self.main_view = MainInfo(city_name=self.current_city)
        self.content_layout.addWidget(self.main_view)

    def update_info(self, new_city):
        self.current_city = new_city
        
        if hasattr(self, 'main_view'):
            self.content_layout.removeWidget(self.main_view)
            self.main_view.deleteLater()
        
        self.main_view = MainInfo(city_name=self.current_city)
        self.content_layout.addWidget(self.main_view)

main_window = Window()
