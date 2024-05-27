# -*- coding: utf-8 -*-
"""
Created on Wed May 15 10:36:49 2024

@author: HP
"""

from martypy import Marty

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


controller = MartyController("wifi", "192.168.0.112")
controller.connect()
#controller.marty.walk(5)  
if controller.marty is not None:
    controller.marty.walk(5)
    #controller.marty.dance()
#controller.disconnect()
