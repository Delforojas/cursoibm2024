"""""
#Definimos una variable x con una cadena
x = "El valor de (a+b)*c"

#Podemos realizar multiples asignaciones
a, b, c =4, 3, 20

#Realizamos operaciones con a,b,c
d=(a +b) * c

#Definimos una varibale booleana 
imprimir =True

#Si imprimir , print()
if imprimir:
    print(x, d)

#Salida: El valor de (a+b)*c es 14


def funcion (a, b, c):
    return a+b+c

d = funcion(10,23,3)

print (d)

print ('Hola Mundo!')

import math
print(math.pi * 4)

print(math.pi **4)

print(math.sqrt(4))

print (math. sqrt(12))


import random
num = random.random()
print (num)
lista = [1, 2, 3,4]

elem =random.choice(lista)
print (elem)

random.shuffle(lista)
print(lista)

print( 2* 3 +2*4)
print(2*(3+2)*4)


def suma(a,b):
    return a+b
resultado = suma(2,3)
resultado1= suma(2.7, 4.0)
resultado2= suma('Me gusta','Python')
print(resultado , resultado1 , resultado2)

def en_pantalla(frase1 ,frase2):
    print(frase1, frase2)

en_pantalla('Me gusta' , 'Python')

def f1(a):
    print(a)
    b=100
    def f2(x):
        print(x)
    f2(b)
f1('Python')


def factorial(x):
    if x>1:
        return x*factorial(x-1)
    else:
        return 1
var =factorial(5)
print(var)

def maxmin(lista):
    return max(lista), min (lista)
l =[1, 3, 5, 6, 0]
maximo, minimo = maxmin(l)
print(minimo, maximo, sep=' ')

a= 'Python'
print('valor fuera:', a)

def funcion():
    a=33
    print('valor dentro', a)

funcion()
print ('valor fuera', a)

G= 'Esta variable es de ambito Global'
def f1():
    E='Esta variable es local a f1'
    def f2():
        L='Esta variable es local a f2'
        print(L, E, G, sep= '\n')
        f2()
f1()

G = 'Esta variable es de ambito Global'
def f1():
    E = 'Esta variable es local a f1'
    def f2():
        L = 'Esta variable es local a f2'
        E = 'E tambien es local a f2'
        G = 'G tambien es local a f2'
        print(L, E, G, sep='\n')
        def f3():
            print(E, G, sep='\n')
        f2()
        f3() 

f1()

def suma (a, b):
    return a +b

print (suma(2, 3))
print (suma(40, 30))

def suma(a, b):
    a= 3
    b =4
    return a+b
a, b = 5, 10
print (suma(a, b))
print(a, b)


def minimo(l):
    l[0] =1000
    return min(l)
l =[1, 2, 3]
print(l)
print(minimo(l))
print(l)

def f(a,b,c):
    print(a,b,c)
#f(1,2,3)
#f(c=12, a=10, b=100)

def f(a, b=10, c=30):
    print (a,b,c)

f(1)
f(1, 12)
f(1, 12, 19)

def f(*args):
    print(args)

f()
f(1)
f(1, 2)
f(1, 2, 3, 4, 5, 6)

def f(**args):
    print(args)
f()
f(a=1)
f(a=1, b=2)
f(a=1, c=3, b=2)

def f (a, b, c, d):
    print(a, b, c, d)
argumentos ={'b':20, 'a':1, 'c':300, 'd':4000}
f(**argumentos)
argumentos = {'b':200, 'c':300, 'd':400}
f(10, **argumentos)    

def f(a, *b, c):
    print(a, b, c)
f(1, c=2)
f(1, 2, c=3)
f(1, 2, 3, 4, 5, c=10)

la =[1, 2, 3, 4, 5]
lb =list('abcde')
lc= list('ABCDE')

zlist=list(zip(la, lb, lc))
zlist
a, b, c =zip(*zlist)
print(la, lb, lc, sep = '\n')
print(la, lb)

texto= input("Introduce algo por teclado : ")
type (texto)
Out: str
print(texto)

l = list()
texto= input("Introduce un numero por teclado: ")
if texto.isnumeric():
    num = int(texto)
    l.append(num)
    print("Numero " +str(num) +"añadido a la lista")
else:
    print("No has introducido un numero entero")

d ={"50862634 " : 37 , "43394932" : 32}
texto = input("Introduce un documento de identidad")
if texto in d:
    print("La edad de" + texto + "es" + str(d[texto]))
else:
    edad = input("Documento no existente.Introduce edad: ")
    if edad.isnumeric():
        num =int(edad)
        d[texto] = num
        print("Añadido al diccionario")
print(d)


#read python dict from a file 
pkl_file=open('myfile.pkl', 'rb')
mydict2 =pickle.load(pkl_file)
pkl_file.close

#write python dict to a file
mydict ={'a':1, 'b':2, 'c':3}
output = open ('myfile.pkl', 'wb')
pickle.dump(mydict, output)
output.close()


import pickle
from pathlib import Path

#create an empty dictionary from
file_name = input("Introduce el nombre del archivo con los datos:")

#Comprobamos que existe 
path = Path(file_name)
if path.is_file():
    #open file in reading mode
    input_file = open (file_name, 'rb')
    d=pickle.load(input_file)
    #Close de file
    input_file.close()
else:
    print("El file no existe, creamos diccionario vacio")

#Check for values or add new ones
document_number = input("Introduce un documento de identidad")
if document_number in d : #Check wether it is on dict or not
       print ("La edad de " + document_number + "es" +str(d[document_number]))
else:
     age = input("Documento no existente.Introduce edad: ")
     if age.isnumeric():
          num = int(age)
          d[document_number] = num
          print ("Añadido al diccionario")
#Save dict on file and close
output_file = open(file_name,'wb')
pickle.dump(d, output_file)
output_file.close()


a = 0
while a<3:
    print(a, end='')
    a +=1
print(a)
print('Hemos salido fuera del while')

a = 5 
while a:
    print(a, end='')
    if a == 2:
          break
    a -= 1
print ('\Fuera del Bucle')
print ('Valor de a:{}'.format(a))

a = 7
while bool(a):
      a -= 1
      if a % 2 == 0:
           continue
      print(a, end='')
print('\nFuera del Bucle')
a =12
b = a //2
while b > 1:
    if a % b == 0:
        print('{b}es factor de {a}'.format(b,a))
        break
    b -= 1
else: 
     print('{} es primo'.format(a))
print('Fuera del bucle.')   

for s in ['Me ', 'gusta ', 'python! ']:
    print(s, end='')

a = 0
for x in [1, 2, 3, 4]:
    a += x
print (a)

for c in 'Me gusta python! ':
    print(c, end=' ')

keys =['nombre', 'apellidos', 'edad']
values=['Guido', 'van Rossum', '60']
d = dict(zip(keys, values))

for k in d:
    info= '{}: {}'.format(k, d[k])
    print(info)

a1 = [10, 20, 30, 40]
b1 = [5, 25, 50, 10]
for a, b in zip(a1, b1):
    m = max (a,b)
    print(m , end=' ')


keys =['nombre', 'apellidos', 'edad']
values=['Guido', 'van Rossum', '60']
d = dict(zip(keys, values))
for k, v in d.items():
    print('{}:{}'.format(k,v))


zen = '''\
...Bello es mejor que feo.
...Explicito es mejor que implicito
...Simple es mejor que complejo
...complejo es mejor que complicado
...'''
f = open('short.zen.txt', 'w')
f.writelines(zen)
f.close
f = open ('short.zen.txt', 'r')
f.readline()
'Bello es mejor que feo.\n'
f.readline()
'Explicito es mejor que implicito\n'
f.readline()
'Simple es mejor que complejo\n'
f.readline()
'complejo es mejor que complicado'
f.readline
''
for linea in open('short.zen.txt'):
     print(linea.upper(), end='')

lista=[1, 2, 3]
next(lista)


li= iter(lista)
next(li)
1
next(li)
2

next(li)
3

next(li)


class Repetidor():

    def __init__(self, veces, item):
       self.veces = veces
       self.item = item
       self.counter = 0
    def __next__(self):
        if self.counter == self.veces:
            raise StopIteration('Iterador consumido')
        self.counter += 1
        return self.item
    def __iter__(self):
        return self

for r in Repetidor(3, 'Python'):
    print(r, end=' ')


class Repetidor():
    def __init__(self, veces, *items):
        self.veces=veces
        self.items= items
    
    def __iter__(self):
        return iter(self.items *self.veces)
for r in Repetidor(3, 'a', 'b', 'c'):
    print(r, end='')

nombre = input('introduce tu nombre')

print("Hola, " + nombre)
print(type(nombre))

num = int (input('Introduce un numero'))
add = num+1
print(add)


a, b, c = map(int,input('Introduce los numeros: ').split())
print ("Los numeros son: ", end= ' ')
print(a, b, c)


lista = list(map(int, input('Introduzca los elementos de la lista').split()))
conjunto = set(map(int, input('Introduzca los elementos del set').split()))

print('Lista', lista)
print(conjunto)


lista = list()
conjunto = set()
l = int(input('Introduzca el tamaño de la lista: '))
s = int(input('Introduzca el tamaño del conjunto: '))

print('Introduzca el tamaño de la lista: ' )
for i in range (l):
    lista.append(int(input()))
print('Introduzca el tamaño del conjunto: ' )
for i in range (s):
    elemento = int(input())
    conjunto.add(elemento)

print('Lista:', lista)
print('Conjunto', conjunto)


T =(2, 3, 4, 5, 6)
print("Tupla inicial")
print(T)
L=list(T)
elem = int( input('Introduzca el nuevo elemento: '))
L.append(elem)
T=tuple(L)
print("Tupla final")
print(T)

def indexador(objeto, indice):
    return objeto[indice]
try:
  print(indexador('Python', 3))
except IndexError:
   print('Has puesto un índice muy grande')
   print('Hemos salido del try-catch')

notaIn = int (input('Introduzca nota:'))

if notaIn <5:
    calificacion = 'Suspenso'
else: calificacion ='Aprobado'
print(calificacion)


variable = 19
if variable == True:
    print('contiene información')
else:
    print('no contiene información')


edad = int (input('Introduce edad: '))
if edad < 18:
    print ('No puedes pasar')
elif edad > 100:
    print ('edad incorrecta')
else:
    print('Adelante')

nota = int(input('Introduce tu nota: '))

if nota <5:
    print('suspenso')
elif nota<7:
    print ('aprobado')
elif nota<9:
    print ('notable')
else:
    print('sobresaliente')

num1 = 5
num2 =10
if num1<num2: print(num2,'es mayor qque', num1)

edad =80
if 0<edad<100:
    print('edad correcta')
else:
    print('edad incorrecta')

salarioPresidente = int (input("Introduce salario presidente: "))
print('El salario del presidente es de ', salarioPresidente)
salarioDirector = int (input("Introduce salario director: "))
print('El salario del director es de ', salarioDirector)
salarioJefe = int (input("Introduce salario jefe: "))
print('El salario del jefe es de ', salarioJefe)
salarioOperario = int (input("Introduce salario operario: "))
print('El salario del operario es de ', salarioOperario)

if salarioOperario<salarioJefe<salarioDirector<salarioPresidente:
    print('todo ok')
else:
    print('algo va mal')

distancia = int (input ('Introduce distacia: '))
numH= int(input('Introduce numero de hermanos'))
notaMedia = int(input('Introduce nota media'))
if distancia>20 or numH<2 or notaMedia<=5:
    print('no eres candidato a la beca')
else:
    print ('Eres candidato a la beca')


edad = int(input (' introduzca su edad:'))
dinero = int(input('introduzca su presupuesto:'))

if edad<18:
    print('no tienes la edad suficiente para conducir')
else:
    if dinero<20000:
        print('tienes la edad pero no el dinero')
    else:
        print('puedes comprar el coche')

if num % 2 == 0:
    print('par')
else: print('impar')

for i in [1,5,10]:
    print('hola')

for i in ['primavera', 'verano', 'invierno','otoño']:
    print(i)


miEmail=input ("Introduce email")
email= False
for i in miEmail:
    if i =='@':
        email=True
if email:
    print ("El mail es correcto")
else:
    print('El email es incorrecto')


for i in range(14,20 , 2):
    print(f'Valor de la variable {i}')


valido=False
email= input('Introduce tu email: ')
for i in range(len(email)):
    if email[i]=='@':
        valido=True
if valido:
    print('email correcto')
else:
    print('email incorecto')

for x in 'banana':
    print(x)

frutas=['manzana', 'banana', 'cereza']
for x in frutas:
    print(x)
    if x == 'banana':
        break

frutas = ['manzana', 'banana', 'cereza']
for x in frutas:
    if x == 'banana':
        break
    print(x)

frutas = ['manzana', 'banana', 'cereza']
for x in frutas:
    if x == 'banana':
        continue
    print(x)

for x in range(2,10,3):
    print(x)


color =['verde','amarillo','roja']
frutas=['manzana','banana','cereza']

for x in color:
    for y in frutas:
      print(x,y)
edad = 0 
while edad< 18:
    edad=edad+1
print('Tienes'+str(edad))

edad= int(input("Introduce edad: "))
while edad<0:
    print("Edad incorrecta")
    edad=int(input('Introduce edad: '))
print("tu edad es: "+str(edad))

import math;
intentos= 0;
num = int(input("Introduce un numero: "))

while num >0:
    intentos=intentos+1
    num= int(input("Introduce numero: "))

    if intentos==2:
        print('demasiados intentos')
        break;
if intentos<2:
    intentos=intentos+1
    solucion=math.sqrt(num)
    print("La raiz cuadrada de "+str(num)+" es "+str(solucion))

miLista=list("PYTHON")
print(miLista)


miLista =[22, True, "unacadena", [1,2]]
print(miLista[2])

miLista =[[1,2] , [3,4] ,[5,6]]
miVar = miLista[1][0]
print(miVar)


def miFuncion(listaFrutas):
    for x in listaFrutas:
        print(x)
frutas =['manzana', 'banana', 'cereza']
miFuncion(frutas)


miTupla =("manzana", "banana", "cereza")
print(miTupla[1])


miTupla = tuple(("manzana", "banana", "cereaza","kiwi", "melon","mango"))
print(miTupla[2:5])

miTupla =("manzana", "banana", "cereza")
miLista =list(miTupla)
miLista[1] ="kiwi"
miTupla = tuple(miLista)
print(miTupla)


miTupla =("kiwi", "banana", "cereza")
if "manzana" in miTupla:
        print('manzana esta en la tuppla')
else: 
        print('po no')


miTupla =("manzana", "banana", "cereza")
print(len(miTupla))

tupla1 = ('a', 'b', 'c')
tupla2 = (1, 2, 3)
tupla3 = tupla1 + tupla2
print(tupla3)

miTupla =("manzana", "banana", "cereza","manzana")
print(miTupla.count('manzana'))


miTupla=("Angel",4,5.35, True, 4)
nombre,num1,num2,valor1,num3= miTupla
print(nombre)
print(num1)
print(num2)
print(valor1)
print(num3)


miDiccionario={
    'brand': 'ford',
    'model':'mustang',
    'year':'1964'
}
print(miDiccionario)


peliculas = {"Love Actually": "RichardCurtis",
"Kill Bill": "Tarantino",
"Amélie": "Jean-Pierre Jeunet"}
peliculas["killbill"] = "Quentin Tarantino"
print(peliculas)

miDiccionario3 = {'nombre':'jordan','Equipo':'bulls','anillos':[1993,1994,1995,1996]}
print((miDiccionario3["anillos"]))


peliculas = {"Love Actually": "RichardCurtis",
"Kill Bill": "Tarantino",
"Amélie": "Jean-Pierre Jeunet"}
peliculas.pop("Love Actually")
print(peliculas)

lista_claves=['nombre', 'edad']
lista_valores=['Angel', 43]
diccionario =dict(zip(lista_claves,lista_valores))
print(diccionario)
'nombre' in diccionario


peliculas = {"Love Actually": "RichardCurtis",
"Kill Bill": "Tarantino",
"Amélie": "Jean-Pierre Jeunet"}
for x in peliculas:
    print (peliculas[x])
print (len(peliculas))


miDiccionario = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
miDiccionario['color'] ='red'
print(miDiccionario)
miDiccionario.popitem()
print(miDiccionario)
miDiccionario.popitem()
print(miDiccionario)

miDiccionario = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
midict = dict(miDiccionario)
print(miDiccionario)


child1={
    "name" : "email",
    "year" : 2004
}
child2={
    "name" : "paco",
    "year" : 2007
}
child3={
    "name" : "pepe",
    "year" : 2009
}
myfamily={
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(myfamily['child2'])


conjunto ={'angel', 'poder', 'paca'}
conjunto2 ={'manolo','juan','pepe'}
conjunto3 =set(('lolo','fran','neo'))
print(conjunto3)
conjunto.add('antonio')
conjunto2.update({'tito', 'roi'})
print(conjunto)
print(conjunto2)
union = conjunto | conjunto2
print(union)
interseccion = conjunto2 & conjunto3
print(interseccion)

miSet ={'manzana', 'banana' , 'cereza'}
x=miSet.pop()
print(x)
print(miSet)
miSet.clear()
print(miSet)
del miSet
print(miSet)


set1 = {'a','b','c'}
set2 = {1, 2 ,3}
set3 =set1.union(set2)
print(set3)
set1.update(set2)
print(set1)


def my_funcion():
    print("Estamos ejecutando la funcion")

print(my_funcion())


def suma():
    num1 =3
    num2 =5
    print("suma = ", num1+num2)

print(suma())


def suma():
    num1=3
    num2=5
    resultado = num1 + num2
    return print('El resultado es', resultado)

print(suma())


def miFunción():
      print('this will print')
      print('so will this')
      x=7
print(miFunción())


def duplica(num):
    x =num *2
    return x

print(duplica(4))

def multiplica(arg1, arg2):
    return arg1 * arg2

print(multiplica(2,5))


def suma(a, b):
    return a + b

result = suma (b=2, a=3)
print(result)

def f(x, y):
    return x*2, y*2
a, b = f(1, 2)


def miFuncion(num1, num2):
    return(num1+ num2)
print(miFuncion(2,3))

def holaConNombre(name):
    print("Hola " + name  )

holaConNombre("Angel")

"""
def imprimir(precio, iva=1.21):
    print(precio*iva)

print(imprimir(1.08,300))

