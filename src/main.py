# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       levyz                                                        #
# 	Created:      1/12/2026, 5:12:55 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

brain = Brain()
 # Setting up motors and controller

# Left side motors
motor_1a = Motor(Ports.PORT1)
motor_2a = Motor(Ports.PORT2)
motor_3a = Motor(Ports.PORT3)
    
# Right side motors
motor_1b = Motor(Ports.PORT4)
motor_2b = Motor(Ports.PORT5)
motor_3b = Motor(Ports.PORT6)
    
# Initalize motor groups
motor_group_1 = MotorGroup(motor_1a, motor_2a, motor_3a)
motor_group_2 = MotorGroup(motor_1b, motor_2b, motor_3b)
motor_intake_1 = Motor(Ports.PORT8)
motor_intake_2 = Motor(Ports.PORT9)

#Initialize controller
controller_1 = Controller()

# Initialize DT
drivetrain = DriveTrain(motor_group_1, motor_group_2)

# Initialize inertial sensor
inertial_1 = Inertial(Ports.PORT7)

brain.screen.print("Hello Vex World!")

def user_control():
    # Varianble for speed
    speed_wheels = 50
    speed_ramp = 200
    # Setting up controller for user control portion
    while True:
        wait(20,MSEC)
        brain.screen.clear_screen()
        # brain.screen.print("driver control")
        # Setting up controller for user control portion
        
        # Left motor group
        if controller_1.buttonUp.pressing():
            motor_group_1.spin(REVERSE,speed_wheels,PERCENT)
        elif controller_1.buttonDown.pressing():
            motor_group_1.spin(FORWARD,speed_wheels,PERCENT)
        else:
            motor_group_1.stop()

        # Right motor group
        if controller_1.buttonX.pressing():
            motor_group_2.spin(FORWARD,speed_wheels,PERCENT)
        elif controller_1.buttonB.pressing():
            motor_group_2.spin(REVERSE,speed_wheels,PERCENT)
        else:
            motor_group_2.stop()

        # Intake pull
        if controller_1.buttonR1.pressing():
            motor_intake_1.spin(FORWARD,speed_ramp,PERCENT)
        elif controller_1.buttonR2.pressing():
            motor_intake_1.spin(REVERSE,speed_ramp,PERCENT)
        else:
            motor_intake_1.stop()

        # Intake discharge
        if controller_1.buttonL1.pressing():
            motor_intake_2.spin(REVERSE,speed_ramp,PERCENT)
        elif controller_1.buttonL2.pressing():
            motor_intake_2.spin(FORWARD,speed_ramp,PERCENT)
        else:
            motor_intake_2.stop()
        
        # Speed Modification
        if controller_1.axis2.position() > 10 and speed_wheels < 600:
            speed_wheels += 5
        elif controller_1.axis2.position() < -10 and speed_wheels > 0:
            speed_wheels -= 5
        if controller_1.axis3.position() > 10 and speed_ramp < 200:
            speed_ramp += 5
        elif controller_1.axis3.position() < -10 and speed_ramp > 0:
            speed_ramp -= 5
        


        brain.screen.set_cursor(8,12)
        brain.screen.print(speed_wheels)
        brain.screen.set_cursor(8,15)
        brain.screen.print(": Wheel Speed")
        brain.screen.set_cursor(9,12)
        brain.screen.print(speed_ramp)
        brain.screen.set_cursor(9,15)
        brain.screen.print(": Ramp Speed")

def autonomous(): #calibrate the inertial sensor
    inertial_1.calibrate()
    while inertial_1.is_calibrating():
        wait(20, MSEC)

    #new CODE              
    #                      !FIRST SECTOR!
    #-------------SECTOR 1: GO TO MIDGOAL AND INTAKE 3 BALLS----------------
    #Note: 
    #intake_motor.spin(FORWARD, 100, RPM) #start the intake
    drivetrain.drive_for(FORWARD, 1219, MM, 190,RPM) #drive forward 4 feet
    #intake_motor.stop() #stop the intake after reaching the 3 balls near the midgoal

    #-------------SECTOR 2:  APPRACHING THE DISPENSER AND INTAKING 3 BALLS ----------------

    drivetrain.drive_for(REVERSE, 609.6, MM, 190, RPM) #drive backward 2 feet
    drivetrain.turn_for(90, DEGREES) #turn to face 90 degrees 
    drivetrain.drive_for(FORWARD, 609.6, MM, 190,RPM) #drive towards, between the long goal and the dispenser
    drivetrain.turn_for(180, DEGREES) #turn to face 90 degrees  
    #WE DONT KNOW THE RATE OF SPEED OF THE INTAKE AND OUTPUT SYSTEM YET! So for now it is commented out 
    #  intake_motor.spin(FORWARD, 100, RPM) #start the intake
    drivetrain.drive_for(FORWARD, 609.6, MM, 190, RPM) #drive towards the dispenser
    wait(3000, MSEC) #wait 3000 miliseconds (3 sec) to intake the balls
    #intake_motor.stop() #stop the intake after reaching the dispenser

    #                                 !FINAL SECTOR!
    #---------------SECTOR 3: GO TO LONG GOAL AND OUTPUT 6 BALLS ----------------

    drivetrain.drive_for(REVERSE, 1219, MM,190, RPM) #drive backward from the dispenser straight to the long goal
    #output_motor.spin(FORWARD, 100, RPM) #start the output to shoot the balls into the long goal
    #intake_motor.spin(FORWARD, 100, RPM) #start the intake to help push the balls into the long goa
    #wait(1500, MSEC) #wait 1.5 seconds to output the balls into the long goal
    #output_motor.stop() #stop the output
    #intake_motor.stop() #stop the intake



# create competition instance
comp = Competition(user_control, autonomous)

# actions to do when the program starts
brain.screen.clear_screen()