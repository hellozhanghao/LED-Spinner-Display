import serial
import time
# port='/dev/tty.Bluetooth-Incoming-Port'

port = 'COM4'

bluetooth = serial.Serial(port,115200,timeout=1)
print("Connected")

#while True:
#    print(bluetooth.readline())

data = [
    [1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1],
    [1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1],
    [1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1],
    [1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1],
    [1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1],
    [1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1],
    [1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1]
    ]

#while True:
#    bluetooth.write()
#

time.sleep(4)

while True:
    bluetooth.write(b'1')
    print(bluetooth.readline())

for line in data:
    for digit in line:
        bluetooth.write(b'1')
        print(bluetooth.readline())