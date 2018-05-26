import RPi.GPIO as GPIO
import time

TRIG = 23
ECHO = 24

class UltraSonic:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)
        GPIO.output(TRIG, False)

    '''
    def __del__(self):
        GPIO.cleanup()
    '''

    def distance(self):
        GPIO.output(TRIG, True)
    	time.sleep(0.00001)
    	GPIO.output(TRIG, False)
    	while GPIO.input(ECHO)==0:
    		pulse_start = time.time()
    	while GPIO.input(ECHO)==1:
    		pulse_end = time.time()
    	pulse_duration = pulse_end - pulse_start
    	distance = pulse_duration*17150
    	distance = round(distance, 2)
        print distance
        return distance

if __name__ == '__main__':
    test = UltraSonic()
    for i in range(5):
        print test.distance()
        time.sleep(1)
    GPIO.cleanup()
