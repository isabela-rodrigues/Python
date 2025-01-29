a = [1,1,2,2,3,3,4]
def lonelyinteger(a):
    counts = {}
    for num in a:
        counts[num] = counts.get(num, 0) + 1
    for num, count in counts.items():
        if count == 1:
            return num

print(f"O número não repetido é o {lonelyinteger(a)}")