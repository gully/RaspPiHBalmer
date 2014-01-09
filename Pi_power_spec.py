import time
import RPi.GPIO as io
from subprocess import call
io.setmode(io.BCM)

pir_pin = 24
power_pin=23

io.setup(pir_pin, io.IN)
io.setup(power_pin, io.OUT)
io.output(power_pin, False)

ii=0

while (ii < 1):
        if io.input(pir_pin): 
                print ii
                ii=ii+1
                print('power on')
                io.output(power_pin, True)
	        call(['raspistill', '-f', '-t', '10000'])
                time.sleep(1)
                print('power off')
                io.output(power_pin, False)
                time.sleep(1)
        time.sleep(0.2)

print 'the end'
