import numpy as np


def test2():
    print(__file__)
    pass


def test8():
    a = np.array([(1, 2, 3), (2, 3, 4)])
    print(a.data)
    print(a.dtype)
    print(a)
    print(a.ndim)
    print(a.size)
    print(a.itemsize)
    pass


def test19():
    print(np.zeros((2, 3)))
    print(np.zeros([2, 3]))
    print(np.zeros(2))
    print(np.ones((2, 3)))
    print(np.ones((2, 3), dtype=np.int8))
    print(np.empty((2, 3)))
    print(np.empty((2, 3), dtype=np.int32))
    pass


def test30():
    from numpy import pi
    print(pi)
    print(np.arange(0, 10, pi))
    print(np.linspace(0.0, 10.0, 9, dtype=np.float32))
    a = np.linspace(0.0, 2 * pi, 4, dtype=np.float32)
    print(a)
    print(np.sin(a))
    print(np.arange(12).reshape(3, 4))
    print(np.arange(12).reshape(4, 3))
    print(np.arange(12).reshape((2, 2, 3)))
    np.set_printoptions(threshold=10000, linewidth=10000)
    print(np.arange(10000).reshape((100, 100)), file=open('z:/test.tmp', 'wt'))


def test():
    a = np.array([20, 30, 40, 50, ])
    print(a)
    b = np.arange(4)
    print(b)
    print('a-b=\n', a - b)
    print(b ** 2)
    print(np.sin(a))
    print(a < 35)
    pass

def test57():
    import os
    print(os.path)
    import pexpect
    pass
