"""
Crear una función para sumar los valores
recibidos de tipo numérico,
utilizando argumentos variables *args
como parámetro de la función
y regresar como resultado la suma de
todos los valores pasados como
argumentos.


def sumar_valores(*args):
    resultado = 0
    #Iteramos cada elemento
    for valor in args:
        #resultado = resultado + valor
        resultado += valor
    return resultado
print(sumar_valores(3, 5, 9, 4, 6, 45, 444))

#Distintos tipos de datos como argumentos en python

nombres =['Juan','pepe', 'rol']

def desplegarnombres(nombres):
    for nombre in nombres:
        print(nombre)

print(desplegarnombres(nombres))
print(desplegarnombres('carlos'))
print(desplegarnombres((10,11)))
"""
def factorial(numero):
    if numero== 1:
        return 1
    else:
        return numero * factorial(numero-1)
    
numero = 6
resultado = factorial(numero)
print(f'El factorial de {numero} es ¨{resultado}')