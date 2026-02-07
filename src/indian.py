
'''#OLD CODE
    #example turn right 90 degrees
  #  while Inertial_sensor.heading () < 90:
   #     left_drive.spin(FORWARD, 80, RPM)
#        right_drive.spin(REVERSE, 80, RPM)
    #left_drive.stop()
   # right_drive.stop()

    #THE DEBUG OUTPUT
    #brain.screen.print(Inertial_sensor.heading())

from vex import *

#initialize the brain
brain = Brain()

# Initialize les motors
left_drive =MotorGroup(Ports.PORT1, Ports.PORT2, Ports.PORT3)
right_drive =MotorGroup(Ports.PORT4, Ports.PORT5, Ports.PORT6) 

#initialize the drivetrain
drivetrain=DriveTrain(left_drive, right_drive, 319.19, 320, 40, MM, 1)

intake_motor = Motor(Ports.PORT8)
output_motor = Motor(Ports.PORT9)
Inertial_sensor = Inertial(Ports.PORT7)

def autonomous (): #calibrate the inertial sensor
    Inertial_sensor.calibrate()
    while Inertial_sensor.is_calibrating():
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
    #intake_motor.stop() #stop the intake'''

from vex import *

# ================== Brain ==================
brain = Brain()

# ================== Drivetrain Motors ==================
# (Created ONCE — used by both auton and driver)

left_drive = MotorGroup(
    Motor(Ports.PORT1,True),
    Motor(Ports.PORT2,True),
    Motor(Ports.PORT3,True)
)

right_drive = MotorGroup(
    Motor(Ports.PORT4),
    Motor(Ports.PORT5),
    Motor(Ports.PORT6)
)



# ================== DRIVER CODE ALIASES (ADDED) ==================
# These names are REQUIRED by the driver code.
# DO NOT REMOVE.

motor_group_1 = left_drive
motor_group_2 = right_drive

# ================== Other Motors & Sensors ==================
intake_motor = Motor(Ports.PORT8)
output_motor = Motor(Ports.PORT9)

# DRIVER CODE EXPECTS THESE NAMES TOO
motor_intake_1 = intake_motor
motor_intake_2 = output_motor

Inertial_sensor = Inertial(Ports.PORT7)

# ================== Drivetrain Object ==================
drivetrain = SmartDrive(motor_group_1,motor_group_2,Inertial_sensor)

# ================== Autonomous ==================
def darealauton():

    # Calibrate inertial
    Inertial_sensor.calibrate()
    while Inertial_sensor.is_calibrating():
        wait(20, MSEC)

    # --------- SECTOR 1: MIDGOAL ---------
    drivetrain.drive_for(FORWARD, 1219, MM, 190, RPM)
    
    
    # --------- SECTOR 2: DISPENSER ---------
    drivetrain.drive_for(REVERSE, 609.6, MM, 190, RPM)
    drivetrain.turn_for(90, DEGREES)
    drivetrain.drive_for(FORWARD, 609.6, MM, 190, RPM)
    drivetrain.turn_for(180, DEGREES)
    drivetrain.drive_for(FORWARD, 609.6, MM, 190, RPM)

    wait(3000, MSEC)

    # --------- SECTOR 3: LONG GOAL ---------
    drivetrain.drive_for(REVERSE, 1219, MM, 190, RPM)
