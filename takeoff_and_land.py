from dronekit import connect, VehicleMode, LocationGlobalRelative
from pymavlink import mavutil
import time

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--connect', default='127.0.0.1:14550')
args = parser.parse_args()


print
'Connecting to vehicle on: %s' % args.connect
vehicle = connect(args.connect, baud=57600, wait_ready=True)



def arm_and_takeoff(aTargetAltitude):
    print
    "Basic pre-arm checks"

    while not vehicle.is_armable:
        print
        " Waiting for vehicle to initialise..."
        time.sleep(1)

    print
    "Arming motors"

    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        print
        " Waiting for arming..."
        time.sleep(1)

    print
    "Taking off!"
    vehicle.simple_takeoff(aTargetAltitude)


    while True:
        print
        " Altitude: ", vehicle.location.global_relative_frame.alt

        if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
            print
            "Reached target altitude"
            break
        time.sleep(1)



arm_and_takeoff(20)

print("Take off complete")


time.sleep(10)

print("Now let's land")
vehicle.mode = VehicleMode("LAND")


vehicle.close()