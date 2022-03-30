import numpy as np


def newton(f, Df, x0, epsilon, max_iter):
    xn = x0
    for n in range(0, max_iter):
        fxn = f(*xn)
        if abs(np.sum(fxn)) < epsilon:
            print(f'sum = {np.sum(fxn)}, {fxn}')
            return xn
        Dfxn = Df(*xn)
        zn = np.linalg.solve(np.array(Dfxn), -np.array(fxn))
        xn = xn + zn
        print(f"wartosc po {1 + n} iteracji: {xn}")


x0 = (0, 1)
f = lambda x, y: [[4 * x ** 2 - y ** 2 - 1], [4 * x * y ** 2 - x - 3]]
Df = lambda x, y: [[8 * x, 2 * y], [4 * y ** 2 - 1, 8 * x * y]]

# x0 = -1
# f = lambda x: 4*x**3 - 2*x**2 - 2
# Df = lambda x: 12*x**2 -4*x

print(newton(f, Df, x0, 0.00000000000001, 100))
