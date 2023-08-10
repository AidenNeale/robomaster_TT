import cv2, time
from cv2 import aruco
import numpy as np
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

        self.pos_x = 0
        self.pos_y = 0

        self.current_image = np.array([])

        self.markerID = -1
        self.markerIDPos = {'x': 0, 'y': 0}

        self.thread = Thread(target=self.camera_thread, name='camera_thread', args=(display,))


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
            self.current_image = img
            if display: # If this works, this can be used for computer vision -> ROS? ArUco Tag Detection, etc.
                markerTags, markerIds, rejectedCandidates = self.detector_aruco.detectMarkers(img)
                if markerIds is not None:
                    ids = markerIds.flatten()
                    for (markerCorner, markerID) in zip(markerTags, ids):
                        if markerID == 10:
                            corners = markerCorner.reshape((4, 2))
                            (topLeft, topRight, bottomRight, bottomLeft) = corners
                            centreX = round((topLeft[0]+bottomRight[0])/2)
                            centreY = round((topLeft[1]+bottomRight[1])/2)
                            self.markerID = markerID
                            self.markerIDPos = {'x': centreX, 'y': centreY}
                aruco.drawDetectedMarkers(img, markerTags, markerIds)
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
        self.flight.up(distance=150).wait_for_completed()  


    def land(self):
        self.flight.land().wait_for_completed()


    def head_to_start(self):
        self.move_forward(position=60)
        self.move_forward(position=60)
        self.move_forward(position=60)
        self.move_forward(position=60)
        self.move_right()
        self.move_right()
        self.move_right(position=75)


    def return_home(self):
        return_dist = self.pos_y /2
        if self.pos_x > 0:
            self.move_left(self.pos_x)
        else:
            self.move_right(-self.pos_x)
        self.move_backward(return_dist) # Offset introduced to prevent drift causing drone to crash into wall
        self.move_backward(return_dist) # Offset introduced to prevent drift causing drone to crash into wall


    def move_forward(self, position=135):
        self.flight.forward(distance=position).wait_for_completed()
        time.sleep(0.5)
        self.pos_y += position


    def move_backward(self, position=135):
        self.flight.backward(distance=position).wait_for_completed()
        time.sleep(0.5)
        self.pos_y -= position


    def move_left(self, position=125):
        self.flight.left(distance=position).wait_for_completed()
        time.sleep(0.5)
        self.pos_x -= position


    def move_right(self, position=125):
        self.flight.right(distance=position).wait_for_completed()
        time.sleep(0.5)
        self.pos_x += position


if __name__ == '__main__':
    print("You're running the class program")