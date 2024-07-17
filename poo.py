#Definimos unos cuantos clientes
clientes = [
     {'Nombre':'Hector', 'Apellidos':'Costa Guzman','dni':'154325A'},
     {'Nombre':'Juan','Apellidos':'Gonzalez Marquez', 'dni':'15433625B'}
     ]
#Creamos una funcion que muestra un cliente en una lista a partir del DNI
def mostrar_cliente(clientes, dni):
    for c in clientes:
        if(dni==c['dni']):
            print('{} {}'.format(c['Nombre'],c['Apellidos']))
            return 
        print('Cliente no encontrado')

#Creamos una funcion que borra un cliente en una lista a partir del dni
def borrar_cliente(clientes,dni):
    for i, c in enumerate(clientes):
        if(dni ==c['dni']):
            del(clientes[i])
            print(str(c), ">BORRADO")
            return
    print('Cliente no encontrado')

#Fijate muy bien como se utiliza el codigo estructurado 

print("==LISTADO DE CLIENTES==")
print(clientes)

print("\nMOSTRAR CLIENTES POR DNI")
mostrar_cliente(clientes,'154325A')
mostrar_cliente(clientes,'154336257B')

print("\n BORRAR CLIENTES POR DNI")
borrar_cliente(clientes,'154325l')
borrar_cliente(clientes,'15433625B')

print("==LISTADO DE CLIENTES==")
print(clientes)