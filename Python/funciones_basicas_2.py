def multiplicar_dos(num):
    lista = []
    for i in range(0, (num *2)+1):
        if i % 2 == 0:
            lista.append(i)
    return lista

print("\nResultado ejercicio 1:\n", multiplicar_dos(5))

def suma_y_restar(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    return suma, resta

print("\nResultado ejercicio 2:\n", suma_y_restar(5, 4))

def sumatoria_menos_longitud(lista):
    sumatoria = sum(lista)
    longitud = len(lista)
    resultado = sumatoria - longitud
    return resultado

print("\nResultado ejercicio 3:\n", sumatoria_menos_longitud([1, 2, 3, 4]))

def valores_multiplicados_segundo():   # Ya no necesitas parámetro
    entrada = input("\nIngrese una lista de números separados por comas: ")
    lista = [int(x) for x in entrada.split(",")]

    if len(lista) < 2:
        return []
    else:
        segundo_valor = lista[1]
        resultado = [x * segundo_valor for x in lista]
        return resultado

resultado = valores_multiplicados_segundo()
print("\nResultado ejercicio 4:\n", 
        "> largo de la lista: ", len(resultado),
        "\n > valores multiplicados: ", resultado)

def valor_multiplicado_longitud(valor, longitud):
    lista = []

    valor = int(input("\nIngrese un número para Valor: "))
    longitud = int(input("\nIngrese un número para Longitud: "))

    for i in range(0, longitud):
        lista.append(valor * longitud)
    return lista    

print("\nResultado ejercicio 5:\n", valor_multiplicado_longitud(5, 2))