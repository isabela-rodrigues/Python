# x1 - posição inicial do canguru 1
# v1 - velocidade do canguru 1
# x2 - posição inicial do canguru 2
# v2 - velocidade do canguru 2
def kangaroo(x1, v1, x2, v2):   
    if v1 == v2 and x1 == x2:
        return 'YES'
    elif ((v1 - v2) * (x2 - x1) > 0) and ((x2 - x1) % (v1 -v2) == 0):
        return 'YES'
    elif v1 == v2 and x1 != x2:
        return 'NO'
    elif (v1 > v2 and x1 > x2) or (v2 > v1 and x2 > x1):
        return 'NO'
    else:
        return 'NO'