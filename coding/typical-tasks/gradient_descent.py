"""
Implement a gradient descent algorithm for linear regression
"""

import numpy as np

x = np.array([0, 1, 2, 3, 4, 5])
y = 6 * x + 3

l = len(x)


def gradient(b0, b1):
    err = (b1 * x + b0 - y)
    q1 = (2 / l) * np.sum(x * err)
    q0 = (2 / l) * np.sum(err)

    b0 = b0 - eta * q0
    b1 = b1 - eta * q1

    return b0, b1


if __name__ == "__main__":

    eta = 0.01
    b0 = 10
    b1 = 10
    iterations = 1000

    for _ in range(iterations):
        b0, b1 = gradient(b0, b1)

    print(f"y = {b0} + {b1} * x")
