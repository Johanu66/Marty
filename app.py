import sys
from martypy import Marty
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QLabel, QGridLayout, QSlider

def create_custom_button(image, text):
    button = QPushButton()
    button.setFixedSize(QSize(150, 150))
    button_layout = QVBoxLayout()
    
    button_icon = QLabel()
    button_icon.setPixmap(QPixmap('./img/'+ image +'_btn.png'))
    button_icon.setScaledContents(True)
    
    button_layout.addWidget(button_icon, alignment=Qt.AlignmentFlag.AlignCenter)
    button_layout.addWidget(QLabel(text), alignment=Qt.AlignmentFlag.AlignCenter)
    button.setLayout(button_layout)

    button.clicked.connect(lambda: handle_button_click(image))
    
    return button

def direction_button(image):
    button = QPushButton()
    button.setFixedSize(QSize(80, 80))
    button.setIcon(QIcon('./img/'+ image +'_button.png'))
    button.setIconSize(QSize(60,60))
    button.clicked.connect(lambda: handle_button_click(image))

    return button

def handle_button_click(type):
    match type:
        case 'left_top':
            marty.left_top()
        case 'top':
            marty.top()
        case 'right_top':
            marty.right_top()
        case 'left':
            marty.left()
        case 'center':
            marty.center()
        case 'right':
            marty.right()
        case 'down':
            marty.down()
        case 'get_ready':
            marty.get_ready()
        case 'show_off':
            marty.show_off()
        case 'wave_left':
            marty.wave_left()
        case 'wave_right':
            marty.wave_right()
        case 'dance':
            marty.dance()
        case 'wiggle_eyes':
            marty.wiggle_eyes()
        case 'kick_left':
            marty.kick_left()
        case 'kick_right':
            marty.kick_right()
        case _:
            print('Unknown action')



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Marty's App")

        left_top_button = direction_button('left_top')
        top_button = direction_button('top')
        right_top_button = direction_button('right_top')
        left_button = direction_button('left')
        center_button = direction_button('center')
        right_button = direction_button('right')
        down_button = direction_button('down')

        get_ready_btn = create_custom_button('get_ready', 'Get Ready')
        show_off_btn = create_custom_button('show_off', 'Show Off')
        wave_left_btn = create_custom_button('wave_left', 'Wave Left')
        wave_right_btn = create_custom_button('wave_right', 'Wave Right')
        dance_btn = create_custom_button('dance', 'Dance!')
        wiggle_eyes_btn = create_custom_button('wiggle_eyes', 'Wiggle Eyes')
        kick_left_btn = create_custom_button('kick_left', 'Kick Left')
        kick_right_btn = create_custom_button('kick_right', 'Kick Right')

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
        self.label = QLabel('Speed: 0', self)
        
        # Create a QSlider
        self.slider = QSlider(Qt.Orientation.Horizontal, self)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(0)
        
        # Connect the slider value change to the function
        self.slider.valueChanged.connect(self.updateSpeed)

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

    def updateSpeed(self, value):
        self.label.setText(f'Speed: {value}')
        marty.set_speed(value)

app = QApplication(sys.argv)

window = MainWindow()

#marty = Marty('wifi', '192.168.0.107')

window.show()

# Styling
app.setStyleSheet("MainWindow { background-color: rgba(212, 237, 244, 0.8) }")

app.exec()
