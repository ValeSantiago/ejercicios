def ingresar_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = float(input(f"Ingrese el valor para la fila {i+1}, columna {j+1}: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

filas_a = int(input("Ingrese el número de filas de la matriz A: "))
columnas_a = int(input("Ingrese el número de columnas de la matriz A: "))
matriz_a = ingresar_matriz(filas_a, columnas_a)

filas_b = int(input("Ingrese el número de filas de la matriz B: "))
columnas_b = int(input("Ingrese el número de columnas de la matriz B: "))
matriz_b = ingresar_matriz(filas_b, columnas_b)

def producto_matrices(a, b):
    filas_a = len(a)
    filas_b = len(b)
    columnas_a = len(a[0])
    columnas_b = len(b[0])
    if columnas_a != filas_b:
        return None
    # Asignar espacio al producto. Es decir, rellenar con "espacios vacíos"
    producto = []
    for i in range(filas_b):
        producto.append([])
        for j in range(columnas_b):
            producto[i].append(None)
    # Rellenar el producto
    for c in range(columnas_b):
        for i in range(filas_a):
            suma = 0
            for j in range(columnas_a):
                suma += a[i][j]*b[j][c]
            producto[i][c] = suma
    return producto

producto = producto_matrices(matriz_a, matriz_b)

if producto:
    # Imprimir resultado
    for fila in producto:
        for valor in fila:
            # Imprimir sin salto de línea. Usando un espacio al final
            print(valor, end=" ")
        print("")
else:
    print("El número de columnas de A es distinto al número de filas de B")
