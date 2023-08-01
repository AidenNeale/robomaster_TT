from drone import Drone


if __name__ == '__main__':
    drone = Drone(display=True)
    drone.enable_camera()
    drone.takeoff()

    # Moves forward 200cm || Will make up the new head_to_start function
    drone.move_forward()
    drone.move_forward()
    drone.move_forward()
    drone.move_forward()
    drone.move_forward()

    # Moves right 300cm || Will make up the new head_to_start function
    drone.move_right()
    drone.move_right()
    drone.move_right()
    drone.move_right()
    drone.move_right()
    drone.move_right()
    
    x = 0
    y = 0

    with open('flight_path.txt', 'r') as file:
        while True:
            line = file.readline().strip()
            if line == "forward":
                drone.move_forward()
            elif line == "backward":
                drone.move_backward()
            elif line == "left":
                drone.move_left()
            elif line == "right":
                drone.move_right()
            elif not line:
                break
            else:
                print(f"THERE IS AN UNHANDLED INPUT WITHIN FLIGHT PATH: {line}")

    print(f"X: {drone.pos_x}, Y: {drone.pos_y}")