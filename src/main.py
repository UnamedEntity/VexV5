import sys 
import vex
from vex import *
import math

brain = vex.Brain()

frontLeftMotor = vex.Motor(vex.Ports.PORT8, vex.GearSetting.RATIO_18_1, False)
frontRightMotor = vex.Motor(vex.Ports.PORT9, vex.GearSetting.RATIO_18_1, True)
backLeftMotor = vex.Motor(vex.Ports.PORT7, vex.GearSetting.RATIO_18_1, False)
backRightMotor = vex.Motor(vex.Ports.PORT6, vex.GearSetting.RATIO_18_1, True)
chainSaw = vex.Motor(vex.Ports.PORT10, vex.GearSetting.RATIO_18_1, True)

controller = vex.Controller(vex.ControllerType.PRIMARY)

def xDrive(forward, strafe, turn):

    fl = forward + strafe + turn
    fr = forward - strafe - turn
    bl = forward - strafe + turn
    br = forward + strafe - turn
    

    frontLeftMotor.spin(vex.DirectionType.REVERSE, fl, vex.VelocityUnits.PERCENT)
    frontRightMotor.spin(vex.DirectionType.REVERSE, fr, vex.VelocityUnits.PERCENT)
    backLeftMotor.spin(vex.DirectionType.REVERSE, bl, vex.VelocityUnits.PERCENT)
    backRightMotor.spin(vex.DirectionType.REVERSE, br, vex.VelocityUnits.PERCENT)

def chainsaw(turn):
    chainSaw.spin(vex.DirectionType.REVERSE, turn, vex.VelocityUnits.PERCENT)

while True:
    forward = controller.axis3.value() 
    strafe = controller.axis4.value()  
    turn = controller.axis1.value()
    xDrive(forward, strafe, turn)
    while controller.buttonA.pressing():
        chainsaw(100)
        forward = controller.axis3.value() 
        strafe = controller.axis4.value()  
        turn = controller.axis1.value()
        xDrive(forward, strafe, turn)
    while controller.buttonB.pressing():
        chainsaw(-100)
        forward = controller.axis3.value() 
        strafe = controller.axis4.value()  
        turn = controller.axis1.value()
        xDrive(forward, strafe, turn)
    chainsaw(0)
    
