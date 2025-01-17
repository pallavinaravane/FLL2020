#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, MoveTank, MoveSteering
from ev3dev2.motor import LargeMotor, SpeedPercent
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from time import sleep, time
import math
from BasicFunctions import *
import Constants
from sys import stderr
# from ev3dev.ev3 import *
# import ev3dev.fonts as fonts

robot = MoveSteering(OUTPUT_A, OUTPUT_B)
colorLeft = ColorSensor(INPUT_1)
colorRight = ColorSensor(INPUT_3)
motorA = LargeMotor(OUTPUT_A)
motorD = LargeMotor(OUTPUT_D)
motorC = LargeMotor(OUTPUT_C)

motorC.off(brake=True)
motorD.off(brake=True)

Constants.STOP = False

GyroDrift()

show_text("Robot Run 2")

acceleration(degrees=DistanceToDegree(70), finalSpeed=50, steering=2)
while colorLeft.reflected_light_intensity > 10 and False == Constants.STOP:
    robot.on(steering=2, speed=20)
robot.off()

acceleration(degrees=DistanceToDegree(13), finalSpeed=20, steering=2)

while colorLeft.reflected_light_intensity < Constants.WHITE and False == Constants.STOP:
    #robot.on_for_degrees(speed=20, steering = 0, degrees = DistanceToDegree(2))
    #print("RobotRun2 stop=" + str(Constants.STOP), file=stderr)
    MoveForwardWhite(distanceInCm=2)
    robot.on_for_degrees(degrees=DistanceToDegree(0.75), steering=2, speed=-10)
robot.off()

counter = 0
while counter < 5 and False == Constants.STOP:
    robot.on_for_degrees(speed=20, steering = 0, degrees = DistanceToDegree(2))
    robot.on_for_degrees(degrees=DistanceToDegree(0.75), steering=2, speed=-10)
    counter += 1
robot.off()

accelerationMoveBackward(degrees=DistanceToDegree(10), steering=-15, finalSpeed=-20)
GyroTurn(steering=-100, angle=40)
acceleration(degrees=DistanceToDegree(10.5), finalSpeed=20)
while colorRight.reflected_light_intensity < Constants.WHITE and False == Constants.STOP:
    robot.on(speed=10, steering=0)
robot.off()
acceleration(degrees=DistanceToDegree(2), finalSpeed=20)
GyroTurn(steering=-100, angle=45)

# wall square
robot.on_for_seconds(steering=5, speed=-10, seconds=2)

acceleration(degrees=DistanceToDegree(55), finalSpeed=30, steering=1)
#lineFollowPID(degrees=DistanceToDegree(40), kp=1.25, ki=0.01, kd=5, color=ColorSensor(INPUT_3))
lineSquare()

acceleration(degrees=DistanceToDegree(20), finalSpeed=30, steering=-2)
motorC.on_for_seconds(speed=-20, seconds=0.5, brake=False)
motorC.on_for_degrees(speed=20, degrees=7, brake=True)
accelerationMoveBackward(degrees=DistanceToDegree(20), finalSpeed=30)

lineSquare()

GyroTurn(steering=-45, angle=85)
acceleration(degrees=DistanceToDegree(3.5), finalSpeed=10)
GyroTurn(steering=-50, angle=15)
acceleration(degrees=DistanceToDegree(5), finalSpeed=10)
accelerationMoveBackward(degrees=DistanceToDegree(1.5), finalSpeed=10)
motorC.on_for_seconds(speed=10, seconds=0.5, brake=True)
acceleration(degrees=DistanceToDegree(2), finalSpeed=10)
motorC.on_for_seconds(speed=10, seconds=0.2, brake=False)
acceleration(degrees=DistanceToDegree(7), finalSpeed=10)

motorC.on_for_seconds(speed=10, seconds=0.2, brake=True)

exit()

accelerationMoveBackward(degrees=DistanceToDegree(2), finalSpeed=30)
GyroTurn(steering=100, angle=35)

acceleration(degrees=DistanceToDegree(30), finalSpeed=30, steering=5)
GyroTurn(angle=15, steering=-50)
lineSquare()

motorD.on_for_seconds(speed=-10, seconds=0.2, brake=False)
motorC.on_for_seconds(speed=-10, seconds=0.2, brake=False)

GyroTurn(angle=35, steering=50)
acceleration(degrees=DistanceToDegree(17), finalSpeed=30)

accelerationMoveBackward(degrees=DistanceToDegree(1), finalSpeed=10)
motorC.on_for_seconds(speed=10, seconds=0.5, brake=True)
accelerationMoveBackward(degrees=DistanceToDegree(0.5), finalSpeed=10)
motorC.on_for_seconds(speed=10, seconds=0.5, brake=True)
acceleration(degrees=DistanceToDegree(2), finalSpeed=10)
motorC.on_for_degrees(speed=20, degrees=40, brake=True)
accelerationMoveBackward(degrees=DistanceToDegree(10), finalSpeed=10)

GyroTurn(angle=40, steering=-50)
acceleration(degrees=DistanceToDegree(70), finalSpeed=100)
motorC.off(brake=False)
motorD.off(brake=False)

