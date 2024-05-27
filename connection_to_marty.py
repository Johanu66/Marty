
from martypy import Marty

class MartyController:
    def __init__(self, connection_type, ip_address):
        self.marty = None
        self.connection_type = connection_type
        self.ip_address = ip_address
        self.speed = 1500
        self.step_length = 25

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

    
    def forward(self):
        self.marty.walk(1, "auto", 0, self.step_length, self.speed)
        print("Marty avance")
        
    def backward(self):
        self.marty.walk(1, "auto", 0, -1 * self.step_length, self.speed)
        print("Marty recule")
        
    def get_ready(self):
        self.marty.get_ready()

    def setSpeed(self, new_speed):
        self.speed = new_speed
        
    def setStepLength(self, new_step_length):
        self.step_length = new_step_length
        

controller = MartyController("wifi", "192.168.0.7")
controller.connect()
if controller.marty is not None:
    controller.get_ready()
    controller.forward()
    controller.backward()