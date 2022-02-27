def reward(b):
    r = 50.0
    h = 210000
    if (b < h):
        return r
    else:
        return reward(b-h)/2

def num_BTC(n):
    c = 0.0
    for x in range (0,b):
        c = c + reward(x)
    return c
