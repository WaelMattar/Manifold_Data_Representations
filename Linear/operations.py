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


if __name__ == '__main__':
    print(curve(np.linspace(-np.pi, np.pi, 10)))
    print(upsample([1, 3, 5, 6, 9]))
    print(downsample(upsample([1, 3, 5, 6, 9])))

