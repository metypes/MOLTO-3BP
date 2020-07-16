def x_crossing(et, state, mu1, mu2):
    return state[1]

def y_crossing(et, state, mu1, mu2):
    return state[0]

def earth_SE_crossing(et, state, mu1, mu2):
    [x, y] = state[:2]

    tol = 1e-5

    if abs(x - mu1) < 1e-2 and (x - mu1) < 0:
        check = abs(y) > tol
    elif  abs(y) > 0.02:
        check = 0
    else:
        check = 1
    return check
