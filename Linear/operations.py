import numpy as np
import matplotlib.pyplot as plt
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


def cubic_reconstruct(low_resolution, detail_coefficients):
    refined = cubic_refine(low_resolution)
    return np.add(refined, detail_coefficients)


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


def cubic_inverse_pyramid(pyramid):
    reconstructed = pyramid[0]
    for k in range(len(pyramid) - 1):
        reconstructed = cubic_reconstruct(reconstructed, pyramid[k+1])
    return reconstructed


def pyramid_visualization(pyramid, interval):
    fig, axs = plt.subplots(len(pyramid), sharex=True, sharey=True, gridspec_kw={'hspace': 0})
    fig.suptitle('Pyramid Representation')
    axs[0].plot(np.linspace(interval[0], interval[1], len(pyramid[0])), pyramid[0], '*', color='red')
    axs[0].set_ylim(1.2 * min(pyramid[0]), 1.2 * max(pyramid[0]))
    for k in range(len(pyramid) - 1):
        axs[k+1].plot(np.linspace(interval[0], interval[1], len(pyramid[k+1])), pyramid[k+1], 'o', color='blue')
        axs[k+1].set_ylim(1.2 * min(pyramid[k+1]), 1.2 * max(pyramid[k+1]))
    for ax in axs:
            ax.label_outer()
    plt.show()


def details_layer_plot(detail_coefficients, interval):
    norms = abs(detail_coefficients)
    x = np.linspace(interval[0], interval[1], len(detail_coefficients))
    plt.plot(x, norms, '*', color='blue')


if __name__ == '__main__':
    grid = np.linspace(-np.pi, np.pi, 41)
    pyramid1 = cubic_pyramid(curve(grid), 3, 0.01)
    inv_pyramid = cubic_inverse_pyramid(pyramid1)
    diff = np.subtract(curve(grid), inv_pyramid)
    print(np.linalg.norm(diff))
    pyramid_visualization(pyramid1, [-np.pi, np.pi])
    details_layer_plot(pyramid1[2], [-np.pi, np.pi])





