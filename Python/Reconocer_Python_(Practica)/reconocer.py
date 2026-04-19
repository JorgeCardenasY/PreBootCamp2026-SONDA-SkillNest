numero1 = 70 #dato integer
numero2 = 3.14 #dato float o punto flotante
booleano = False #dato booleano
cadena = 'Hola Mundo' #dato string o cadena de texto
ingredientes_pastel = ['Harina', 'Leche', 'Huevos', 'Vainilla', 'Chocolate'] #dato lista o array
persona = {'nombre': 'Patricio', 'pais': 'México', 'edad': 35, 'soltero': False} #dato diccionario
frutas = ('guayaba', 'fresa', 'papaya') #dato tupla
print(type(frutas)) #imprime el tipo de dato de la variable 'frutas'. En este caso es una tupla o tuple.
print(ingredientes_pastel[2]) #imprime el elemento en la posición 2 de la lista 'ingredientes_pastel'. En este caso es 'Huevos'.
ingredientes_pastel.append('Mantequilla') #agrega el elemento 'Mantequilla' al final de la lista 'ingredientes_pastel'.
print(persona['nombre']) #imprime el valor asociado a la clave 'nombre' en el diccionario 'persona'. En este caso es 'Patricio'.
persona['nombre'] = 'Kevin' #asigna el valor 'Kevin' a la clave 'nombre' en el diccionario 'persona'.
persona['color_ojos'] = 'cafe' #agrega la clave 'color_ojos' con el valor 'cafe' al diccionario 'persona'.
print(frutas[2]) #imprime el elemento en la posición 2 de la tupla 'frutas'. En este caso es 'papaya'.

if numero1 > 45:
    print("Numero mayor")
else:
    print("Numero menor") #imprime "Numero mayor" porque el valor de 'numero1' es 70, que es mayor que 45.

if len(cadena) < 5:
    print("Cadena corta")
elif len(cadena) > 15:
    print("Cadena larga")
else:
    print("Cadena perfecta") #imprime "Cadena perfecta" porque la longitud (len(cadena))de 'cadena' es 11, que no es ni menor que 5 ni mayor que 15.

for x in range(8):
    print(x) #imprime los números del 0 al 7
for x in range(2,8):
    print(x) #imprime los números del 2 al 7
for x in range(2,8,2):
    print(x) #imprime los números del 2 al 7, saltando de dos en dos
x = 0
while(x < 8):
    print(x)
    x += 1 #x = x + 1

ingredientes_pastel.pop() #elimina el último elemento de la lista 'ingredientes_pastel'. En este caso es 'Mantequilla'.
ingredientes_pastel.pop(1)  #elimina el elemento en la posición 1 de la lista 'ingredientes_pastel'. En este caso es 'Leche'.

print(persona) #imprime el diccionario 'persona' con las modificaciones realizadas. En este caso es {'nombre': 'Kevin', 'pais': 'México', 'edad': 35, 'soltero': False, 'color_ojos': 'cafe'}.
persona.pop('color_ojos') #elimina la clave 'color_ojos' y su valor asociado del diccionario 'persona'. En este caso se elimina 'color_ojos': 'cafe'.
print(persona) # vuelve a imprimir el diccionario 'persona' con la modificación realizada.

for ingrediente in ingredientes_pastel:
    if ingrediente == 'Harina':
        continue
    print('Después de la primera sentencia')
    if ingrediente == 'Chocolate':
        break #Este ciclo for recorre cada elemento de la lista 'ingredientes_pastel'. Si el ingrediente es 'Harina', se salta a la siguiente iteración sin ejecutar el resto del código dentro del ciclo (continue). Si el ingrediente es 'Chocolate', se detiene completamente el ciclo (break). Para cualquier otro ingrediente, se imprime 'Después de la primera sentencia'.

def imprime_hola_10_veces():
    for numero in range(10):
        print('Hola')

imprime_hola_10_veces() #Llama a la función 'imprime_hola_10_veces', que imprime 'Hola' diez veces. La función no recibe ningún argumento y, dado el rango de 0 a 9, imprimirá 'Hola' diez veces.

def imprime_hola_n_veces(n):
    for numero in range(n):
        print('Hola') #Define una función llamada 'imprime_hola_n_veces' que toma un argumento 'n'. La función imprime 'Hola' 'n' veces utilizando un ciclo for que itera desde 0 hasta n-1. 

imprime_hola_n_veces(5) #Llama a la función 'imprime_hola_n_veces' con el argumento 5, por lo que se imprimirá 'Hola' cinco veces.

def imprime_hola_n_o_diez_veces(n = 10):
    for numero in range(n):
        print('Hola') #Define una función llamada 'imprime_hola_n_o_diez_veces' que toma un argumento opcional 'n' con un valor predeterminado de 10. La función imprime 'Hola' 'n' veces utilizando un ciclo for que itera desde 0 hasta n-1. Si no se proporciona un valor para 'n' al llamar a la función, se utilizará el valor predeterminado de 10.

imprime_hola_n_o_diez_veces() #Llama a la función 'imprime_hola_n_o_diez_veces' sin argumentos, por lo que se imprimirá 'Hola' diez veces utilizando el valor predeterminado de 'n'. Por ello, se imprimirá 'Hola' sólo diez veces.
imprime_hola_n_o_diez_veces(5) #Llama a la función 'imprime_hola_n_o_diez_veces' con el argumento 5, por lo que se imprimirá 'Hola' cinco veces. Esta función sobrescribe el valor predeterminado de 'n' con el valor proporcionado (5) y, por lo tanto, se imprimirá 'Hola' cinco veces.


"""
Sección BONUS
"""

print(numero3) # Esto generará un error de tipo 'NameError' debido a que la variable 'numero3' no ha sido definida antes de esta línea.
numero3 = 86 # Se define la variable 'numero3' con el valor de 86.
frutas[0] = 'naranja' # Este array intenta modificaractualizar el valor del primer elemento de la tupla 'frutas' a 'naranja'. Es relevante señalar que esto generará un error de tipo 'TypeError' porque 'frutas' es una tupla, y las tuplas son inmutables, lo que significa que no se pueden modificar después de su creación.
print(persona['hobbies']) # Este código intenta acceder al valor asociado a la clave 'hobbies' en el diccionario 'persona'. Sin embargo, dado que la clave 'hobbies' no existe en el diccionario, esto generará un error de tipo 'KeyError'.
print(ingredientes_pastel[11]) # Este código intenta acceder al elemento en la posición 11 de la lista 'ingredientes_pastel'. Si la lista no tiene al menos 12 elementos (índices del 0 al 11), esto generará un error de tipo 'IndexError' debido a que se está intentando acceder a un índice que está fuera del rango de la lista.
print(booleano) # Este código imprimirá el valor de la variable 'booleano', que es 'False'. No generará ningún error, ya que 'booleano' está definido correctamente como un valor booleano.
frutas.append('manzana') # Este código intenta agregar el elemento 'manzana' al final de la tupla 'frutas' utilizando el método 'append' (append agrega un elemento al final de una *lista*). Sin embargo, esto generará un error de tipo 'AttributeError' porque las tuplas no tienen un método 'append', ya que son inmutables y no se pueden modificar después de su creación.
frutas.pop(1) # Este código intenta eliminar el elemento en la posición 1 (segunda posición) de la tupla 'frutas' utilizando el método 'pop' (pop elimina un elemento de una *lista*). Sin embargo, esto generará un error de tipo 'AttributeError' porque las tuplas no tienen un método 'pop', ya que son inmutables y no se pueden modificar después de su creación.