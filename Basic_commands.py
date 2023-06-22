
from djitellopy import Tello # ensure library is installed from settings prior to testing
import time

drone = Tello()
tello.connect() # Connects the tello
tello.takeoff() # Sends the command to the tello drone to takeoff
tello.move_up(80) # Sends the command to move the tello upwards 80cm

tello.move_down(50)  # Sends the command to move the tello 50cm downwards

tello.move_left(50)  # Sends the command to move the tello  50cm to the left

tello.move_right(50) # Sends the command to move the tello  50cm to the right

tello.land() # sends a landing command to the tello

tello.disconnect() # Disconnects the tello to the code

time.sleep(2) #given in seconds 

# Distances in parentheses are given in centimeters!
