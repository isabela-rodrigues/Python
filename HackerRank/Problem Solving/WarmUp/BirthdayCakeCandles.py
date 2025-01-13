def birthdayCakeCandles(candles):
    maior_vela = max(candles)
    qt_vela = 0
    for i in candles:
        if i == maior_vela:
            qt_vela += 1
    return qt_vela