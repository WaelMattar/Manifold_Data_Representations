import numpy as np
import matplotlib.pyplot as plt
import Linear.operations as op


num_of_iter, refinements, grids = 6, [], []
refinements.append(np.random.normal(0, 0.1, 11))


for iteration in range(num_of_iter):
    refinements.append(op.cubic_refine(refinements[iteration]))
    grids.append(np.linspace(0, 10, 10 * np.power(2, iteration) + 1))

for iteration in range(num_of_iter):
    if iteration == 0:
        plt.plot(grids[0], refinements[0], color='r')
    else:
        plt.clf()
        plt.plot(grids[0], refinements[0], color='r')
        plt.plot(grids[iteration], refinements[iteration], color='b')
    plt.pause(0.5)
plt.show()
