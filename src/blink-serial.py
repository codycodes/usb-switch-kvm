import serial
import os

ARDUINO_SERIAL_PORT = os.environ['ARDUINO_SERIAL_PORT']

ser = serial.Serial(ARDUINO_SERIAL_PORT) # open serial port
print(ser.name)
while True:
    ard_data = ser.readline()
    print(ard_data)