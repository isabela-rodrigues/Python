def timeConversion(s):
    hora_12 = datetime.strptime(s, "%I:%M:%S%p")
    hora_24 = hora_12.strftime("%H:%M:%S")
    return hora_24