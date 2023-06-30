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

    tl_drone.close()

