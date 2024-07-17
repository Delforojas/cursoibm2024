#Declaracion de la clase 
class Coche():

#Declaracion de los atributos
 largo =250
 ancho = 120
 ruedas = 4
 peso = 900
 color = "rojo"
 is_enMarcha = False

#Declaración de métodos
 def arrancar(self):#self hace referenia a la instancia de clase
   self.is_enMarcha = True #como si pusiesesemos miCoche.es enMArcha = True

 def estado(self):
   if(self.is_enMarcha == True):
      return "El coche está arrancado"
   else:
      return "El coche está parado"
   
miCoche = Coche()
miCoche2 = Coche()

#Acceso a un atributo de la clase Coche.Nomenclatura del punto
print("El largo del coche es de ", miCoche.largo,"cm")
miCoche.arrancar()
print(miCoche.estado())

#Acceso a un método de la clase Coche.Nomenclatura del punto.
print("El coche está arrancado", miCoche.arrancar())

#Modificamos el valor de una propiedad 
miCoche2.ruedas = 10
print("El coche2 tiene", miCoche2.ruedas,"ruedas")