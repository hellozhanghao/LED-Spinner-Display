import math
import pprint
import time
import serial

pp = pprint.PrettyPrinter(indent=5)


port = 'COM4'

bluetooth = serial.Serial(port, 115200, timeout=1)
print("Connected")

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
    # print(image.data)

    # ans = "["
    # for line in image.slice(47):
    #     ans += "["
    #     for char in line:
    #         ans += str(char)
    #         ans += ","
    #     ans = ans[:-1]
    #     ans +="],\n"
    # ans = ans[:-2]
    # ans += "]"

    upload(image.slice(47))

def upload(data):
    time.sleep(4)
    print("Upload Start!")
    for line in data:
        for digit in line:
            if digit == 1:
                bluetooth.write(b'1')
            else:
                bluetooth.write(b'2')
            time.sleep(0.01)
        bluetooth.write(b'n')
    bluetooth.write(b'e')
    print("Upload finished!")



