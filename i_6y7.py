# PERSONA
class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def set_nombre(self, nuevo_nombre):
        if nuevo_nombre.strip() != "":
            self.nombre = nuevo_nombre
        else:
            print("El nombre no puede estar en blanco.")

    def set_edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.edad = nueva_edad
        else:
            print("La edad tiene que ser mayor a 0")

    def set_dni(self, nuevo_dni):
        if len(nuevo_dni) >= 7 <= 8:
            self.dni = nuevo_dni
        else:
            print("Formato DNI incorrecto")


    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad
    
    def get_dni(self):
        return self.dni
    
    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("DNI:", self.dni)

    def es_mayor_de_edad(self):
        return print(f"Mayor de edad: {self.edad >= 18}")

# CUENTA
class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.__cantidad = cantidad

    def get_cantidad(self):
        return self.__cantidad
    
    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.__cantidad = cantidad
            
    def mostrar(self):
        print(f"Titular: {self.titular.nombre}")
        print(f"Cantidad: {self.__cantidad}")
        
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
            
    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad

# INSTANCIAR PERSONA
sanguche = Persona("Sanguche", 31, "35555666")
# persona.set_nombre("Milanesa")
# persona.set_edad(32)
# persona.set_dni("36666555")
sanguche.mostrar()
sanguche.es_mayor_de_edad()

# INSTANCIAR CUENTA
cuenta_Sanguche = Cuenta(sanguche)
# Ingresar dinero en la cuenta
cuenta_Sanguche.ingresar(1000)
cuenta_Sanguche.mostrar()
# Retirar dinero de la cuenta
cuenta_Sanguche.retirar(500)
cuenta_Sanguche.mostrar()