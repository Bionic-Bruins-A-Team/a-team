from vex import *

# Brain
brain = Brain()

# Motor Definition

# Right Motors
motor_1b = Motor(Ports.PORT4)
motor_2b = Motor(Ports.PORT5)
motor_3b = Motor(Ports.PORT6)

# Left Motors
motor_1a = Motor(Ports.PORT1)
motor_2a = Motor(Ports.PORT2)
motor_3a = Motor(Ports.PORT3)

# Motor Groups
motor_group_1 = MotorGroup(motor_1a, motor_2a, motor_3a)
motor_group_2 = MotorGroup(motor_1b, motor_2b, motor_3b)

# Intake Motors
motor_intake_1 = Motor(Ports.PORT8)
motor_intake_2 = Motor(Ports.PORT9)

# Controller
controller_1 = Controller()

brain.screen.clear_screen()
brain.screen.print("driver control")

# User control function setting up controller and handling buttons
def user_control():
    # Setting up controller for user control portion
    while True:
        wait(20,MSEC)
        brain.screen.clear_screen()
        brain.screen.print("driver control")
        # Setting up controller for user control portion
        
        # Left motor group
        if controller_1.buttonUp.pressing():
            motor_group_1.spin(FORWARD,60,PERCENT)
        elif controller_1.buttonDown.pressing():
            motor_group_1.spin(REVERSE,60,PERCENT)
        else:
            motor_group_1.stop()

        # Right motor group
        if controller_1.buttonX.pressing():
            motor_group_2.spin(FORWARD,60,PERCENT)
        elif controller_1.buttonB.pressing():
            motor_group_2.spin(REVERSE,60,PERCENT)
        else:
            motor_group_2.stop()

        # Intake pull
        if controller_1.buttonR1.pressing():
            motor_intake_1.spin(FORWARD,60,PERCENT)
        elif controller_1.buttonR2.pressing():
            motor_intake_1.spin(REVERSE,60,PERCENT)
        else:
            motor_intake_1.stop()

        # Intake discharge
        if controller_1.buttonL1.pressing():
            motor_intake_2.spin(FORWARD,60,PERCENT)
        elif controller_1.buttonL2.pressing():
            motor_intake_2.spin(REVERSE,60,PERCENT)
        else:
            motor_intake_2.stop()
