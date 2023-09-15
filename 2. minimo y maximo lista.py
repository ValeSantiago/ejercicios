# Iniciar una lista vacía para almacenar los números ingresados
numeros = []

# Define una variable para controlar si el usuario desea continuar ingresando números
continuar = True

# Usa un bucle while para solicitar números al usuario
while continuar:
    try:
        numero = float(input("Ingrese un número (o ingrese cualquier otro valor para detenerse): "))
        numeros.append(numero)
    except ValueError:
        # Si el usuario ingresa un valor no numérico, el bucle se detiene
        continuar = False

# Imprime la lista de números ingresados
print ("Los números ingresados son:", numeros)

# Encontrar el mínimo y el máximo de la lista después de recopilar los números
if numeros:
    minimo = min(numeros)
    maximo = max(numeros)
    print("El número mínimo es:", minimo)
    print("El número máximo es:", maximo)
else:
    print("No se ingresaron números.")
