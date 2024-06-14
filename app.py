import sys
from martypy import Marty
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QLabel, QGridLayout, QSlider
from ColorCalibrator import ColorCalibrator
from connection_to_marty import MartyController

main_marty_calib = True

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        QPushButton.__init__(self, *args, **kwargs)
        self.setAutoRepeat(True)
        self.setAutoRepeatDelay(1000)
        self.setAutoRepeatInterval(1000)
        self.clicked.connect(self.handleClicked)
        self._state = 0
        self.type = ""

    def setType(self, type):
        self.type = type

    def handleClicked(self):
        if self.isDown():
            if self._state == 0:
                self._state = 1
                # float to int
                self.setAutoRepeatInterval(int(marty.get_speed() + marty.get_speed()*1/4))
                handle_button_click(self.type)
            else:
                handle_button_click(self.type)
        elif self._state == 1:
            self._state = 0
            self.setAutoRepeatInterval(int(marty.get_speed() + marty.get_speed()*1/4))
        else:
            handle_button_click(self.type)

def handle_button_click(type):
    global main_marty_calib
    window.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
    window.setFocus()
    intervalle = 3
    match type:
        case 'left_top':
            marty.turn_left()
        case 'top':
            marty.forward()
        case 'right_top':
            marty.turn_right()
        case 'left':
            marty.left_side_step()
        case 'right':
            marty.right_side_step()
        case 'down':
            marty.backward()
        case 'get_ready':
            marty.get_ready()
        case 'show_off':
            marty.celebrate()
        case 'wave_left':
            marty.lift_left_arm()
        case 'wave_right':
            marty.lift_right_arm()
        case 'dance':
            marty.dance()
        case 'wiggle_eyes':
            marty.wiggle_eyes()
        case 'kick_left':
            marty.left_kick()
        case 'kick_right':
            marty.right_kick()
        case 'connect':
            if main_marty_calib:
                if marty.marty is None:
                    marty.connect()
                    if marty.marty is not None:
                        marty.get_ready()
            else:
                if marty2.marty is None:
                    marty2.connect()
                    if marty2.marty is not None:
                        marty2.get_ready()
        case 'down_left':
            marty.reconnaissance()
            marty2.reconnaissance()
        case 'down_right':
            marty.auto_guide()
        case 'marty1_calib':
            main_marty_calib = True
            print("Current marty is Marty1")
        case 'marty2_calib':
            main_marty_calib = False
            print("Current marty is Marty2")
        case 'red':
            # color = marty.get_color_number()
            # marty.set_red_values((color-intervalle, color+intervalle))
            if main_marty_calib:
                color = marty.marty.get_color_sensor_hex('left')
            else:
                color = marty2.marty.get_color_sensor_hex('left')
            ColorCalibrator.calibrate_color(1, 'red', color)
        case 'pink':
            # color = marty.get_color_number()
            # marty.set_pink_values((color-intervalle, color+intervalle))
            if main_marty_calib:
                color = marty.marty.get_color_sensor_hex('left')
            else:
                color = marty2.marty.get_color_sensor_hex('left')
            ColorCalibrator.calibrate_color(1, 'pink', color)
        case 'yellow':
            # color = marty.get_color_number()
            # marty.set_yellow_values((color-intervalle, color+intervalle))
            if main_marty_calib:
                color = marty.marty.get_color_sensor_hex('left')
            else:
                color = marty2.marty.get_color_sensor_hex('left')
            ColorCalibrator.calibrate_color(1, 'yellow', color)
        case 'green':
            # color = marty.get_color_number()
            # marty.set_green_values((color-intervalle, color+intervalle))
            if main_marty_calib:
                color = marty.marty.get_color_sensor_hex('left')
            else:
                color = marty2.marty.get_color_sensor_hex('left')
            ColorCalibrator.calibrate_color(1, 'green', color)
        case 'light_blue':
            # color = marty.get_color_number()
            # marty.set_light_blue_values((color-intervalle, color+intervalle))
            if main_marty_calib:
                color = marty.marty.get_color_sensor_hex('left')
            else:
                color = marty2.marty.get_color_sensor_hex('left')
            ColorCalibrator.calibrate_color(1, 'light_blue', color)
        case 'dark_blue':
            # color = marty.get_color_number()
            # marty.set_dark_blue_values((color-intervalle, color+intervalle))
            if main_marty_calib:
                color = marty.marty.get_color_sensor_hex('left')
            else:
                color = marty2.marty.get_color_sensor_hex('left')
            ColorCalibrator.calibrate_color(1, 'dark_blue', color)
        case 'black':
            # color = marty.get_color_number()
            # marty.set_black_values((color-intervalle, color+intervalle))
            if main_marty_calib:
                color = marty.marty.get_color_sensor_hex('left')
            else:
                color = marty2.marty.get_color_sensor_hex('left')
            ColorCalibrator.calibrate_color(1, 'black', color)
        case _:
            print('Unknown action')

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

def direction_button(image, text=""):
    button = Button(text)
    button.setFixedSize(QSize(80, 80))
    button.setIcon(QIcon('./img/'+ image +'_button.png'))
    button.setIconSize(QSize(60,60))
    button.setType(image)
    return button

def color_button(type, color, text=""):
    button = Button(text)
    button.setStyleSheet("QPushButton { background-color: "+ color +"; text-align: center; }")
    button.setFixedSize(QSize(40, 40))
    # button.setIcon(QIcon('./img/'+ image +'_button.png'))
    # button.setIconSize(QSize(60,60))
    button.setType(type)
    return button

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Marty's App")
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setFocus()

        # black, red, pink, yellow, green, light_blue and dark_blue button
        red_button = color_button("red", "red")
        pink_button = color_button("pink", "pink")
        yellow_button = color_button("yellow", "yellow")
        green_button = color_button("green", "green")
        black_button = color_button("black", "black")
        light_blue_button = color_button("light_blue", "#87CEEB")
        dark_blue_button = color_button("dark_blue", "#00008B")

        marty1_calib_button = color_button("marty1_calib", "#3EC8ED", "M1")
        marty2_calib_button = color_button("marty2_calib", "#3EC8ED", "M2")

        left_top_button = direction_button('left_top')
        top_button = direction_button('top')
        right_top_button = direction_button('right_top')
        left_button = direction_button('left')
        connect_button = direction_button('connect')
        right_button = direction_button('right')
        down_button = direction_button('down')
        down_left_button = direction_button('down_left', "Reconnais")
        down_right_button = direction_button('down_right', "Auto guid")

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
        left_layout.addWidget(connect_button, 1, 1)
        left_layout.addWidget(right_button, 1, 2)
        left_layout.addWidget(down_left_button, 2, 0)
        left_layout.addWidget(down_button, 2, 1)
        left_layout.addWidget(down_right_button, 2, 2)

        left_layout.addWidget(red_button, 3, 0, alignment=Qt.AlignmentFlag.AlignCenter)
        left_layout.addWidget(pink_button, 3, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        left_layout.addWidget(yellow_button, 3, 2, alignment=Qt.AlignmentFlag.AlignCenter)
        left_layout.addWidget(green_button, 4, 0, alignment=Qt.AlignmentFlag.AlignCenter)
        left_layout.addWidget(light_blue_button, 4, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        left_layout.addWidget(dark_blue_button, 4, 2, alignment=Qt.AlignmentFlag.AlignCenter)
        left_layout.addWidget(black_button, 5, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        left_layout.addWidget(marty1_calib_button, 5, 0, alignment=Qt.AlignmentFlag.AlignCenter)
        left_layout.addWidget(marty2_calib_button, 5, 2, alignment=Qt.AlignmentFlag.AlignCenter)

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
        
        # Create a QSlider
        self.slider = QSlider(Qt.Orientation.Horizontal, self)
        self.slider.setMinimum(1000)
        self.slider.setMaximum(3000)
        self.slider.setValue(2000)
        
        # Connect the slider value change to the function
        self.slider.valueChanged.connect(self.updateSpeed)

        # Create QLabel for images
        slider_left_image_label = QLabel(self)
        slider_right_image_label = QLabel(self)

        # Load images into QLabels
        left_image = QPixmap('./img/slow.png').scaled(100, 100)
        right_image = QPixmap('./img/fast.png').scaled(100, 100)

        slider_left_image_label.setPixmap(left_image)
        slider_right_image_label.setPixmap(right_image)

        # Create a QHBoxLayout for the slider and images
        slider_layout = QHBoxLayout()
        slider_container = QWidget()
        slider_container.setLayout(slider_layout)
        slider_layout.addWidget(slider_left_image_label)
        slider_layout.addWidget(self.slider)
        slider_layout.addWidget(slider_right_image_label)

        # Create a QLabel
        # self.label = QLabel('Speed: 1500', self)
        # right_layout.addWidget(self.label)

        right_layout.addWidget(slider_container)
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
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setFocus()
        # self.label.setText(f'Speed: {value}')
        marty.set_speed(4000-value)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Left or event.key() == Qt.Key.Key_4:
            handle_button_click('left')
        elif event.key() == Qt.Key.Key_Right or event.key() == Qt.Key.Key_6:
            handle_button_click('right')
        elif event.key() == Qt.Key.Key_Up or event.key() == Qt.Key.Key_8:
            handle_button_click('top')
        elif event.key() == Qt.Key.Key_Down or event.key() == Qt.Key.Key_2:
            handle_button_click('down')
        elif event.key() == Qt.Key.Key_5:
            handle_button_click('center')
        elif event.key() == Qt.Key.Key_7:
            handle_button_click('left_top')
        elif event.key() == Qt.Key.Key_9:
            handle_button_click('right_top')
        elif event.key() == Qt.Key.Key_Space:
            handle_button_click('get_ready')
        elif event.key() == Qt.Key.Key_C:
            handle_button_click('show_off')
        elif event.key() == Qt.Key.Key_W:
            handle_button_click('wiggle_eyes')
        elif event.key() == Qt.Key.Key_D:
            handle_button_click('dance')
        else:
            print(f'Key {event.text()} is pressed')

    # def keyReleaseEvent(self, event):
    #     print('Key was released')

app = QApplication(sys.argv)

window = MainWindow()

marty = MartyController("wifi", "192.168.0.5")
marty2 = MartyController("wifi", "192.168.0.8")

window.show()

# Styling
app.setStyleSheet("MainWindow { background-color: rgba(212, 237, 244, 0.8) }")

app.exec()

marty.disconnect()