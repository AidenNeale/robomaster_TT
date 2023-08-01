import cv2, time
from cv2 import aruco
from threading import Thread, Event

import robomaster
from robomaster import robot


class Drone():
    def __init__(self, logging=False, display=False):
        if logging:
            robomaster.enable_logging_to_file()

        robomaster.config.LOCAL_IP_STR = '192.168.10.2'
        self.drone = robot.Drone()
        self.drone.initialize()

        self.condition = Event()

        self.flight = self.drone.flight
        self.camera = self.drone.camera

        self.thread = Thread(target=self.camera_thread, name='camera_thread', args=(display,))

        self.current_frame_id = 0

        dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
        parameters =  aruco.DetectorParameters()
        self.detector_aruco = aruco.ArucoDetector(dictionary, parameters)


    def enable_camera(self):
        self.camera.start_video_stream(display=False)
        time.sleep(2.5)
        self.thread.start()
        time.sleep(2.5)

    def camera_thread(self, display):
        while True:
            if self.condition.is_set():
                break
            img = self.camera.read_cv2_image(strategy="newest")
            img = cv2.flip(img, 0) # flips vertically
            if display: # If this works, this can be used for computer vision -> ROS? ArUco Tag Detection, etc.
                markerCorners, markerIds, rejectedCandidates = self.detector_aruco.detectMarkers(img)
                if markerIds != None:
                    print(markerIds)
                aruco.drawDetectedMarkers(img, markerCorners, markerIds)
                cv2.imshow('capture', img)
                cv2.waitKey(1)


    def close(self):
        self.condition.set()
        try:
            cv2.destroyAllWindows()
        except Exception as e:
            print(e)
            pass
        self.camera.stop_video_stream()
        self.camera.stop()
        self.drone.close()
        



    def takeoff(self):
        self.flight.takeoff().wait_for_completed()
        self.flight.up(distance=50).wait_for_completed()  


    def land(self):
        self.flight.land().wait_for_completed()


    def head_to_start(self):
        self.move_forward(position=100)
        self.move_forward(position=100)
        self.move_left(position=100)
        self.move_left(position=100, capture_frame=True)


    def return_home(self):
        self.move_backward(position=100)
        self.move_left(position=100)
        self.move_left(position=100)
        self.move_left(position=100)
        self.move_left(position=100)
        self.move_backward(position=100)
        self.move_backward(position=100)
        self.move_backward(position=100)
        self.move_backward(position=100)
        self.move_backward(position=100)


    def move_forward(self, position=0, capture_frame=False):
        self.flight.forward(distance=position).wait_for_completed()


    def move_backward(self, position=0, capture_frame=False):
        self.flight.backward(distance=position).wait_for_completed()


    def move_left(self, position=0, capture_frame=False):
        self.flight.left(distance=position).wait_for_completed()


    def move_right(self, position=0, capture_frame=False):
        self.flight.right(distance=position).wait_for_completed()


if __name__ == '__main__':
    print("You're running the class program")