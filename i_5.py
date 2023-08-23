#recursiva
def get_int_r():
    try:
        number = int(input("Ingresá un número entero:\n"))
        return "Perfecto (recursivo)"       
    except ValueError as error:
        print(error)
        return get_int_r()

#iterativa
def get_int_i():
    while True:
        try:
            number = int(input("Ingresá un número entero:\n"))
            return "Perfecto (iterativo)"
        except ValueError as error:
            pass

x = input("Usar forma RECURSIVA o ITERATIVA?\nR o I?")
if x == "r" or "R":
    x = get_int_r()
    print(x)
elif x == "i" or "I":
    x = get_int_i()
    print(x)

