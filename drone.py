import cv2, time

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

        self.current_frame_id = 0


    def enable_camera(self, display_on_screen=False):
        self.camera.start_video_stream(display=display_on_screen)


    def close(self):
        self.camera.stop_video_stream()
        self.camera.stop()
        self.drone.close()


    def frame_capture(self):
        time.sleep(1.5) # Sleep to stabilise drone before image capture
        img = self.camera.read_cv2_image()
        filepath = 'RoboMaster_Img_' + self.current_frame_id
        self.current_frame_id += 1 # Increment ID of Frame
        cv2.imwrite(filepath, img)


    def takeoff(self):
        self.flight.takeoff().wait_for_completed()
        self.flight.up(distance=50).wait_for_completed()  


    def land(self):
        self.flight.land().wait_for_completed()


    def head_to_start(self):
        self.move_forward(position=200)
        self.move_left(position=200)


    def return_home(self):
        self.move_backward(position=400)
        self.move_left(position=300)
        self.move_backward(position=100)


    def move_forward(self, position=0, capture_frame=False):
        self.flight.forward(distance=position).wait_for_completed()
        if capture_frame:
            self.frame_capture()


    def move_backward(self, position=0, capture_frame=False):
        self.flight.backward(distance=position).wait_for_completed()
        if capture_frame:
            self.frame_capture()


    def move_left(self, position=0, capture_frame=False):
        self.flight.left(distance=position).wait_for_completed()
        if capture_frame:
            self.frame_capture()


    def move_right(self, position=0, capture_frame=False):
        self.flight.right(distance=position).wait_for_completed()
        if capture_frame:
            self.frame_capture()


if __name__ == '__main__':
    pass