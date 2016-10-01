import matplotlib.pyplot as plt
import numpy as np


def test2():
    print(__file__)
    pass


def test5():
    plt.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16], 'ro')
    plt.show()
    pass


def test14():
    t = np.arange(-5.0, 5.0, 0.2)
    plt.plot(t, t, 'r', t, t ** 2, 'bs', t, t ** 3, 'g^')
    plt.show()
    pass
