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
        return self.edad >= 18


persona = Persona("Sanguche", 31, "35555666")

persona.set_nombre("Milanesa")
persona.set_edad(32)
persona.set_dni("36666555")

persona.mostrar()

persona.es_mayor_de_edad()