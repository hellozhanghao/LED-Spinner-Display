import numpy as np
import pprint
import scipy
import matplotlib.pyplot as plt
import math

pp = pprint.PrettyPrinter(indent=5)


class Pixel:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

    def distance(self, other):
        return (float(self.xpos - other.xpos) ** 2 + (self.ypos - other.ypos) ** 2) ** 0.5


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
            # print(self.radius)
            for j in range(self.radius+1):
                x = self.radius + j * math.sin(angle)
                y = self.radius + j * math.cos(angle)
                x, y = int(round(x)), int(round(y))
                print(x,y)
                ans[-1].append(self.data[x][y])

        pp.pprint(ans)


                # pp.pprint(self.data)


data = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

image = Image(10, data)
image.trim()
# pp.pprint(image.data)


sliced = [[0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
          [0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
          [0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
          ]

# pp.pprint(sliced)

image.slice(64)
