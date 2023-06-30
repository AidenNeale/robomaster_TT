import time

import robomaster
from robomaster import robot


if __name__ == '__main__':
    robomaster.enable_logging_to_file() # Enable this if program breaks
    tl_drone = robot.Drone()

    robomaster.config.LOCAL_IP_STR = '192.168.10.2'

    tl_drone.initialize(conn_type='ap')

    version = tl_drone.get_sdk_version()
    print(f"Drone SDK Version: {tl_drone.get_sdk_version()}")

    print(f"Serial Number: {tl_drone.get_sn()}")

    print(f"Drone Version: {tl_drone.get_drone_version()}")

    tl_led = tl_drone.led
    tl_led.set_led(r=0, g=0, b=0)

    rgb_list = [(100, 100, 100), (255, 255, 255), (255, 0, 0), (0, 0, 255),
                (0, 255, 0), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

    for rgb_info in rgb_list:
        tl_led.set_led(r=rgb_info[0], g=rgb_info[1], b=rgb_info[2])
        time.sleep(0.5)

    tl_drone.close()

