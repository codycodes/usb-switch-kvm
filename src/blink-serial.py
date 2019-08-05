import serial
import os
from pynput import keyboard
from time import sleep

COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(char='b')},
    {keyboard.Key.shift, keyboard.KeyCode(char='B')},
]

ARDUINO_SERIAL_PORT = os.environ['ARDUINO_SERIAL_PORT']

ser = serial.Serial(ARDUINO_SERIAL_PORT, timeout=1) # open serial port
print("you're using {}".format(ser.name)) # confirm it's correct

current = set()

def execute():
    # ard_data = ser.readline()
    # print(ard_data)
    ser.write(b'b')
    # sleep(1)

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()