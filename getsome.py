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
                
    def get_video_flux(self):

        if self.marty is not None:
            try:
                self.marty.start_camera()

                while True:
                    frame = self.marty.get_camera_frame()
                    
                    # Flip the frame horizontally (as Marty's camera is reversed)
                    frame = cv2.flip(frame, 1)
                    
                    cv2.imshow('Marty Video', frame)

                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

                cv2.destroyAllWindows()
            except Exception as e:
                print("An error occurred while streaming video: " + str(e))
        else:
            print("Marty is not connected.")
    def get_color_sensor(self):

        color =""
        ground= self.marty.foot_on_ground('RightIRFoot')
        if (ground):
            color_right = self.marty.get_ground_sensor_reading('RightIRFoot') 
            
            if(color_right<=173 and color_right>=175) :
                color = "red"
                print(color)

            elif(color_right==177) :
                color = "yellow"
                print(color)        

            elif( color_right==173) :
                color = "blue"
                print(color)                              

            elif(color_right ==170 or color_right ==171):
                color = "violet"
                print(color)




        
            print(color_right , color) 
            return color_right ,   
        else :
            print ("marty is on the ground")
            
            
    
            
            
        
        
        

        


controller = MartyController("wifi", "192.168.0.4")
controller.connect()
#controller.marty.walk(5)  
if controller.marty is not None:
    
    #controller.marty.dance()

    controller.get_battery_percentage()
    controller.get_color_sensor()
    
    
    controller.disconnect()

