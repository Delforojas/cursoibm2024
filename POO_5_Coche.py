class Coche:
    # Declaracion de los atributos
    largo = 250
    ancho = 120
    ruedas = 4
    peso = 900
    color = "rojo"
    is_enMarcha = False

    def __init__(self):
        self.largo = 250
        self.ancho = 120
        self.ruedas = 4
        self.peso = 900
        self.color = "rojo"
        self.is_enMarcha = False

    # Declaracion de metodos
    def arrancar(self):
        # self hace referencia a la instancia de la clase 
        self.is_enMarcha = True
        # Es como si pusiesemos miCoche.is_enMarcha = True

    def estado(self):
        if self.is_enMarcha:
            return "El coche está arrancado"
        else:
            return "El coche está parado"

# Declaracion de una instancia de la clase, objeto de clase o ejemplar de clase
coche_1 = Coche()

# Acceso a un atributo de la clase Coche. Nomenclatura del punto.
coche_1.ruedas = 7
print("El largo del coche es de", coche_1.largo, "cm")

# Acceso a un metodo de la clase Coche. Nomenclatura del punto.
coche_1.arrancar()
print(coche_1.estado())

print("El coche está arrancado:", coche_1.is_enMarcha)

#Declaración de dos instancias de clase pasandoles los parametro requeridos por el constructor
coche_1 = Coche(100,100,4,1200,"amarillo", True)
coche_2 = Coche (420, 150,4,1500,"verde",False)