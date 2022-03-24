def f(x):
    return x ** 3 + x + 1


def fprime(x):
    return 3 * x ** 2 + 1


def sgn(x):
    return x >= 0


a = -2
b = 2
e = b - a
delta = 0.00000001
eps1 = 0.000001
M = 100
fa = f(a)
fb = f(b)
ya = None
yb = None
x = a - f(a) / fprime(a)
for i in range(M):
    ya = f(a)
    yb = f(b)
    x = x - f(x) / fprime(x)
    y = f(x)
    if abs(y) < eps1 or abs(x - a) < delta or abs(x - b) < delta:
        print(f" (c,f(c)) = {x, f(x)}")
        break
    else:
        if ya * y > 0:
            a = x
            ya = y
        else:
            b = x
            yb = y
    if i == M - 1:
        print(f" (c,f(c)) = {x, f(x)} - dla przedzialu {a, b}")
