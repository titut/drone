import time
from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
import tkinter as tk

vehicle = connect('com4', wait_ready=True, baud=57600)
print('Connected!')

def arm_and_takeoff(aTargetAltitude):
    print("Basic pre-arm checks:")
    #Don't try to arm until autopilot is ready
    while not vehicle.is_armable:
        print("Waiting for vehicle to initialize...")
        time.sleep(1)
    
    print("Arming motors:")
    #Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    #Confirm vehicle armed before attempting to take off
    while not vehicle.armed:
        print("Waiting for arming...")
        time.sleep(1)

    print("Taking off!")
    vehicle.simple_takeoff(aTargetAltitude) # Take off to certain altitude

    while True:
        print("Alittude:", vehilce.location.global_relative_frame.alt)
        if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95:
            print "Reached target altitude"
            break
        time.sleep(1)

#Fly 2 meters
arm_and_takeoff(2)

print("Takeoff complete...")

#Hover 5 seconds
time.sleep(5)

print("Landing...")
vehicle.mode = VehicleMode("LAND")

#Disconnect from vehicle
vehicle.close()