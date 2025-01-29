def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2) - 1 # menos 1 para trocar a posição corretamente, começa do 0 a contagem
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2 # menos 2 para chegar na posição do número 6
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1 # decrementa pro loop executar apenas 1 vez

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)