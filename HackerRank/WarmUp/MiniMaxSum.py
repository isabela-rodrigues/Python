def miniMaxSum(arr):
    arr.sort()
    soma = 0
    for i in arr:
        soma = soma + i
    print(soma - arr[4], soma - arr[0])