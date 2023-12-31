
from djitellopy import Tello # ensure library is installed from settings prior to testing
import time

drone = Tello()
drone.connect() # Connects the tello
drone.takeoff() # Sends the command to the tello drone to takeoff
drone.move_up(80) # Sends the command to move the tello upwards 80cm

drone.move_down(50)  # Sends the command to move the tello 50cm downwards

drone.move_left(50)  # Sends the command to move the tello  50cm to the left

drone.move_right(50) # Sends the command to move the tello  50cm to the right

drone.land() # sends a landing command to the tello

drone.disconnect() # Disconnects the tello to the code

time.sleep(2) #given in seconds 

# Distances in parentheses are given in centimeters!
