from djitellopy import Tello
import cv2

drone = Tello()
drone.connect()
print(f"Battery: {drone.get_battery()}%") # Prints the battery level of the
drone.streamon()

while True:
    drone.takeoff()  # Sends the command to the Tello drone to take off
    drone.move_up(80)  # Sends the command to move the Tello upwards 80cm
    drone.flip("f")  # 'b' for backward flip

    drone_image  = drone.get_frame_read().frame
    drone_image  = cv2.resize(drone_image , (360, 240)) #Numbers in the paranathese can be changed according to preferred size of frame
    cv2.imshow("Image", drone_image)
    cv2.waitKey(1)
    drone.land()

