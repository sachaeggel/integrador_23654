diccionario = {"sacha":1, "augusto":5, "eggel":3, "sanguche":5, "milanesa":1}

def tupla(a):
    x = list(a.values())
    mayor = max(x)
    final=[]
    for palabra in a:
        valor = a[palabra]
        if valor >= mayor:
           x = final.append(palabra)
    return x

sacha = tupla(diccionario)
print(sacha)