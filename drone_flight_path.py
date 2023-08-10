import cv2

from drone import Drone


if __name__ == '__main__':
    drone = Drone(display=True)
    drone.enable_camera()
    drone.takeoff()

    drone.head_to_start()

    with open('flight_path.txt', 'r') as file:
        found = False
        while True:
            line = file.readline().strip()
            if drone.markerID == 10 and found == False:
                print("MARKER FOUND!")
                found = True
                break
            if line == "forward" or line == "f":
                drone.move_forward()
            elif line == "backward":
                drone.move_backward()
            elif line == "left":
                drone.move_left(position=125)
            elif line == "right":
                drone.move_right(position=125)
            elif not line:
                break
            else:
                print(f"THERE IS AN UNHANDLED INPUT WITHIN FLIGHT PATH: {line}")

    if found == True:
        #Align over tag
        #  cv2.imshow("drone", drone.current_image)
        #  cv2.waitKey(1)
        print(drone.current_image)
        print(f"Position of Marker in frame: {drone.markerIDPos}")

    print(f"X: {drone.pos_x}, Y: {drone.pos_y}")

    drone.return_home()

    drone.land()
    drone.close()