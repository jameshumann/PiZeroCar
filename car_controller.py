from email.policy import default
import subprocess
import threading
from time import sleep
import pygame
from motor_functions import motor
from leds import headlights, indicator_light

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
mot = motor()
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
CHECK_ON_OFF_HZ = 4
# HEADLIGHTS_HZ = 5

### Operating variables ### 
is_on = False
control_input = {'turn_on':False, 'turn_off':False, 'left_stick':0, 'right_stick':0}
mode = "BOOTUP" # ON, SHUTDOWN
###########################

def read_control_input():
    global control_input
    global mode
    hl = headlights()

    while(mode == "BOOTUP" or mode == "ON"):
        for event in pygame.event.get():
##            print(event)
            if(event.type == pygame.JOYAXISMOTION and event.__dict__['axis']==1):
##                print("Axis zeromoved")
##                print(event.__dict__['value'])
                control_input['left_stick'] = - event.__dict__['value']
            elif(event.type == pygame.JOYAXISMOTION and event.__dict__['axis']==3):
##                print("Axis 3 moved")
##                print(event.__dict__['value'])
                control_input['right_stick'] = - event.__dict__['value']
            elif(event.type == pygame.JOYBUTTONDOWN):
                # Buttons are A:0, B:1, X:3, Y:4
                # print("button depressed")
                # print(event)
                # print(type(event))
                if(event.button == 0):
                    if(mode == "BOOTUP"):
                        mode = "ON"
                    elif(mode == "ON"):
                        mode = "SHUTDOWN"
                elif(event.button == 3):
                    hl.toggle()
        print("MODE is ", mode)
        sleep(1/READ_HZ)

def send_motor_cmd():
    global control_input
##    print("SEND MOTOR COMMAND LEFT = " + str(control_input['left_stick']))
##    print("SEND MOTOR COMMAND RIGHT = " + str(control_input['right_stick']))
    while(mode == "BOOTUP"):
        sleep(0.1)

    while(mode == "ON"):
##        print("dummy motor command")
##        print("Commands R/L: " + str(control_input['right_stick']) + " " + str(conrol_input['left_stick']))
##        print("SEND MOTOR COMMAND LEFT = " + str(control_input['left_stick']))
##        print("SEND MOTOR COMMAND RIGHT = " + str(control_input['right_stick']))
        if(control_input['right_stick'] < 0): #Right stick is right motor board is board 1
            mot.direct_board1(-1)
        elif(control_input['right_stick'] == 0):
            mot.direct_board1(0)
        elif(control_input['right_stick'] > 0):
            mot.direct_board1(1)
        mot.set_speed_board1(100*abs(control_input['right_stick']))
        
        if(control_input['left_stick'] < 0): #Left stick is left motor board is board 2
            mot.direct_board2(-1)
        elif(control_input['left_stick'] == 0):
            mot.direct_board2(0)
        elif(control_input['left_stick'] > 0):
            mot.direct_board2(1)
        mot.set_speed_board2(100*abs(control_input['left_stick']))
                           
        
        sleep(1/MOTOR_CMD_HZ)

def indicate():
    indi = indicator_light()
    while(mode == "BOOTUP"):
        indi.flash_num(3,0.25)
        sleep(0.5)
    while(mode == "ON"):
        indi.stay_on()
    while(mode == "OFF"):
        indi.flash_num(10, 0.1)
        sleep(0.5)
    


t_read = threading.Thread(group=None, target=read_control_input)
##t_check = threading.Thread(group = None, target = check_on_off)
t_cmd = threading.Thread(group = None, target = send_motor_cmd)
t_ind = threading.Thread(group = None, target = indicate)

t_read.start()
#t_check.start()
t_cmd.start()
t_ind.start()

t_read.join()
t_cmd.join()

subprocess.run(["shutdown", "-h", "now"])