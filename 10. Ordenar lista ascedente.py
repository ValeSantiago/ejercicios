# Solicitar al usuario ingresar la cantidad de números en la lista
n = int(input("Ingrese la cantidad de números que desea ordenar: "))

# Inicializar una lista vacía para almacenar los números
numeros = []

# Solicitar al usuario ingresar los números y agregarlos a la lista
for i in range(n):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

# Ordenar la lista de números en orden ascendente
numeros.sort()

# Imprimir la lista ordenada
print("Lista ordenada de forma ascendente:")
for numero in numeros:
    print(numero)
