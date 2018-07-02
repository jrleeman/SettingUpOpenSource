"""Makes special plots for our library."""

import matplotlib.pyplot as plt

import numpy as np


def random_plot(num_points, seed=None):
    if seed:
        np.random.seed(seed)
    x = np.random.rand(num_points)
    y = np.random.rand(num_points)
    z = np.random.rand(num_points)

    fig = plt.figure(figsize=(5, 5))
    ax = plt.subplot(1, 1, 1)
    ax.scatter(x, y, c=z)
    return fig, ax
