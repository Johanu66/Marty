
from martypy import Marty
import cv2

class MartyController:
    def __init__(self, connection_type, ip_address):
        # les variables
        self.marty = None
        self.connection_type = connection_type
        self.ip_address = ip_address
        self.speed = 1500
        self.step_length = 25
        self.turn_right_degree = -15
        self.turn_left_degree = 15
        self.eyes_expression = "wiggle"
        self.song_celebration_file_name = "excited"
        self.twist_right_kick = 0
        self.twist_left_kick = 0
        self.lift_right_arm_angle = 100
        self.lift_left_arm_angle = 100

        self.route_codes = {"light_blue": "begin", "dark_blue": "right", "pink": "left", "green": "forward", "yellow": "backward", "red": "end"}

        self.routes = list([{"origin": "light_blue", "distance": 5, "destination": "pink"},
                            {"origin": "pink", "distance": 8, "destination": "green"},
                            {"origin": "green", "distance": 4, "destination": "yellow"},
                            {"origin": "yellow", "distance": 6, "destination": "dark_blue"},
                            {"origin": "dark_blue", "distance": 10, "destination": "red"},
                            {"origin": "red", "distance": 2, "destination": None}])
    
    # les methodes
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
    
    def forward(self, distance=1):
        self.marty.walk(distance, "auto", 0, self.step_length, self.speed)
        print("Marty moves forward")
        
    def backward(self, distance=1):
        self.marty.walk(distance, "auto", 0, -1 * self.step_length, self.speed)
        print("Marty moves backward")
    
    def left_side_step(self, distance=1):
        self.marty.sidestep("left", distance, self.step_length, self.speed)
        print("Marty makes a left step")
        
    def right_side_step(self, distance=1) :
        self.marty.sidestep("right", distance, self.step_length, self.speed)
        print("Marty makes a right step")
    
    def turn_right(self):
        try:
            self.marty.walk(0, "auto",self.turn_right_degree, self.step_length, self.speed)
            print("Marty turns right")

        except Exception as e:
            print("An error occurred while connecting to Marty: " + str(e))
            
    def turn_left(self):
        try:
            self.marty.walk(0, "auto",self.turn_left_degree, self.step_length, self.speed)
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
            # self.marty.set_volume(self, new_volume=100)
            self.marty.play_sound("no_way", 1000, 5000)
            self.marty.celebrate(self.speed*2)
            self.marty.circle_dance("right",self.speed)
            self.marty.celebrate(self.speed*2)
            print("Marty is celebrating")
        except Exception as e:
            print("An error occurred while connecting to Marty: " + str(e))

    def left_kick(self):
            self.marty.kick("left", self.twist_left_kick, self.speed*2)
            print("Marty kicks left")
    
    def right_kick(self):
        self.marty.kick("right", self.twist_right_kick, self.speed*2)
        print("Marty kicks right")
        
    def lift_left_arm(self):
        self.marty.arms(self.lift_left_arm_angle, 0, self.speed/3)
        self.marty.arms(0*self.lift_left_arm_angle, 0, self.speed/3)
        self.marty.arms(self.lift_left_arm_angle, 0, self.speed/3)
        self.marty.arms(0*self.lift_left_arm_angle, 0, self.speed/3)
        print("Marty lifts left arm")
        
    def lift_right_arm(self):
        self.marty.arms(0, self.lift_right_arm_angle, self.speed/3)
        self.marty.arms(0, 0*self.lift_right_arm_angle, self.speed/3)
        self.marty.arms(0, self.lift_right_arm_angle, self.speed/3)
        self.marty.arms(0, 0*self.lift_right_arm_angle, self.speed/3)
        print("Marty lifts right arm")


    def auto_guide(self):
        for route in self.routes:
            if self.route_codes[route["origin"]] == "begin":
                self.get_ready()
                self.forward(route["distance"])
            if route["destination"] is not None:
                if self.route_codes[route["origin"]] == "forward":
                    self.forward(route["distance"])
                elif self.route_codes[route["origin"]] == "backward":
                    self.backward(route["distance"])
                elif self.route_codes[route["origin"]] == "left":
                    self.left_side_step(route["distance"])
                elif self.route_codes[route["origin"]] == "right":
                    self.right_side_step(route["distance"])
                elif self.route_codes[route["origin"]] == "end":
                    self.celebrate()
            else:
                self.celebrate()
    
    # les getters

    def get_speed(self):
        return self.speed
    
    def get_step_length(self):
        return self.step_length
    
    def get_turn_right_degree(self):
        return self.turn
    
    def get_turn_left_degree(self):
        return self.turn_left_degree
    
    def get_eyes_expression(self):
        return self.eyes_expression
    
    def get_song_celebration_file_name(self):
        return self.song_celebration_file_name
    
    def get_twist_right_kick(self):
        return self.twist_right_kick
    
    def get_twist_left_kick(self):
        return self.twist_left_kick
    
    def get_lift_right_arm_angle(self):
        return self.lift_right_arm_angle
    
    def get_lift_left_arm_angle(self):
        return self.lift_left_arm_angle
    
    # les setters
    
    def set_speed(self, new_speed):
        self.speed = new_speed    
        
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
        
    def set_twist_right_kick(self, new_twist_right_kick):
        self.twist_right_kick = new_twist_right_kick
        
    def set_twist_left_kick(self, new_twist_left_kick):
        self.twist_left_kick = new_twist_left_kick
        
    def set_lift_right_arm_angle(self, new_lift_right_arm):
        self.lift_right_arm_angle = new_lift_right_arm
        
    def set_lift_left_arm_angle(self, new_lift_left_arm):
        self.lift_left_arm_angle = new_lift_left_arm
