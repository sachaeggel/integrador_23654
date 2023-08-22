oracion = input("Escribir una oración:\n")

def separador(cad):
    diccionario = {}
    cadena = cad.split()
    unico = set(cadena)
    for palabra in cadena:
        x = cad.count(cadena)
        #if x > 1:
        diccionario[x]=palabra #acá está el quilombo, reemplaza palabra!!
    return diccionario


sacha = separador(oracion)
print(sacha)
