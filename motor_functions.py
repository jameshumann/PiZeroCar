import RPi.GPIO as GPIO          
from time import sleep

class motor:
    def __init__(self):
        ##### Physical Pin Numbers on Raspberry Pi Zero #####
        ### Board 1 ###
        # Motor 1
        self.in1_1 = 16    # Input  1, Board 1
        self.in2_1 = 18    # Input  2, Board 1
        self.enA_1 = 12    # Enable A, Board 1

        # Motor 2
        self.in3_1 = 22    # Input  3, Board 1
        self.in4_1 = 24    # Input  4, Board 1
        self.enB_1 = 32    # Enable B, Board 1

        ### Board 2 ###
        # Motor 3
        self.in1_2 = 23    # Input  1, Board 2
        self.in2_2 = 29    # Input  2, Board 2
        self.enA_2 = 33    # Enable A, Board 2

        # Motor 4
        self.in3_2 = 31    # Input  3, Board 2
        self.in4_2 = 37    # Input  4, Board 2
        self.enB_2 = 35    # Enable B, Board 2
        ###############################

    def setup_motors(self):
        GPIO.setmode(GPIO.BOARD) # Use Physical Board Numbers (To use GPIO Pin Numbers use 'BCM')

	### Set Pins as Outputs ###
        GPIO.setup(self.in1_1,GPIO.OUT)
        GPIO.setup(self.in2_1,GPIO.OUT)
        GPIO.setup(self.enA_1,GPIO.OUT)

        GPIO.setup(self.in3_1,GPIO.OUT)
        GPIO.setup(self.in4_1,GPIO.OUT)
        GPIO.setup(self.enB_1,GPIO.OUT)

        GPIO.setup(self.in1_2,GPIO.OUT)
        GPIO.setup(self.in2_2,GPIO.OUT)
        GPIO.setup(self.enA_2,GPIO.OUT)

        GPIO.setup(self.in3_2,GPIO.OUT)
        GPIO.setup(self.in4_2,GPIO.OUT)
        GPIO.setup(self.enB_2,GPIO.OUT)
        ##########################

        ### Set Input Pins to Low ###
        GPIO.output(self.in1_1,GPIO.LOW)
        GPIO.output(self.in2_1,GPIO.LOW)

        GPIO.output(self.in3_1,GPIO.LOW)
        GPIO.output(self.in4_1,GPIO.LOW)

        GPIO.output(self.in1_2,GPIO.LOW)
        GPIO.output(self.in2_2,GPIO.LOW)

        GPIO.output(self.in3_2,GPIO.LOW)
        GPIO.output(self.in4_2,GPIO.LOW)
        ##########################

        ### Set-up PWM ###
        # Create PWM Objects
        freq = 20 # Frequency of PWM
        self.pA_1=GPIO.PWM(self.enA_1,freq)
        self.pB_1=GPIO.PWM(self.enB_1,freq)
        self.pA_2=GPIO.PWM(self.enA_2,freq)
        self.pB_2=GPIO.PWM(self.enB_2,freq)

        # Start PWM Generation of Specified Duty Cycle
        duty_start = 0
        self.pA_1.start(duty_start)
        self.pB_1.start(duty_start)
        self.pA_2.start(duty_start)
        self.pB_2.start(duty_start)
        ########################

### Board 1 Direction Function ###
    def direct_board1(self, direction):
        if direction == 1:
            GPIO.output(self.in1_1, GPIO.HIGH)
            GPIO.output(self.in2_1, GPIO.LOW)
            GPIO.output(self.in3_1, GPIO.HIGH)
            GPIO.output(self.in4_1, GPIO.LOW)
        elif direction == -1:
            GPIO.output(self.in1_1, GPIO.LOW)
            GPIO.output(self.in2_1, GPIO.HIGH)
            GPIO.output(self.in3_1, GPIO.LOW)
            GPIO.output(self.in4_1, GPIO.HIGH)
        elif direction == 0:
            GPIO.output(self.in1_1, GPIO.LOW)
            GPIO.output(self.in2_1, GPIO.LOW)
            GPIO.output(self.in3_1, GPIO.LOW)
            GPIO.output(self.in4_1, GPIO.LOW)
        return
#######################

### Board 2 Direction Function ###
    def direct_board2(self, direction):
        if direction == 1:
            GPIO.output(self.in1_2, GPIO.HIGH)
            GPIO.output(self.in2_2, GPIO.LOW)
            GPIO.output(self.in3_2, GPIO.HIGH)
            GPIO.output(self.in4_2, GPIO.LOW)
        elif direction == -1:
            GPIO.output(self.in1_2, GPIO.LOW)
            GPIO.output(self.in2_2, GPIO.HIGH)
            GPIO.output(self.in3_2, GPIO.LOW)
            GPIO.output(self.in4_2, GPIO.HIGH)
        elif direction == 0:
            GPIO.output(self.in1_2, GPIO.LOW)
            GPIO.output(self.in2_2, GPIO.LOW)
            GPIO.output(self.in3_2, GPIO.LOW)
            GPIO.output(self.in4_2, GPIO.LOW)
        return
#######################

### Board 1 Speed Function ###
    def set_speed_board1(self, duty):
        duty = min(duty, 100) # Ensure duty is <= 100
        duty = max(0, duty)   # Ensure duty is >= 0
        self.pA_1.ChangeDutyCycle(duty)
        self.pB_1.ChangeDutyCycle(duty)
        print("setting motor1 duty: ", duty)
        #print(duty)
        return
#######################

### Board 2 Speed Function ###
    def set_speed_board2(self, duty):
        duty = min(duty, 100) # Ensure duty is <= 100
        duty = max(0, duty)   # Ensure duty is >= 0
        self.pA_2.ChangeDutyCycle(duty)
        self.pB_2.ChangeDutyCycle(duty)
        return
#######################
    def gpio_cleanup(self):
        GPIO.cleanup() 

    

### Test Commands ###
if(__name__=="__main__"):
    ###
    print("\n")
    print("The default speed & direction of motor is LOW & Forward.....")
    print("\n")
    
    mot = motor()
    mot.setup_motors()
    
    print("sending command to set board 1 to +1...\n")
    mot.direct_board1(1)
    sleep(3)
    print("sending command to move board 1 at speed of 50...\n")
    mot.set_speed_board1(50)
    sleep(3)
    print("sending command to set board 1 to -1...\n")
    mot.direct_board1(-1)
    sleep(3)
    print("sending command to move board 1 at speed of 100...\n")
    mot.set_speed_board1(100)
    sleep(3)
    print("sending command to stop moving board 1...\n")
    mot.set_speed_board1(0)
    
    mot.gpio_cleanup()

##print("sending command to set board 2 to -1...\n")
##direct_board2(-1)
##print("sending command to move board 2 at speed of 10...\n")
##set_speed_board2(10)
##sleep(3)
##print("sending command to stop moving board 2...\n")
##set_speed_board2(0)

 

