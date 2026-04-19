#1
def cantidad_de_vocales():
    return 5
print(cantidad_de_vocales())

'''
respuesta: 5

'''


#2
def cantidad_de_glaciares_argentina():
    return 16968
print(cantidad_de_dias_o_meses_o_semanas_en_anio() + cantidad_de_glaciares_argentina())

'''
Respuesta: 16968, porque la función cantidad_de_dias_o_meses_o_semanas_en_anio no tiene parámetros 
y no se le ha dado ningún valor, por lo que no se puede ejecutar y no devuelve ningún valor. 
Por lo tanto, la suma de cantidad_de_dias_o_meses_o_semanas_en_anio() + cantidad_de_glaciares_argentina() 
solo devuelve el valor de cantidad_de_glaciares_argentina(), que es 16968.

'''

#3
def anio_independencia_chile():
    return 1810
    return 1851
print(anio_independencia_chile())

'''
Respuesta: 1810, porque la función anio_independencia_chile tiene dos sentencias return, pero solo se ejecuta 
la primera sentencia return que encuentra, que es return 1810. 
La segunda sentencia return 1851 nunca se ejecuta, por lo que no afecta el resultado de la función.
Ergo, la función devuelve 1810.

'''

#4
def cantidad_de_departamentos_colombia():
    return(32)
    print(33)
print(cantidad_de_departamentos_colombia())

'''
Resultado: 32, porque la función cantidad_de_departamentos_colombia tiene una sentencia return que devuelve el valor 32.
La sentencia print(33) nunca se ejecuta, porque la función ya ha devuelto un valor y ha terminado su ejecución.
Por lo tanto, la función devuelve 32 y no imprime nada más.

'''

#5
def altura_machu_picchu():
    print(2438)
x = altura_machu_picchu()
print(x)

'''
Respuesta: 2438, None. La función altura_machu_picchu imprime el valor 2438 pero no devuelve ningún valor explícito, 
por lo que, por defecto, devuelve None.
Cuando se asigna el resultado de la función a la variable x, x toma el valor None. 
Por lo tanto, al imprimir x, debiera imprimir None después de imprimir 2438.

'''

#6
def suma(a, b):
    print(a+b)
print(suma(10, 5) + suma(4, 3))

'''
Resultado: 15, 7, TypeError. La función suma imprime la suma de a y b pero
no devuelve ningún valor explícito, por lo que, por defecto, devuelve None.
Cuando se llama a suma(10, 5), se imprime 15 pero la función devuelve None. 
Cuando se llama a suma(4, 3), se imprime 7 pero la función devuelve None. 
Al intentar sumar los resultados de ambas funciones (None + None), se produce 
un error de tipo (TypeError) porque no se pueden sumar valores de tipo None. 
Por lo tanto, el resultado final es 15, 7, seguido de un error de tipo.
'''


#7
def concatenar(a, b):
    return str(b) + str(a)
print(concatenar(7, 15))

'''
Resultado: 157, porque la función concatenar convierte ambos argumentos a cadenas de texto (str) y luego los concatena.
En este caso, el primer argumento es 7 y el segundo argumento es 15.
Al convertir ambos a cadenas, obtenemos "7" y "15".
Luego, al concatenar "15" + "7", obtenemos "157", que es lo que se imrime en pantalla.
'''


#8
def paises_latinoamerica_o_lenguas_indigenas():
    a = 560
    print(a)
    if a < 180:
        return 33
    else:
        return 46
    return 21
print(paises_latinoamerica_o_lenguas_indigenas())

'''
Resultado: 560, 46. La función paises_latinoamerica_o_lenguas_indigenas asigna el valor 560
a la variable a y lo imprime. Luego, evalúa la condición if a < 180, que es falsa,
por lo que ejecuta el bloque else y devuelve 46.
La función no llega a ejecutar la última sentencia return 21, porque ya ha devuelto un valor (46) y ha terminado su ejecución.
Por lo tanto, el resultado final es 560 seguido de 46.'''

#9
def cantidad_de_dias_o_meses_o_semanas_en_anio(a, b):
    if a < b:
        return 365
    else:
        return 12
    return 52
print(cantidad_de_dias_o_meses_o_semanas_en_anio(1, 3))
print(cantidad_de_dias_o_meses_o_semanas_en_anio(7, 4))
print(cantidad_de_dias_o_meses_o_semanas_en_anio(7, 4) + cantidad_de_dias_o_meses_o_semanas_en_anio(1, 3))

'''
Resultado: 365, 12, 377. La función cantidad_de_dias_o_meses_o_semanas_en_anio evalúa la condición if a < b.
En la primera llamada, cantidad_de_dias_o_meses_o_semanas_en_anio(1, 3), la condición es verdadera (1 < 3),
por lo que devuelve 365. En la segunda llamada, cantidad_de_dias_o_meses_o_semanas_en_anio(7, 4),
la condición es falsa (7 < 4), por lo que devuelve 12. En la tercera llamada,
cantidad_de_dias_o_meses_o_semanas_en_anio(7, 4) + cantidad_de_dias_o_meses_o_semanas_en_anio(1, 3),
se suman los resultados de ambas funciones:
- cantidad_de_dias_o_meses_o_semanas_en_anio(7, 4) devuelve 12
- cantidad_de_dias_o_meses_o_semanas_en_anio(1, 3) devuelve 365

Al sumar ambos resultados (12 + 365), obtenemos 377, que es lo que se imprime en pantalla.
'''


#10
def sumatoria(a, b):
    return a + b
    return 157
print(sumatoria(3, 4))

'''
Resultado: 7, porque la función sumatoria devuelve la suma de a y b, que en este caso es 3 + 4 = 7.
La segunda sentencia return 157 nunca se ejecuta.

'''

#11
a = 150
print(a)
def funcion():
    a = 350
    print(a)
print(a)
funcion()
print(a)

'''
Resultado: 150, 150, 350, 150. La variable a se define inicialmente con el valor 150 y se imprime.
Luego, se define la función funcion, que asigna el valor 350 a una variable local a y la imprime.
Al imprimir a fuera de la función, se sigue mostrando el valor 150, porque la variable a dentro
de la función es una variable local que no afecta a la variable a fuera de la función.
Al llamar a funcion(), se imprime 350, pero al imprimir a nuevamente después de llamar a la función,
se sigue mostrando 150, porque la variable a fuera de la función no ha sido modificada por la función. 

Por lo tanto, el resultado final es 150, 150, 350, 150.

'''


#12
a = 150
print(a)
def funcion():
    a = 350
    print(a)
    return a
print(a)
funcion()
print(a)

'''
Resultado; 150, 150, 350, 150. La variable a se define inicialmente con el valor 150 y se imprime.
Luego, se define la función funcion, que asigna el valor 350 a una variable local a y la imprime.
Al imprimir a fuera de la función, se sigue mostrando el valor 150, porque la variable a
dentro de la función es una variable local que no afecta a la variable a fuera de la función.
Al llamar a funcion(), se imprime 350, pero al imprimir a nuevamente después de llamar a la función,
se sigue mostrando 150, porque la variable a fuera de la función no ha sido modificada por la función.
Por lo tanto, el resultado final es 150, 150, 350, 150.
'''

#13
a = 150
print(a)
def funcion():
    a = 350
    print(a)
    return a
print(a)
a = funcion()
print(a)

'''
Resultado:
150, 150, 350, 350. 
La variable a se define inicialmente con el valor 150 y se imprime. Luego,
se define la función funcion, que asigna el valor 350 a una variable local a y la imprime.
Al imprimir a fuera de la función, se sigue mostrando el valor 150, porque la variable a dentro de la función 
es una variable local que no afecta a la variable a fuera de la función. Al llamar a funcion(), se imprime 350 
pero se devuelve el valor 350, que se asigna a la variable a fuera de la función.
Por lo tanto, al imprimir a nuevamente después de llamar a la función, se muestra el valor 350, porque la variable 
afuera de la función ha sido modificada por la asignación a = funcion(). 

Por lo tanto, el resultado final es 150, 150, 350, 350.

'''


#14
def funcion1():
    print(3)
    funcion2()
    print(2)
def funcion2():
    print(1)
funcion1()

'''
Resultado: 3, 1, 2. La función funcion1 imprime el número 3, luego llama a la función funcion2,
que imprime el número 1. La funcion1 es llamada luego de serdefinidos os argumentos y las funciones
embebidas en funcion1, por lo que se ejecuta en el orden en que están escritos. Después de llamar
a funcion2, la función funcion1 continúa ejecutándose e imprime el número 2. 

Así, el resultado final es 3, 1, 2.
'''

#15
def funcion1():
    print(3)
    a = funcion2()
    print(a)
    return 4
def funcion2():
    print(1)
    return 0
b = funcion1()
print(b)



