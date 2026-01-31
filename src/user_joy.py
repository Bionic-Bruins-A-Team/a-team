brain = Brain()
# Motor Definition

# Right
motor_1b = Motor(vex.Ports.PORT4)
motor_2b = Motor(vex.Ports.PORT5)
motor_3b = Motor(vex.Ports.PORT6)

# Left
motor_1a = Motor(vex.Ports.PORT1)
motor_2a = Motor(vex.Ports.PORT2)
motor_3a = Motor(vex.Ports.PORT3)

# Motor Groups
motor_group_1 = MotorGroup(motor_1a, motor_2a, motor_3a)
motor_group_2 = MotorGroup(motor_1b, motor_2b, motor_3b)

# Controller
controller_1 = vex.Controller()

def user_joy():
    brain.screen.clear_screen()
    brain.screen.print("driver control")
    # Setting up controller for user control portion
    while True:
        wait(20, MSEC)
        if controller_1.axis3.position() > 10:
            motor_group_1.spin()