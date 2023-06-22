from djitellopy import Tello

drone = Tello()
drone.connect() # establish connections with the drones
drone.takeoff() # Gives the command to take off the drone

drone.move_forward(70) # Commands the drone to move forward by 70cm
drone.move_up(50) # Gives the command to move the drone up by 50cm


# Commands to execute flips using the Tello Drone 
drone.flip("f")  # Gives the command for the drone to do a forward flip
drone.flip_left() # Gives the command for the drone to do a left-sided flip
drone.flip_right() # Gives the command for the drone to do a right-sided flip
drone.flip_back()  # Gives the command for the drone to a backflip

# Commands to execute flips using the Tello Drone 
drone.rotate_cw(120) # Gives the command for the drone to rotate 120 degrees in a clockwise direction.
drone.rotate_counter_clockwise(90) #  # Gives the command for the drone to rotate 120 degrees in a counter-clockwise direction.


drone.land()
