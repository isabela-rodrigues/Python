def compareTriplets(a, b):
    alice = 0
    bob = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            alice = alice + 1
        elif a[i] < b[i]:
            bob = bob + 1
        elif a[i] == b[i]:
            alice = alice
            bob = bob
    score=[alice, bob]
    return score