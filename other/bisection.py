import math

f = lambda x: x ** 3 + x + 1
a = -3
b = 3


# f = lambda x: math.sin(x)
# a = math.pi / 6
# b = math.pi + 1


def sgn(x):
    return x >= 0


e = b - a
delta = 0.00000001
eps = 0.000001
M = 100
fa = f(a)
fb = f(b)
fc = None
if sgn(fa) == sgn(fb):
    raise Exception('wrong starting params')
for i in range(M):
    print(i + 1)
    e = e / 2
    c = a + e
    fc = f(c)
    if abs(e) < delta or abs(fc) < eps:
        break
    if sgn(fc) != sgn(fa):
        b = c
        fb = fc
    else:
        a = c
        fa = fc
    print(f" (c,f(c)) = {c, fc} - dla przedzialu {a, b}")
    print()
