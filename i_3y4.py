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

def tupla(a):
    x = list(a.values())
    mayor = max(x)
    final=[]
    for palabra in a:
        valor = a[palabra]
        if valor >= mayor:
            conc=palabra, valor
            final.extend(conc)
    return tuple(final)

dic = separador(oracion)
print(f"Diccionario PALABRA : FRECUENCIA\n{dic}")
a = tupla(dic)
print(f"PALABRA más repetida y FRECUENCIA:{a}")
