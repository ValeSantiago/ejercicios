def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def lista_primos_en_rango(inicio, fin):
    primos = []
    for numero in range(max(2, inicio), fin + 1):
        if es_primo(numero):
            primos.append(numero)
    return primos

# Solicitar al usuario ingresar el rango
inicio = int(input("Ingrese el número de inicio del rango: "))
fin = int(input("Ingrese el número final del rango: "))

# Generar la lista de números primos en el rango especificado
primos_en_rango = lista_primos_en_rango(inicio, fin)

# Imprimir la lista de números primos
print(f"Números primos en el rango de {inicio} a {fin}:")
print(primos_en_rango)
