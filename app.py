import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QLabel, QGridLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Marty's App")

        left_top_button = QPushButton("Press")
        left_top_button.setFixedSize(QSize(80, 80))
        top_button = QPushButton("Press")
        top_button.setFixedSize(QSize(80, 80))
        right_top_button = QPushButton("Press")
        right_top_button.setFixedSize(QSize(80, 80))
        left_button = QPushButton("Press")
        left_button.setFixedSize(QSize(80, 80))
        center_button = QPushButton("Press")
        center_button.setFixedSize(QSize(80, 80))
        right_button = QPushButton("Press")
        right_button.setFixedSize(QSize(80, 80))
        down_button = QPushButton("Press")
        down_button.setFixedSize(QSize(80, 80))

        get_ready_btn = QPushButton("Get Ready")
        get_ready_btn.setFixedSize(QSize(150, 150))
        #get_ready_btn.clicked.connect(self.handleButton)
        get_ready_btn.setIcon(QIcon('./img/get_ready_btn.png'))
        get_ready_btn.setIconSize(QSize(100,100))
        show_off_btn = QPushButton("Show Off")
        show_off_btn.setFixedSize(QSize(150, 150))
        wave_left_btn = QPushButton("Wave Left")
        wave_left_btn.setFixedSize(QSize(150, 150))
        wave_right_btn = QPushButton("Wave Right")
        wave_right_btn.setFixedSize(QSize(150, 150))
        dance_btn = QPushButton("Dance!")
        dance_btn.setFixedSize(QSize(150, 150))
        wiggle_eyes_btn = QPushButton("Wiggle Eyes")
        wiggle_eyes_btn.setFixedSize(QSize(150, 150))
        kick_left_btn = QPushButton("Kick Left")
        kick_left_btn.setFixedSize(QSize(150, 150))
        kick_right_btn = QPushButton("Kick Right")
        kick_right_btn.setFixedSize(QSize(150, 150))

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

        right_layout.addWidget(QLabel("Nav Bar"))
        right_layout.addWidget(actions_btn_container)

        main_layout.addWidget(left_container)
        main_layout.addWidget(right_container)

        # Styling
        left_container.setStyleSheet("QPushButton { background-color: #3EC8ED }")
        right_container.setStyleSheet("QPushButton { "+
            "background-color: #9BD0DE;"+
            "color: #77A1B2;"+
            "border: 2px solid #3EC8ED;"+
            "border-radius: 20px;"
        "}")

        self.setCentralWidget(main_container)

app = QApplication(sys.argv)

window = MainWindow()
window.show()


# Styling
app.setStyleSheet("QWidget { background-color: rgba(212, 237, 244, 0.6) }")



app.exec()
