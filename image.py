import numpy as np
import pprint
import scipy

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

    def slice(self,div):
        # -- Generate some data...
        x, y = np.mgrid[-5:5:0.1, -5:5:0.1]
        z = np.sqrt(x ** 2 + y ** 2) + np.sin(x ** 2 + y ** 2)
        lena = scipy.misc.lena()  # ADDED THIS ASYMMETRIC IMAGE
        z = lena[320:420, 330:430]  # ADDED THIS ASYMMETRIC IMAGE

        # -- Extract the line...
        # Make a line with "num" points...
        x0, y0 = 5, 4.5  # These are in _pixel_ coordinates!!
        x1, y1 = 60, 75
        num = 500
        x, y = np.linspace(x0, x1, num), np.linspace(y0, y1, num)

        # Extract the values along the line, using cubic interpolation
        # zi = scipy.ndimage.map_coordinates(z, np.vstack((x, y)))  # THIS DOESN'T WORK CORRECTLY
        zi = scipy.ndimage.map_coordinates(np.transpose(z), np.vstack((x, y)))  # THIS SEEMS TO WORK CORRECTLY

        # -- Plot...
        fig, axes = plt.subplots(nrows=2)
        axes[0].imshow(z)
        axes[0].plot([x0, x1], [y0, y1], 'ro-')
        axes[0].axis('image')

        axes[1].plot(zi)

        plt.show()


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

image = Image(10,data)
image.trim()
pp.pprint(image.data)


sliced = [  [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
            [0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
            ]

pp.pprint(sliced)