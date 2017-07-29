import serial

import time
# port='/dev/tty.Bluetooth-Incoming-Port'

port = '/dev/tty.usbmodem1421'

bluetooth = serial.Serial(port,9600)
print("Connected")


print(bluetooth.readline())
bluetooth.write(1)

