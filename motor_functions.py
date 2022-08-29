import RPi.GPIO as GPIO          
from time import sleep


##### Physical Pin Numbers on Raspberry Pi Zero #####
### Board 1 ###
# Motor 1
in1_1 = 16    # Input  1, Board 1
in2_1 = 18    # Input  2, Board 1
enA_1 = 12    # Enable A, Board 1

# Motor 2
in3_1 = 22    # Input  3, Board 1
in4_1 = 24    # Input  4, Board 1
enB_1 = 32    # Enable B, Board 1

### Board 2 ###
# Motor 3
in1_2 = 23    # Input  1, Board 2
in2_2 = 29    # Input  2, Board 2
enA_2 = 33    # Enable A, Board 2

# Motor 4
in3_2 = 31    # Input  3, Board 2
in4_2 = 37    # Input  4, Board 2
enB_2 = 35    # Enable B, Board 2
###############################

GPIO.setmode(GPIO.BOARD) # Use Physical Board Numbers (To use GPIO Pin Numbers use 'BCM')

### Set Pins as Outputs ###
GPIO.setup(in1_1,GPIO.OUT)
GPIO.setup(in2_1,GPIO.OUT)
GPIO.setup(enA_1,GPIO.OUT)

GPIO.setup(in3_1,GPIO.OUT)
GPIO.setup(in4_1,GPIO.OUT)
GPIO.setup(enB_1,GPIO.OUT)

GPIO.setup(in1_2,GPIO.OUT)
GPIO.setup(in2_2,GPIO.OUT)
GPIO.setup(enA_2,GPIO.OUT)

GPIO.setup(in3_2,GPIO.OUT)
GPIO.setup(in4_2,GPIO.OUT)
GPIO.setup(enB_2,GPIO.OUT)
##########################

### Set Input Pins to Low ###
GPIO.output(in1_1,GPIO.LOW)
GPIO.output(in2_1,GPIO.LOW)

GPIO.output(in3_1,GPIO.LOW)
GPIO.output(in4_1,GPIO.LOW)

GPIO.output(in1_2,GPIO.LOW)
GPIO.output(in2_2,GPIO.LOW)

GPIO.output(in3_2,GPIO.LOW)
GPIO.output(in4_2,GPIO.LOW)
##########################

### Set-up PWM ###
# Create PWM Objects
freq = 20 # Frequency of PWM
pA_1=GPIO.PWM(enA_1,freq)
pB_1=GPIO.PWM(enB_1,freq)
pA_2=GPIO.PWM(enA_2,freq)
pB_2=GPIO.PWM(enB_2,freq)

# Start PWM Generation of Specified Duty Cycle
duty_start = 0
pA_1.start(duty_start)
pB_1.start(duty_start)
pA_2.start(duty_start)
pB_2.start(duty_start)
########################

### Board 1 Direction Function ###
def direct_board1(direction):
    if direction == 1:
        GPIO.output(in1_1, GPIO.HIGH)
        GPIO.output(in2_1, GPIO.LOW)
        GPIO.output(in3_1, GPIO.HIGH)
        GPIO.output(in4_1, GPIO.LOW)
    elif direction == -1:
        GPIO.output(in1_1, GPIO.LOW)
        GPIO.output(in2_1, GPIO.HIGH)
        GPIO.output(in3_1, GPIO.LOW)
        GPIO.output(in4_1, GPIO.HIGH)
    elif direction == 0:
        GPIO.output(in1_1, GPIO.LOW)
        GPIO.output(in2_1, GPIO.LOW)
        GPIO.output(in3_1, GPIO.LOW)
        GPIO.output(in4_1, GPIO.LOW)

    return
#######################

### Board 2 Direction Function ###
def direct_board2(direction):
    if direction == 1:
        GPIO.output(in1_2, GPIO.HIGH)
        GPIO.output(in2_2, GPIO.LOW)
        GPIO.output(in3_2, GPIO.HIGH)
        GPIO.output(in4_2, GPIO.LOW)
    elif direction == -1:
        GPIO.output(in1_2, GPIO.LOW)
        GPIO.output(in2_2, GPIO.HIGH)
        GPIO.output(in3_2, GPIO.LOW)
        GPIO.output(in4_2, GPIO.HIGH)
    elif direction == 0:
        GPIO.output(in1_2, GPIO.LOW)
        GPIO.output(in2_2, GPIO.LOW)
        GPIO.output(in3_2, GPIO.LOW)
        GPIO.output(in4_2, GPIO.LOW)
    return
#######################

### Board 1 Speed Function ###
def set_speed_board1(duty):
    duty = min(duty, 100) # Ensure duty is <= 100
    duty = max(0, duty)   # Ensure duty is >= 0
    pA_1.ChangeDutyCycle(duty)
    pB_1.ChangeDutyCycle(duty)
    return
#######################

### Board 2 Speed Function ###
def set_speed_board2(duty):
    duty = min(duty, 100) # Ensure duty is <= 100
    duty = max(0, duty)   # Ensure duty is >= 0
    pA_2.ChangeDutyCycle(duty)
    pB_2.ChangeDutyCycle(duty)
    return
#######################

###

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("\n")    

GPIO.cleanup()  

