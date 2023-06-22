from djitellopy import Tello

tello = Tello()
tello.connect()
tello.takeoff() # Gives command to take off the drone

for x in range(3): # Call a for loop to execute 3 times.
    tello.move_forward(100)  # Gives the command to move the drone forward 100cm
    tello.rotate_cw(120)  # Moves the drone 120 degrees in a clockwise direction.

tello.land() # sends command to land the drone
tello.end() # ends the connection between laptop and drone
