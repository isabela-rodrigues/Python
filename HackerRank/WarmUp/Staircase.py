def staircase(n):    
    caracter = "#"
    i = n
    espaco = " "

    while i > 0:
        i -= 1
        qt_caracter = n - i
        qt_espaco = n - qt_caracter
        if i > 0:
            print(espaco * qt_espaco + caracter * qt_caracter)
        else:
            print(caracter * qt_caracter) 