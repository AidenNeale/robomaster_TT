from drone import Drone


if __name__ == '__main__':
    drone = Drone()
    drone.enable_camera()
    drone.takeoff()

    drone.head_to_start()

    drone.move_forward(position=100, capture_frame=True)
    drone.move_forward(position=100, capture_frame=True)
    drone.move_forward(position=100, capture_frame=True)
    drone.move_forward(position=100, capture_frame=True)

    drone.move_right(position=100, capture_frame=True)

    drone.move_backward(position=100, capture_frame=True)
    drone.move_backward(position=100, capture_frame=True)
    drone.move_backward(position=100, capture_frame=True)
    drone.move_backward(position=100, capture_frame=True)

    drone.move_right(position=100, capture_frame=True)

    drone.move_forward(position=100, capture_frame=True)
    drone.move_forward(position=100, capture_frame=True)
    drone.move_forward(position=100, capture_frame=True)
    drone.move_forward(position=100, capture_frame=True)


    drone.move_right(position=100, capture_frame=True)

    drone.move_backward(position=100, capture_frame=True)
    drone.move_backward(position=100, capture_frame=True)
    drone.move_backward(position=100, capture_frame=True)
    drone.move_backward(position=100, capture_frame=True)

    drone.move_right(position=100, capture_frame=True)

    drone.move_forward(position=100, capture_frame=True)
    drone.move_forward(position=100, capture_frame=True)
    drone.move_forward(position=100, capture_frame=True)
    drone.move_forward(position=100, capture_frame=True)

    drone.move_right(position=100, capture_frame=True)

    drone.move_backward(position=100, capture_frame=True)
    drone.move_backward(position=100, capture_frame=True)
    drone.move_backward(position=100, capture_frame=True)
    drone.move_backward(position=100, capture_frame=True)

    drone.move_right(position=100, capture_frame=True)

    drone.move_forward(position=100, capture_frame=True)
    drone.move_forward(position=100, capture_frame=True)
    drone.move_forward(position=100, capture_frame=True)
    drone.move_forward(position=100, capture_frame=True)


    drone.land()
    drone.close()