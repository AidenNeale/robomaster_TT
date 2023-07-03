import time

import robomaster
from robomaster import robot


class Drone():
    def __init__(self, logging=False):
        if logging:
            robomaster.enable_logging_to_file()

        robomaster.config.LOCAL_IP_STR = '192.168.10.2'
        self.drone = robot.Drone()
        self.drone.initialize()


        self.flight = self.drone.flight
        self.camera = self.drone.camera

    def camera_capture(self, display_on_screen=False):
        self.camera.start_video_stream(display=display_on_screen)


    def close(self):
        self.camera.stop_video_stream()
        self.camera.stop()
        self.drone.close()


    def takeoff(self):
        self.flight.takeoff().wait_for_completed()

    def land(self):
        self.flight.land().wait_for_completed()


    def move_forward(self, position):
        self.flight.forward(distance=position).wait_for_completed()


    def move_backward(self, position):
        self.flight.backward(distance=position).wait_for_completed()


    def move_left(self, position):
        self.flight.left(distance=position).wait_for_completed()


    def move_right(self, position):
        self.flight.right(distance=position).wait_for_completed()

if __name__ == '__main__':
    drone = Drone()
    drone.camera_capture()
    drone.takeoff()

    drone.close()
