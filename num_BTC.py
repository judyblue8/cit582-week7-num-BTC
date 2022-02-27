def reward(n):
    r = 50.0
    h = 210000
    if (n < h):
        return r
    else:
        return reward(n-h)/2

def num_BTC(b):
    c = 0.0
    for x in range (0,b):
        c = c + reward(x)
    return c
