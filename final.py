

from dronekit import connect, VehicleMode, LocationGlobalRelative
from pymavlink import mavutil
import time
import argparse

from pyzbar.pyzbar import decode
import cv2
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--connect', default='127.0.0.1:14550')
args = parser.parse_args()



# Connect to the Vehicle
print
'Connecting to vehicle on: %s' % args.connect
vehicle = connect(args.connect, baud=57600, wait_ready=True)


# Function to arm and then takeoff to a user specified altitude
def arm_and_takeoff(aTargetAltitude):


print
"Basic pre-arm checks"
# Don't let the user try to arm until autopilot is ready
while not vehicle.is_armable:
    print
    " Waiting for vehicle to initialise..."
time.sleep(1)

print
"Arming motors"

# Copter should arm in GUIDED mode
vehicle.mode = VehicleMode("GUIDED")
vehicle.armed = True

while not vehicle.armed:
    print
    " Waiting for arming..."
time.sleep(1)

print
"Taking off!"
vehicle.simple_takeoff(aTargetAltitude)
# Take off to target altitude and altitide is in meters


# Check that vehicle has reached takeoff altitude
while True:
    print
    " Altitude: ", vehicle.location.global_relative_frame
# Break and return from function just below target altitude

if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
    print
    "Reached target altitude"
break
time.sleep(1)

# Initialize the takeoff sequence to 6m
arm_and_takeoff(6)

print("Take off complete")

if barcodeReader= 2:
   print("Now let's land")

   vehicle.mode = VehicleMode("LAND")

elif:
  time.sleep(10)
  vehicle.mode = VehicleMode("LAND")


vehicle.close()



def barcodeReader(image, bgr):
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


barcodes = decode(gray_img)


for decodedObject in barcodes:
    points = decodedObject.polygon

    pts = np.array(points, np.int32)
    pts = pts.reshape((-1, 1, 2))
cv2.polylines(image, [pts], True, (0, 255, 0), 3)

for bc in barcodes:
    cv2.putText(frame, bc.data.decode("utf-8") + " - " + bc.type, (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, bgr, 2)

return "Barcode: {} - Type: {}".format(bc.data.decode("utf-8"), bc.type)

bgr = (8, 70, 208)




cap = cv2.VideoCapture(0)
while (True):
    ret, frame = cap.read()
barcode = barcodeReader(frame, bgr)
print(barcode)
cv2.imshow('Barcode reader', frame)
code = cv2.waitKey(10)
if code == ord('q'):
    break
