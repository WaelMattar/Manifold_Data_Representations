import numpy as np
import matplotlib.pyplot as plt
import math
import Linear.operations as op

# grid definition
level_of_sampling = 7
number_of_samples = np.int(math.pow(2, level_of_sampling))
sampling_grid = np.linspace(-np.pi, np.pi, num=number_of_samples + 1)

# pyramid transform
curve = op.curve(sampling_grid)
pyramid = op.cubic_pyramid(curve, 7, .001)

# demonstrations
plt.figure(1)
plt.plot(sampling_grid, curve, color='g')
plt.grid()
plt.title('Original Signal')
op.pyramid_visualization(pyramid, [-np.pi, -np.pi])
plt.show()


