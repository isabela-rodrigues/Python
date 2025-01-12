def plusMinus(arr):
    len_array = len(arr)
    positivo = 0
    negativo = 0
    zero = 0
    
    for i in arr:
        if i > 0:
            positivo += 1
        elif i < 0:
            negativo += 1
        elif i == 0:
            zero += 1
    
    print("{:.6f}".format(positivo/len_array))
    print("{:.6f}".format(negativo/len_array))
    print("{:.6f}".format(zero/len_array))