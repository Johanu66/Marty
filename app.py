import sys

from martypy import Marty

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QLabel, QGridLayout, QSlider

def create_custom_button(image_path, text):
    button = QPushButton()
    button.setFixedSize(QSize(150, 150))
    button_layout = QVBoxLayout()
    
    button_icon = QLabel()
    button_icon.setPixmap(QPixmap(image_path))
    button_icon.setScaledContents(True)
    
    button_layout.addWidget(button_icon, alignment=Qt.AlignmentFlag.AlignCenter)
    button_layout.addWidget(QLabel(text), alignment=Qt.AlignmentFlag.AlignCenter)
    
    button.setLayout(button_layout)
    
    return button

def direction_button(image_path):
    button = QPushButton()
    button.setFixedSize(QSize(80, 80))
    button.setIcon(QIcon(image_path))
    button.setIconSize(QSize(60,60))

    return button


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Marty's App")

        left_top_button = direction_button('./img/left_top_button.png')
        top_button = direction_button('./img/top_button.png')
        right_top_button = direction_button('./img/right_top_button.png')
        left_button = direction_button('./img/left_button.png')
        center_button = direction_button('./img/center_button.png')
        right_button = direction_button('./img/right_button.png')
        down_button = direction_button('./img/down_button.png')

        get_ready_btn = create_custom_button('./img/get_ready_btn.png', 'Get Ready')
        show_off_btn = create_custom_button('./img/show_off_btn.png', 'Show Off')
        wave_left_btn = create_custom_button('./img/wave_left_btn.png', 'Wave Left')
        wave_right_btn = create_custom_button('./img/wave_right_btn.png', 'Wave Right')
        dance_btn = create_custom_button('./img/dance_btn.png', 'Dance!')
        wiggle_eyes_btn = create_custom_button('./img/wiggle_eyes_btn.png', 'Wiggle Eyes')
        kick_left_btn = create_custom_button('./img/kick_left_btn.png', 'Kick Left')
        kick_right_btn = create_custom_button('./img/kick_right_btn.png', 'Kick Right')

        main_layout = QHBoxLayout()
        main_container = QWidget()
        main_container.setLayout(main_layout)

        left_layout = QGridLayout()
        left_container = QWidget()
        left_container.setLayout(left_layout)

        left_layout.addWidget(left_top_button, 0, 0)
        left_layout.addWidget(top_button, 0, 1)
        left_layout.addWidget(right_top_button, 0, 2)
        left_layout.addWidget(left_button, 1, 0)
        left_layout.addWidget(center_button, 1, 1)
        left_layout.addWidget(right_button, 1, 2)
        left_layout.addWidget(down_button, 2, 1)

        actions_btn_layout = QGridLayout()
        actions_btn_container = QWidget()
        actions_btn_container.setLayout(actions_btn_layout)

        actions_btn_layout.addWidget(get_ready_btn, 0, 0)
        actions_btn_layout.addWidget(show_off_btn, 0, 1)
        actions_btn_layout.addWidget(wave_left_btn, 0, 2)
        actions_btn_layout.addWidget(wave_right_btn, 0, 3)
        actions_btn_layout.addWidget(dance_btn, 1, 0)
        actions_btn_layout.addWidget(wiggle_eyes_btn, 1, 1)
        actions_btn_layout.addWidget(kick_left_btn, 1, 2)
        actions_btn_layout.addWidget(kick_right_btn, 1, 3)

        right_layout = QVBoxLayout()
        right_container = QWidget()
        right_container.setLayout(right_layout)

        # Create a QLabel
        self.label = QLabel('Value: 0', self)
        
        # Create a QSlider
        self.slider = QSlider(Qt.Orientation.Horizontal, self)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(0)
        
        # Connect the slider value change to the function
        self.slider.valueChanged.connect(self.updateLabel)

        right_layout.addWidget(self.label)
        right_layout.addWidget(self.slider)
        right_layout.addWidget(actions_btn_container)

        main_layout.addWidget(left_container)
        main_layout.addWidget(right_container)

        self.setCentralWidget(main_container)

        # Styling
        left_container.setStyleSheet("QPushButton { background-color: #3EC8ED }")
        right_container.setStyleSheet("QPushButton { "+
            "background-color: #9BD0DE;"+
            "color: #77A1B2;"+
            "border: 2px solid #3EC8ED;"+
            "border-radius: 20px;"
        "} QLabel { "+
            "color: #77A1B2;"+
        "}")

    def updateLabel(self, value):
        self.label.setText(f'Value: {value}')

app = QApplication(sys.argv)

window = MainWindow()
window.show()


# Styling
app.setStyleSheet("MainWindow { background-color: rgba(212, 237, 244, 0.8) }")



app.exec()
