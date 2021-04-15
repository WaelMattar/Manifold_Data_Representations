import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

plt.style.use('seaborn-whitegrid')

def upsample(data_points):
    up = [0] * (2*len(data_points)-1)
    for i in range(len(data_points)):
        up[2*i] = data_points[i]
    return up


def downsample(data_points):
    down = []
    for i in range(np.int((len(data_points) + 1)/2)):
        down = np.append(down, data_points[2 * i])
    return down


def cubic_refine(data_points):
    alpha = np.multiply(1/8, [1, 4, 6, 4, 1])
    return signal.convolve(upsample(data_points), alpha, mode='same')


def cubic_decimate(data_points, truncation_parameter):
    alpha = np.multiply(1 / 8, [1, 4, 6, 4, 1])
    inverse_mask = zeta(alpha, truncation_parameter)
    return signal.convolve(downsample(data_points), inverse_mask, mode='same')


def curve(x):
    return np.sin(3*np.array(x))


def zeta(mask, truncation_parameter):
    padded_vec = np.pad(downsample(mask), (47, 47), 'constant', constant_values=(0, 0))
    xi = np.fft.fft(padded_vec)
    gamma = np.real(np.fft.ifft(1/xi))
    truncated = gamma[abs(gamma) > truncation_parameter]
    return truncated / np.sum(truncated)


def average(data_points, weights):
    return np.dot(data_points, weights)


def cubic_decompose(data_points, truncation_parameter):
    low_resolution = cubic_decimate(data_points, truncation_parameter)
    refined = cubic_refine(low_resolution)
    return [low_resolution, np.subtract(data_points, refined)]


def cubic_pyramid(data_points, scale, truncation_parameter):
    coarse_approximation = data_points
    pyramid = []
    while scale > 0:
        decomposition = cubic_decompose(coarse_approximation, truncation_parameter)
        coarse_approximation = decomposition[0]
        pyramid.insert(0, decomposition[1])
        scale -= 1
    pyramid.insert(0, coarse_approximation)
    return pyramid


def pyramid_visualization(pyramid, interval):
    x = np.linspace(interval[0], interval[1], len(pyramid[0]))
    plt.plot(x, pyramid[0], 'o', color='black')
    plt.show()


if __name__ == '__main__':
    x = np.linspace(-np.pi, np.pi, 21)
    print(curve(x))
    pyramid = cubic_pyramid(curve(x), 2, 0.01)
    pyramid_visualization(pyramid, [-np.pi, np.pi])




