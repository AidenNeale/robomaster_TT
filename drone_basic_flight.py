import robomaster
from robomaster import robot


if __name__ == '__main__':
    robomaster.enable_logging_to_file() # Enable this if program breaks
    tl_drone = robot.Drone()

    robomaster.config.LOCAL_IP_STR = '192.168.10.2'
    tl_drone.initialize()

    tl_flight = tl_drone.flight
    tl_camera= tl_drone.camera

    tl_flight.takeoff().wait_for_completed()

    # tl_camera.start_video_stream(display=True)
    tl_flight.up(distance=50).wait_for_completed()
    tl_flight.forward(distance=50).wait_for_completed() # Attempt to realign with takeoff position

    tl_flight.forward(distance=150).wait_for_completed()

    tl_flight.left(distance=100).wait_for_completed()
    tl_flight.left(distance=100).wait_for_completed()

    tl_flight.forward(distance=100).wait_for_completed()
    tl_flight.forward(distance=100).wait_for_completed()
    tl_flight.forward(distance=100).wait_for_completed()
    tl_flight.forward(distance=100).wait_for_completed()

    tl_flight.right(distance=100).wait_for_completed()

    tl_flight.backward(distance=100).wait_for_completed()
    tl_flight.backward(distance=100).wait_for_completed()
    tl_flight.backward(distance=100).wait_for_completed()
    tl_flight.backward(distance=100).wait_for_completed()

    tl_flight.right(distance=100).wait_for_completed()

    tl_flight.forward(distance=100).wait_for_completed()
    tl_flight.forward(distance=100).wait_for_completed()
    tl_flight.forward(distance=100).wait_for_completed()
    tl_flight.forward(distance=100).wait_for_completed()

    tl_flight.right(distance=100).wait_for_completed()

    tl_flight.backward(distance=100).wait_for_completed()
    tl_flight.backward(distance=100).wait_for_completed()
    tl_flight.backward(distance=100).wait_for_completed()
    tl_flight.backward(distance=100).wait_for_completed()

    tl_flight.right(distance=100).wait_for_completed()

    tl_flight.forward(distance=100).wait_for_completed()
    tl_flight.forward(distance=100).wait_for_completed()
    tl_flight.forward(distance=100).wait_for_completed()
    tl_flight.forward(distance=100).wait_for_completed()

    tl_flight.right(distance=100).wait_for_completed()

    tl_flight.backward(distance=100).wait_for_completed()
    tl_flight.backward(distance=100).wait_for_completed()
    tl_flight.backward(distance=100).wait_for_completed()
    tl_flight.backward(distance=100).wait_for_completed()

    tl_flight.right(distance=100).wait_for_completed()

    tl_flight.forward(distance=100).wait_for_completed()
    tl_flight.forward(distance=100).wait_for_completed()
    tl_flight.forward(distance=100).wait_for_completed()
    tl_flight.forward(distance=100).wait_for_completed()

    tl_flight.backward(distance=100).wait_for_completed()
    tl_flight.backward(distance=100).wait_for_completed()
    tl_flight.backward(distance=100).wait_for_completed()
    tl_flight.backward(distance=100).wait_for_completed()

    tl_flight.left(distance=100).wait_for_completed()
    tl_flight.left(distance=100).wait_for_completed()
    tl_flight.left(distance=100).wait_for_completed()

    tl_flight.backward(distance=100).wait_for_completed()
    tl_flight.land().wait_for_completed()

    # tl_camera.stop_video_stream()
    # tl_camera.stop()

    tl_drone.close()