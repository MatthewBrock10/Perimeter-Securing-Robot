#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from time import sleep
import random


# Initialisation.
ev3 = EV3Brick()
ultrasonic = UltrasonicSensor(Port.S2)
colour = ColorSensor(Port.S3)
pickup_motor = Motor(Port.A, Direction.CLOCKWISE)
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
wheel_diameter = 56
axle_track = 118
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
distance_to_bomb = 0

# Function Definitions
# Bomb pickup
def pickup_bomb():
    robot.drive_time(50,0,2000)
    pickup_motor.run_target(30,130)
    robot.drive_time(20,0,4500)
    pickup_motor.run_target(30,30)
# Bomb dropoff and backing away
def drive_dropoff_bomb():
    robot.drive_time(50,-15,3000)
    robot.drive_time(50,0,2000)
    pickup_motor.run_target(100,125)
    rnum = random.randrange(1,5)
    if rnum == 1:
        ev3.speaker.say("Matthew Brock sends his regards")
    elif rnum == 2:
        ev3.speaker.say("Execute order 66")
    elif rnum == 3:
        ev3.speaker.say("There's always a bigger fish")
    elif rnum == 4:
        ev3.speaker.say("It's over Anakin, I have the high ground")
    elif rnum == 5:
        ev3.speaker.say("Asta la vista baby")
    robot.drive_time(-40,0,1500)
    pickup_motor.run_target(200,0)
    robot.drive_time(-50,15,3000)
    robot.drive_time(-100,0,2000)   
# Testing if it has picked up a bomb or not
def find_and_move_bomb():
    pickup_bomb()
    if colour.color() != None:
        ev3.speaker.say("It's a trap")
        drive_dropoff_bomb()
    else:
        ev3.speaker.say("These are not the droids you are looking for")
        robot.turn(90)
        pickup_motor.run_target(100,0)

# Main Program.
ev3.speaker.say("I am See-Threepio, human-cyborg relations")
distance_driven = 0
counter = 0
while(counter < 5):
    # Drive forward until something is detected
    if ultrasonic.distance() > 229:
        robot.drive_time(100,0,100)
        distance_driven = distance_driven + 100
        if(distance_driven > 7999):
            counter = counter + 1
            robot.turn(90)
            distance_driven=0
    else:
        ev3.speaker.say("It will be done my lord")
        find_and_move_bomb()
ev3.speaker.say("Perimeter cleared")