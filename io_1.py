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
            print(f"An error occurred while connecting to Marty: {e}")

    def disconnect(self):
        if self.marty is not None:
            try:
                self.marty.close()
                print("Disconnected from Marty successfully.")
            except Exception as e:
                print(f"An error occurred while disconnecting from Marty: {e}")
        else:
            print("Marty is not connected.")

    def get_ready(self):
        self.marty.get_ready()
    
    def forward(self):
        self.marty.walk(1, "auto", 0, self.step_length, self.speed)
        print("Marty is moving forward")
        
    def backward(self):
        self.marty.walk(1, "auto", 0, -self.step_length, self.speed)
        print("Marty is moving backward")
    
    def turn(self, angle):
        try:
            if angle > 30:
                angle = 30
            self.marty.walk(0, "auto", angle)
            print(f"Marty is turning {angle} degrees")
        except Exception as e:
            print(f"An error occurred while turning Marty: {e}")

    def gaze(self, expression):
        self.marty.eyes(expression, self.speed)
        print(f"Marty is making a {expression} expression")

    def dance(self):
        try:
            self.marty.dance()
            print("Marty is dancing")
        except Exception as e:
            print(f"An error occurred while making Marty dance: {e}")

    def celebrate(self):
        try:
            self.marty.celebrate()
            print("Marty is celebrating")
        except Exception as e:
            print(f"An error occurred while making Marty celebrate: {e}")

    def set_speed(self, new_speed):
        self.speed = new_speed
        
    def set_step_length(self, new_step_length):
        self.step_length = new_step_length
        
