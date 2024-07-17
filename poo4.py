class Usuario:
    # Atributos de la clase
    nombre = 'Delfin'
    edad = 37
    login = "delfo"
    password = 1234
    email = 'Perro'
    telefono = 600790607

    def resumen(self):
        print(f'Nombre: {self.nombre}\n'
              f'Edad: {self.edad}\n'
              f'Login: {self.login}\n'
              f'Email: {self.email}\n'
              f'Telefono: {self.telefono}\n')

    def cambiaEdad(self):
        edadIntroducida = int(input("Introduce edad entre 18-100: "))
        if 18 < edadIntroducida < 100:
            self.edad = edadIntroducida
            print("Edad Introducida correcta")
        else:
            print("La edad introducida no es correcta.")
            self.cambiaEdad()

    def muestraEdad(self):
        print("La edad del usuario es:", self.edad, "años")

# Creación de una instancia de la clase Usuario a la que llamaremos administrador
administrador = Usuario()

# Una vez creado el objeto administrador, hacemos uso del método resumen()
administrador.resumen()

# Usamos los métodos cambiaEdad() y muestraEdad() de la clase Usuario
administrador.cambiaEdad()
administrador.muestraEdad()