import numpy as np
import matplotlib.pyplot as plt
import math

def curve(x):
    curve = math.sin(3*x)
    return curve
curve = np.vectorize(curve)

level_of_sampling = 6
number_of_samples = np.int(math.pow(2, level_of_sampling))
sampling_grid = np.linspace(0.0, 2*math.pi, num=number_of_samples)

plt.plot(sampling_grid, curve(sampling_grid))
plt.show()



