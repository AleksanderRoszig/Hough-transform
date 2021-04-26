import PIL
import numpy as np
import math
import matplotlib.pyplot as plt
image = PIL.Image.open('xxx.png')
image_data = np.asarray(image)

#variables
y_max = (image_data.shape[1]) #height
x_max = (image_data.shape[0]) #width

theta_max = 1.0 * math.pi
theta_min = 0.0

r_min = 0.0
r_max = math.hypot(x_max, y_max)

r_dim = 200 #height of Hough space
theta_dim = 300 #width of Hough space

hough_space = np.zeros((r_dim,theta_dim))

for x in range(x_max):
    for y in range(y_max):
        if image_data[x,y] == 1:
            for itheta in range(theta_dim):
                theta = 1 * itheta * theta_max / theta_dim
                r = x * math.cos(theta) + y * math.sin(theta)
                ir = r_dim * ( 1.0 * r ) / r_max
                hough_space[int(ir),itheta] = hough_space[int(ir),itheta] + 1
