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
            
            
    
            
            
        
        
        

        


controller = MartyController("wifi", "192.168.0.4")
controller.connect()
#controller.marty.walk(5)  
if controller.marty is not None:
    
    #controller.marty.dance()

    controller.get_battery_percentage()
    controller.get_color_sensor()
    
    
    controller.disconnect()


