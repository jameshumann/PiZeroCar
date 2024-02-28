import RPi.GPIO as GPIO          
from time import sleep

class headlights():
    def __init__(self, gpio_pin = 36):
        ##### Physical Pin Numbers on Raspberry Pi Zero #####
        self.output_pin = gpio_pin
        self.mode = GPIO.LOW

        GPIO.setmode(GPIO.BOARD) # Use Physical Board Numbers (To use GPIO Pin Numbers use 'BCM')

	    ### Set Pins as Outputs ###
        GPIO.setup(self.output_pin, GPIO.OUT)

        self.refresh()

    def turn_headlights_on(self):
        self.mode = GPIO.HIGH
        self.refresh()

    def turn_headlights_off(self):
        self.mode = GPIO.LOW
        self.refresh()

    def toggle(self):
        if(self.mode == GPIO.LOW):
            self.mode = GPIO.HIGH
        else:
            self.mode = GPIO.LOW
        self.refresh()
        
    def refresh(self):
        GPIO.output(self.output_pin, self.mode)

class indicator_light():
    def __init__(self, gpio_pin = 13):
        ##### Physical Pin Numbers on Raspberry Pi Zero #####
        self.output_pin = gpio_pin
        # self.mode = GPIO.LOW
        GPIO.setmode(GPIO.BOARD) # Use Physical Board Numbers (To use GPIO Pin Numbers use 'BCM')

	    ### Set Pins as Outputs ###
        GPIO.setup(self.output_pin, GPIO.OUT)
        GPIO.output(self.output_pin, GPIO.LOW)
        # self.refresh()

    def stay_on(self):
        GPIO.output(self.output_pin, GPIO.HIGH)

    def flash_num(self, times, period):# = 0.25):
        """
        Flashes on for period/2 and off for period/2, times times
        """
        # length = (duration * 0.98) / times / 2
        for i in range(times):
            GPIO.output(self.output_pin, GPIO.HIGH)
            sleep(period/2)
            GPIO.output(self.output_pin, GPIO.LOW)
            sleep(period/2)

    # def turn_headlights_off(self):
    #     self.mode = GPIO.LOW
    #     self.refresh()

    # def refresh(self):
    #     GPIO.output(self.output_pin, self.mode)

        