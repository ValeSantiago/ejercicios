# Iniciar una lista vacía para almacenar las respuestas ingresadas
respuestas = []

# Usa un bucle while para solicitar respuestas al usuario
while True:
    entrada = input("Ingrese un número o texto (o ingrese una cadena vacía para detenerse): ")
    
    if not entrada.strip():
        break  # Si la entrada es una cadena vacía, detenemos el bucle
    
    respuestas.append(entrada)

# Muestra las respuestas ingresadas
print("Respuestas ingresadas:", respuestas)

# Invierte la lista de respuestas ingresadas
respuestas.reverse()

# Muestra la lista en orden inverso
print("La lista en orden inverso es:", respuestas)
