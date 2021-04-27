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
        if image_data[x, y, 0] == 0:
            for itheta in range(theta_dim):
                theta = 1 * itheta * theta_max / theta_dim
                r = x * math.cos(theta) + y * math.sin(theta)
                ir = r_dim * (1.0 * r) / r_max
                hough_space[int(ir), itheta] = hough_space[int(ir), itheta] + 1

### chart1
plt.imshow(hough_space, origin='lower')
plt.xlim(0, theta_dim)  # we set maximum value on the x-axis of the graph
plt.ylim(0, r_dim)  # we do the same for y

# this parameters changes the axis signature of the chart
stepfor_axis_x = 40
stepfor_axis_y = 20

tick_locs = [i for i in range(0, theta_dim, stepfor_axis_x)] # The list of xtick locations.
tick_labels = [round((1.0 * i * theta_max) / theta_dim, 1) for i in range(0, theta_dim, stepfor_axis_x)] # The list of xlabel Text objects.
plt.xticks(tick_locs, tick_labels)

tick_locs = [i for i in range(0, r_dim, stepfor_axis_y)] # The list of ytick locations.
tick_labels = [round((1.0 * i * r_max) / r_dim, 1) for i in range(0, r_dim, stepfor_axis_y)] # The list of ylabel Text objects.
plt.yticks(tick_locs, tick_labels)

plt.xlabel(r'Theta')
plt.ylabel(r'r')
plt.title('Hough Space')

plt.savefig("hough_space_r_theta.png", bbox_inches='tight')

plt.close()
