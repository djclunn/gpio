import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 4
ECHO = 18
CM = 0.000058
MM = CM/10
IN = MM*25.4
DISTANCE_UNIT = CM

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, True)
time.sleep(0.0001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO) == False:
    start = time.time()

while GPIO.input(ECHO) == True:
    end = time.time()

sig_time = end-start


distance = sig_time / DISTANCE_UNIT

print('Distance: {} cm'.format(distance))

GPIO.cleanup()

