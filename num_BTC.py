import math

def reward(b):
    r = 50.0
    h = 210000
    if (n < h):
        return r
    else:
        return reward(b-h)/2

def num_BTC(b):
    a = 0.0
    for x in range (0,b):
        a = a + reward(x)
    return a


