# -*- coding: utf-8 -*-
"""
Created on Wed May 15 10:36:49 2024

@author: HP
"""

from martypy import Marty


import cv2

class MartyController:
    def __init__(self, connection_type, ip_address):
        self.marty = None
        self.connection_type = connection_type
        self.ip_address = ip_address

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
      color = ""
      ground = self.marty.foot_on_ground('RightIRFoot')
      if ground:
          
            left_color = self.marty.get_ground_sensor_reading("Left")
            print(f"Value of the left color sensor: {left_color}")
            if 70 <= left_color <= 74:
                color = "Red"
            elif 42 <= left_color <= 46:
                color = "Light Blue"
            elif 26 <= left_color <= 30:
                color = "Green"
            elif 160 <= left_color <= 164:
                color = "Yellow"
                  
            elif 83 <= left_color <= 87:
                color = "Pink"
            elif 18 <= left_color <= 22:
                color = "Dark Blue"
            elif 12 <= left_color <= 16:
                color = "Black"
                  
            else:
                color = "Unrecognized"
            return color
        
      else:
          print("Marty's foot is not on the ground.")
           
               
       
if __name__ == "__main__":
    controller = MartyController("wifi", "192.168.0.105")
    controller.connect()
    # 
    if controller.marty is not None:
        controller.marty.walk(5)
        print(controller.get_color_sensor())
        
           
            
    
            
            
        
        
        

        





