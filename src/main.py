import sys 
import vex
from vex import *
import math
 
#brain = vex.Brain()
#frontLeftMotor = vex.Motor(vex.Ports.PORT8, vex.GearSetting.RATIO_18_1, False)
#frontRightMotor = vex.Motor(vex.Ports.PORT9, vex.GearSetting.RATIO_18_1, True)
backLeftMotor = vex.Motor(vex.Ports.PORT7, vex.GearSetting.RATIO_36_1, False)
backRightMotor = vex.Motor(vex.Ports.PORT6, vex.GearSetting.RATIO_36_1, True)
chainSaw = vex.Motor(vex.Ports.PORT10, vex.GearSetting.RATIO_36_1, True)
cap = vex.Motor(vex.Ports.PORT11, vex.GearSetting.RATIO_6_1, True)
controller = vex.Controller(vex.ControllerType.PRIMARY)
reversed = vex.DirectionType.FORWARD


def xDrive(forward, strafe, turn, direction):
    fl = forward + strafe + turn
    fr = forward - strafe - turn
    bl = forward - strafe + turn
    br = forward + strafe - turn
    #frontLeftMotor.spin(direction, fl, vex.VelocityUnits.PERCENT)
    #frontRightMotor.spin(direction, fr, vex.VelocityUnits.PERCENT)
    backLeftMotor.spin(direction, bl, vex.VelocityUnits.PERCENT)
    backRightMotor.spin(direction, br, vex.VelocityUnits.PERCENT)

def chainsaw(turn):
    chainSaw.spin(vex.DirectionType.REVERSE, turn, vex.VelocityUnits.PERCENT)

def capturn(turn):
    cap.spin(vex.DirectionType.REVERSE, turn, vex.VelocityUnits.PERCENT)


while True:
    forward = controller.axis3.value() 
    strafe = controller.axis4.value()  
    turn = controller.axis1.value()
    xDrive(forward, strafe, turn, reversed)

    while controller.buttonA.pressing():
        chainsaw(100)
        forward = controller.axis3.value() 
        strafe = controller.axis4.value()  
        turn = controller.axis1.value()
        xDrive(forward, strafe, turn, reversed)
    while controller.buttonB.pressing():
        chainsaw(-100)
        forward = controller.axis3.value() 
        strafe = controller.axis4.value()  
        turn = controller.axis1.value()
        xDrive(forward, strafe, turn, reversed)
        
    while controller.buttonUp.pressing():
        capturn(100)
        forward = controller.axis3.value() 
        strafe = controller.axis4.value()  
        turn = controller.axis1.value()
        xDrive(forward, strafe, turn, reversed)

    while controller.buttonDown.pressing():
        capturn(100)
        forward = controller.axis3.value() 
        strafe = controller.axis4.value()  
        turn = controller.axis1.value()
        xDrive(forward, strafe, turn, reversed)

    if controller.buttonX.pressed:
        if reversed is vex.DirectionType.FORWARD:
            reversed = vex.DirectionType.REVERSE
        if reversed is vex.DirectionType.REVERSE:
            reversed = vex.DirectionType.FORWARD
    
    chainsaw(0)
    capturn(0)
    
