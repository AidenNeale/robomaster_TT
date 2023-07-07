from drone import Drone
import sys

if __name__ == '__main__':
    drone = Drone()
    drone.enable_camera()
    drone.takeoff()
    drone.frame_capture()
    drone.move_forward(position=30, capture_frame=True)
    drone.move_forward(position=30, capture_frame=True)
    drone.move_forward(position=30, capture_frame=True)

    drone.move_backward(position=90)

    drone.land()

    print("Reached")