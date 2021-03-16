import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import signal

def curve(x):
    curve = math.sin(3*x)
    return curve
curve = np.vectorize(curve)

def upsample(data_points):
    L = len(data_points)
    new_data_points = [0] * (2*L-1)
    for i in range(L-1):
        new_data_points[2*i] = data_points[i]
    return new_data_points

def cubic_refine(points):
    alpha =  np.multiply(1/8, [1, 4, 6, 4, 1])
    return signal.convolve(upsample(points), alpha, mode='same')

level_of_sampling = 4
number_of_samples = np.int(math.pow(2, level_of_sampling))
sampling_grid = np.linspace(0.0, 2*math.pi, num=number_of_samples)

plt.plot(cubic_refine(curve(sampling_grid)))
plt.show()

