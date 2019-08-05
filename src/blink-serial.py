import serial
import os
from time import sleep

ARDUINO_SERIAL_PORT = os.environ['ARDUINO_SERIAL_PORT']

ser = serial.Serial(ARDUINO_SERIAL_PORT, timeout=1) # open serial port
print("you're using {}".format(ser.name)) # confirm it's correct

while True:
    ard_data = ser.readline()
    print(ard_data)
    ser.write(b'b')
    sleep(1)