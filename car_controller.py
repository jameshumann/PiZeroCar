from email.policy import default
import threading
from time import sleep
import pygame
import motor_functions as mot

# Switch input to controller
print("Swap out keyboard for gamepad in 5 sec")
sleep(1.00)
print("4 sec")
sleep(1.00)
print("3 sec")
sleep(1.00)
print("2 sec")
sleep(1.00)
print("1 sec")
sleep(1.00)

# Set up motors
print("Initializing motors")
mot.setup_motors()
sleep(3)

# Gamepad setup
print("Initializing gamepad")
pygame.init()
pygame.joystick.init()
print("Num joysticks connected:")
print(pygame.joystick.get_count())
pygame.joystick.Joystick(0).init()

# Board setup
LEFT_PWM_PIN = 15
RIGHT_PWM_PIN = 22
ON_OFF_PIN = 12

# Control setup
READ_HZ = 10
MOTOR_CMD_HZ = 10
CHECK_ON_OFF_HZ = 2

### Operating variables ### 
is_on = False
control_input = {'turn_on':False, 'turn_off':False, 'left_stick':0, 'right_stick':0}
###########################

def read_control_input():
    global control_input
    while(True):
        for event in pygame.event.get():
##            print(event)
            if(event.type == pygame.JOYAXISMOTION and event.__dict__['axis']==1):
                print("Axis zeromoved")
                print(event.__dict__['value'])
                control_input['left_stick'] = - event.__dict__['value']
            elif(event.type == pygame.JOYAXISMOTION and event.__dict__['axis']==3):
                print("Axis 3 moved")
                print(event.__dict__['value'])
                control_input['right_stick'] = - event.__dict__['value']
        sleep(1/READ_HZ)

def check_on_off():
    global is_on
    global control_input
    while(True):
        inp_on = control_input['turn_on'] #.get('turn_on')
        inp_off = control_input['turn_off'] #.get('turn_off')
        if(not is_on and inp_on):
            sleep(1)
            if(inp_on):
                is_on = True

        if(is_on and inp_off):
            sleep(1)
            if(inp_off):
                is_on = False
        sleep(1/CHECK_ON_OFF_HZ)

def send_motor_cmd():
    global control_input
##    print("SEND MOTOR COMMAND LEFT = " + str(control_input['left_stick']))
##    print("SEND MOTOR COMMAND RIGHT = " + str(control_input['right_stick']))
    while(True):
##        print("dummy motor command")
##        print("Commands R/L: " + str(control_input['right_stick']) + " " + str(conrol_input['left_stick']))
##        print("SEND MOTOR COMMAND LEFT = " + str(control_input['left_stick']))
##        print("SEND MOTOR COMMAND RIGHT = " + str(control_input['right_stick']))
        if(control_input['right_stick'] < 0): #Right stick is right motor board is board 1
            mot.direct_board1(-1)
        elif(control_input['right_stick'] == 0):
            mot.direct_board1(0)
        else:
            mot.direct_board1(1)
        mot.set_speed_board1(100*abs(control_input['right_stick']))
                           
        
        sleep(1/MOTOR_CMD_HZ)

t_read = threading.Thread(group=None, target=read_control_input)
##t_check = threading.Thread(group = None, target = check_on_off)
t_cmd = threading.Thread(group = None, target = send_motor_cmd)

t_read.start()
#t_check.start()
t_cmd.start()