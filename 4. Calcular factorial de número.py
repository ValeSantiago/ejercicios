def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Solicitar al usuario el número para calcular su factorial
numero = int(input("Ingrese un número para calcular su factorial: "))

# Llamar a la función factorial y mostrar el resultado
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")
