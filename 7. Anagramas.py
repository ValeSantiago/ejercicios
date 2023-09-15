def es_anagrama(palabra1, palabra2):
    # Elimina los espacios en blanco y convierte las palabras a minúsculas para una comparación sin distinción de mayúsculas y minúsculas
    palabra1 = palabra1.replace(" ", "").lower()
    palabra2 = palabra2.replace(" ", "").lower()
    
    # Ordena las letras de ambas palabras y compáralas
    return sorted(palabra1) == sorted(palabra2)

# Solicitar al usuario ingresar dos palabras distintas
palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")

# Verificar si las dos palabras son anagramas
if es_anagrama(palabra1, palabra2):
    print(f"{palabra1} y {palabra2} son anagramas.")
else:
    print(f"{palabra1} y {palabra2} no son anagramas.")
