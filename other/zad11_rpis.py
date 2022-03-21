import numpy as np

r = 100
tokens = np.floor(np.random.normal(loc=10,scale=2, size=r))
print(f'Before: {tokens}')
curr_players = r
p1 = p2 = None
while curr_players > 1:
    while True:
        p1, p2 = np.floor(np.random.uniform(0, r, size=2))
        p1 = int(p1)
        p2 = int(p2)
        if p1 != p2 and tokens[p2] > 0 and tokens[p1] > 0:
            break
    tokens[p1] += 1
    tokens[p2] -= 1
    if tokens[p2] == 0:
        curr_players -= 1


print(f'After {tokens}. Player no {np.where(tokens > 0)} won')
