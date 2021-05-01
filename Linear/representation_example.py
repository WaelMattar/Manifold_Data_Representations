import numpy as np
import matplotlib.pyplot as plt
import Linear.operations as op
import math

# grid definition
level_of_sampling = 6
number_of_samples = np.int(math.pow(2, level_of_sampling))
sampling_grid = np.linspace(-np.pi, np.pi, num=number_of_samples + 1)

# pyramid transform
curve = op.curve(sampling_grid)
truncation_parameter = .001
pyramid = op.cubic_pyramid(curve, level_of_sampling, truncation_parameter)

# demonstrations
op.pyramid_visualization(pyramid, [-np.pi, -np.pi])
plt.plot(sampling_grid, curve, color='g')
plt.title('Original Signal')
plt.show()


