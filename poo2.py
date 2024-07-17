# Creo una estructura para los clientes
class Cliente:
    def __init__(self, dni, nombre, apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellidos)

# Y otra para las empresas 
class Empresa:
    def __init__(self, clientes=[]):
        self.clientes = clientes

    def mostrar_cliente(self, dni):
        for c in self.clientes:
            if c.dni == dni:
                print(c)
                return
        print('Cliente no encontrado')

    def borrar_cliente(self, dni):
        for i, c in enumerate(self.clientes):
            if c.dni == dni:
                del(self.clientes[i])
                print(str(c), "> BORRADO")
                return
        print('Cliente no encontrado')

# Ahora utilizo ambas estructuras
# Creo un par de clientes
hector = Cliente(dni='11111111B', nombre='Hector', apellidos='Costa Guzman')
juan = Cliente(dni='2222222B', nombre="Juan", apellidos="Gonzalez Marquez")

# Creo una empresa con los clientes iniciales
empresa = Empresa(clientes=[hector, juan])

# Muestro todos los clientes 
print("== LISTADO DE CLIENTES ==")
for cliente in empresa.clientes:
    print(cliente)

print("\n== MOSTRAR CLIENTES POR DNI ==")
# Consulto clientes por DNI
empresa.mostrar_cliente("11111111B")
empresa.mostrar_cliente("11111111A")

print("\n== BORRAR CLIENTES POR DNI ==")
# Borro un cliente por DNI
empresa.borrar_cliente("2222222B")
empresa.borrar_cliente("2222222A")

# Muestro de nuevo todos los clientes
print("\n== LISTADO DE CLIENTES ==")
for cliente in empresa.clientes:
    print(cliente)
