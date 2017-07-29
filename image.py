import math
import pprint

pp = pprint.PrettyPrinter(indent=5)


import serial

import time
port='/dev/tty.Bluetooth-Incoming-Port'

bluetooth = serial.Serial(port,9600)
bluetooth.flushInput()
print("Connected")

bluetooth.write(b'asdfasdf')
bluetooth.flush()




class Image:
    def __init__(self, radius, data=None):
        self.radius = radius
        self.data = data

        if data is None:
            temp_arr = []
            for i in range(radius * 2 + 1):
                temp_arr.append([])
                for j in range(radius * 2 + 1):
                    temp_arr[i].append(1)
            self.data = temp_arr

    def trim(self):
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if float((i - self.radius) ** 2 + (j - self.radius) ** 2) ** 0.5 > self.radius:
                    self.data[i][j] = 0

    def slice(self, div):
        ans = []
        for i in range(div):
            angle = (2 * math.pi / div) * i
            ans.append([])
            for j in range(self.radius + 1):
                x = self.radius + j * math.sin(angle)
                y = self.radius + j * math.cos(angle)
                x, y = int(round(x)), int(round(y))
                # print(x,y)
                ans[-1].append(self.data[x][y])

        return ans


def run(data):
    image = Image(15, data)
    image.trim()
    # pp.pprint(image.data)

    ans = "{"
    for line in image.slice(50):
        ans += "{"
        for char in line:
            ans += str(char)
            ans += ","
        ans = ans[:-1]
        ans +="},\n"
    ans = ans[:-2]
    ans += "}"

    print(ans)




