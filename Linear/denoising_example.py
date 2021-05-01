import numpy as np
import matplotlib.pyplot as plt
import Linear.operations as op
import math

# grid definition
level_of_sampling = 7
number_of_samples = np.int(math.pow(2, level_of_sampling))
sampling_grid = np.linspace(-np.pi, np.pi, num=number_of_samples + 1)

# adding noise
clean_curve = op.curve(sampling_grid)
noise_level = .06
noisy_curve = op.add_noise(clean_curve, noise_level)

# noise removal algorithm
noisy_pyramid = op.cubic_pyramid(noisy_curve, 3, .0001)
clean_pyramid = noisy_pyramid.copy()
shrinking_threshold = .5
for layer in range(1, len(clean_pyramid)):
    clean_pyramid[layer] = op.details_shrink(clean_pyramid[layer], shrinking_threshold)
noise_free = op.cubic_inverse_pyramid(clean_pyramid)

# demonstrations
plt.figure(1)
plt.plot(sampling_grid, clean_curve, color='b', linestyle='--')
plt.plot(sampling_grid, noisy_curve, color='r')
plt.title('Dashed Ground Truth with Noisy Curve')
plt.figure(2)
plt.plot(sampling_grid, noise_free, color='g')
plt.plot(sampling_grid, clean_curve, color='b', linestyle='--')
plt.title('Dashed Ground Truth with Noise-Free Curve')
plt.show()

