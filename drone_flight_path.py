from drone import Drone


if __name__ == '__main__':
    drone = Drone(display=True)
    drone.enable_camera()
    drone.takeoff()

    # Moves forward 200cm || Will make up the new head_to_start function
    drone.move_forward(position=60)
    drone.move_forward(position=60)
    drone.move_forward(position=60)

    # Moves right 350cm || Will make up the new head_to_start function
    drone.move_right()
    drone.move_right()
    drone.move_right(position=75)

    with open('flight_path.txt', 'r') as file:
        while True:
            line = file.readline().strip()
            if drone.markerID == 10:
                print("MARKER FOUND!")
                # break
            elif line == "forward" or line == "f":
                drone.move_forward()
            elif line == "backward":
                drone.move_backward()
            elif line == "left":
                drone.move_left(position=75)
            elif line == "right":
                drone.move_right(position=75)
            elif not line:
                break
            else:
                print(f"THERE IS AN UNHANDLED INPUT WITHIN FLIGHT PATH: {line}")


    print(f"X: {drone.pos_x}, Y: {drone.pos_y}")

    drone.land()
    drone.close()