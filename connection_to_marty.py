
from collections import Counter
from martypy import Marty


import cv2

from ColorCalibrator import ColorCalibrator
from GenerateRoute import GenerateRoute
from GridManager import GridManager

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

        self.grille_size = 3

        self.grille = [["black" for _ in range(self.grille_size)] for _ in range(self.grille_size)]

        self.route_codes = {"light_blue": "begin", "dark_blue": "right", "pink": "left", "green": "forward", "yellow": "backward", "red": "end"}

        distance = 7

        self.routes = list([{"origin": "light_blue", "distance": distance},
                            {"origin": "pink", "distance": distance},
                            {"origin": "green", "distance": distance},
                            {"origin": "yellow", "distance": distance},
                            {"origin": "dark_blue", "distance": distance},
                            {"origin": "red", "distance": 0}])
        
        self.red_values = (74, 87)
        self.pink_values = (91, 101)
        self.yellow_values = (180, 190)
        self.green_values = (25, 35)
        self.light_blue_values = (52, 56)
        self.dark_blue_values = (18, 22)
        self.black_values = (12, 16)
    
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
                print(self.marty.get_obstacle_sensor_reading("Left"))
                return self.marty.get_obstacle_sensor_reading("Left")
            except Exception as e:
                print("An error occurred while getting the sensor distance: " + str(e))

    def get_color_number(self):
        return self.marty.get_ground_sensor_reading("Left")
                
    def get_color_sensor(self):
        color = ""
        if self.marty is not None:
            try:
                # ground = self.marty.foot_on_ground('RightIRFoot')
                # if ground:
                # left_color = self.marty.get_ground_sensor_reading("Left")
                left_color = self.marty.get_color_sensor_hex("left")
                print(f"Value of the left color sensor: {left_color}")
                # if self.red_values[0] <= left_color <= self.red_values[1]:
                #     color = "red"
                # elif self.light_blue_values[0] <= left_color <= self.light_blue_values[1]:
                #     color = "light_blue"
                # elif self.green_values[0] <= left_color <= self.green_values[1]:
                #     color = "green"
                # elif self.yellow_values[0] <= left_color <= self.yellow_values[1]:
                #     color = "yellow"
                # elif self.pink_values[0] <= left_color <= self.pink_values[1]:
                #     color = "pink"
                # elif self.dark_blue_values[0] <= left_color <= self.dark_blue_values[1]:
                #     color = "dark_blue"
                # elif self.black_values[0] <= left_color <= self.black_values[1]:
                #     color = "black"

                if ColorCalibrator.detect_color(1, left_color) == "red":
                    color = "red"
                elif ColorCalibrator.detect_color(1, left_color) == "light_blue":
                    color = "light_blue"
                elif ColorCalibrator.detect_color(1, left_color) == "green":
                    color = "green"
                elif ColorCalibrator.detect_color(1, left_color) == "yellow":
                    color = "yellow"
                elif ColorCalibrator.detect_color(1, left_color) == "pink":
                    color = "pink"
                elif ColorCalibrator.detect_color(1, left_color) == "dark_blue":
                    color = "dark_blue"
                elif ColorCalibrator.detect_color(1, left_color) == "black":
                    color = "black"
                else:
                    color = "yellow"
                # else:
                #     print("Marty's foot is not on the ground.")
                #     color = "black"
                return color
            except Exception as e:
                print("An error occurred while getting the color sensor reading: " + str(e))

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
        GenerateRoute.produce_route()
        print(GenerateRoute.routes)
        for route in GenerateRoute.routes:
            if self.route_codes[route["origin"]] == "begin":
                self.get_ready()
                self.forward(route["distance"])
            if route["distance"] != 0:
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
    
    def top_occurrences(self, lst):
        # Comptage des occurrences de chaque élément dans la liste
        counts = Counter(lst)
        # Obtenir les trois éléments les plus fréquents
        most_common_three = counts.most_common(self.grille_size)
        # Créer une liste des éléments les plus fréquents sans les compteurs
        most_common_elements = [item[0] for item in most_common_three]
        # Réordonner les éléments en conservant leur ordre d'apparition original dans la liste
        top_three = []
        for item in lst:
            if item in most_common_elements and item not in top_three:
                top_three.append(item)
        return [item for item in top_three]

    def reconnaissance1(self):
        forward_or_backward_steps = 13
        right_steps = 8
        colors = list()
        for _ in range(forward_or_backward_steps):
            colors.append(self.get_color_sensor())
            self.forward()
            colors.append(self.get_color_sensor())
        print(colors)
        colors = [x for x in colors if x != "unrecognized"]
        print(colors)
        top_colors = self.top_occurrences(colors)
        print(top_colors)
        for i in range(self.grille_size):
            if GridManager.grille[0][i] == "black":
                GridManager.grille[0][i] = top_colors[i]
        for _ in range(right_steps):
            self.right_side_step()
        print(colors)

        colors = list()
        for _ in range(forward_or_backward_steps):
            colors.append(self.get_color_sensor())
            self.backward()
            colors.append(self.get_color_sensor())
        colors = [x for x in colors if x != "unrecognized"]
        top_colors = self.top_occurrences(colors)
        top_colors.reverse()
        print(top_colors)
        for i in range(self.grille_size):
            if GridManager.grille[0][i] == "black":
                GridManager.grille[1][i] = top_colors[i]
        for _ in range(right_steps):
            self.right_side_step()
        print(colors)

        colors = list()
        for _ in range(forward_or_backward_steps):
            colors.append(self.get_color_sensor())
            self.forward()
            colors.append(self.get_color_sensor())
        colors = [x for x in colors if x != "unrecognized"]
        top_colors = self.top_occurrences(colors)
        print(top_colors)
        for i in range(self.grille_size):
            if GridManager.grille[0][i] == "black":
                GridManager.grille[2][i] = top_colors[i]
        print(colors)

        print(GridManager.grille)

    def reconnaissance(self):
        forward_or_backward_steps = 7
        right_steps = 7
        colors = list()

        ligne = 0
        colors.append(self.get_color_sensor())
        self.forward(forward_or_backward_steps)
        colors.append(self.get_color_sensor())
        self.forward(forward_or_backward_steps)
        colors.append(self.get_color_sensor())
        for i in range(GridManager.grille_size):
            if GridManager.grille[ligne][i]=="black":
                GridManager.grille[ligne][i] = colors[i]
            elif GridManager.grille[ligne][i] != colors[i]:
                if GridManager.grille[ligne][0] == GridManager.grille[ligne][1] or GridManager.grille[ligne][1] == GridManager.grille[ligne][2]:
                    GridManager.grille[ligne][i] = colors[i]
        colors = list()


        ligne = 1
        self.right_side_step(right_steps)
        colors.append(self.get_color_sensor())
        self.backward(forward_or_backward_steps)
        colors.append(self.get_color_sensor())
        self.backward(forward_or_backward_steps)
        colors.append(self.get_color_sensor())
        colors.reverse()
        for i in range(GridManager.grille_size):
            if GridManager.grille[ligne][i]=="black":
                GridManager.grille[ligne][i] = colors[i]
            elif GridManager.grille[ligne][i] != colors[i]:
                if GridManager.grille[ligne][0] == GridManager.grille[ligne][1] or GridManager.grille[ligne][1] == GridManager.grille[ligne][2]:
                    GridManager.grille[ligne][i] = colors[i]
        colors = list()

        ligne = 2
        self.right_side_step(right_steps)
        colors.append(self.get_color_sensor())
        self.forward(forward_or_backward_steps)
        colors.append(self.get_color_sensor())
        self.forward(forward_or_backward_steps)
        colors.append(self.get_color_sensor())
        for i in range(GridManager.grille_size):
            if GridManager.grille[ligne][i]=="black":
                GridManager.grille[ligne][i] = colors[i]
            elif GridManager.grille[ligne][i] != colors[i]:
                if GridManager.grille[ligne][0] == GridManager.grille[ligne][1] or GridManager.grille[ligne][1] == GridManager.grille[ligne][2]:
                    GridManager.grille[ligne][i] = colors[i]
        colors = list()

        print(GridManager.grille)

    def auto_marty1(self):
        self.reconnaissance()


    def auto_marty2(self):
        self.reconnaissance()

    
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

    def set_red_values(self, value):
        self.red_values = value
        print(value)

    def set_pink_values(self, value):
        self.pink_values = value
        print(value)

    def set_yellow_values(self, value):
        self.yellow_values = value
        print(value)

    def set_green_values(self, value):
        self.green_values = value
        print(value)

    def set_light_blue_values(self, value):
        self.light_blue_values = value
        print(value)

    def set_dark_blue_values(self, value):
        self.dark_blue_values = value
        print(value)

    def set_black_values(self, value):
        self.black_values = value
        print(value)

