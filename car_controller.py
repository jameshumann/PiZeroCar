from email.policy import default
import threading
from time import sleep

# Board setup
LEFT_PWM_PIN = 15
RIGHT_PWM_PIN = 22
ON_OFF_PIN = 12

# Control setup
READ_HZ = 50
MOTOR_CMD_HZ = 20
CHECK_ON_OFF_HZ = 5

### Operating variables ### 
is_on = False
control_input = {}
###########################

def read_control_input():
    pass

def check_on_off():
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

def send_motor_cmd():
    pass

t_read = threading.Timer(1/READ_HZ, read_control_input)
t_check = threading.Timer(1/CHECK_ON_OFF_HZ, check_on_off)
t_cmd = threading.Timer(1/MOTOR_CMD_HZ, send_motor_cmd)
