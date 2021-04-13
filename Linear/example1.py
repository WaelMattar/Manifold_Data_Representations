import numpy as np
import matplotlib.pyplot as plt
import math
import Linear.operations as op


level_of_sampling = 4
number_of_samples = np.int(math.pow(2, level_of_sampling))
sampling_grid = np.linspace(0.0, 2*math.pi, num=number_of_samples)


plt.plot(op.cubic_refine(op.curve(sampling_grid)))
plt.show()

