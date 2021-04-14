import numpy as np
from scipy import signal


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


def cubic_refine(points):
    alpha = np.multiply(1/8, [1, 4, 6, 4, 1])
    return signal.convolve(upsample(points), alpha, mode='same')


def curve(x):
    return np.sin(3*np.array(x))


def zeta(x, truncation_parameter):
    padded_vec = np.pad(downsample(x), (47, 47), 'constant', constant_values=(0, 0))
    xi = np.fft.fft(padded_vec)
    gamma = np.real(np.fft.ifft(1/xi))
    truncated = gamma[abs(gamma) > truncation_parameter]
    return truncated / np.sum(truncated)


if __name__ == '__main__':
    print(curve(np.linspace(-np.pi, np.pi, 10)))
    print(upsample([1, 3, 5, 6, 9]))
    print(downsample(np.multiply(1/8, [1, 4, 6, 4, 1])))
    print(zeta(np.multiply(1/8, [1, 4, 6, 4, 1]), 0.01))
    print(np.sum(zeta(np.multiply(1/8, [1, 4, 6, 4, 1]), 0.01)))
    #print(np.append([0] * 4, [3, 4, 5, 1], [0] * 4))
