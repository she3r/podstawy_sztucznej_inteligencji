import numpy as np


def game():
    S1 = 0
    last1 = 0
    S2 = 0
    last2 = 0

    while S1 < 100:
        last1 = np.random.uniform(1, 100)
        S1 += last1
    while S2 < 200:
        last2 = np.random.uniform(1, 100)
        S2 += last1
    if last1 > last2:
        return 1
    elif last1 == last2:
        return 0
    else:
        return -1


# zwraca stosunek zwyciestw drugiego gracza do ilosci symulacji
def testGame(n=100000):
    count1 = 0
    count2 = 0
    for i in range(n):
        result = game()
        if result == 1:
            count1 += 1
        elif result == -1:
            count2 += 1

    return count1 / n, count2 / n, abs(n - count1 - count2) / n


print(testGame())
