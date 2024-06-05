
from martypy import Marty

class MartyController:
    def __init__(self, connection_type, ip_address):
        self.marty = None
        self.connection_type = connection_type
        self.ip_address = ip_address
        self.speed = 1500
        self.step_length = 25
        self.turn_right_degree = 50
        self.turn_left_degree = -50
        self.eyes_expression = "normal"
        self.song_celebration_file_name = "excited"

    def connect(self):
        try:
            self.marty = Marty(self.connection_type, self.ip_address)
            print("Connected to Marty successfully.")
        except Exception as e:
            print("An error occurred while connecting to Marty: " + str(e))

    def disconnect(self):
        if self.marty is not None:
            try:
                self.marty.close()
                print("Disconnected from Marty successfully.")
            except Exception as e:
                print("An error occurred while disconnecting from Marty: " + str(e))
        else:
            print("Marty is not connected.")

    def get_ready(self):
        self.marty.get_ready()
    
    def forward(self):
        self.marty.walk(1, "auto", 0, self.step_length, self.speed)
        print("Marty moves forward")
        
    def backward(self):
        self.marty.walk(1, "auto", 0, -1 * self.step_length, self.speed)
        print("Marty moves backward")
    
    def turn_right(self):
        try:
            self.forward()
            self.marty.walk(0, "auto",self.turn_right_degree, 25, self.speed)
            print("Marty turns right")

        except Exception as e:
            print("An error occurred while connecting to Marty: " + str(e))
            
    def turn_left(self):
        try:
            self.forward()
            self.marty.walk(0, "auto",self.turn_left_degree, 25, self.speed)
            print("Marty turns left ")

        except Exception as e:
            print("An error occurred while connecting to Marty: " + str(e))

    def gaze(self):
        self.marty.eyes(self.eyes_expression, self.speed)
        print("Marty ")

    def dance(self):
        try :
            self.marty.dance()
            print("Marty is dancing")
        except Exception as e:
            print("An error occurred while connecting to Marty: " + str(e))

    def celebrate(self):
        try :
            self.marty.play_sound(self.song_celebration_file_name)
            self.marty.celebrate(self.speed*4)
            print("Marty is celebrating")
        except Exception as e:
            print("An error occurred while connecting to Marty: " + str(e))

    def set_speed(self, new_speed):
        self.speed = new_speed

    def getSpeed(self):
        return self.speed
        
    def set_step_length(self, new_step_length):
        self.step_length = new_step_length
        
    def set_turn_right_degree(self, new_turn_right_degree):
        self.turn_right_degree = new_turn_right_degree
    
    def set_turn_left_degree(self, new_turn_left_degree):
        self.turn_left_degree = new_turn_left_degree
    
    def set_eyes_expression(self, new_eyes_expression):
        self.eyes_expression = new_eyes_expression
        
    def set_song_celebration_file_name(self, new_song_celebration_file_name):
        self.song_celebration_file_name = new_song_celebration_file_name

controller = MartyController("wifi", "192.168.0.4")
controller.connect()
if controller.marty is not None:
    controller.get_ready()
    controller.forward()
    controller.turn_left()
    # controller.gaze()
    # controller.get_ready()
    # controller.dance()
    # controller.forward()
    # controller.celebrate()
    # controller.backward()
    # controller.get_ready()
    controller.disconnect()
