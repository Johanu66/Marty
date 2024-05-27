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
                print (self.marty.get_battery_remaining())
                print(self.marty.get_battery_voltage() )
                return self.marty.get_battery_voltage() 
                return self.marty.get_battery_remaining()
            
            except Exception as e:
                print("An error occurred while getting the battery percentage: " + str(e))
    
    def get_sensor_distace(self):
        
        if self.marty is not None:
            try:
                print (self.marty.get_distance_sensor())
                return self.marty.get_distance_sensor()
                
            
            except Exception as e:
                print("An error occurred while getting the battery percentage: " + str(e))
                
    def get_video_flux(self):
        self.marty.start_camera()
        while True:
            frame = self.marty.get_camera_frame()  

            cv2.imshow('Marty Video', frame) 

            if cv2.waitKey(1) & 0xFF == ord('q'): 
                break
    def get_color_sensor(self):
        
        ground= self.mary.foot_on_ground('RightIRFoot')
        if (ground):
            color_right = self.marty.get_color_sensor_reading('RightFoot')  
            color_left = self.marty.get_color_sensor_reading('LeftFoot')  
            return color_right, color_left 
        else :
            print ("marty aint on the ground")
            
        
        
            
            
        
        
        

        


controller = MartyController("wifi", "192.168.0.112")
controller.connect()
#controller.marty.walk(5)  
if controller.marty is not None:
    controller.marty.walk(5)
    #controller.marty.dance()
#controller.disconnect()
