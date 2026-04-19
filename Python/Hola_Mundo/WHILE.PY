x = 6

while x > 2:
    print(x)
    x -= 1
    if x == 3:
        break
else: #Recuerda: Solo se ejecuta en una salida normal, NO en un break
    print("Sentencia final")