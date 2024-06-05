
from martypy import Marty
import cv2

class MartyController:
    def __init__(self, connection_type, ip_address):
        self.marty = None
        self.connection_type = connection_type
        self.ip_address = ip_address
        self.speed = 1500
        self.step_length = 25
        self.turn_right_degree = -15
        self.turn_left_degree = 15
        self.eyes_expression = "wiggle"
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
            
    def get_battery_percentage(self):
        if self.marty is not None:
            try:
                print ("battery percentage is :",self.marty.get_battery_remaining())
                
                
                return self.marty.get_battery_remaining()
            
            except Exception as e:
                print("An error occurred while getting the battery percentage: " + str(e))
    
    def get_sensor_distace(self):
        
        if self.marty is not None:
            try:
                
                print(self.marty.get_obstacle_sensor_reading("Left"))\
               
                return self.marty.get_obstacle_sensor_reading("Left")
            
                
            
            except Exception as e:
                print("An error occurred while getting the battery percentage: " + str(e))
                
    
    def get_color_sensor(self):

        color =""
        ground= self.marty.foot_on_ground('RightIRFoot')
        if (ground):
             
           color_right = self.marty.get_color_sensor_hex('LEFT')
           if(0x000000<=color_right<=0x1F1F1F):
                color="Black"
                return color
               
           if(0xFF0000<=color_right<=0xFFEFEF):
                color="Red"
                return color
           

           if(0xFFFF00<=color_right<=0xFFFFC0):
                color="Yellow"
                return color
           
           if(0x0000FF<=color_right<=0x7F7FFF):
                color="Blue"
                return color
           
           if(color_right==0x404051):
                color="Skyblue"
                return color
               
               
                
        else :
            print ("marty is not the ground")
            
            
    
            
            
        
        
        

        

    def get_ready(self):
        self.marty.get_ready()
    
    def forward(self):
        self.marty.walk(1, "auto", 0, self.step_length, self.speed)
        print("Marty moves forward")
        
    def backward(self):
        self.marty.walk(1, "auto", 0, -1 * self.step_length, self.speed)
        print("Marty moves backward")
    
    def left_side_step(self) :
        self.marty.sidestep("left", 1, self.step_length, self.speed)
        print("Marty makes a left step")
        
    def right_side_step(self) :
        self.marty.sidestep("right", 1, self.step_length, self.speed)
        print("Marty makes a right step")
    
    def turn_right(self):
        try:
            self.marty.walk(0, "auto",self.turn_right_degree, 25, self.speed)
            print("Marty turns right")

        except Exception as e:
            print("An error occurred while connecting to Marty: " + str(e))
            
    def turn_left(self):
        try:
            self.marty.walk(0, "auto",self.turn_left_degree, 25, self.speed)
            print("Marty turns left ")

        except Exception as e:
            print("An error occurred while connecting to Marty: " + str(e))

    def wiggle_eyes(self):
        self.marty.eyes(self.eyes_expression, self.speed*2)
        print("Marty Wiggle")

    def dance(self):
        try :
            self.marty.dance()
            print("Marty is dancing")
        except Exception as e:
            print("An error occurred while connecting to Marty: " + str(e))

    def celebrate(self):
        try :
            self.marty.play_sound("no_way", 1000, 5000)
            self.marty.celebrate(self.speed*2)
            self.marty.circle_dance("right",1000)
            self.marty.celebrate(self.speed*2)
            print("Marty is celebrating")
        except Exception as e:
            print("An error occurred while connecting to Marty: " + str(e))

    def set_speed(self, new_speed):
        self.speed = new_speed

    def get_speed(self):
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
