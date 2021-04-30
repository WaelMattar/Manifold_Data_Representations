import numpy as np
import matplotlib.pyplot as plt
import math
import Linear.operations as op

# grid definition
level_of_sampling = 7
number_of_samples = np.int(math.pow(2, level_of_sampling))
sampling_grid = np.linspace(-np.pi, np.pi, num=number_of_samples + 1)

# adding noise
clean = op.curve(sampling_grid)
noisy = op.add_noise(clean, .06)
plt.plot(sampling_grid, clean, color='b')
plt.plot(sampling_grid, noisy, color='r')
plt.show()
