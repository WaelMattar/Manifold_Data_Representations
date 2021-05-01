import numpy as np
import matplotlib.pyplot as plt
import Linear.operations as op
import math

# grid definition
level_of_sampling = 7
number_of_samples = np.int(math.pow(2, level_of_sampling))
sampling_grid = np.linspace(-np.pi, np.pi, num=number_of_samples + 1)

# adding jump points
curve = op.curve(sampling_grid)
for index in range(np.int64(len(curve)/3), np.int64(2 * len(curve)/3)):
    curve[index] = - 0.05 * curve[index] + 0.2
pyramid = op.cubic_pyramid(curve, 1, .001)

# detection
details = pyramid[1]
red_flag = .05
abnormal_points = np.array([i for i, v in enumerate(details) if abs(v) > red_flag])
print('Abnormal behaviors detected at: ', 2 * np.pi * np.subtract(abnormal_points / len(details), .5))

# demonstration
plt.figure(1)
plt.plot(sampling_grid, curve, color='g')
plt.title('Signal with Two Jump Points')
op.pyramid_visualization(pyramid, [-np.pi, np.pi])
plt.show()
