# Solicitar al usuario ingresar una lista de números separados por comas
entrada_usuario = input("Ingrese una lista de números separados por comas: ")

# Dividir la entrada del usuario en una lista de cadenas de caracteres
numeros = entrada_usuario.split(",")

# Convertir las cadenas de caracteres a números enteros
numeros = [int(numero.strip()) for numero in numeros]

# Verificar si hay al menos dos elementos en la lista
if len(numeros) < 2:
    print("La lista debe contener al menos dos elementos.")
else:
    # Encontrar el elemento más grande en la lista
    maximo = max(numeros)
    
    # Eliminar el elemento más grande de la lista
    numeros.remove(maximo)
    
    # Encontrar el segundo elemento más grande en la lista (ahora que el más grande ha sido eliminado)
    segundo_maximo = max(numeros)
    
    print(f"El segundo elemento más grande en la lista es: {segundo_maximo}")
