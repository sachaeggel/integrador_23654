oracion = input("Escribir una oración:\n")

def separador(chain):
    diccionario = {}
    palabras = chain.split()
#    unico = list(set(palabras))
    unico = set(palabras)
    for palabra in unico:
        frecuencia = palabras.count(palabra)
        diccionario[palabra]=frecuencia
    return diccionario

dic = separador(oracion)
print(f"Diccionario PALABRA : FRECUENCIA\n{dic}")
