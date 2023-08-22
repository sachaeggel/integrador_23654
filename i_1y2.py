# Para encontrar el MCD de a=50 y b=12 utilizando el algoritmo de Euclides, 
# primero debemos dividir a=50 por b=12. El cociente es q=4 y el resto es r=2. 
# Luego, dividimos b=12 por r=2. El cociente es q=6 y el resto es r=0. 
# Como el resto es 0, el MCD de 50 y 12 es el último divisor no nulo, 
# que en este caso es b=2.

def MCD(a,b):
    r = a%b #resto
    if r!=0:
        while True:
            a = b
            b = r
            r = a%b
            if r == 0:
                return b
    return b

# Para calcular el mcm(a, b) se utiliza el MCD(a, b)
# junto a ésta fórmula mcm = (a * b) / MCD(a, b)

def mcm(a, b):
    m = MCD(a,b)
    r = (a*b)/m 
    return int(r)

print("1-Máximo Común Divisor \n2-mínimo común múltiplo \nIngresar opción y presionar Enter")
x = int(input())
a = int(input("Ingresar primer número: "))
b = int(input("Ingresar segundo número: "))

if x == 1:
    resultado = MCD(a,b)
    print(f"MCD = {resultado}")
elif x == 2:
    resultado = mcm(a,b)
    print(f"mcm = {resultado}")