from itertools import permutations

def rooks(n):
    if n==1:
        yield [0,]
    else:
        for y in rooks(n-1):
            x = [n-1] + y
            yield x
            for i in range(n-1):
                x[i], x[i+1] = x[i+1], x[i]
                yield x

def queens(n):
    for possibility in rooks(n):
        if is_queen_positions(possibility):
            yield possibility

def is_queen_positions(t):
    diff, add = set(), set()
    for x,y in enumerate(t):
        if x-y in diff:
            return False
        if x+y in add:
            return False
        diff.add(x-y)
        add.add(x+y)
    return True

def generator_size(x):
    return sum(map(lambda _: 1, x))

import matplotlib.pyplot as plt
import numpy as np

def draw_position(p):
    n = len(p)
    M = np.zeros((n,n,3))
    for x,y in enumerate(p):
        M[x,y] = [255,255,255]
    plt.imshow(M)